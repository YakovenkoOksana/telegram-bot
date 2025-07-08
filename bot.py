from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters, ContextTypes
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Type /help to see what I can do.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are some things you can try:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/about - Info about me\n"
        "/buttons - Try interactive buttons\n"
        "Or just type anything and I'll echo it!"
    )

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 I'm a test bot created by Oksana using Python!")

# Echo handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

# /buttons command – inline buttons
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Say Hello 👋", callback_data="say_hello")],
        [InlineKeyboardButton("Send a photo 📸", callback_data="send_photo")],
    ]
    await update.message.reply_text(
        "Choose an action:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Handle button presses
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "say_hello":
        await query.edit_message_text("Hello there! 😊")
    elif query.data == "send_photo":
        await query.edit_message_text("Here’s a random photo!")
        await query.message.reply_photo("https://picsum.photos/400/300")

# Main entry point
def main():
    app = ApplicationBuilder().token("8173104711:AAF7Ryg1mG6Wz-aPBziJWAHmySRYTmjC7Qo").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("buttons", buttons))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
