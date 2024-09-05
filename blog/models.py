from django.conf import settings
from django.db import models
from django.utils import timezone

# class means we're defining an object, in this case, the model
# Post is the name of the model
# models.Model means that Post is a Django Model, so it knows that it should be saved in the database

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title