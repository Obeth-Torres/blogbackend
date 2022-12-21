from django.urls import path
from .views import PostApiView, PostDetail

urlpatterns = [
    path('', PostApiView.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
