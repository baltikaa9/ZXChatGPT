# ZXChatGpt

## Telegram bot to communicate with ChatGPT


### link to the bot - [@zxchatgptbot](https://t.me/zxchatgptbot)


## Using bot
To start communicating with the bot, just write him any message. This message will send to the ChatGPT.
The bot also has the following commands:
- `/q <message>` to communicate with the bot in groups or supergroups (not private chats)
- `/context` displays the communication history with the bot in the current chat
- `/deletecontext` delete the dialog context with the bot in the current chat



## Setup bot
Before launching the bot you need to create a file `.env` in which you should write the following:
- BOT_TOKEN - the telegram bot token received in [BotFather](https://t.me/BotFather)
- OPENAI_API_KEY - openai api key received in [OpenAI API](https://platform.openai.com/account/api-keys)

The structure of `.env` file:
```
BOT_TOKEN=your_token
OPENAI_API_KEY=your_api_key
```

Also, you should install the requirements using the command: `pip install -r requirements.txt`.

Now you can launch the bot using the command `python main.py`.

[P.S.] The dialog contexts of each chat are stored in the `data/context.json` file that will be created automatically.

## Docker
- Create a directory `data` if it is not created: `mkdir data`
- Create a bot image: `docker build -t zxchatgpt .`
- Create and run a container: `docker run --name zxchatgpt -v zxchatgpt-data:/data -d zxchatgpt`
