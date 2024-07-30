# from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
#
# def tariff_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('🌟 Start Tariff 🌟'))
#     keyboard.add(KeyboardButton('🚀 Development Tariff 🚀'))
#     keyboard.add(KeyboardButton('💼 Professional Tariff 💼'))
#     return keyboard
#
# def payment_button():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton('💳 Pay', callback_data='pay'))
#     return keyboard
#
# def admin_menu_keyboard():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('👥 User List'), KeyboardButton('📜 User Receipts'), KeyboardButton('❓ Answers to Questions'))
#     keyboard.add(KeyboardButton('➕ Add Cheat Sheet'), KeyboardButton('✏️ Edit Cheat Sheet'), KeyboardButton('🔍 View Cheat Sheets'))
#     keyboard.add(KeyboardButton('📧 Broadcast'), KeyboardButton('➕ Add Administrator'))
#     return keyboard
#
#
# def receipt_action_buttons(receipt_id, selected_tariff):
#     buttons = [
#         InlineKeyboardButton(text="✅ Approve", callback_data=f"approve_{receipt_id}"),
#         InlineKeyboardButton(text="❌ Reject", callback_data=f"reject_{receipt_id}")
#     ]
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     return keyboard
#
# def user_profile_update_buttons(tariff):
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     keyboard.add(InlineKeyboardButton('✏️ Edit Name', callback_data='edit_name'))
#     keyboard.add(InlineKeyboardButton('📞 Edit Contact Information', callback_data='edit_contact'))
#     return keyboard
#
# def user_profile_buttons(tariff):
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('📞 Contact Manager'))
#     if tariff != "Professional Tariff":
#         keyboard.add(KeyboardButton('🔄 Switch to a New Tariff'))
#     keyboard.add(KeyboardButton('Back'))
#     return keyboard
#
# def start_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('👤 My Profile'))
#     keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('📚 Useful Materials'))
#     keyboard.add(KeyboardButton('📞 Contact Manager'))
#     return keyboard
#
# def development_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('👤 My Profile'))
#     keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('📚 Useful Materials'))
#     # keyboard.add(KeyboardButton('🔍 Stage Verification'))
#     keyboard.add(KeyboardButton('📞 Contact Manager'))
#     return keyboard
#
# def professional_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('👤 My Profile'))
#     keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('📚 Useful Materials'))
#     keyboard.add(KeyboardButton('📞 Contact Manager'))
#     return keyboard
#
# def upgrade_buttons():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton('🚀 Development Tariff', callback_data='upgrade_development'))
#     keyboard.add(InlineKeyboardButton('💼 Professional Tariff', callback_data='upgrade_professional'))
#     return keyboard
#
# def back_button():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('Back'))
#     return keyboard

# # -------
# from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
#
# def tariff_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('Start Tariff'))
#     keyboard.add(KeyboardButton('Development Tariff'))
#     keyboard.add(KeyboardButton('Professional Tariff'))
#     return keyboard
#
# def payment_button():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton('Pay', callback_data='pay'))
#     return keyboard
#
# def admin_menu_keyboard():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('User List'))
#     keyboard.add(KeyboardButton('User Receipts'))
#     keyboard.add(KeyboardButton('Answers to Questions'))
#     keyboard.add(KeyboardButton('Broadcast'))
#     return keyboard
#
# def receipt_action_buttons(receipt_id, selected_tariff):
#     buttons = [
#         InlineKeyboardButton(text="Approve", callback_data=f"approve_{receipt_id}"),
#         InlineKeyboardButton(text="Reject", callback_data=f"reject_{receipt_id}")
#     ]
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     return keyboard
#
# def user_profile_update_buttons(tariff):
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     keyboard.add(InlineKeyboardButton('Edit Name', callback_data='edit_name'))
#     keyboard.add(InlineKeyboardButton('Edit Contact Info', callback_data='edit_contact'))
#     return keyboard
#
# def user_profile_buttons(tariff):
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('Contact Manager'))
#     if tariff != "Professional Tariff":
#         keyboard.add(KeyboardButton('Switch to a New Tariff'))
#     keyboard.add(KeyboardButton('Back'))
#     return keyboard
#
# def start_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('My Profile'))
#     keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('Useful Materials'))
#     keyboard.add(KeyboardButton('Contact Manager'))
#     return keyboard
#
# def development_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('My Profile'))
#     keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('Useful Materials'))
#     keyboard.add(KeyboardButton('Stage Verification'))
#     keyboard.add(KeyboardButton('Contact Manager'))
#     return keyboard
#
# def professional_buttons():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('My Profile'))
#     keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('Useful Materials'))
#     keyboard.add(KeyboardButton('Contact Manager'))
#     return keyboard
#
# def upgrade_buttons():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton('Development Tariff', callback_data='upgrade_development'))
#     keyboard.add(InlineKeyboardButton('Professional Tariff', callback_data='upgrade_professional'))
#     return keyboard
#
# def back_button():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(KeyboardButton('Back'))
#     return keyboard
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

def tariff_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('🌟 Тариф Старт 🌟'))
    keyboard.add(KeyboardButton('🚀 Тариф Развитие 🚀'))
    keyboard.add(KeyboardButton('💼 Тариф Профессионал 💼'))
    return keyboard

def payment_button():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('💳 Оплатить', callback_data='pay'))
    return keyboard

def admin_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('👥 Список пользователей'), KeyboardButton('📜 Чеки пользователей'), KeyboardButton('❓ Ответы на вопросы'))
    keyboard.add(KeyboardButton('➕ Добавить шпаргалку'), KeyboardButton('✏️ Редактировать шпаргалку'), KeyboardButton('🔍 Просмотр шпаргалок'))
    keyboard.add(KeyboardButton('📧 Рассылка'), KeyboardButton('➕ Добавить администратора'))
    keyboard.add(KeyboardButton('Ответы пользователей'))
    return keyboard

def receipt_action_buttons(receipt_id, selected_tariff):
    buttons = [
        InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"approve_{receipt_id}"),
        InlineKeyboardButton(text="❌ Отклонить", callback_data=f"reject_{receipt_id}")
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

def user_profile_update_buttons(tariff):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton('✏️ Редактировать имя', callback_data='edit_name'))
    keyboard.add(InlineKeyboardButton('📞 Редактировать контактные данные', callback_data='edit_contact'))
    return keyboard

def user_profile_buttons(tariff):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('📞 Связаться с менеджером'))
    if tariff != "Тариф Профессионал":
        keyboard.add(KeyboardButton('🔄 Перейти на новый тариф'))
    keyboard.add(KeyboardButton('Назад'))
    return keyboard

def start_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('👤 Мой профиль'))
    keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('📚 Полезные материалы'))
    keyboard.add(KeyboardButton('📞 Связаться с менеджером'))
    return keyboard

def development_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('👤 Мой профиль'))
    keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('📚 Полезные материалы'))
    keyboard.add(KeyboardButton('🔍 Проверка этапов'))
    keyboard.add(KeyboardButton('📞 Связаться с менеджером'))
    return keyboard

def professional_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('👤 Мой профиль'))
    keyboard.row(KeyboardButton('ChatGPT'), KeyboardButton('📚 Полезные материалы'))
    keyboard.add(KeyboardButton('📞 Связаться с менеджером'))
    return keyboard

def upgrade_buttons():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('🚀 Тариф Развитие', callback_data='upgrade_development'))
    keyboard.add(InlineKeyboardButton('💼 Тариф Профессионал', callback_data='upgrade_professional'))
    return keyboard

def back_button():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Назад'))
    return keyboard