from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoices(models.TextChoices):
    ADMIN = 'admin', _('管理员')
    REGION_ACCOUNT = 'region_account', _('战区账户')
