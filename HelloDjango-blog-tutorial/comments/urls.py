from django.urls import path

from comments import views

# 别忘了给这个评论的 URL 模式规定命名空间，即 app_name = 'comments'
app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment')
]
