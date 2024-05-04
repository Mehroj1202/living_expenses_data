import json
import get_data
def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    a=list((get_data.get_data(file_path)).values())
    return sum(a)
print(total_expenses('data.json'))


# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
