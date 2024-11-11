# основной файл запуска, укажи свой token в init.py
import init
import logging
from telegram import Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    MessageHandler,
    CallbackQueryHandler,
    CommandHandler,
    filters,
)

from handlers import help_command, button, start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Path(__file__).parent / "newsletter_strings.yml", 'r'


def run() -> None:
    application = Application.builder().token(init.bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    run()
