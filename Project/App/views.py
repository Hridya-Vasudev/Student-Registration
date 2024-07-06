from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import StudentRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.conf import settings
import jwt
from .serializers import UserSerializer, StudentSerializer
from .models import Student

# Registration View
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('profile')
    else:
        user_form = UserCreationForm()
        student_form = StudentRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form, 'student_form': student_form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'profile.html', {'student': student})


class PracticeToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            if not username or not password:
                return Response({'status': 0, 'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                token_payload = {"username": user.username}
                token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm="HS256")

               
                user_serializer = UserSerializer(user)

                
                if hasattr(user, 'student'):
                    student_serializer = StudentSerializer(user.student)
                    serialized_data = {
                        "token": token,
                        "user": user_serializer.data,
                        "student": student_serializer.data,
                        "status": 1
                    }
                else:
                    serialized_data = {
                        "token": token,
                        "user": user_serializer.data,
                        "status": 1
                    }

                return Response(serialized_data, status=status.HTTP_200_OK)
            else:
                return Response({'status': 0, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print(f"Exception occurred: {e}")
            return Response({'status': 0, 'message': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.models import User
# import jwt
# from django.conf import settings 

# class PracticeToken(APIView):
#     def post(self, request, format=None):
#         try:
#             username = request.data.get('username')
#             password = request.data.get('password')

#             if not username or not password:
#                 return Response({'status': 0, 'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 auth_login(request, user)
#                 token_payload = {"username": user.username}
#                 token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm="HS256")

#                 data = {
#                     "token": token,
#                     "status": 1
#                 }
#                 return Response(data, status=status.HTTP_200_OK)
#             else:
#                 return Response({'status': 0, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#         except Exception as e:
#             print(f"Exception occurred: {e}")
#             return Response({'status': 0, 'message': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)