from django.urls import path
from . import views

app_name = 'login'
#name为反向解析名
urlpatterns = [
    path('index/', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('logout/', views.logout,name='logout'),
    path('confirm/', views.user_confirm),
]
# 错误处理增加的条目
# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.page_error