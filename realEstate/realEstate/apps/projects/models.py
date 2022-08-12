from django.db import models
from nanoid import generate
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .help_text import help_text1, help_text2, help_text3, help_text4, help_text5, help_text6, help_text7


def nanoid_generate():
    return generate(size=10)


def project_files_path_generate(instance, filename):
    return f'projects/{instance.id}/{filename}'


class ProjectBase(models.Model):
    id = models.CharField(_('系统编码'), max_length=10, default=nanoid_generate, primary_key=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_dt = models.DateTimeField(_("创建时间"), auto_now_add=True)
    update_dt = models.DateTimeField(_("修改时间"), auto_now=True)
    is_deleted = models.BooleanField(_("已删除"), default=False)
    is_finished = models.BooleanField(_("已提交"), default=False)
    is_protected = models.BooleanField(_("已封存"), default=False)

    class Meta:
        abstract = True


class ProjectFiles(ProjectBase):
    # 项目附件
    file = models.FileField(upload_to=project_files_path_generate)


class ProtocolMain(ProjectBase):
    # 项目用地条件及规划条件分析
    part1_p1 = models.OneToOneField("Protocol1_1", on_delete=models.CASCADE, null=True, blank=True)
    part1_p2 = models.OneToOneField("Protocol1_2", on_delete=models.CASCADE, null=True, blank=True)
    part1_p3 = models.OneToOneField("Protocol1_3", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'protocol_main'


class Protocol1_1(ProjectBase):
    # 项目用地条件及规划条件分析
    # 1.1规划条件解读（1）
    subtitles = [
        {
            'page': 1,
            'text': f"""解读要求： 1、明确规划条件的出处（控规/规划意 见书/土地入市条件），可附文件照片。 2、整理所有设计相关规划限制条件， 以表格和文字说明形式呈现。 3、同时附上地块红线图或规划意见书 附图等。 4、如涉及多个地块，应编制汇总表。""",
            'html': f"""<p>解读要求：</p>"""
        },
        {
            'page': 2,
            'text': f"""解读要求： 1、红线退让及开口要求： 2、街景控制要求： XX侧应布置XX建筑（高度、面宽要求） 3、配套用房设置要求： 4、车位配置要求： 5、架空层设置要求： 6、相关部门诉求： ...""",
            'html': f"""<p>解读要求：</p>"""
        }

    ]
    land_code = models.CharField(_("土地编号"), max_length=255)
    position = models.CharField(_("土地位置"), max_length=255)
    usage = models.CharField(_("土地用途"), max_length=255)
    area = models.FloatField(_("使用权面积"), help_text="单位平方米", default=0.0)
    price1 = models.FloatField(_("起始价"), help_text="万元", default=0.0)
    price2 = models.FloatField(_("熔断价"), help_text="万元", default=0.0)
    price3 = models.FloatField(_("竞地价最高限价"), help_text="万元", default=0.0)
    price4 = models.FloatField(_("竞买保证金"), help_text="万元", default=0.0)
    sold_years = models.FloatField(_("出让年限"), help_text="年", default=-1.0)
    progress = models.CharField(_("开发程度"), max_length=100, null=True, blank=True)
    net_publish_dt = models.DateField(_("网上挂牌公告时间"))
    net_dt = models.DateField(_("网上挂牌时间"))
    u_area = models.FloatField(_("用地面积"), help_text="单位平方米", default='0.0', max_length=50)
    v_percentage = models.CharField(_("容积率"), help_text="单位%", default='0.0', max_length=50)  # 98 => 98/100 +%
    b_density = models.CharField(_("建筑密度"), help_text="单位%", default='0.0', max_length=50)
    b_height = models.CharField(_("建筑高度"), help_text="单位米", default='0.0', max_length=50)
    v_entrance = models.TextField(_("机动车出入口"))
    green_percentage = models.CharField(_("绿地率"), help_text="单位%", default='0.0', max_length=50)
    business_percentage = models.CharField(_("商业占比"), help_text="单位%", default='0.0', max_length=50)
    gov_percentage = models.CharField(_("保障房占比"), help_text="单位%", default='0.0', max_length=50)
    reserve_percentage = models.CharField(_("住宅自持占比"), help_text="单位%", default='0.0', max_length=50)
    gov_file = models.FileField(_("政府挂牌文件"), upload_to=project_files_path_generate)
    map_image = models.ImageField(_("用地红线图"), upload_to=project_files_path_generate)
    map_cad = models.FileField(_("用地红线图CAD"), upload_to=project_files_path_generate)

    class Meta:
        db_table = 'protocol1_1'

    def get_subtitle_by_page(self, page):
        return self.subtitles[page]

    @staticmethod
    def get_title():
        return f"""1.1规划条件解读"""


class Protocol1_2(ProjectBase):
    # 1.2设计规范要点分析
    sun = models.TextField(_("日照要求"), help_text=help_text1)
    park = models.TextField(_("停车位配比及其他"), help_text=help_text2)
    safe = models.TextField(_("人防面积规定"), help_text=help_text3)
    public = models.TextField(_("配套公建规定"), help_text=help_text4)
    area = models.TextField(_("面积计算规定"), help_text=help_text5)
    build = models.TextField(_("建筑退让及建筑间距计算规定"), help_text=help_text6)
    other = models.TextField(_("其他需说明"), help_text=help_text7)

    class Meta:
        db_table = 'protocol1_2'

    @staticmethod
    def get_title():
        return f"""1.2设计规范要点分析"""


class Protocol1_3(ProjectBase):
    file = models.FileField(_("上位规划分析图"), upload_to=project_files_path_generate)

    class Meta:
        db_table = 'protocol1_3'

    @staticmethod
    def get_title():
        return f"""1.3城市上位规划分析"""

    @staticmethod
    def get_info():
        return f"""
        备注： 上位规划是下位规划的指导性规划 （控制性详细规划属于修建性详细规划 的上位规划，城市总体规划是控制性详 细规划的上位规划）
        """
