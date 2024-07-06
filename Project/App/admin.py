from django.contrib import admin

# Register your models here.
from .models import Student, College, Course, WorkExperience
class StudentAdmin(admin.ModelAdmin):
    list_display = ['enquiry_no', 'name', 'college', 'contact_no']
    search_fields = ['enquiry_no', 'name', 'college__name', 'contact_no']
    list_filter = ['gender', 'qualification', 'has_work_experience']

admin.site.register(Student,StudentAdmin)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(WorkExperience)