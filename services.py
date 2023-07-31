import json
import os.path

import openai

from config import OPENAI_API_TOKEN, CONTEXT_DB

openai.api_key = OPENAI_API_TOKEN


def create_context_file(path: str) -> None:
    if not os.path.exists(path):
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump({}, file, indent=4, ensure_ascii=False)


def get_context(chat_id: int) -> list[dict]:
    create_context_file(CONTEXT_DB)
    with open(CONTEXT_DB, 'r', encoding='UTF-8') as file:
        context_json = json.load(file)
    context = context_json.get(str(chat_id), [])
    return context


def set_context(chat_id: int, context: list[dict]):
    create_context_file(CONTEXT_DB)
    with open(CONTEXT_DB, 'r', encoding='UTF-8') as file:
        context_json = json.load(file)
    context_json[str(chat_id)] = context
    with open(CONTEXT_DB, 'w', encoding='UTF-8') as file:
        json.dump(context_json, file, indent=4, ensure_ascii=False)


async def get_chat_gpt_response(message: str, chat_id: int) -> str:
    model = 'gpt-3.5-turbo'
    context = get_context(chat_id)
    context.append({'role': 'user', 'content': message})
    set_context(chat_id, context)
    response = await openai.ChatCompletion.acreate(
        model=model,
        messages=context
    )
    return response.choices[0].message.content
