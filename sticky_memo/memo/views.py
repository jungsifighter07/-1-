from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from memo.models import Memo

# Create your views here.
# sticky_memo/memo/views.py
# 아이디 admin 비번 abc123 이메일 admin@gmail.com

def get_all_memo(request):
    memo_list = Memo.objects.all()
    context = {"memos": memo_list}

    return render(request, "memo_list.html", context)

def get_memo(request, id):
    memo = Memo.objects.get(id=id)
    context = {"memo" : memo}

    return render(request, "memo_detail.html", context)

from memo.forms import MemoForm
def create_memo(request):
    if request.method == 'GET':
        form = MemoForm()
        context = {'form': form}
        return render(request, 'memo_create.html', context)
    elif request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
        

# sticky_memo/memo/views.py

def update_memo(request, id):
    memo = Memo.objects.get(id=id)

    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    

def delete_memo(request, id):
    memo = Memo.objects.get(id=id)

    if request.method == 'POST':
        memo.delete()
        return redirect('memo_list')