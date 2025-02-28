from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Card(models.Model):
    slug = models.SlugField(max_length = 200, unique = True, null = False, default ="")
    title = models.CharField('Название', max_length=60, null=False)
    image = models.ImageField('Картинка', upload_to='card_images/%Y-%m-%d/')
    price = models.FloatField('Цена')
    information = models.TextField('Информация', null = False, default ="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField('Имя пользователя', max_length=100)
    text = models.TextField('Ваш комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name