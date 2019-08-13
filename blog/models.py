from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    """
    用户信息
    """
    nid = models.AutoField(primary_key=True)
    telephone = models.CharField(verbose_name="手机号码",max_length=11, null=True, unique=True)
    avatar = models.FileField(verbose_name="用户头像",upload_to='static/upload', default="avatars/default.png")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    blog = models.OneToOneField(to='Blog', to_field='nid', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Blog(models.Model):
    """
    博客信息
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=64)
    site_name = models.CharField(verbose_name='站点名称', max_length=64)
    theme = models.CharField(verbose_name='博客主题', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '博客信息'
        # verbose_name = '标签'
class Category(models.Model):
    """
    博主个人文章分类表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='文章分类'
        verbose_name='分类'


class Tag(models.Model):
    """
    文章标签
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='文章标签'
        verbose_name='标签'

class Article(models.Model):
    """
    文章
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="文章标题",max_length=50)
    desc = models.CharField(verbose_name="文章描述",max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    content = models.TextField()

    comment_count = models.IntegerField(verbose_name="评论数",default=0)
    up_count = models.IntegerField(verbose_name="点赞数",default=0)
    down_count = models.IntegerField(verbose_name="踩灭数",default=0)

    user = models.ForeignKey(verbose_name='作者', to='UserInfo', to_field='nid', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', to_field='nid', null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        to="Tag",
        through='Article2Tag',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='文章编辑'
        verbose_name='文章'




class Article2Tag(models.Model):
    """
    文章和分类关系表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid', on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='nid', on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ('article', 'tag'),
        ]



    # def __str__(self):
    #     v = self.article.title + "---" + self.tag.title
    #     return v


class ArticleUpDown(models.Model):
    """
    点赞表
    """

    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(verbose_name="用户id", to='UserInfo',null=True, on_delete=models.CASCADE)
    article = models.ForeignKey(verbose_name="文章id", to="Article",null=True, on_delete=models.CASCADE)
    is_up = models.BooleanField(verbose_name="点赞和踩灭",default=True)

    class Meta:
        unique_together = [
            ('article', 'user'),
        ]
        verbose_name_plural='点赞/反对统计'
        verbose_name='文章'


class Comment(models.Model):
    """

    评论表

    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='nid', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    parent_comment = models.ForeignKey(verbose_name="父级评论id", to='Comment',null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


    class Meta:
        verbose_name_plural='评论统计'
        verbose_name='评论'