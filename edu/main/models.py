from django.db import models
from uuid import uuid4


class BaseUser(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=250)


class Student(BaseUser):
    cart = models.OneToOneField('Cart', on_delete=models.CASCADE)
    courses = models.ManyToManyField('Course', null=True, blank=True)
    wishlist = models.ManyToManyField('Course', null=True, blank=True)


class Course(models.Model):
    instructor = models.ForeignKey(
        'Instructor', on_delete=models.CASCADE, related_name='instructor')
    name = models.CharField(max_length=250)
    description = models.TextField()
    reviews_count = models.IntegerField()
    students_count = models.IntegerField()
    created_by = models.ForeignKey(
        'Instructor', on_delete=models.PROTECT, related_name='instructor')
    last_update = models.DateField(auto_now=True)
    requirements = models.TextField(null=True, blank=True)
    objectives = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, related_name='courses')
    welcome_message = models.CharField(max_length=250)


class Category(models.Model):
    name = models.CharField(max_length=250)
    courses_count = models.IntegerField()


class Review(models.Model):
    instructor = models.ForeignKey(
        'Instructor', on_delete=models.PROTECT, related_name='instructor')

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='reviews')

    student = models.ForeignKey(
        Student, on_delete=models.PROTECT, related_name='reviews')

    # TODO: how to make PROTECT while the at least
    # one of the three fields is still there?
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    body = models.TextField()


class Instructor(BaseUser):
    courses_count = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    reviews_count = models.IntegerField()
    students = models.ManyToManyField(Student, blank=True, null=True)
    students_count = models.IntegerField()
    bio = models.TextField(null=True, blank=True)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='student')
    courses = models.ManyToManyField(Course)
    total_price = models.IntegerField()


class CourseContent(models.Model):
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, related_name='content')


class Section(models.Model):
    course_content = models.ForeignKey(
        CourseContent, on_delete=models.CASCADE, related_name='sections')


class MaterialItem(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=250)
    # file TODO


class Question(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='questions')

    body = models.CharField(max_length=250)
    answered = models.BooleanField(default=False)


class Answer(models.Model):
    question = models.ForeignKey(
        Question, models.CASCADE, related_name='answer')
    body = models.CharField(max_length=250)
