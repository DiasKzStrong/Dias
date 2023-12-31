from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [

    path('token-obtain/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('token-refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    path('token-verify/',TokenVerifyView.as_view(),name='token-verify'),

]