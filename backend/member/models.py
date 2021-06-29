from django.db import models


class Member(models.Model):
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()


    class Meta:
        managed = True
        db_table = 'members'

    def __str__(self):
        return f'[{self.pk}] is username = {self.username},' \
               f'[{self.pk}] is password = {self.password},' \
               f'[{self.pk}] is name = {self.name},' \
               f'[{self.pk}] is email = {self.email},'\
