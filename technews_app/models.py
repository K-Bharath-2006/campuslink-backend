from mongoengine import Document, StringField, DateTimeField, URLField
from datetime import datetime

class TechNews(Document):
    title = StringField(required=True, max_length=255)
    description = StringField(required=True)
    application_link = URLField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'ordering': ['-created_at']
    }

    def __str__(self):
        return f"{self.title} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
