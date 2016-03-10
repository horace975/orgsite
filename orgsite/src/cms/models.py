from django.db import models

# from sorl.thumbnail import ImageField

# Create your models here.
class NavBlock(models.Model):
    shopname = models.CharField(
        verbose_name="Shop Name",
        max_length=30,
        help_text=("商店的名字"),
        default=None,
    )
    services = models.CharField(
        verbose_name="Our Services",
        max_length=30,
        default=None,
    )
    portfolio = models.CharField(
        verbose_name="Our Portfolio",
        max_length=30,
    )
    aboutus = models.CharField(
        verbose_name="About Us",
        max_length=30,
        default=None,
    )

class HomeBlock(models.Model):
    title = models.CharField(
        verbose_name="Main Title",
        max_length=100,
        default=None,
    )
    subtitle = models.CharField(
        verbose_name="Sub Title",
        help_text="商店介紹",
        max_length=100,
        default=None,
    )
    photo = models.ImageField(
        verbose_name='Home Picture',
        upload_to='photos',
        blank=True,
    )

    def __str__(self):
        return self.title

class ServicesBlock(models.Model):
    pic = models.CharField(
        verbose_name="Services Pic",
        help_text="請在 ",
        max_length=30,
        default=None,
    )
    title = models.CharField(
        verbose_name="Services Title",
        max_length=30,
        default=None,
    )
    content = models.CharField(
        verbose_name="Services Content",
        max_length=100,
        default=None,
    )
    sequence_num = models.IntegerField(
        verbose_name='Services Sequence',
        help_text="請輸入1~8, 數字越小此篇介紹放越前面",
        default=1,
    )

    def __str__(self):
        return self.title + self.sequence_num

    class Meta:
        ordering = ['-sequence_num']
    
class PortfolioBlock(models.Model):
    title = models.CharField(
        verbose_name="Portfolio name",
        max_length=30,
        default=None,
    )
    tag = models.CharField(
        verbose_name="Portfolio tag",
        max_length=30,
        default=None,
    )
    photo = models.ImageField(
        verbose_name='Portfolio Picture',
        upload_to='photos',
        blank=True,
    )
    sequence_num = models.IntegerField(
        verbose_name='Portfolio Sequence',
        help_text="請輸入1~8, 數字越小此篇介紹放越前面",
        default=1,
    )

    def __str__(self):
        return self.title + self.sequence_num

    class Meta:
        ordering = ['-sequence_num']

class AboutBlock(models.Model):
    pic = models.CharField(
        verbose_name="About Pic",
        help_text="請輸入",
        max_length=30,
        default=None,
    )
    title = models.CharField(
        verbose_name="About Title",
        max_length=30,
        default=None,
    )
    content = models.CharField(
        verbose_name="About Content",
        max_length=100,
        default=None,
    )
    sequence_num = models.IntegerField(
        verbose_name='About Sequence',
        help_text="數字越小此篇介紹放越前面",
        default=1,
    )
    shop_mail = models.EmailField(
        verbose_name='Official E-mail',
        help_text="公司的 mail",
        max_length=254,
        default=None,
    )

    def __str__(self):
        return self.title + self.sequence_num

    class Meta:
        ordering = ['-sequence_num']
        