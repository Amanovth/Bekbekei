from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User, UserDetail


class UserDetailInline(admin.StackedInline):
    model = UserDetail
    extra = 1
    max_num = 1
    

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone",
                    "password",
                    "bonus_id",
                    "bonus",
                    "qrimg",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            _("Верификация"),
            {"fields": ("activated", "code",)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = ("id", "phone", "is_staff",)
    list_display_links = ("id", "phone",)
    search_fields = ("first_name", "last_name",)
    ordering = ("-id",)
    inlines = (UserDetailInline,)