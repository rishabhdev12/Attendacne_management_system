from django.db import models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    class_name = models.CharField(max_length=50)  # Renamed `class` to `class_name` to avoid conflicts with Python keywords
    lecture_hours = models.IntegerField()
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)  # Renamed `class` to `class_name` to avoid conflicts with Python keywords
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class AttendanceLog(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    present = models.BooleanField()
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"AttendanceLog for {self.student.full_name} in {self.course.course_name}"
