function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function firebaseUpload(element,clout_path) {
    var firebaseConfig = {
        apiKey: "AIzaSyDpL_jangAHa-fNG7_UOzaKSBQyH2lOpOM",
        authDomain: "coursecompanion.firebaseapp.com",
        databaseURL:"https://coursecompanion/firebaseio.com",
        projectId: "coursecompanion",
        storageBucket: "coursecompanion.appspot.com",
        messagingSenderId: "502681390731",
        appId: "1:502681390731:web:bcbf9a4154d76a36c34e8e",
        measurementId: "G-BP0GSF1CL1"
    };
    firebase.initializeApp(firebaseConfig);

    var storage = firebase.storage();

    var file = document.getElementById("upload")

        var file = element.files[0]
        var storageRef = firebase.storage().ref(clout_path)
        storageRef.put(file);
    }

    function lookup(endpoint,method,data,callback) {
        if (data) data = JSON.stringify(data)
        const xhr = new XMLHttpRequest()
        xhr.responseType = 'json'
        xhr.open(method,endpoint)
        xhr.setRequestHeader('Content-Type','application/json')
        xhr.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest")
        xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
        xhr.setRequestHeader('X-CSRFToken',getCookie('csrftoken'))
        xhr.onload = () =>{
            console.log(xhr.response,xhr.status)
            if (xhr.status===201 || xhr.status===200){
                callback(xhr.response,xhr.status)
            }
        }
        xhr.send(data)
    }

