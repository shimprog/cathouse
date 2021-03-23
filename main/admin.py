from django.contrib import admin
from .models import Product, News, Obratnaya, Svoyamodel, Materialimodel, Zakazmodel

# Register your models here.
admin.site.register(Product)
admin.site.register(News)
admin.site.register(Obratnaya)
admin.site.register(Svoyamodel)
admin.site.register(Materialimodel)
admin.site.register(Zakazmodel)
