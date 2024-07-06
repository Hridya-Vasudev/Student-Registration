from django.urls import path
from . import views
from .views import StudentListAPIView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('api/login/', views.PracticeToken.as_view(), name='api_login'),
    path('api/students/', StudentListAPIView.as_view(), name='student-list'),
    path('api/token/', views.PracticeToken.as_view(), name='token_obtain'),
]