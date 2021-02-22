from django.shortcuts import render
from .models import Topic
from .models import Entry
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')
# render()要提供两个参数：request为原始请求对象，第二个参数为可用于创建网页的模板
# Create your views here.

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    if topic.owner != request.user:
        raise Http404
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 检查是否为post请求
        form = TopicForm()
        # if not submit data : create a new form
    else:
        # Data submitted by POST, data processing
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # 将表单填入的数据写进数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            # 重定向到网页topics
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 检查是否为post请求
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # 我们向save（）传递实参commit=False，将创建的新条目对象储存到new_entry中，但不保存到数据库中
            new_entry.topic = topic
            # 我们将new_entry的属性topic 设置为在这个函数开头从数据库中获取的主题
            new_entry.save()
            # 然后调用save(),且不指定任何实参。这将把条目保存到数据库,并将其与正确的主题相关联。
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    else:
        if request.method != 'POST':
            form = EntryForm(instance=entry)
        else:
            form = EntryForm(instance=entry, data=request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

