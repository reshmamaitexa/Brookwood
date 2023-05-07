from django.contrib import admin
from .models import Log,brookuser,complaint,product

# Register your models here.
admin.site.register(Log),
admin.site.register(brookuser),
admin.site.register(complaint),
admin.site.register(product),