import telebot
from config import TOKEN, API_FB, SECRET_KEY
from logic import Text2ImageAPI

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_FB, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]

    api.save_image(images, 'decoded_image.jpg')

    with open('decoded_image.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


bot.infinity_polling()