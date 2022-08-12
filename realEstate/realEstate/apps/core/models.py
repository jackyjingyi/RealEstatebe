from django.db import models
from django.utils.translation import gettext_lazy as _
from nanoid import generate


def nanoid_generate():
    return generate(size=10)


def buildings_image_upload_path_generate(instance, filename):
    return f'management/{instance.id}/{filename}'


class ManagementFiles(models.Model):
    id = models.CharField(_('系统编码'), max_length=10, default=nanoid_generate, primary_key=True)
    name = models.CharField(_('名称'), max_length=100, default='')
    code = models.CharField(_('代码'), max_length=10, default='')
    file = models.FileField(_('文件'), upload_to='')
