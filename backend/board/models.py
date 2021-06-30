from django.db import models



class PostVO(models.Model):
    # id = models.CharField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True
        db_table = 'posts'

    def __str__(self):
        return f'[{self.pk}] is username = {self.title},' \
               f'[{self.pk}] is password = {self.content},' \

