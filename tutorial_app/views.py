from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# パラメータを受けてテンプレートを表示する
def index(request):
    if 'msg' and 'title' in request.GET:
        title, msg = request.GET['title'], request.GET['msg']
        params = {
            'title': title,
            'msg': msg
        }
    else:
        params = {
            'title': 'Hello Gjangooooo',
            'msg': 'これはサンプルページで作ったテンプレートでーす'
        }
    params['goto'] = 'next'
    params['numbers'] = range(5)
    params['items'] = ['apple', 'ninnjin', 'daikon', 'tomato']
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'hello/next',
        'msg': 'これはサンプルページで作ったnextページでーす',
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)

# テンプレートを使わずViewだけで返すのと、URLを受けて表示する
def information(request, id, name, age):
    res = "Your name: {}, Your id: {}, Your age: {}".format(name,id,age)
    return HttpResponse(res)