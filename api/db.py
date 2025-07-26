from pymongo import MongoClient

MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["campuslink_db"]

users_col = db["users"]
announcements_col = db["announcements"]
complaints_col = db["complaints"]
timetable_col = db["timetables"]
lostfound_col = db["lostfound"]
