from django.urls import path, include
from accounts.api import LoginAPI, UserAPI, TenantRegisterAPI, OwnerRegisterAPI, OwnerOnlyView, TenantOnlyView
from knox import views as knox_views

urlpatterns = [
    
    # REST FRAMEWORK ENDPOINTS
    path('api/auth/', include('knox.urls')),
    
    # CORE APP ENDPOINTS
    path('api/register/owner/', OwnerRegisterAPI.as_view(), name = 'owner-register'),
    path('api/register/tenant/', TenantRegisterAPI.as_view(), name = 'tenant-register'),
    
    # ACCOUNT APP ENDPOINTS
    path('api/login/', LoginAPI.as_view(), name='user-login'), # login endpoint url
    # path('api/auth/change-password/', ChangePasswordAPI.as_view(), name='change-password'),
    path('api/auth/user/', UserAPI.as_view(), name='user-details'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'), # KNOX LOGOUT
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'), # KNOX LOGOUT ALL   
    
    # DASHBOARD ENDPOINTS
    path('api/owner/dashboard/', OwnerOnlyView.as_view(), name='owner-dashboard'),
    path('api/tenant/dashboard/', TenantOnlyView.as_view(), name='tenant-dashboard'),
]