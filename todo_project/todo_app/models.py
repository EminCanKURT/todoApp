from django.db import models
from datetime import datetime

# Create your models here.
class TOdos(models.Model):
    title = models.CharField(max_length=100)#başlıgımız
    description = models.TextField(max_length=1000,blank=True)#acıklamamız blank=true yazınca ıstersek bos bırakabılırz demek am yazmazsak zorunlu doldurman lazım
    finished = models.BooleanField(default=False)#true yapınca default olarak true gelıyor demek oyuzde false yapalımki biizm projemızde olup olmadıgı bellı degıl cunku
    date = models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.title
