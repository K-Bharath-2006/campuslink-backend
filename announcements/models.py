from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class Announcement(Document):
    title = StringField(required=True)
    message = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'ordering': ['-created_at'],
        'indexes': [
            {
                'fields': ['created_at'],
                'expireAfterSeconds': 2592000 
            }
        ]
    }

    def __str__(self):
        return f"{self.title} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
