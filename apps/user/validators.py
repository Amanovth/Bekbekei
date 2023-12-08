from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    if len(value) != 19:
        raise ValidationError(
            _("Введите парвильный номер"),
            params={"value": value},
        )
