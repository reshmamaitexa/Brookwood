from django.contrib import admin
from .models import Log,brookuser,product,feedback,complaint,cart,order

# Register your models here.
admin.site.register(Log),
admin.site.register(brookuser),
admin.site.register(product),
admin.site.register(feedback),
admin.site.register(complaint),
admin.site.register(cart),
admin.site.register(order)