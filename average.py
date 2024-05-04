import json
import get_data 
def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    

    a=list((get_data.get_data(file_path)).values())
    return sum(a)/len(a)
print(average_expenses(('data.json')))