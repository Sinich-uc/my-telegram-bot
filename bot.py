"""
Telegram Bot for Sinich - Bothost Version
Bothost автоматически подставляет токен вместо {{token}}
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ============================================
# НАСТРОЙКА ЛОГГИРОВАНИЯ
# ============================================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ============================================
# КОМАНДЫ БОТА
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🎮 Привет, {user.first_name}! Я твой бот на Bothost!\n\n"
        f"Используй /help для списка команд"
    )

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, Полик! Бот работает! 🚀")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 **Доступные команды:**
/start - Начать
/hello - Приветствие
/help - Эта справка
/info - Информация

💬 Напиши любое сообщение - я отвечу!
    """
    await update.message.reply_text(help_text)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = """
📊 **Информация о боте:**
• Хостинг: Bothost.org
• Статус: ✅ Работает
• Для: Sinich (Полик)
• Назначение: Помощник для геймера
    """
    await update.message.reply_text(info_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Вы написали: {update.message.text}")

# ============================================
# ГЛАВНАЯ ФУНКЦИЯ ДЛЯ BOTHOST
# ============================================
def main():
    """
    Bothost ищет эту функцию и вызывает её.
    Bothost автоматически подставит токен вместо {{token}}
    """
    
    print("=" * 50)
    print("🤖 БОТ ЗАПУЩЕН НА BOTHOST")
    print("=" * 50)
    
    # Bothost подставляет реальный токен вместо {{token}}
    app = Application.builder().token("{{token}}").build()
    
    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("info", info))
    
    # Регистрируем обработчик обычных сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("✅ Бот инициализирован")
    print("✅ Ожидаю сообщения...")
    print("=" * 50)
    
    return app

# ============================================
# БЛОК ДЛЯ ЛОКАЛЬНОГО ТЕСТИРОВАНИЯ
# ============================================
if __name__ == "__main__":
    """
    Этот блок выполняется ТОЛЬКО при локальном запуске.
    На Bothost он игнорируется.
    """
    
    print("=" * 50)
    print("⚠️  Этот код для Bothost!")
    print("=" * 50)
    print("Для локального теста:")
    print("1. Замените '{{token}}' на строка 59 на реальный токен")
    print("2. Удалите или закомментируйте этот блок (строки 75-79)")
    print("3. Запустите: python bot.py")
    print("=" * 50)
    
    # Раскомментируйте для локального теста:
    # TOKEN = "ВАШ_ТОКЕН_ЗДЕСЬ"  # <-- Вставьте реальный токен
    # app = Application.builder().token(TOKEN).build()
    # app.add_handler(CommandHandler("start", start))
    # app.add_handler(CommandHandler("hello", hello))
    # app.add_handler(CommandHandler("help", help_cmd))
    # app.add_handler(CommandHandler("info", info))
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # print("Бот запускается локально...")
    # app.run_polling()