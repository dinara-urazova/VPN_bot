from bot.api_client import send_message, delete_message, get_updates
import time
from bot.api_client import InlineButton

next_update_id = 0

while True:
    try:  # ask Telegram for new updates
        response = get_updates(next_update_id)
        data = response.json()
        print(data)
        updates = data["result"]

        for update in updates:
            next_update_id = update["update_id"] + 1
            message = update.get("message")
            if not message:
                continue

            message_text = message.get("text")
            chat_id = message["chat"]["id"]
            message_id = message.get("message_id")
            if not chat_id or not message_text:
                continue
            if message_text == "/start":
                text = "👋 Привет!  Это Telegram-бот для подключения к VPN. Вам доступен бесплатный период - 10 дней. Для начала работы нажмите в меню кнопку ⚡️Подключиться ↓"
                reply_buttons = [
                    ["ℹ️ Статус", "⚡️ Подключиться"],
                    ["🔥 Купить", "❓ Помощь"],
                ]
                send_message(
                    chat_id=chat_id,
                    text=text,
                    reply_buttons=reply_buttons,
                )

            elif message_text in "ℹ️ Статус":
                delete_message(chat_id, message_id)
            elif message_text == "⚡️ Подключиться":
                delete_message(chat_id, message_id)
            elif message_text == "🔥 Купить":
                delete_message(chat_id, message_id)
            elif message_text == "❓ Помощь":
                delete_message(chat_id, message_id)
                text = "Если у вас проблемы с подключением, отправьте статус из бота и скриншот из приложения, которым вы пользуетесь для доступа к VPN в поддержку.Ниже представлены инструкции для подключения к сервису ↓"
                url_buttons = [
                    InlineButton(
                        text="Подключить iOS/MacOS 🍏",
                        url="https://telegra.ph/Podklyuchenie-v2raytun-iOS-11-09",
                    ),
                    InlineButton(
                        text="Подключить Android 🤖",
                        url="https://telegra.ph/Podklyuchenie-v2RayTun-Android-11-09",
                    ),
                    InlineButton(
                        text="Подключить Windows 🖥️",
                        url="https://telegra.ph/Nastrojka-VPN-PK-Windows-08-08",
                    ),
                    InlineButton(
                        text="🆘Поддержка",
                        url="https://web.telegram.org/k/#@artydevx",
                    ),
                    InlineButton(
                        text="Назад",
                        url="go_back",
                    ),
                ]
                send_message(chat_id=chat_id, text=text, inline_url_buttons=url_buttons)

    except Exception as e:
        print(f"The error is {e}")

    time.sleep(2)
