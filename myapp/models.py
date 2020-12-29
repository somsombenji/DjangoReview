from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('data published') #날짜와 시간을 나타내는 데이터 필드
    body = models.TextField() #CharField보다 긴 글

    def __str__(self):
        return self.title