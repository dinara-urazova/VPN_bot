from bot.api_client import send_message, delete_message, get_updates
import time
from bot.buttons import (
    start_button,
    status_button,
    connection_button,
    buy_button,
    help_button,
    one_month,
    three_months,
    six_months,
)


def process_update_message(message: dict):
    try:
        message_text = message.get("text")
        chat_id = message.get("chat", {}).get("id")
        message_id = message.get("message_id")

        if not chat_id or not message_text:
            return None

        if message_text == "/start":
            text, reply_buttons = start_button()
            send_message(
                chat_id=chat_id,
                text=text,
                reply_buttons=reply_buttons,
            )

        elif message_text == "ℹ️ Статус":
            delete_message(chat_id, message_id)
            text, url_buttons = status_button()
            send_message(
                chat_id=chat_id,
                text=text,
                parse_mode="HTML",
                inline_url_buttons=url_buttons,
            )

        elif message_text == "⚡️ Подключиться":
            delete_message(chat_id, message_id)
            text, url_buttons = connection_button()
            send_message(
                chat_id=chat_id,
                text=text,
                parse_mode="HTML",
                inline_url_buttons=url_buttons,
            )

        elif message_text == "🔥 Купить":
            delete_message(chat_id, message_id)
            text, url_buttons = buy_button()
            send_message(
                chat_id=chat_id,
                text=text,
                parse_mode="HTML",
                inline_url_buttons=url_buttons,
            )

        elif message_text == "❓ Помощь":
            delete_message(chat_id, message_id)
            text, url_buttons = help_button()
            send_message(
                chat_id=chat_id,
                text=text,
                parse_mode="HTML",
                inline_url_buttons=url_buttons,
            )

    except Exception as e:
        print(f"The error is {repr(e)}")


def process_update_callback(callback_query: dict):
    try:
        data = callback_query.get("data")
        message = callback_query.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        message_id = message.get("message_id")

        if not chat_id or not data:
            return

        if data == "go_back":
            delete_message(chat_id, message_id)
        else:
            buy_options = {
                "one_month": one_month,
                "three_months": three_months,
                "six_months": six_months,
            }
            if data in buy_options:
                text, url_buttons = buy_options[data]()
                send_message(chat_id=chat_id, text=text, inline_url_buttons=url_buttons)
            else:
                print(f"Unknown callback data: {data}")

    except Exception as e:
        print(f"The error is {repr(e)}")


next_update_id = 0

while True:
    try:  # ask Telegram for new updates
        response = get_updates(next_update_id)
        data = response.json()
        print(data)
        updates = data["result"]

        for update in updates:
            next_update_id = update["update_id"] + 1
            if "callback_query" in update:
                process_update_callback(update["callback_query"])
            elif "message" in update:
                process_update_message(update["message"])
            else:
                continue

    except Exception as e:
        print(f"The error is {e}")

    time.sleep(2)
