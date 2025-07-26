from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TechNews
from datetime import datetime

# Manual serializer
def serialize_technews(obj):
    return {
        "id": str(obj.id),
        "title": obj.title,
        "description": obj.description,
        "application_link": obj.application_link,
        "created_at": obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }

# 🔹 Get all TechNews (student + admin)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_technews(request):
    tech_news = TechNews.objects.order_by('-created_at')
    serialized = [serialize_technews(tn) for tn in tech_news]
    return Response(serialized)

# 🔹 Admin: Create TechNews
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_technews(request):
    data = request.data
    title = data.get("title")
    description = data.get("description")
    application_link = data.get("application_link")

    # Basic validation
    if not title or not description or not application_link:
        return Response({"error": "All fields are required."}, status=400)

    tech_news = TechNews(
        title=title,
        description=description,
        application_link=application_link,
        created_at=datetime.utcnow()
    )
    tech_news.save()
    return Response({"message": "Tech News created successfully!"})
