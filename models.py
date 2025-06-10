from django.db import models
from django.contrib.auth.models import User


class PlantQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plant_queries')
    image = models.ImageField(upload_to='plant_images/')
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Plant query by {self.user.username} at {self.created_at}"