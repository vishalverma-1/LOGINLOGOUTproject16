from django.urls import path
from.import views
urlpatterns=[
    path('k/',views.myfun,name="myfun"),
    path('kk/',views.login,name="login"),
    path('kkk/',views.mypage,name="mypage"),
    path('',views.logout,name="logout"),
]