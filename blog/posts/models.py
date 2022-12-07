from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def _str_(self):
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=20)

    def _str_(self):
        return self.title

class Post(models.Model):
    tittle = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.IntegerField(default = 0)
    comment_count = models.IntegerField  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def _str_(self):
        return self.title