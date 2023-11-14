from django.db import models
from users.models import User


# Create your models here.
class Advert(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def get_comments(self):
        return [comment.text for comment in self.comments.all()]


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        unique_together = ('user', 'advert')



