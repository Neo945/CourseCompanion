import pyrebase

config = {
    "apiKey": "AIzaSyDpL_jangAHa-fNG7_UOzaKSBQyH2lOpOM",
    "authDomain": "coursecompanion.firebaseapp.com",
    "databaseURL":"https://coursecompanion/firebaseio.com",
    "projectId": "coursecompanion",
    "storageBucket": "coursecompanion.appspot.com",
    "messagingSenderId": "502681390731",
    "appId": "1:502681390731:web:bcbf9a4154d76a36c34e8e",
    "measurementId": "G-BP0GSF1CL1"
}
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