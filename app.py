import telegram
from telegram.ext import Updater, CommandHandler
import openai

# Set your OpenAI API key
openai.api_key = "your open api token"

# Set up the Telegram bot
bot = telegram.Bot(token='your telegram bot token')
updater = Updater(bot.token)

# Define the handler function for the /chatgpt command
def chatgpt(update, context):
    # Get the user's message
    print("[{0}] is recieved...".format(update.message.text))
    message = update.message.text
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        prompt=message,
        model="text-davinci-003",
        max_tokens=1024,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Send the response to the user
    update.message.reply_text(text=response.choices[0].text)


# Set up the /chatgpt command in the bot
updater.dispatcher.add_handler(CommandHandler('chatgpt', chatgpt))

# Start the bot
updater.start_polling()
