from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    #not inheriting only creating relationship
    contact_Number=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.user.username
