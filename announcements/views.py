# announcements/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializer

# Get All Announcements (any user)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_announcements(request):
    announcements = Announcement.objects.order_by('-created_at')
    serializer = AnnouncementSerializer(announcements, many=True)
    return Response(serializer.data)

# Admin: Create Announcement
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_announcement(request):
        # if not request.user.is_superuser:
        #     return Response({"error": "Unauthorized"}, status=403)

    serializer = AnnouncementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Announcement created!"})
    return Response(serializer.errors, status=400)


