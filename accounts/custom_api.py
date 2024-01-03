from rest_framework.views import APIView
from accounts.models import User

class GroupAPIView(APIView):
    queryset = User.objects.none()