from django.urls import path

from index import views

urlpatterns = [
    # 负责匹配后缀
    path('index1', views.index_view)
]