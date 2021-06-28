from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()


    class Meta:
        managed = True
        db_table = 'members'