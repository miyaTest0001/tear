import re

import markdown
from django.shortcuts import render, get_object_or_404

# Create your views here.
# from django.http import HttpResponse
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from blog.models import Post, Category, Tag


def index(request):
    # return HttpResponse("欢迎访问我的博客首页~~~ ^-^ ")
    # return render(request, 'blog/index.html', context={
    #     'title': '我的博客首页',
    #     'welcome': '哈哈，欢迎访问的我博客首页~~~'
    # })
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc',
        # TocExtension 在实例化时其 slugify 参数可以接受一个函数，这个函数将被用于处理标题的锚点值。Markdown 内置的处理方法不能处理中文标题，所以我们使用了 django.utils.text 中的 slugify 方法，该方法可以很好地处理中文
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
