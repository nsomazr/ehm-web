from django.urls import path,re_path
from .views import ProjectsAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "projects"  

urlpatterns = [
               path("projects/",view=ProjectsAPIView.projetcs, name='projects' ),
               path('add-projects/', ProjectsAPIView.add_project, name="add-project"),
               path('<str:slug>/', ProjectsAPIView.read_project, name="index-read-blog"),
            #    path('read-blog/<str:slug>/', NewsAPIView.read_blog, name="read-blog"),
               path('projects/projetcs-list/review-project/publish-project/<int:id>', ProjectsAPIView.publish_project, name="publish-project"),
               path('projects/project-list/review-projects/<int:id>', ProjectsAPIView.review_project, name="review-project"),
               path('projects-list/view-project/<int:id>', ProjectsAPIView.view_project, name="view-project"),
               path('projects/projects-list/delete-project/<int:id>', ProjectsAPIView.delete_project, name="delete-project"),
               path('projects/projects-list/', ProjectsAPIView.projects_list, name="projects-list"),
               path('api/projects', ProjectsAPIView.as_view(), name="projects-api")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)