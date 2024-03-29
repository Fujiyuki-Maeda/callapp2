from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

def validate_title(value):
    try:
        int_value = int(value)
    except ValueError:
        raise ValidationError("半角の整数を入力してください!")

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True ,blank=True)
    title = models.CharField(max_length=100, validators=[validate_title])
    description = models.TextField(null=True,blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    #並び替えを行う[]内を変更することで並び替えの内容を変更できる
    class Meta:
        ordering = ["title"]
