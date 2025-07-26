from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Timetable

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_or_update_timetable(request):
    try:
        username = request.user.username
        data = request.data.get("schedule")

        if not data:
            return Response({"error": "Schedule data is missing."}, status=400)

        timetable = Timetable.objects(student=username).first()
        if timetable:
            timetable.schedule = data
            timetable.save()
            return Response({"message": "Timetable updated successfully."})
        else:
            Timetable(student=username, schedule=data).save()
            return Response({"message": "Timetable saved successfully."})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student_timetable(request):
    try:
        username = request.user.username
        timetable = Timetable.objects(student=username).first()

        if timetable:
            return Response({"schedule": timetable.schedule}, status=200)
        else:
            return Response({"message": "No timetable found for this student."}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
