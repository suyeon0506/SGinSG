from django.db import models

# Create your models here.

class Users(models.Model):
    UserName = models.CharField(max_length = 100)
    UserId = models.CharField(max_length = 20)
    UserPw = models.CharField(max_length = 20)
    UserAge = models.IntegerField()
    UserEmail = models.TextField()
    UserLike = models.IntegerField()
    
    def __str__(self):
        return [self.UserName, self.UserId, self.UserPw, self.UserAge, self.UserEmail, self.UserLike]