from django.urls import path 

from . import views


app_name = 'izanamijinja'
urlpatterns = [
    path('', views.index, name="index"),
    path('seikei/', views.SeikeiView.as_view(), name='seikei'),
    path('zenshin/', views.zenshin, name='zenshin'),
    path('shiren/', views.shiren, name='shiren'),
    path('zanshin/', views.zanshin, name='zanshin'),
]