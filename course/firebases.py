import pyrebase
from .confidentials.config import config

def firebase_upload(path_on_cloud,path_local):
# path_local = "../assets/foo.jpg"
# path_on_cloud = "foo.jpg"
    firebase = pyrebase.initialize_app(config=config)
    storage = firebase.storage()
    storage.child(path_on_cloud).put(path_local)


def firebase_download(path_on_cloud):
    firebase = pyrebase.initialize_app(config=config)
    storage = firebase.storage()
    k = storage.child(path_on_cloud).get_url(None)
    return k
# storage.child(path_on_cloud).download(download_file)

def firebase_delete(path_on_cloud):
    firebase = pyrebase.initialize_app(config=config)
    storage = firebase.storage()
    storage.child(path_on_cloud).delete(path_on_cloud)
    # storage.child().delete(path_on_cloud)

    