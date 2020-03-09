from django.urls import path,include
from . import views



urlpatterns = [
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post-delete'),
    path('',views.home,name='home'),
    path('login/', views.login,name='login'),
    # path('login/',views.LoginView.as_view(),name='login'),
    # path('superUser/', views.home,name='superUser'),
    path('create/', views.register, name='create'),
    path('post/new/<int:id>',views.PostCreateView.as_view(),name='create-post')


   
]