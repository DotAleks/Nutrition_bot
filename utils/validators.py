from typing import Tuple

def is_number(value:str):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def is_valid_weight(number: str) -> Tuple[str, bool]:
    if is_number(number):
        temp = float(number)
        if temp <= 0:
            return "Вес не может быть меньше или равен 0", False
        elif temp < 30:
            return "Вес не может быть меньше 30 кг", False
        elif temp > 200:
            return "Вес не может быть больше 200 кг", False
        else:
            return number, True
    else:
        return "Введите число",False
    
def is_valid_water(number: str) -> Tuple[str|float, bool]:
    if is_number(number):
        temp = float(number)
        if temp <= 0:
            return "Вода не может быть меньше или равна 0!", False
        elif temp > 30_000:
            return "Нельзя за раз выпить столько воды!", False
        else:
            return temp, True
    else:
        return "Введите число",False
    