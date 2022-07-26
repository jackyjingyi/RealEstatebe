from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoices(models.TextChoices):
    ADMIN = 'admin', _('管理员')
    REGION_ACCOUNT = 'region_account', _('战区账户')  # 拥有上传权限
    REGION_COMPANY_LEADER = 'region_company_leader', _('战区领导')
    CITY_ACCOUNT = 'city_account', _('城市设计公司')  # 无上传权限
    CO_LEADER = 'group_leader', _('集团领导')

