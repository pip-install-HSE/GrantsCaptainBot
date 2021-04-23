from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def get_face_keyboard() -> InlineKeyboardMarkup:
    """
    Возвращает инлайн клавиатуру, на которой пользователь выбирает, является он юр лицом или физ лицом
    :return:
    """
    individual_person_btn = InlineKeyboardButton(text='Юридическое лицо', callback_data='face_individual')
    legal_person_btn = InlineKeyboardButton(text='Физическое лицо', callback_data='face_legal')
    keyboard = InlineKeyboardMarkup()
    keyboard.row(*(individual_person_btn, legal_person_btn))
    return keyboard


def get_support_keyboard() -> InlineKeyboardMarkup:
    """
    Возвращает инлайн клавиатуру с типами поддержки из бд
    :return:
    """
    support_btn1 = InlineKeyboardButton(text='Направление поддержки 1', callback_data='support_IT')
    support_btn2 = InlineKeyboardButton(text='Направление поддержки 2', callback_data='support_Science')
    support_btn3 = InlineKeyboardButton(text='Направление поддержки 3', callback_data='support_Education')
    support_btn4 = InlineKeyboardButton(text='Направление поддержки 4', callback_data='support_Business')
    support_btn5 = InlineKeyboardButton(text='Направление поддержки 5', callback_data='support_Ecology')

    keyboard = InlineKeyboardMarkup()
    keyboard.add(*(support_btn1, support_btn2))
    keyboard.add(*(support_btn3, support_btn4))
    keyboard.add(support_btn5)
    return keyboard


def get_permanent_keyboard() -> ReplyKeyboardMarkup:
    """
    Возвращает основную клавиатуру с двумя кнопками 'О проекте' и 'Поддержать проект'
    :return:
    """
    about_project_btn = KeyboardButton(text='О проекте')
    support_project = KeyboardButton(text='Поддержать проект')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*(about_project_btn, support_project))
    return keyboard
