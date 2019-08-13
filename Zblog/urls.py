
from django.contrib import admin
from django.conf.urls import url

from blog import  views
urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', views.login),
    url('index/', views.index),
    url(r'^pc/', views.gettest),
    url('logout/', views.logout),
    # path('code/', views.code),
    #注册
    url('zhuce/', views.zhuce),
    url('zhuce_ajax/', views.zhuce_ajax),

    #点赞或者踩灭
    url('digg/', views.digg),
    # 评论
    url('comment/', views.comment),
    # 后台管理
    url('backend/', views.backend),
    # 文章管理
    url('backend/add_article/', views.add_article),
    url(r'^backend/modify_article/(?P<id>\d+)', views.modify_article),
    url('backend/delete_article/', views.delete_article),
    # 上传文件
    url('11/', views.upload),

    #分类管理
    url('backend/add_category/', views.add_category),
    url('backend/manage_category/', views.manage_category),
    url('backend/delete_category/', views.delete_category),
    url(r'^backend/modify_category/(?P<id>\d+)', views.modify_category),

    #标签管理
    url('backend/add_tag/', views.add_tag),
    url('backend/manage_tag/', views.manage_tag),
    url('backend/delete_tag/', views.delete_tag),
    url(r'^backend/modify_tag/(?P<id>\d+)', views.modify_tag),

    #评论管理
    url('backend/manage_comment/', views.manage_comment),
    url('backend/delete_comment/', views.delete_comment),

    #文章详情
    url(r'^(?P<username>\w+)/articles/(?P<article_id>\d+)/$', views.article_detail),
    # 跳转
    url(r'^(?P<username>\w+)/(?P<condition>category|tag|achrive)/(?P<params>.*)/$', views.homesite),
    # 个人站点
    url(r'^(?P<username>\w+)/$', views.homesite),
]
