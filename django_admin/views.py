from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

POST_FORM = '''
<form method='post' action='test_get_post'>
    用户名:<input type='text' name='uname'>
    <input type='submit' value='提交'>
</form>
'''

def page_2003_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def index_view(request):
    html = "这是我的首页"
    return HttpResponse(html)


def page1_view(request):
    html = "这是编号为1的网页"
    return HttpResponse(html)


def page2_view(request):
    html = "这是编号为2的网页"
    return HttpResponse(html)


def pagen_view(request, pg):
    html = "这是编号为%s的网页!"%(pg)
    return HttpResponse(html)

# 22-2-27-优化
def calculator(request, number1, op, number2):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse('Your op is wrong')
    if op == 'add':
        count = number1 + number2
    elif op == 'sub':
        count = number1 - number2
    elif op == 'mul':
        count = number1 * number2
    html = "结果为%d的网页！！"%(count)
    return HttpResponse(html)


# def calculator_sub(request, number1, number2):
#     count = number1 - number2
#     html = "结果为%d的网页！！"%(count)
#     return HttpResponse(html)
#
#
# def calculator_mul(request, number1, number2):
#     count = number1 * number2
#     html = "结果为%d的网页！！"%(count)
#     return HttpResponse(html)

def cal2_view(request, x, op, y):
    html = 'x:%s op:%s y:%s'%(x, op, y)
    return HttpResponse(html)


def birthday_views(request, year, month, day):
    html = '%s年%s月%s日'%(year, month, day)
    return HttpResponse(html)


def test_request(request):
    print('path info is', request.path_info)
    print('method is', request.method)
    print('querystring is', request.GET)
    print('full path is', request.get_full_path())
    #return HttpResponse('test request ok')
    return HttpResponseRedirect('/page/1')


def test_get_post(request):
    if request.method == 'GET':
        print(request.GET)
        # print(request.GET['a'])
        # 此种情况下GET.get不行 http://127.0.0.1:8000/test_get_post?a=400&a=100&a=100
        print(request.GET.get('a', 'no c'))
        # 此种情况http://127.0.0.1:8000/test_get_post?a=400&a=100&a=100 用getlist
        # 经典场景 问卷调查 form get 兴趣爱好-复选框-值多个--根据业务场景
        # 之前的计算器也可以用查询字符串来做
        print(request.GET.getlist('a', 'no c1'))
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        # 处理用户提交数据
        print('uname is', request.POST['uname'])
        return HttpResponse('post is ok')
        pass
    else:
        pass
    return HttpResponse('--test get post is ok--')


def test_html(request):
    # 加载方式1
    # from django.template import loader
    # # 配置文件里面去找
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    # 加载方式2
    from django.shortcuts import render
    dic = {'username':'张三','age':18}
    return render(request, 'test_html.html', dic)


def test_html_param(request):
    dic = {}
    dic['int'] = 88
    dic['str'] = 'aaa'
    dic['lst'] = ['Tom', 'Jack', 'Lily']
    dic['dict'] = {'a':9, 'b':8}
    # 函数
    dic['func'] = say_hi
    # 类实体化对象
    dic['class_obj'] = Dog()
    dic['script'] = '<script>alert(111)</script>' # js代码
    return render(request, 'test_html_param.html', dic)


def say_hi():
    return 'hahaha'


class Dog:
    def say(self):
        return 'wangwang'


def test_if_for(request):
    dic = {}
    dic['x'] = 10
    dic['lst'] = ['1', '2', '3']
    return render(request, 'test_if_for.html', dic)


def test_mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        # 处理计算 文本框默认传字符串，需要转
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        # locals()会将当前函数局部变量封装成一个字典
        # 相当于dic={'x':x,'y':y,'op':op}
        return render(request, 'mycal.html', locals())


def base_view(request):
    lst = ['Tom', 'Jack']
    return render(request, 'base.html', locals())


def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')


def test_url(request):
    return render(request, 'test_url.html')


def test_url_result(request, age):
    # 302跳转
    from django.urls import reverse
    # 视图使用url反向解析--302响应--浏览器如何知道要跳转到哪里呢？
    # 是响应头里面的location!
    url = reverse('base_index')
    return HttpResponseRedirect(url)
    # return HttpResponse('---test url res is ok')


def test_static(request):
    return render(request, 'test_static.html')


def set_cookies(request):
    resp = HttpResponse('set cookie is ok')
    resp.set_cookie('uuname', 'gxn', 500)
    return resp


def get_cookies(request):
    value = request.COOKIES.get('uuname')
    return HttpResponse('value is %s'% (value))


def set_session(request):
    request.session['uname'] = 'wwc'
    return HttpResponse('set session is ok')


def get_session(request):
    value = request.session['uname']
    return HttpResponse('session value is %s'%(value))

