from django.contrib import admin
from .models import Book, Author


# 后台模型--可以导入自己的模型
# Register your models here.


class BookManager(admin.ModelAdmin):
    """
    估计原因在于，原本django版本是4.0.12--但是武汉使用的django版本是3.2.12
    导致未按照预期显示
    """
    # 列表页显示哪些字段的列--3-16--未成功显示--django_version--3.2.12
    list_display = ('id', 'title', 'pub', 'price', 'price')
    # 控制list_display_links中的字段，哪些可以链接到修改页
    list_display_links = ('title')
    # 添加过滤器
    list_filter = ('pub')
    # 添加搜索框[模糊查询]
    search_fields = ('title')
    # 添加可在列表页编辑的字段--和links互斥
    list_editable = ('price')


class AuthorManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')


admin.site.register(Book)
# 注册
admin.site.register(Author)
