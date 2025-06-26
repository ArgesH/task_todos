from django.db import models
from django.db.model import AbstractUser

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')  # files go into MEDIA_ROOT/photos/ -> /media/photos/

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"Director - {self.name}"


class Manager(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    title = models.CharField(max_length=100)
    director = models.ForeignKey(Director, related_name="managers", on_delete=models.CASCADE)

    def __str__(self):
        return f"Manager - {self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    title = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, related_name="employees", on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Manager, related_name="supervisor_employees", on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee - {self.name}"


class CustomUser(AbstractUser):
    rol = models.CharField(max_length=100, choices=[("dev", "Developer"), ("pm", "Project Manager")], default="dev")


class Employee(models.Model):
    user_id = model.OneToOneField(CustomUser, related_name="employee", on_delete=models.CASCADE)


class Project(models.Model):
    employees = models.ManyToManyField(Employee, related_name="projects", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    upwork_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=[("draft", "Draft"), ("Done", "Done")], default="draft")


class Task(models.Model):
    project_id = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    main_employee = models.ForeignKey(Employee, related_name="main_tasks", on_delete=models.CASCADE)
    pair_employee = models.ForeignKey(Employee, related_name="pair_tasks", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=[("draft", "Draft"), ("Done", "Done")], default="draft")
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=100, choices=[("draft", "Draft"), ("Done", "Done")], default="draft")
    story_points = model.CharField(max_length=100, choices=[("draft", "Draft"), ("Done", "Done")], default="draft")


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name="comments", on_delete=model.CASCADE)

