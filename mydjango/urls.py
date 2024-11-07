"""
URL configuration for mydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from djangoapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("m",views.fun),
    path("hj",views.fun1),
    path("b",views.fun3),
    path("c",views.fun4),
    path("d",views.fun5),
    path("e",views.fun6,name='hi'),
    path('f',views.add_user),
    path('g',views.user_),
    path("h",views.fun7),
    path('i',views.users),
    path("w",views.fun8,name='my'),
    path("z",views.pro),
    path('y',views.fun9,name='k'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('update/<int:id>',views.update_user,name='update'),
    path("py",views.funn10),
    path("pp",views.funn11,name='c'),
    path('dele/<int:id>',views.deleee,name="id"),
    path('upd/<int:id>',views.updat,name='idd'),
    path('jj',views.userr),
    path('kk',views.usertbl,name='mo'),
    path('uda/<int:id>',views.userup,name='ide'),
    path('nn',views.produ),
    path('kn',views.publi,name='ww'),
    path('orm',views.modeldis),
    path('deli/<int:id>',views.delbook,name='bid'),
    path('ubk/<int:id>',views.upbook,name='upb'),

    path('cor',views.course,name='tbl'),
    path('for',views.stddeatials),
    path('up/<int:id>',views.upstudent,name='upid'),
    


    path('n',views.view_gust,name='d'),
    path('o',views.add_gust),
    path('p/<int:id>',views.dlt_gust,name='gid'),
    path('q/<int:id>',views.uptd_gust,name='iid'),


    path('bm',views.userfor),


    path('pf',views.profileform),
    path('uv',views.usertable,name='vw'),
    path('ur/<int:id>',views.profileupdate,name='pid'),
    # path('log',views.log),
    path('bl',views.blog),
    path('bt',views.blogtable,name='bt'),


    path('re',views.register),
    path('ui',views.usi),

    path('im',views.image),
    path('di',views.dis_im,name='im'),

    path('',views.home),
    path('home',views.homepage),
    path('about',views.about),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)