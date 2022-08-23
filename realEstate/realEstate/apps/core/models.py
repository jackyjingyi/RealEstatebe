from django.db import models
from django.utils.translation import gettext_lazy as _
from nanoid import generate


def nanoid_generate():
    return generate(size=10)


def buildings_image_upload_path_generate(instance, filename):
    return f'management/{instance.id}/{filename}'


def upload_path_generate1(instance, filename):
    return f'materials/{instance.id}/{filename}'


class ManagementFiles(models.Model):
    id = models.CharField(_('系统编码'), max_length=10, default=nanoid_generate, primary_key=True)
    name = models.CharField(_('名称'), max_length=100, default='')
    code = models.CharField(_('代码'), max_length=50, default='')
    file = models.FileField(_('文件'), upload_to=buildings_image_upload_path_generate)
    download_file = models.FileField(_('下载文件'), upload_to=buildings_image_upload_path_generate, null=True, blank=True)
    # seq =

    def __str__(self):
        return self.name


class Materials(models.Model):
    id = models.CharField(_('系统编码'), max_length=10, default=nanoid_generate, primary_key=True)
    name = models.CharField(_('名称'), max_length=100, default='')
    code = models.CharField(_('代码'), max_length=50, default='')
    file = models.FileField(_('文件'), upload_to=upload_path_generate1)
    cdn_url = models.TextField(_('cdn路径'), default='', blank=True, null=True)
    mtype = models.CharField(_('材料类型'), max_length=50, default='image')
    is_active = models.BooleanField(_('激活'), default=True)
    seq = models.IntegerField(_('顺序'), default=-1)
    mposition = models.CharField(_('位置'), max_length=25, default='slides')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['seq']
