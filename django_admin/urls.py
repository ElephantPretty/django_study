"""django_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from . import views
"""
01--06--day1内容
07--00--day2内容
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/page/2003/
    # page/2003/ 从url来讲叫path
    path('page/2003/', views.page_2003_view),
    # http://127.0.0.1:8000/
    path('', views.index_view),
    # http://127.0.0.1:8000/page/1
    path('page/1/', views.page1_view),
    # http://127.0.0.1:8000/page/2
    path('page/2/', views.page2_view),
    # 05path转换器
    path('page/<int:pg>', views.pagen_view),
    path('page/<int:pg>', views.pagen_view),
    # day1-06计算器仅仅计算1-2位数
    # http://127.0.0.1:8000/整数2/操作符/整数2 http://127.0.0.1:8000/20/add/21
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal2_view),
    # 05计算器练习-使用了path转换器
    # http://127.0.0.1:8000/整数/操作符/整数
    # path('calculator/<int:number1>/add/<int:number2>', views.calculator_add),
    # 优化计算器
    path('<int:number1>/<str:op>/<int:number2>', views.calculator),
    # path('calculator/<int:number1>/sub/<int:number2>', views.calculator_sub),
    # 06生日匹配练习 http:127.0.0.1:8000/birthday/4位数字/1到2位数字/1到2位数字
    re_path(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$', views.birthday_views),
    # day02-request-info
    path('test_request', views.test_request),
    path('test_get_post', views.test_get_post),
    path('test_html', views.test_html),
    path('test_html_param', views.test_html_param),
    path('test_if_for', views.test_if_for),
    path('mycal', views.test_mycal),
    path('base_index', views.base_view, name='base_index'),
    path('music_index', views.music_view),
    path('sport_index', views.sport_view),
    # http://127.0.0.1:8000/test/url
    path('test/url', views.test_url),
    path('test_url_result/<int:age>', views.test_url_result, name="tr"), # 取别名
    # day03
    path('test_static', views.test_static),
    # 这边涉及到分布式路由，和flask蓝图差不多！
    path('music/', include('music.urls')),
    path('sport/', include('sport.urls')),
    path('news/', include('news.urls')),
    #day004
    path('bookstore/', include('bookstore.urls')),
    path('set_cookies/', views.set_cookies),
    path('get_cookies/', views.get_cookies),
    path('set_session/', views.set_session),
    path('get_session/', views.get_session)
]
