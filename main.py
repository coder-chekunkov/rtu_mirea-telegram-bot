from telegram.ext import Updater, CommandHandler

token = "5219565252:AAETCFyyTmY3ioY6yQr56Eiz5iTSdJ5jl4s"

print("Бот запущен. Нажмите Ctrl+C для завершения")

updater = Updater(token, use_context=True)

updater.start_polling()
updater.idle()




