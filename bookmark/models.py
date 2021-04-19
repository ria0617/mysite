from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark (models.Model):
    # 프라이머리키가 없으면 자동으로 1씩 증가하는 프라이머리키 id를 만들어준다.
    title = models.CharField('TITLE', max_length=100, blank=True, )
    url = models.URLField('URL', unique=True)
    
    #편집기능
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    
    def __str__(self):
        return "%s %s" %(self.title, self.url)
    
    