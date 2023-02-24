import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendacerealtime-75e2a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "RA2111003010742":
        {
            "name": "Albi Thomson K",
            "dept": "CSE CORE",
            "total_attendance": 11,
            "sec": "K1",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "RA2111003010745":
        {
            "name": "Eswara",
            "dept": "CSE CORE",
            "total_attendance": 12,
            "sec": "K1",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
     "RA2111003010748":
        {
            "name": "Akash B",
            "dept": "CSE CORE",
            "total_attendance": 13,
            "sec": "K1",
            "last_attendance_time": "2022-12-11 00:54:34"
        }


}
for key, value in data.items():
    ref.child(key).set(value)
    