from telegram import Update, ChatJoinRequest
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "7716484951:AAEnUpNbnqmsb9lcmAXsk_zD0E7o6YEoRQY"

# Auto approve join requests and send welcome message
async def approve_and_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request: ChatJoinRequest = update.chat_join_request
    await context.bot.approve_chat_join_request(chat_id=request.chat.id, user_id=request.from_user.id)
    
    await context.bot.send_message(
        chat_id=request.chat.id,
        text=f"👋 Welcome {request.from_user.mention_html()} to the group!",
        parse_mode="HTML"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve_and_welcome))
    app.run_polling()

if __name__ == '__main__':
    main()
