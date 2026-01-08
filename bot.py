import sys
import signal
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Красиво обрабатываем Ctrl+C
def handle_keyboard_interrupt(signum, frame):
    print("\n" + "=" * 50)
    print("🛑 БОТ ОСТАНОВЛЕН")
    print("=" * 50)
    sys.exit(0)

signal.signal(signal.SIGINT, handle_keyboard_interrupt)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# ТОКЕН - ВСТАВЬТЕ СВОЙ!
TOKEN = "8309462119:AAGHOQz1VdtAi1EYbhv7BEkn7Oc343MmYz0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает! Для остановки нажмите Ctrl+C в консоли.")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, Полик! 👋")

def main():
    print("=" * 50)
    print("ЗАПУСК БОТА - ДЛЯ ОСТАНОВКИ: Ctrl+C")
    print("=" * 50)
    
    if TOKEN == "ВАШ_ТОКЕН_ЗДЕСЬ":
        print("❌ Вставьте свой токен от @BotFather!")
        return
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    
    print("✅ Бот запущен и готов к работе!")
    print("✅ Телеграм -> Найдите бота -> /start или /hello")
    print("=" * 50)
    
    app.run_polling()

if __name__ == '__main__':
    main()