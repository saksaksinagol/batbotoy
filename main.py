import telebot
import openai
import os
from gtts import gTTS
# initialize OpenAI API client
openai.api_key = " enter open ai api key here "

bot = telebot.TeleBot(' enter telegram token here ')


@bot.message_handler(commands=['reply'])
def generate_reply(message):
    try:
        if message.chat.type == "private":
            chat_id = message.from_user.id
            bot.send_message(chat_id=chat_id, reply_to_message_id=message.message_id, text="Use this command in a group and reply to a message.")
            return
        reply_to_message = message.reply_to_message
        prompt = reply_to_message.text
        if len(message.text.split()) > 1:
            prompt = prompt + "\n" + " ".join(message.text.split()[1:])
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048
        )
        if len(response["choices"][0]["text"]) > 3900:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text="Message is too big, Telegram doesn't support")
        else:
            if reply_to_message.from_user.is_bot:
                bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id,text=response["choices"][0]["text"])
            else:
                bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=response["choices"][0]["text"])
        print(f'\n\n=======================================================================================\n{message.from_user.username} : {prompt} \n\nChatGPT : {response["choices"][0]["text"]}')
    except Exception:
        try:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text="Reply to a message.")
        except Exception as e:
            print(e)


@bot.message_handler(commands=['roasthim'])
def generate_roastreply(message):
    try:
        if message.chat.type == "private":
            chat_id = message.from_user.id
            bot.send_message(chat_id=chat_id, reply_to_message_id=message.message_id, text="Use this command in a group and reply to a message.")
            return
        reply_to_message = message.reply_to_message
        prompt = reply_to_message.text
        if len(message.text.split()) > 1:
            prompt = prompt + "\n" + " ".join(message.text.split()[1:])
        prompt = "Roast this : " + prompt
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048
        )
        if len(response["choices"][0]["text"]) > 3900:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text="Message is too big, Telegram doesn't support")
        else:
            if reply_to_message.from_user.is_bot:
                bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id,text=response["choices"][0]["text"])
            else:
                bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=response["choices"][0]["text"])
            print(f'\n\n=======================================================================================\n{message.from_user.username} : {prompt} \n\nChatGPT : {response["choices"][0]["text"]}')
    except Exception:
        try:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text="Reply to a message.")
        except Exception as e:
            print(e)


@bot.message_handler(commands=['gpt'])
def generate_gpt(message):
    try:
        if message.chat.type != "private":
        # message was sent in a group, respond to the group
            chat_id = message.chat.id
        else:
        # message was sent in private chat, respond to the sender
            chat_id = message.from_user.id
        prompt_array = message.text.split()[1:]
        if len(prompt_array) < 2:
            bot.send_message(chat_id=chat_id, reply_to_message_id=message.message_id, text="Please provide a message after the command '/gpt'")
            return
        prompt = message.text.split()[1:] # get the text after the command '/gpt'
        prompt = ' '.join(prompt)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048
        )
        response_text = response["choices"][0]["text"]
        if len(response_text) > 3900:
            raise Exception("Message is too big, Telegram doesn't support messages with more than 3900 characters.")
        bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=response_text)
        print(f'\n\n=======================================================================================\n{message.from_user.username} : {prompt} \n\nChatGPT : {response["choices"][0]["text"]}')
    except Exception as e:
        try:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=str(e))
        except Exception as e:
            print(e)


@bot.message_handler(commands=['tl'])
def generate_trengpt(message):
    try:
        if message.chat.type != "private":
        # message was sent in a group, respond to the group
            chat_id = message.chat.id
        else:
        # message was sent in private chat, respond to the sender
            chat_id = message.from_user.id

        prompt_array = message.text.split()[1:]
        reply_to_message = message.reply_to_message

        if reply_to_message is not None:
            prompt_array = [reply_to_message.text]

        if len(prompt_array) < 1:
            bot.send_message(chat_id=chat_id, reply_to_message_id=message.message_id, text="Please provide a message after the command '/tl' or reply to a Message")
            return
        prompt = ' '.join(prompt_array)
        prompt = "Translate in English : "+prompt
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048
        )
        response_text = response["choices"][0]["text"]
        if len(response_text) > 3900:
            raise Exception("Message is too big, Telegram doesn't support messages with more than 3900 characters.")
        bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=response_text)
        print(f'\n\n=======================================================================================\n{message.from_user.username} : {prompt} \n\nChatGPT : {response["choices"][0]["text"]}')
    except Exception as e:
        try:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=str(e))
        except Exception as e:
            print(e)

@bot.message_handler(commands=['gpta'])
def generate_gptaudio(message):
    try:
        if message.chat.type != "private":
        # message was sent in a group, respond to the group
            chat_id = message.chat.id
        else:
        # message was sent in private chat, respond to the sender
            chat_id = message.from_user.id
        prompt_array = message.text.split()[1:]
        if len(prompt_array) < 2:
            bot.send_message(chat_id=chat_id, reply_to_message_id=message.message_id, text="Please provide a message after the command '/audio'")
            return
        prompt = message.text.split()[1:] # get the text after the command '/audio'
        prompt = ' '.join(prompt)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048
        )
        response_text = response["choices"][0]["text"]
        if len(response_text) > 3900:
            raise Exception("Message is too big, Telegram doesn't support messages with more than 3900 characters.")

        # Convert the text to audio using gTTS library
        tts = gTTS(response_text, lang='en')
        tts.save("dev_@dhir4j.mp3")

        # Send the audio file
        with open("dev_@dhir4j.mp3", "rb") as f:
            bot.send_audio(chat_id=chat_id, reply_to_message_id=message.message_id ,audio=f)

        os.remove("dev_@dhir4j.mp3") # Delete the audio file
        print(f'\n\n=======================================================================================\n{message.from_user.username} : {prompt} \n\nChatGPT : {response["choices"][0]["text"]}')
    except Exception as e:
        try:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=str(e))
        except Exception as e:
            print(e)

@bot.message_handler(commands=["tts"])
def tts_handler(message):
    try:
        if message.reply_to_message:
            text = message.reply_to_message.text
        else:
            text = message.text.split(" ", maxsplit=1)[1]
        
        tts = gTTS(text=text, lang='en')
        tts.save("tts_@dhir4j.mp3")
        with open("tts_@dhir4j.mp3", "rb") as f:
            bot.send_audio(chat_id=message.chat.id, reply_to_message_id=message.message_id, audio=f)
        os.remove("tts_@dhir4j.mp3")
    except Exception as e:
        try:
            bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=str(e))
        except Exception as e:
            print(e)


bot.polling()
