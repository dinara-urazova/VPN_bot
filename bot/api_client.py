import requests
import json
from bot.config_reader import env_config

token = env_config.telegram_token.get_secret_value()

def reply_keyboard_builder(buttons: list) -> str | None:
    if not buttons:
        return None
    return json.dumps({
        "keyboard": buttons, 
        "is_persistent": True,
        "one_time_keyboard": False,
        })


def inline_keyboard_builder(buttons: list) -> str | None:
    if not buttons:
        return None
    result = []
    for text, url in buttons:
        result.append(
            {
                "text": text,
                "url": url,
            }
        )

    return json.dumps({"inline_keyboard": [result]})


def inline_keyboard_callbacks_builder(buttons: list) -> str | None:
    if not buttons:
        return None
    result = []
    for text, callback_data in buttons:
        result.append(
            {
                "text": text,
                "callback_data": callback_data,
            }
        )

    return json.dumps({"inline_keyboard": [result]})

def send_message(chat_id: int, text: str, reply_buttons=None, inline_url_buttons=None, inline_callback_buttons=None):
    params = {
        "chat_id": chat_id,
        "text": text,
    }

    if reply_buttons:
        params["reply_markup"] = reply_keyboard_builder(reply_buttons)
    elif inline_url_buttons:
        params["reply_markup"] = inline_keyboard_builder(inline_url_buttons)
    elif inline_callback_buttons:
        params["reply_markup"] = inline_keyboard_callbacks_builder(inline_callback_buttons)

    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", params=params)
  

def delete_message(chat_id: int, message_id: int):
    requests.post(
        f"https://api.telegram.org/bot{token}/deleteMessage",
        params={
            "chat_id": chat_id,
            "message_id": message_id,
        }
    )


def get_updates(next_update_id: int):
    return requests.get(
            f"https://api.telegram.org/bot{token}/getUpdates",
            params={
                "offset": next_update_id,
            },
        )