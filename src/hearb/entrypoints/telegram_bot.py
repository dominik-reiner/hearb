import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from src.hearb.config.settings import settings
from src.hearb.components.orchestrator import orchestrator

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message when the /start command is issued."""
    await update.message.reply_text("Hello! I'm Hearb, your plant's voice. Talk to me about your plant!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming text messages and passes them to the LangGraph orchestrator."""
    user_message = update.message.text

    # TODO: This is a placeholder for the actual invocation of the LangGraph agent.
    # The response from the agent will be sent back to the user.
    # response = orchestrator.invoke({"messages": [("user", user_message)]})
    # agent_response = response.get("messages", [])[-1].content

    agent_response = f"You said: {user_message}" # Placeholder response
    await update.message.reply_text(agent_response)

def main() -> None:
    """Starts the Telegram bot."""
    application = Application.builder().token(settings.telegram_bot_token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
