from django.urls import path 

from . import views


app_name = 'izanamijinja'
urlpatterns = [
    path('<int:ryugi_id>/', views.filtered_index, name="filteredindex"),
    path('', views.index, name="index"),
    path('seikei/', views.SeikeiView.as_view(), name='seikei'),
    path('kataaratame/<int:kata_id>', views.KataAratameView.as_view(), name='kataaratame'),
    path('muyou/<int:kata_id>', views.muyou, name='muyou'),
    path('zenshin/', views.zenshin, name='zenshin'),
    path('shiren/', views.shiren, name='shiren'),
    path('zanshin/', views.zanshin, name='zanshin'),
]