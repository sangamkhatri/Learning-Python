"""Assume the existence of a function named check_uv_level with the method header below:

def check_uv_level(n : int) -> str:

Call the check_uv_level function with the value 10 and assign the result to a variable named uv_level"""


def check_uv_level(uv_index):
    if uv_index < 3:
        return "Low risk"
    elif uv_index < 6:
        return "Moderate risk"
    elif uv_index < 8:
        return "High risk"
    elif uv_index < 11:
        return "Very high risk"
    else:
        return "Extreme risk"


print(check_uv_level(3))
