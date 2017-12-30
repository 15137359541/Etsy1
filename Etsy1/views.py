from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>这是主页函数：</h1>")

