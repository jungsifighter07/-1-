from django.shortcuts import render
from django.shortcuts import HttpResponse
from memo.models import Memo

# Create your views here.
# sticky_memo/memo/views.py
# 아이디 admin 비번 abc123 이메일 admin@gmail.com

def get_all_memo(request):
    memo_list = Memo.objects.all()
    context = {"memos": memo_list}

    return render(request, "memo_list.html", context)

