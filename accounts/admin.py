from django.contrib import admin
from accounts.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'zip_code', 'tag', 'receiver_name')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'image', 'gender', 'date_of_birth', 'phonenumber', 'introduce')



admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Profile, ProfileAdmin)