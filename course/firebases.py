import pyrebase

config = {
    "apiKey": "AIzaSyDpL_jangAHa-fNG7_UOzaKSBQyH2lOpOM",
    "authDomain": "coursecompanion.firebaseapp.com",
    "databaseURL":"https://coursecompanion/firebaseio.com",
    "projectId": "coursecompanion",
    "storageBucket": "coursecompanion.appspot.com",
    "messagingSenderId": "502681390731",
    "appId": "1:502681390731:web:bcbf9a4154d76a36c34e8e",
    "measurementId": "G-BP0GSF1CL1",
    "serviceAccount":{
        "type": "service_account",
        "project_id": "coursecompanion",
        "private_key_id": "278a7bc11885f6bc5b5706c8fd9323bb5513d9d3",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDhEpsxt1hKUW/K\nop1WVwYLGvxXYIRxgKR8iOvb4PhqasyUBs7+W4mieLiPcNad/gE/ULAjBhuj6t4S\ni894yhBE2HMoX4Ay8reW1BU2DQKn2SAoztOYPCeRJFDW8GoSTzZp544eGpW4126F\nE3XPqasxgzdzPM3OgQqydGaT2ybEtFTY6coybIcY1A/NQYka2GHEsIgxlj+4wRWx\neqjp1ewjxsZuTnOLuEvVss73qhKDozmvVIxOpG5z+onJcJHOGrfeSs1hh4J1se6p\n9sjMPgD9MDLyAkSTZgXzD7aLKDRAVSu3ZsBnnmdTKpdKsvj9gu/L1AJgx1AwYMpp\nM2AjpVAnAgMBAAECggEAOvaV47tljOqyv8JEN8dKlQQ30Wg+qkGKVfnE2HCig7aA\n69KwzaALeZ3os+Naxj8x8nVf/3ztJs8z6GXqL3m4M2EFIjGKs0403HWpLOTRqklO\njIJKmpo/v11lNDn9f9hyp+H6sFZEnQ0LLh/AAGwxpiH7F9x5Cj1yIPgvm1KRYHxj\nrYB8ltvd55t6nCccODX/HD8arx2tEw0K5rp4KuCBpp+jXU+D08jepQ5W/YQij7Ys\ndf5QovO6+reh9dUi5FfKO7aLhZqraG9sbuUnmf3DH7dhEz/Ex/5nbZqWyeDxU75s\n8bxKB6/QlQsTsJ9H3Z/T+tzjBcgBPbvphTKSzL4f8QKBgQD/lmp6QB+NwyN+cj8X\nFfncAyxExEX/W8x+2r4qH0Sk+K6bIxKTUZvZ4jsGPXl44nNJBATYxGwxsjPV8d7J\ni5LiSHqJ4T0Yi8/p48Y3c94Cv0i+dgW9WC7dRMzll4rgxyZmDD19xwgWuS8wcNrd\nF7GUrPmiYUzKEkEgIVmBb3t9SQKBgQDhb5Wh0L66/IiW2RzU4uoiD2BniYTaaJV9\nerPdFKnA2g0PlzwoOc1xQFjfrUaAq+1Fs6ojvPhJbJzWnx3ToShxUaF0sF/esRsZ\nLpmPjcOvA8KdMh8mcz8o3AlJCNnrbpHup8mzpmPDkHWReEysOAJykIiMH5SpbgrN\nK3mMKz2R7wKBgEVQGG4w5529Vunat8td9VW6Mo4voEABODMKxVmNA0OuAUQnPclf\n72EmXhVyJHgpCVS610ml8yWDC1Ww81c7F8lwGHM99yCqAeePEtlE/edG0sZ8IVBZ\nEtSE7QAymcIdoAc6uI5cpI/tBqQfZutgmpMUWdq0gmumiazZ/nkAr7+pAoGAJjoO\nrH7CKODzpGiye+Lygs4KsePe1E5RsxJgd4eudVZESrWBbOzISoD30Q4H23/L3zrl\nCeRcUc8KFVar7xvvyK9n6mqSBygPCUkenvoSCZZgpNk/8Pwv5JTTOkA2+7YnJsnq\n6Py5BAt19DHrBnUE7TpW/TPJuKVBTaMmnD8k1J8CgYAlhVFK8BNEwDM3mpYajhDX\n4mYRn901mFJnO9MShRQFK5Ug5Yoc7tE5rbK2VTiNJVnBGMdEnwHsxR+viAOTg68D\nrREbNR5+T/CsX5alBIZRaxNFwEu3kaPuY064LDkhYJZl0fCVgmwCeHyT5tHfdLro\nFHwY2Aoce5c4nPcytpmO6A==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-lsuzq@coursecompanion.iam.gserviceaccount.com",
        "client_id": "100336770293465489760",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lsuzq%40coursecompanion.iam.gserviceaccount.com"
        }
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

def firebase_delete(path_on_cloud):
    firebase = pyrebase.initialize_app(config=config)
    storage = firebase.storage()
    storage.child(path_on_cloud).delete(path_on_cloud)
    # storage.child().delete(path_on_cloud)

    