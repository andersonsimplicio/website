
from django.urls import path
from .views import hello_blog, post_detail


urlpatterns = [
    path('',hello_blog,name="home_blog"),
    path('post/<int:id>',post_detail,name="post_detail"),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)