from django.contrib import admin

from .models import Citizen
from .models import Workers

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name', 'age', 'Status', 'Salary') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('name',) 


admin.site.register(Citizen) 
admin.site.register(Workers) 
