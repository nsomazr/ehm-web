from django.urls import path,re_path
from .views import BlogsAPIView
from django.conf import settings
from django.conf.urls.static import static

app_name = "blogs"  

urlpatterns = [
               path("blogs/",BlogsAPIView.blogs, name='blogs' ),
               path('add-blog/', BlogsAPIView.add_blog, name="add-blog"),
               path('blog/<str:slug>/', BlogsAPIView.read_blog, name="read-blog"),
               path('blogs-list/review-blog/publish-blog/<int:id>', BlogsAPIView.publish_blog, name="publish-blog"),
               path('blogs-list/review-blog/<int:id>', BlogsAPIView.review_blog, name="review-blog"),
               path('blogs-list/view-blog/<int:id>', BlogsAPIView.view_blog, name="view-blog"),
               path('blogs-list/delete-blog/<int:id>', BlogsAPIView.delete_blog, name="delete-blog"),
               path('blogs-list/', BlogsAPIView.blogs_list, name="blogs-list"),
               path('api/blogs', BlogsAPIView.as_view(), name="blogs-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)