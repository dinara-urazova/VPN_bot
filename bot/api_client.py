import requests
import json
from bot.config_reader import env_config
from typing import NamedTuple

token = env_config.telegram_token.get_secret_value()


def reply_keyboard_builder(buttons: list) -> str | None:
    if not buttons:
        return None
    return json.dumps(
        {
            "keyboard": buttons,
            "is_persistent": True,
            "one_time_keyboard": False,
        }
    )


class InlineButton(NamedTuple):
    text: str
    url: str


def inline_keyboard_builder(buttons: list[InlineButton]) -> str | None:
    if not buttons:
        return None

    result = []
    for button in buttons:
        element = {
            "text": button.text,
        }
        buttonKey = "url" if button.url.startswith("https://") else "callback_data"
        element[buttonKey] = button.url
        result.append([element])

    return json.dumps({"inline_keyboard": result})


def send_message(
    chat_id: int,
    text: str,
    reply_buttons=None,
    inline_url_buttons=None,
):
    params = {
        "chat_id": chat_id,
        "text": text,
    }

    if reply_buttons:
        params["reply_markup"] = reply_keyboard_builder(reply_buttons)
    elif inline_url_buttons:
        params["reply_markup"] = inline_keyboard_builder(inline_url_buttons)

    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", params=params)


def delete_message(chat_id: int, message_id: int):
    requests.post(
        f"https://api.telegram.org/bot{token}/deleteMessage",
        params={
            "chat_id": chat_id,
            "message_id": message_id,
        },
    )


def get_updates(next_update_id: int):
    return requests.get(
        f"https://api.telegram.org/bot{token}/getUpdates",
        params={
            "offset": next_update_id,
            "allowed_updates": ["message", "callback_query"],
        },
    )
