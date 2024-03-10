from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("post/", views.PostStream, name="post"),
    path("get/<str:name>/<str:chunk>", views.GetStream, name="get")
]

# path("channel/<int:pk>", views.ChannelDetails, name="channel"),
# path("channel_create/", views.CreateChannel, name="channel_create"),
# path("search/<str:searched_value>", views.Search, name="search"),
# path("camera/", views.CameraView, name="camera"),
# path("screen/", views.ScreenGrab, name="screen"),