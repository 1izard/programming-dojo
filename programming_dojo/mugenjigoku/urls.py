from django.urls import path 

from . import views


app_name = 'mugenjigoku'
urlpatterns = [
    path('', views.index, name="index"),
    path('shingi/', views.ShingiView.as_view(), name='shingi'),
    path('zenshin/', views.zenshin, name='zenshin'),
    path('shiren/', views.shiren, name='shiren'),
    path('zanshin/', views.zanshin, name='zanshin'),
]