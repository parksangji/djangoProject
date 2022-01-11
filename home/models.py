from django.db import models
from django.urls import reverse

# Create your models here.

class cat(models.Model):
    cat_name = models.CharField(max_length=50,help_text="고양이의 종류를 입력하세요")
    cat_image = models.ImageField(blank = True)
    cat_info = models.TextField(help_text="고양이를 설명해주세요")
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name
    #1번 글의 경우 ->cat/1
    def get_absolute_url(self):
        return reverse("cat", args=[str(self.id)])
    def is_content_more100(self):
        return len(self.cat_info) > 300
    def get_content_under100(self):
        return self.cat_info[:100]
    

