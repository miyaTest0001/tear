from django.db import models

# Create your models here.
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        # 这里通过 verbose_name 来指定对应的 model 在 admin 后台的显示名称，
        # 这里 verbose_name_plural 用来表示多篇文章时的复数显示形式。英语中，如果有多篇文章，就会显示为 Posts，
        # 表示复数，中文没有复数表现形式，所以定义为和 verbose_name一样
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        # 解释器显示的内容将会是 __str__ 方法返回的内容
        return '{}:{}'.format(self.name, self.text[:20])
