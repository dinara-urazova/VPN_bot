from bot.api_client import send_message, delete_message, get_updates
import time
from bot.api_client import InlineButton


def process_update_message(message: dict):
    try:
        message_text = message.get("text")
        chat_id = message.get("chat", {}).get("id")
        message_id = message.get("message_id")
        if not chat_id or not message_text:
            return None
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

        elif message_text == "ℹ️ Статус":
            delete_message(chat_id, message_id)
            text = (
                "Доступ: ☑️ <b>Пробный период</b>\n"
                "├ Осталось дней: 10\n"
                "└ Активна до: 20.06.2025 18:00"
            )
            send_message(chat_id=chat_id, text=text, parse_mode="HTML")

        elif message_text == "⚡️ Подключиться":
            delete_message(chat_id, message_id)
            text = (
                "Доступ к VPN в 2 шага:\n\n"
                "1️⃣ <b>Скачать</b> – для скачивания приложения\n"
                "2️⃣ <b>Подключить</b> – для добавления подписки\n\n"
                "<b>Настроить VPN вручную:</b>\n"
                '– <a href="https://telegra.ph/Podklyuchenie-v2RayTun-Android-11-09">Инструкция для Android 🤖</a>\n'
                '– <a href="https://telegra.ph/Podklyuchenie-v2raytun-iOS-11-09">Инструкция для iOS/MacOS 🍏</a>\n'
                '– <a href="https://telegra.ph/Nastrojka-VPN-PK-Windows-08-08">Инструкция для Windows 🖥</a>\n\n'
                "<b>Ссылка для ручного подключения</b>\n"
                "<i>Тапните чтобы скопировать в буфер обмена ↓</i>"
            )
            url_buttons = [
                [
                    InlineButton(
                        text="Скачать Android 🤖",
                        url="https://play.google.com/store/apps/details?id=com.v2raytun.android&hl=ru&gl=US",
                    ),
                    InlineButton(
                        text="Подключить Android 🤖",
                        url="https://apps.artydev.ru/?url=v2raytun://import/https://u.mrzb.artydev.ru/c/2f18b7c0x3f20f8ac#MatadoraVPN",
                    ),
                ],
                [
                    InlineButton(
                        text="Скачать iOS 🍏",
                        url="https://apps.apple.com/ru/app/v2raytun/id6476628951",
                    ),
                    InlineButton(
                        text="Подключить iOS 🍏",
                        url="https://apps.artydev.ru/?url=v2rayTun://import/https://u.mrzb.artydev.ru/c/2f18b7c0x3f20f8ac#MatadoraVPN",
                    ),
                ],
                [
                    InlineButton(
                        text="Скачать Windows 🖥️",
                        url="Hiddify-Windows-Setup-x64.exe",
                    ),
                    InlineButton(
                        text="Подключить Windows 🖥️",
                        url="https://apps.artydev.ru/?url=hiddify://import/https://u.mrzb.artydev.ru/c/2f18b7c0x3f20f8ac",
                    ),
                ],
                [
                    InlineButton(
                        text="Назад",
                        url="go_back",
                    )
                ],
            ]
            send_message(
                chat_id=chat_id,
                text=text,
                parse_mode="HTML",
                inline_url_buttons=url_buttons,
            )

        elif message_text == "🔥 Купить":
            delete_message(chat_id, message_id)
        elif message_text == "❓ Помощь":
            delete_message(chat_id, message_id)
            text = "Если у вас проблемы с подключением, отправьте статус из бота и скриншот из приложения, которым вы пользуетесь для доступа к VPN в поддержку.Ниже представлены инструкции для подключения к сервису ↓"
            url_buttons = [
                [
                    InlineButton(
                        text="Подключить iOS/MacOS 🍏",
                        url="https://telegra.ph/Podklyuchenie-v2raytun-iOS-11-09",
                    )
                ],
                [
                    InlineButton(
                        text="Подключить Android 🤖",
                        url="https://telegra.ph/Podklyuchenie-v2RayTun-Android-11-09",
                    )
                ],
                [
                    InlineButton(
                        text="Подключить Windows 🖥️",
                        url="https://telegra.ph/Nastrojka-VPN-PK-Windows-08-08",
                    )
                ],
                [
                    InlineButton(
                        text="🆘Поддержка",
                        url="https://t.me/olegsklyarov",
                    )
                ],
                [
                    InlineButton(
                        text="Назад",
                        url="go_back",
                    )
                ],
            ]
            send_message(chat_id=chat_id, text=text, inline_url_buttons=url_buttons)
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
