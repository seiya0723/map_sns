from django.urls import path
from.import views

app_name ="map"
urlpatterns=[
    path('', views.index, name="index"),
    path('reply/<int:pk>/', views.reply, name="reply"),
    path('mypage/', views.mypage, name="mypage")
]
