from django.shortcuts import render

# Create your views here.
from .models import Title, Content
from .form import TitleForm, ContentForm
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
# Create your views here.


def titles(request):
    titles = Title.objects.order_by('-date_added')
    context = {'titles': titles}
    return render(request, 'square/titles.html', context)


def title(request, title_id):
    title = Title.objects.get(id=title_id)
    contents = title.content_set.order_by('-date_added')
    context = {'title': title, 'contents': contents}
    return render(request, 'square/title.html', context)


def new_title(request):
    if request.method != 'POST':
# 用户初次访问页面，其浏览器讲发送GET请求，我们使用if函数来过滤掉Get请求(这里选择返回一个空表单），
# 当服务器发送POST请求的时候，我们对填好的表单进行处理。
        form = TitleForm()
    else:
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('square:titles'))

    context = {'form': form}
    return render(request, 'square/new_title.html', context)


def new_content(request, title_id):
    title = Title.objects.get(id=title_id)
    # 获得与内容相关联的主题
    if request.method != 'POST':
        form = ContentForm()
    else:
        form = ContentForm(data=request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            # 此处创建一个新的条目对象，并将它储存到new_content中，commit=False使得django不将表单储存到数据库中
            new_content.title = title
            # 将new_content的属性title设置为开头从数据库中获得的主题
            new_content.save()
            # 将new_content保存到数据库中，以上操作保证内容和主题相关联
            return HttpResponseRedirect(reverse('square:title', args=[title.id]))
            # 重定向到titles.html页面，此处指定列表args要包含url中所有的实参,使其跳转到特定主题的页面
    context = {'title': title, 'form': form}
    return render(request, 'square/new_content.html', context)

def edit_content(request,content_id):
    content = Content.objects.get(id=content_id)
    title = content.title
    if request.method != 'POST':
        form = ContentForm(instance=content)
    else:
        form = ContentForm(instance=content, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('square:title', args=[title.id]))
    context = {'form': form, 'title': title, 'content': content}
    return render(request, 'square/edit_content.html', context)

