import json
import get_data

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    a=list((get_data.get_data(file_path)).values())
    b=list((get_data.get_data(file_path)).keys())
    k=min(a)
    l=a.index(k)
    return b[l]
print(least_expensive('data.json'))
# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
