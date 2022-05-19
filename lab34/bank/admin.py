from django.contrib import admin
from .models import Bank, Manager, Client,User

admin.site.register(Bank)
admin.site.register(Manager)
admin.site.register(Client)
admin.site.register(User)
