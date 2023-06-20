from django.shortcuts import HttpResponse, render

def myhome(request):
    return HttpResponse("<h1>hello world!</h1>")


def index(request):
    return render(request, 'index.html')

# https://dirt-record-7f9.notion.site/1-6-8-769827e2aa07401baa9f2db25efe096c