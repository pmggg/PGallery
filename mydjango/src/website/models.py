from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        username = "Username: " + self.name 
        e_mail = "\ne-mail: " + self.email[0]+ "****"
        text = "\nComment: " + self.comment+ "\n______________________________________________________________________"
        return  username + e_mail + text