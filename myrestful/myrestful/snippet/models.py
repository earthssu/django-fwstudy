from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()


    class Meta:
        ordering = ['created']