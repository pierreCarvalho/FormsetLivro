from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Livro, Dependente

class LivroAdmin(admin.ModelAdmin):
    pass
admin.site.register(Livro, LivroAdmin)

class DependenteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dependente, DependenteAdmin)