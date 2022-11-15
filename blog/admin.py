from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from .models import Post
from .models import Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # model = CustomUser
    list_display = ["email", "username",]
    
admin.site.register(Post)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

