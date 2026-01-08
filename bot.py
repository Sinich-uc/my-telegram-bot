"""
Telegram Bot for Sinich - Bothost Version
Bothost автоматически подставляет токен
"""

import logging
from telegram.ext import Application, CommandHandler

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# ========== КОМАНДЫ ==========
async def start(update, context):
    await update.message.reply_text("✅ Бот работает на Bothost! Привет!")

async def hello(update, context):
    await update.message.reply_text("Привет, Полик! 🎮")

# ========== ГЛАВНАЯ ФУНКЦИЯ ==========
def main():
    """
    Bothost ищет эту функцию
    Bothost подставляет реальный токен вместо {{token}}
    """
    print("=" * 50)
    print("🤖 BOTHOST BOT STARTING...")
    print("=" * 50)
    
    # Bothost автоматически заменяет {{token}} на реальный токен
    app = Application.builder().token("{{token}}").build()
    
    # Добавляем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    
    print("✅ Bot initialized")
    print("=" * 50)
    
    return app

# ========== ТОЧКА ВХОДА ==========
if __name__ == "__main__":
    # Bothost игнорирует этот блок
    print("This code is for Bothost only!")