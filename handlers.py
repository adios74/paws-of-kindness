#здесь куски кода, посвященные определенным функциям
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
)


async def send_inline_keyboard(message) -> None:
    keyboard = [
        [
            InlineKeyboardButton("ПАМАГИТИ", callback_data="help"),
            InlineKeyboardButton("Что-то ещё", callback_data="2"),
        ],
        [InlineKeyboardButton("Выбрать жвотне", callback_data="choose_animal")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await message.reply_text("Выберите действие:", reply_markup=reply_markup)


async def reply(query) -> None:
    if query.data == "help":
        await query.edit_message_text(text="Бог в помощь")
    elif query.data == "choose_animal":
        await query.edit_message_text(text="Меню выбора, например")
    else:
        return

    message = query.message

    await send_inline_keyboard(message)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    await reply(query)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /start to test this bot.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message

    await send_inline_keyboard(message)
