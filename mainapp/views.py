from django.shortcuts import render, get_object_or_404, redirect
from .models import Work
from django.utils import timezone
from .forms import AddWork
from django.contrib.auth.decorators import login_required

def work_list(request):
    works = Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'work/work_list.html', {'works':works})

def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'work/work_detail.html', {'work': work})

@login_required
def work_new(request):
    if request.method == "POST":
        form = AddWork(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.author = request.user
            work.published_date = timezone.now()
            work.save()
        return redirect('work_list')
    else:
        form = AddWork()
        return render(request, 'work/work_edit.html', {'form': form})

@login_required
def work_edit(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.method == "POST":
        form = AddWork(request.POST, instance=work)
        if form.is_valid():
            work = form.save(commit=False)
            work.author = request.user
            work.published_date = timezone.now()
            work.save()
        return redirect('work_list')
    else:
        form = AddWork(instance=work)
        return render(request, 'work/work_edit.html', {'form': form})
        