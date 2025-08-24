import os
from dotenv import load_dotenv

# TODO: Добавить логирование:
# Green(Токен получен) || Red(Токен не получен по ошибке + {error.message})


def get_api_token() -> str:
    """
    Функция получения API токена от бота

    Токен ищется в переменных окружения после загрузки из .env файла.

    Returns:
        str: API_TOKEN
    Raises:
        FileNotFoundError: Если файл не найден
        PermissionError: Если нет прав на чтение файла
        SyntaxError: Если токен имеет неверный формат
        ValueError: Если токен пустой или невалидный
    """
    try:
        if not load_dotenv():
            raise FileNotFoundError("File .env not found!")
    except PermissionError:
        raise PermissionError("Access error to .env file!")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("utf-8", b"", 0, 1, "Invalid encoding in .env file!")
    except SyntaxError as e:
        raise SyntaxError(f"Syntax error in .env file: {e.msg}")

    API_TOKEN = os.getenv("API_TOKEN")
    if API_TOKEN is None or not API_TOKEN.strip():
        raise ValueError("API_TOKEN environment variable is not set!")

    return API_TOKEN
