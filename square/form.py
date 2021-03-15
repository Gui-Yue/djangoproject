from django import forms
from .models import Title, Content


class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['text']
        # 根据模型创建表单，该表单只包含字段text
        labels = {'text': ''}
        # 让django不要为字段text生成标签


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # 定义一个小部件(widgets)的属性，将文本区域宽度设置为80列(默认为40列)
