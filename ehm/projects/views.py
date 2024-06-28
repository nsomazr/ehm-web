from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects
from .serializers import ProjectsModelSerializer
from .forms import ProjectsForm
from django.contrib import messages
# Create your views here.

class ProjectsAPIView(APIView):

    def get(self, request):
        blogs = Projects.objects.all()
        serializer = ProjectsModelSerializer(blogs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectsModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def projects_list(request):
        projects = Projects.objects.all()
        context = {'projetcs':projects}
        return render(request, template_name='backend/pages/projects_list.html', context=context)

    def projetcs(request):
        projects = Projects.objects.filter(publish=1, status=1)
        context = {"projects": projects}
        return render(request, template_name='backend/pages/projects.html', context=context)

    def add_project(request):

        if request.method == 'POST' and request.FILES['thumbnail']:

            project_form = ProjectsForm(request.POST,request.FILES)
            # print(f"Body content: {request.POST['body']}")
            if project_form.is_valid():
                title  = request.POST['title']
                body = project_form.cleaned_data['body']
                thumbnail = request.FILES['thumbnail']
                # header_image = request.FILES['header_image']
                # file= request.FILES['file']
                description = request.POST['description']
                thematic_area= request.POST['thematic_area']
                status = 1
                # print(f"Body content: {body}")
                slug = title.replace(' ','-').lower()
                new_project = Projects(title=title, body=body, thumbnail=thumbnail, description=description, publisher_id=request.session['user_id'], status=status, slug=slug, thematic_area=thematic_area)
                get_objects = Projects.objects.filter(title=title, status=1)
                if get_objects:
                    messages.success(request, "Project already exist." )
                    project_form = ProjectsForm()
                    return render(request, template_name='backend/pages/add_project.html', context={'project_form':project_form})
                else:
                    new_project.save()
                    messages.success(request, "Project successful added." )
                    print("Here")
                    return redirect('projects:projects-list')
            else:
                print(project_form.errors.as_data())
                
        project_form = ProjectsForm()
        return render(request, template_name='backend/pages/add_project.html', context={'project_form':project_form})


    def review_project(request,id):
        projects = Projects.objects.get(id=id)
        context = {'projects':projects}
        return render(request, template_name='backend/pages/review_project.html', context=context)
    
    def read_project(request,slug):
        project = Projects.objects.get(slug=slug)
        projects = Projects.objects.filter(publish=1, status=1).exclude(slug=slug)
        context = {'project':project, 'projects':projects}
        return render(request, template_name='backend/pages/read_project.html', context=context)
    
    def view_project(request,id):
        project = Projects.objects.get(id=id)
        context = {'project':project}
        return render(request, template_name='backend/pages/view_project.html', context=context)
    
    def publish_project(request,id):
            project = Projects.objects.get(id=id)
            project.publish = 1
            project.save()
            return redirect('projects:projects-list')
            
    
    def delete_project(request,id):
        project = Projects.objects.filter(id=id)
        if project:
            project.delete()
            messages.success(request, "Project deleted." )
            return redirect('projects:projects-list')
        messages.success(request, "Project doesn't exist." )
        return redirect('projects:projects-list')