from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    # 注册
    url(r'register/$', views.test, name="register"),
    # 登录
    url(r'login/$', TemplateView.as_view(template_name='login.html'), name="login"),
    # 退出
    url(r'logout/$', views.test, name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.test, name="password_forget"),
    # 重置密码
    url(r'password/reset/token/$',views.test, name="password_reset"),
]