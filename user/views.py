import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User


# Create your views here.
def reg_view(request):
    # 注册
    if request.method == 'GET':
        # GET 返回页面
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # POST 处理提交数据
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST["password_2"]
        # 1-两个密码要保持一致
        if password_1 != password_2:
            return HttpResponse('两次密码输入不一致')
        # 哈希算法-明文转【定长】密文-结果不可逆-md5或sha-256
        # 特点和如何使用就行
        # 定长-md5-32位16进制
        # 不可逆-无法反向计算出对应的明文
        # 雪崩效应-输入改变，输出必然变
        # 场景：1-密码处理 2-文件完整性校验
        # 如何使用
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        # 2-当前用户名是否可用
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已注册')
        # 3-插入数据【明文处理密码-暂时】--请求量大可能会报错！！！
        # 唯一索引-重复插入报错
        # 假设多台机器跑同一个代码-并且用户名1都还没注册-并发场景
        # 唯一索引-必须要用try
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            # 有可能 报错-重复插入[唯一索引注意并发写入问题]
            print('--create user error%s'%(e))
            return HttpResponse('用户名已注册')
        # 免登陆一天--选session-更安全，主键查询比其它查询更快
        request.session['username'] = username
        request.sesssion['uid'] = user.id
        # TODO 修改session存储时间为1天

        return HttpResponseRedirect('/index/index1')


def login_view(request):
    if request.method == 'GET':
        # 获取登陆页面
        # 检查登录状态，'如果登陆了--显示已登录'
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponseRedirect('/index/index1')
        # 检查Cookides
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            # 回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            return HttpResponseRedirect('/index/index1')
        # 这是未登录状态
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 处理数据
        username = request.POST['username']
        password = request.POST['password']
        # 两种查询方案
        """
       方案1更好-前者唯一索引更好-用户名
        方案1-先拿username-尝试获取用户名-在比对密码
        方案2-先拿用户传入的password-md5分一次，在查询数据库密码
        """
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error%s'%(e))
            # 不能给明确的提示信息--不能很具体
            return HttpResponse('用户名或密码错误')
        # 比对密码--因为hash不可逆--所以先md5加一次在比对
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或密码错误')
        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id
        resp = HttpResponseRedirect('/index/index1')
        # 使用cookie应对记住用户名--延长登陆状态这个需求
        # 判断用户是否点选了'记住用户名'
        if 'remember' in request.POST:
            resp.set_cookie('username', username)
            resp.set_cookie('uid', user.id, 3600*24)
        # 点选了->cookie存储username,uid 时间3天
        return resp


def logout_view(request):
    # 删除session值
    if 'username' in  request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    resp = HttpResponseRedirect('/index/index1')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
