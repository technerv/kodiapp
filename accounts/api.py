from django.contrib.auth import login
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from knox.auth import AuthToken
from .permissions import IsOwnerPermission, IsTenantPermission
from knox.views import LoginView as KnoxLoginView
from .serializers import OwnerRegisterSerializer, TenantRegisterSerializer, UserSerializer, LoginSerializer
from accounts.models import User

# Owner Register API
class OwnerRegisterAPI(generics.GenericAPIView):
    serializer_class = OwnerRegisterSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "message": "Owner Account Created Successfully"
        })

# Tenant Register API
class TenantRegisterAPI(generics.GenericAPIView):
    serializer_class = TenantRegisterSerializer
    permission_classes = (permissions.AllowAny,)

    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "message": "Tenant Account Created Successfully"
        })

# OWNER ONLY VIEW    
class OwnerOnlyView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny&IsOwnerPermission,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
       
# TENANT ONLY VIEW
class TenantOnlyView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated&IsTenantPermission,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

# LOGIN API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # _, token = AuthToken.objects.create(user)
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# LOGOUT VIEW
class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

# User API
class UserAPI(generics.RetrieveAPIView):
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer
    
    def get(self, request):
        
        user = request.user
        
        if user.is_authenticated:
            return Response({
                'user_info': {
                'id': user.id,
                'email': user.email,
                'mobile': user.mobile_number  
            },
        })
        return Response({'error': 'not authenticated'}, status = 400)
    
    def get_queryset(self):
        return User.objects.all()

# # Change Password View API
# class ChangePasswordAPI(generics.UpdateAPIView):
#     serializer_class = ChangePasswordSerializer
#     model = User
#     # permission_classes = (IsAuthenticated,)
    
#     def get_object(self, queryset=None):
#         obj = self.request.user      
#         return obj
    
#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)
        
#         if serializer.is_valid():
#             # Check old password.
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong Password"]}, status = status.HTTP_400_BAD_REQUEST)
            
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data':[]
#             }
            
#             return Response(response)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)