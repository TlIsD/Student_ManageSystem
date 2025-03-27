from django.contrib import admin
from django.urls import path, include, re_path
from student import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_student),
    re_path('delete/(\d+)', views.delete_student),
    re_path('edit/(\d+)', views.edit_student),
    # 选课
    path('elective/', views.elective),
    # 筛选
    path('search/', views.search),
    # 通过Excel表格批量导入数据
    path('stu_excel/', views.stu_excel),

    path('details/', views.details),
    path('avatar/', views.avatar),
]