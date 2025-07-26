from mongoengine import Document, StringField, DictField, ReferenceField

class Timetable(Document):
    student = StringField(required=True, unique=True)  # Using username or id
    schedule = DictField()
