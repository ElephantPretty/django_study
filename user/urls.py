from django.urls import path

from user import views

urlpatterns = [
    # 负责匹配后缀
    path('reg', views.reg_view),
    path('login', views.login_view),
    path('logout', views.logout_view)
]