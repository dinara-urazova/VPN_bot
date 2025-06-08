from bot.api_client import InlineButton

def start_button():
    text = "👋 Привет!  Это Telegram-бот для подключения к VPN. Вам доступен бесплатный период - 10 дней. Для начала работы нажмите в меню кнопку ⚡️Подключиться ↓"
    reply_buttons = [
        ["ℹ️ Статус", "⚡️ Подключиться"],
        ["🔥 Купить", "❓ Помощь"],
    ]
    return text, reply_buttons


def status_button():
    text = (
        "Доступ: ☑️ <b>Пробный период</b>\n"
        "├ Осталось дней: 10\n"
        "└ Активна до: 20.06.2025 18:00"
    )
    url_buttons = [
        [
            InlineButton(
                text="Назад",
                url="go_back",
            )
        ],
    ]
    return text, url_buttons


def connection_button():
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
    return text, url_buttons


def buy_button():
    text = (
        "Для полного доступа выберите удобный для вас тариф:\n\n"
        "250₽ / 1 мес\n"
        "650₽ / 3 мес\n"
        "1200₽ / 6 мес\n\n"
        "💳 Можно оплатить через:\n"
        "SberPay, СБП, T-Pay, карты и криптовалюты."
    )
    url_buttons = [
        [
            InlineButton(
                text="✅ 1 Месяц",
                url="1_month",
            )
        ],
        [
            InlineButton(
                text="🔥 3 Месяца",
                url="3_months",
            ),
        ],
        [
            InlineButton(
                text="🚀 6 Месяцев",
                url="6_months",
            )
        ],
        [
            InlineButton(
                text="Назад",
                url="go_back",
            )
        ],
    ]
    return text, url_buttons


def help_button():
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
    return text, url_buttons
