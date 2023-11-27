from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_complete = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, related_name="tasks", blank=True)

    class Meta:
        ordering = ["-date_of_creation"]

    def __str__(self):
        return self.name

    def check_deadline(self):
        if self.date_of_complete:
            return self.date_of_complete <= self.deadline
        return False
