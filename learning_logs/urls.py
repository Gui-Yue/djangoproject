"""定义learning_logs的URL模式"""
from django.conf.urls import url, include
from django.urls import path
from . import views
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # r:让python将接下来的字符串视为原始字符
    # path的第一个参数为route，类似于正则表达式，是匹配url的准则，'^$'表示匹配空url，即为默认基础url(http://localhost:8000/)
    # path的第三个参数为view，view是视图，指的是view.py文件，后面为表示调用的函数。
    # path的name参数为url取名，使其能够在django的任意地方被唯一引用
    # 此处要用到url，但是我并不清楚为什么
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 在此对该正则表达式进行注释：r是指将后面的字符串视为原始字符，^$标注起始,/(?p<topic_id>\d+)/用于匹配一个整数，匹配规则如下：
    # 将匹配到的数字存储在变量名topic_id中,“?p<>”指匹配url中的值并存储到<>中，表达式\d+指与“//”中的任何整数都匹配
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    path('topic_delete/<int:id>', views.topic_delete, name='topic_delete')
]
