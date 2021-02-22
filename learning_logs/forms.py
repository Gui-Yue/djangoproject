from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
# 定义TopicForm使其继承forms.ModelForm类
    class Meta:
        model = Topic
        # 告诉Django根据Topic模型创建表单
        fields = ['text']
        # 该表单只包含字段text
        labels = {'text': ''}
        # 告诉Django不要为字段text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}
