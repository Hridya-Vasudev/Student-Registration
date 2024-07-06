from rest_framework import serializers
from .models import *
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']  # Add more fields if needed

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    college = serializers.PrimaryKeyRelatedField(queryset=College.objects.all())
    work_experience = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'user', 'enquiry_no', 'enquiry_date', 'name', 'gender', 'qualification',
                  'address', 'college', 'contact_no', 'whatsapp_no', 'dob', 'has_work_experience', 'work_experience']

    def get_work_experience(self, obj):
        experiences = WorkExperience.objects.filter(student=obj)
        return WorkExperienceSerializer(experiences, many=True).data