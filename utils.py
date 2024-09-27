import requests
import numpy as np

def download_and_save_file(url, target_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(target_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print('ERROR occurred: ', e)


def create_year_list(start_year: int, end_year: int) -> np.ndarray[str]|None:
    if start_year and end_year:
        return np.arange(start_year, end_year+1).astype(str)
    return None