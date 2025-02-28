from django.contrib import admin
from .models import Card, Category
from django.template.defaultfilters import slugify

admin.site.register(Card)
admin.site.register(Category)


class CardAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'price']
    list_filter = ['title', 'price']
    prepopulated_fields = {'slug':('title',)}

    def save(self,*args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
            super(Card,self).save(*args, **kwargs)
# Register your models here.
