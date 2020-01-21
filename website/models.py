from django.db import models

# Create your models here.
class Categorias(models.TextChoices):
    TECH = 'TC','Tecnologias'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(max_length=2,choices=Categorias.choices,default=Categorias.GR)
    approved = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts',default='posts/dj_default.jpg')
    def __str__(self):
        return self.title

    def full_name(self):
        return str(self.title)+" "+str(self.sub_title)
    #ordenando o campos de exibição do admin pelo title
    full_name.admin_order_field = "title"
