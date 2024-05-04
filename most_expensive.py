import json
import get_data
def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    a=list((get_data.get_data(file_path)).values())
    b=list((get_data.get_data(file_path)).keys())
    k=max(a)
    l=a.index(k)
    return b[l]
print(most_expensive('data.json'))

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)