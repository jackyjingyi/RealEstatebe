from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, UserManager, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from nanoid import generate
from .config import RoleChoices


def nanoid_generate():
    return generate(size=24)


class IAMUser(models.Model):
    id = models.CharField(_('用户ID'), max_length=25, default=nanoid_generate, primary_key=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        validators=[username_validator],
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    password = models.CharField(_('IAM密码'), max_length=32, null=True, blank=True)
    access_key = models.CharField(max_length=255, null=True, blank=True)
    secret_key = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(choices=RoleChoices.choices, verbose_name=_('role'), max_length=25)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(_('用户ID'), max_length=25, default=nanoid_generate, primary_key=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    name = models.CharField(_("name"), max_length=150, blank=True)  # 中文名称
    role = models.CharField(choices=RoleChoices.choices, verbose_name=_('role'), max_length=25)
    access_key = models.CharField(max_length=255, null=True, blank=True)
    secret_key = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(_('战区'), max_length=50, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='users', related_query_name='user',
                                null=True, blank=True)
    company_name = models.CharField(_('公司'), max_length=255, null=True, blank=True)
    iam_username = models.CharField(_('IAM账户名'), max_length=100, null=True, blank=True)
    is_test = models.BooleanField(_('测试账户'), default=False)
    oa_account = models.CharField(_('OA账户'), max_length=50, null=True, blank=True, unique=True, db_index=True)
    phone = models.CharField(_('电话'), max_length=50, null=True, blank=True, unique=True, db_index=True)
    iam_password = models.CharField(_('IAM密码'), max_length=32, null=True, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_admin = models.BooleanField(default=False)
    iam_account = models.ManyToManyField(
        IAMUser, related_name='users', related_query_name='user'
    )

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s" % self.name
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.name

    def __str__(self):
        return self.name + " | " + str(self.username)


class Company(models.Model):
    id = models.CharField(_('组织ID'), max_length=25, default=nanoid_generate, primary_key=True)
    name = models.CharField(_('公司名称'), max_length=150, db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children',
                               related_query_name='child')
    org_code = models.CharField(_('组织代码'), unique=True, max_length=25)
    date_joined = models.DateTimeField(_("加入时间"), default=timezone.now)
    is_active = models.BooleanField(_('激活'), default=True)
    is_dept = models.BooleanField(_('是否部门'), default=False)
    is_deleted = models.BooleanField(_('已删除'), default=False)
    expire_dt = models.DateTimeField(_("过期时间"), null=True)

    def __str__(self):
        return self.name
