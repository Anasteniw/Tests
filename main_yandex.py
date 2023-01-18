import requests

TOKEN = '......'
token =TOKEN
load_url = "https://cloud-api.yandex.net/v1/disk/resources"

  

def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
            'Authorization': token}
    create_fold = requests.put(load_url, headers=headers, params=params)
    return create_fold.status_code

    
def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
            'Authorization': token}
    delete_fold = requests.delete(load_url, headers=headers, params=params)
    return delete_fold.status_code