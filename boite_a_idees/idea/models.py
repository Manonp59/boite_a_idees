from django.db import models
from django.utils import timezone
from main.models import User

class Idea(models.Model):
    titre = models.CharField(max_length=30,null=False,blank=False,unique=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    date = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    likes = models.IntegerField(default=0,null=True)
    dislikes = models.IntegerField(default=0,null=True)
    
    def __str__(self) -> str:
        return f"{self.titre} - {self.user}"

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    idea = models.ForeignKey(Idea,on_delete=models.CASCADE,related_name="idea_likes")


class Dislikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_dislikes")
    idea = models.ForeignKey(Idea,on_delete=models.CASCADE,related_name="idea_dislikes")
