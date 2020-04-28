from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # django 会自动将 fields 中声明的模型字段设置为表单的属性
        fields = ['name', 'email', 'url', 'text']
