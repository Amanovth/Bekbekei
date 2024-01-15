from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User, RollRequest


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "roll_request",
                    "user_roll",
                    "phone",
                    "first_name",
                    "last_name",
                    "password",
                    "bonus_id",
                    "qrimg",
                )
            },
        ),
        (
            _("Детально"),
            {
                "fields": (
                    "email",
                    "birthday",
                    "gender",
                    "language",
                    "married",
                    "status",
                    "city",
                    "children",
                    "animal",
                    "car",
                ),
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
            {
                "fields": (
                    "activated",
                    "code",
                )
            },
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

    list_display = (
        "id",
        "phone",
        "is_staff",
    )
    list_display_links = (
        "id",
        "phone",
    )
    search_fields = (
        "first_name",
        "last_name",
        "phone",
        "email"
    )
    ordering = ("-id",)


@admin.register(RollRequest)
class RollRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'surname', 'date_time', 'roll']
    list_display_links = ['id', 'user']
    list_editable = ['roll']

