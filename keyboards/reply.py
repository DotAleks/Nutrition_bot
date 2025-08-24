from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# TODO: Добавить логирование:
# Green(Клавиатура создана) || Red(Клавиатура не создана по ошибке + {error.message})

def main_menu_kb() -> ReplyKeyboardMarkup:
    """
    Функция создания главной reply-клавиатуры.

    Returns:
        ReplyKeyboardMarkup: Объект клавиатуры для главного меню

    Raises:
        TypeError: При ошибках валидации параметров клавиатуры
        ValueError: При некорректных значениях параметров
        Exception: При любых других непредвиденных ошибках
    """
    builder = ReplyKeyboardBuilder()
    
    try:
        builder = ReplyKeyboardBuilder()
        
        builder.add(KeyboardButton(text="Text"))
        builder.adjust(1)
        
        return builder.as_markup(
            resize_keyboard=True, 
            input_field_placeholder="Нажмите на кнопку"
        )
        
    except TypeError:
        return builder.as_markup()
        
    except ValueError:
        return builder.as_markup()
        
    except Exception:
        return builder.as_markup()