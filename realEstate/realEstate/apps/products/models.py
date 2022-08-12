from django.db import models
from nanoid import generate
from django.utils.translation import gettext_lazy as _


# 产品库

def nanoid_generate():
    return generate(size=10)


def buildings_image_upload_path_generate(instance, filename):
    return f'buildings/{instance.region}/{instance.product_type}/image/{instance.product_code}-{instance.id}/{filename}'


def buildings_thumbnail_upload_path_generate(instance, filename):
    return f'buildings/{instance.region}/{instance.product_type}/thumbnail/{instance.product_code}-{instance.id}/{filename}'


def house_image_upload_path_generate(instance, filename):
    return f'house/{instance.building.region}/image/{instance.product_code}-{instance.id}/{filename}'


def house_thumbnail_upload_path_generate(instance, filename):
    return f'house/{instance.building.region}/thumbnail/{instance.product_code}-{instance.id}/{filename}'


class BuildingProduct(models.Model):
    id = models.CharField(_('系统编码'), max_length=10, default=nanoid_generate, primary_key=True)
    product_code = models.CharField(_('产品编码'), max_length=100)
    region = models.CharField(_('地区'), max_length=50)
    product_type = models.CharField(_('产品类型'), max_length=50)
    staircase_ratio = models.CharField(_('梯户比'), max_length=25, blank=True, null=True)
    house_type_combination = models.CharField(_('户型租户'), max_length=150, blank=True, null=True)
    source = models.CharField(_('户型来源'), max_length=255, blank=True, null=True)
    applicable_area = models.CharField(_('适用地区'), max_length=150, blank=True, null=True)
    residential_type = models.CharField(_('住宅类型'), max_length=100, blank=True, null=True)
    building_attr = models.CharField(_('楼型特征'), max_length=255, blank=True, null=True)
    core_bucket_feature = models.CharField(_('核心筒特征'), max_length=255, blank=True, null=True)
    storey_type = models.CharField(_('层数类型'), max_length=255, blank=True, null=True)
    insulation_area = models.CharField(_('保温地区'), max_length=255, blank=True, null=True)
    up_floors = models.CharField(_('地上层数'), max_length=255, blank=True, null=True)
    applicable_product_line = models.CharField(_('适用产品线'), max_length=255, blank=True, null=True)
    window_floor_ration = models.FloatField(_('窗地比'), blank=True, null=True)
    wall_floor_ration = models.FloatField(_('窗地比'), blank=True, null=True)
    standard_floor_area = models.FloatField(_('窗地比'), blank=True, null=True)
    pool_area = models.FloatField(_('公摊面积'), blank=True, null=True)
    core_area = models.FloatField(_('核心筒面积'), blank=True, null=True)
    standard_floor_width = models.FloatField(_('标准层面宽'), blank=True, null=True)
    standard_floor_depth = models.FloatField(_('标准层进深'), blank=True, null=True)
    value_point = models.TextField(_('价值点'), blank=True, null=True)
    remark = models.TextField(_('备注'), blank=True, null=True)
    rate = models.FloatField(_('评分'))
    is_finished = models.BooleanField(_('已落地项目'), default=True)
    bucket_dir = models.TextField(_('桶文件夹地址'), null=True, blank=True)
    bucket_pdf = models.CharField(_('桶pdf文件地址'), max_length=255, null=True, blank=True)
    bucket_dwg = models.CharField(_('桶dwg文件地址'), max_length=255, null=True, blank=True)
    image_url = models.TextField(_('详情图地址'), null=True, blank=True)
    thumbnail_url = models.TextField(_('缩略图地址'), null=True, blank=True)
    image = models.ImageField(_('详情图'), null=True, blank=True, upload_to=buildings_image_upload_path_generate)
    thumbnail = models.ImageField(_('缩略图'), null=True, blank=True, upload_to=buildings_thumbnail_upload_path_generate)

    def get_rate(self):
        if self.is_finished:
            return str(self.rate)
        else:
            return f"{str(self.rate)}(+7)"

    class Meta:
        db_table = 'building_code'

    def __str__(self):
        return self.product_code


class House(models.Model):
    id = models.CharField(_('系统编码'), max_length=10, default=nanoid_generate, primary_key=True)
    building = models.ForeignKey(BuildingProduct, on_delete=models.CASCADE, related_query_name='houses',
                                 related_name='house')
    product_code = models.CharField(_('产品编码'), max_length=100)
    position = models.CharField(_('户型部位'), max_length=100)
    staircase_ratio = models.CharField(_('梯户比'), max_length=25, blank=True, null=True)
    house_type = models.CharField(_('房型配置'), max_length=100, blank=True, null=True)
    source = models.CharField(_('房型来源'), max_length=100, blank=True, null=True)
    south_rooms = models.IntegerField(_('朝南开间数'), default=0, blank=True, null=True)
    unit_capacity_area = models.FloatField(_('户型计容面积（㎡）'), default=0, blank=True, null=True)
    unit_usable_area = models.FloatField(_('户型套内面积（㎡）'), default=0, blank=True, null=True)
    unit_selling_area = models.FloatField(_('户型销售面积（㎡）'), default=0, blank=True, null=True)
    usable_rate = models.FloatField(_('得房率'), default=0, blank=True, null=True)
    width = models.FloatField(_('面宽-轴线（m）'), default=0, blank=True, null=True)
    depth = models.FloatField(_('进深-轴线（m）'), default=0, blank=True, null=True)
    house_detail = models.JSONField(_('户型级配'), default=dict)
    bucket_dir = models.TextField(_('桶文件夹地址'), null=True, blank=True)
    bucket_pdf = models.CharField(_('桶pdf文件地址'), max_length=255, null=True, blank=True)
    bucket_dwg = models.CharField(_('桶dwg文件地址'), max_length=255, null=True, blank=True)
    image_url = models.TextField(_('图片文件地址'), null=True, blank=True)
    thumbnail_url = models.TextField(_('缩略图文件地址'), null=True, blank=True)
    image = models.ImageField(_('详情图'), null=True, blank=True, upload_to=house_image_upload_path_generate)
    thumbnail = models.ImageField(_('缩略图'), null=True, blank=True, upload_to=house_thumbnail_upload_path_generate)
    balcony_depth = models.FloatField(_('阳台-进深'), default=0, blank=True, null=True)
    balcony_width = models.FloatField(_('阳台-开间'), default=0, blank=True, null=True)
    hallway_depth = models.FloatField(_('玄关-进深'), default=0, blank=True, null=True)
    hallway_width = models.FloatField(_('玄关-开间'), default=0, blank=True, null=True)
    kitchen_depth = models.FloatField(_('厨房-进深'), default=0, blank=True, null=True)
    kitchen_width = models.FloatField(_('厨房-开间'), default=0, blank=True, null=True)
    living_room_depth = models.FloatField(_('客厅-进深'), default=0, blank=True, null=True)
    living_room_width = models.FloatField(_('客厅-开间'), default=0, blank=True, null=True)
    function_room_depth = models.FloatField(_('多功能房-进深'), default=0, blank=True, null=True)
    function_room_width = models.FloatField(_('多功能房-开间'), default=0, blank=True, null=True)
    master_bedroom_depth = models.FloatField(_('主卧-进深'), default=0, blank=True, null=True)
    master_bedroom_width = models.FloatField(_('主卧-开间'), default=0, blank=True, null=True)
    second_bedroom_depth = models.FloatField(_('次卧-进深'), default=0, blank=True, null=True)
    second_bedroom_width = models.FloatField(_('次卧-开间'), default=0, blank=True, null=True)
    master_bathroom_depth = models.FloatField(_('主卫-进深'), default=0, blank=True, null=True)
    master_bathroom_width = models.FloatField(_('主卫-开间'), default=0, blank=True, null=True)
    public_bathroom_depth = models.FloatField(_('公卫-进深'), default=0, blank=True, null=True)
    public_bathroom_width = models.FloatField(_('公卫-开间'), default=0, blank=True, null=True)

    class Meta:
        db_table = 'house_product'


