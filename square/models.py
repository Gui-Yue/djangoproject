from django.db import models

# Create your models here.
class Title(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Content(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contents'

    def __str__(self):
        if len(self.text) >= 50:
            return self.text[:50] + '...'
        else:
            return self.text

