from django.contrib import admin
from accounts.models import Account, Role


admin.site.register(Account)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name']
    readonly_fields = ['id']


admin.site.register(Role, RoleAdmin)

