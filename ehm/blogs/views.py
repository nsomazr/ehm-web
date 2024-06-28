from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blogs
from .serializers import BlogsModelSerializer
from .forms import BlogsForm
from django.contrib import messages
# Create your views here.

class BlogsAPIView(APIView):

    def get(self, request):
        blogs = Blogs.objects.all()
        serializer = BlogsModelSerializer(blogs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogsModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def blogs_list(request):
        blogs = Blogs.objects.filter(publisher=request.session['user_id'])
        context = {'blogs':blogs}
        return render(request, template_name='backend/pages/blogs_list.html', context=context)

    def blogs(request):
        blogs = Blogs.objects.filter(publish=1, status=1,publisher=request.session['user_id'])
        context = {"blogs": blogs}
        return render(request, template_name='backend/pages/blogs.html', context=context)

    def add_blog(request):

        if request.method == 'POST' and request.FILES['thumbnail']:

            blog_form = BlogsForm(request.POST,request.FILES)
            # print(f"Body content: {request.POST['body']}")
            if blog_form.is_valid():
                title  = request.POST['title']
                body = blog_form.cleaned_data['body']
                thumbnail = request.FILES['thumbnail']
                # header_image = request.FILES['header_image']
                # file= request.FILES['file']
                # description = request.POST['description']
                thematic_area= request.POST['thematic_area']
                status = 1
                # print(f"Body content: {body}")
                slug = title.replace(' ','-').lower()
                new_blog = Blogs(title=title, body=body, thumbnail=thumbnail, publisher_id=request.session['user_id'], status=status, slug=slug, thematic_area=thematic_area)
                get_objects = Blogs.objects.filter(title=title, status=1)
                if get_objects:
                    messages.success(request, "News already exist." )
                    blogs_form = BlogsForm()
                    return render(request, template_name='backend/pages/add_blog.html', context={'blog_form':blog_form})
                else:
                    new_blog.save()
                    messages.success(request, "News successful added." )
                    print("Here")
                    return redirect('blogs:blogs-list')
            else:
                print(blogs_form.errors.as_data())
                
        blog_form = BlogsForm()
        return render(request, template_name='backend/pages/add_blog.html', context={'blog_form':blog_form})

    def review_blog(request,id):
        blog = Blogs.objects.get(id=id)
        context = {'blog':blog}
        return render(request, template_name='backend/pages/review_blog.html', context=context)
    
    def read_blog(request,slug):
        blog = Blogs.objects.get(slug=slug)
        blogs = Blogs.objects.filter(publish=1, status=1).exclude(slug=slug)
        context = {'blog':blog, 'blogs':blogs}
        return render(request, template_name='frontend/pages/read_blog.html', context=context)
    
    def view_blog(request,id):
        blog = Blogs.objects.get(id=id)
        context = {'blog':blog}
        return render(request, template_name='backend/pages/view_blog.html', context=context)
    
    def publish_blog(request,id):
            blog = Blogs.objects.get(id=id)
            blog.publish = 1
            blog.save()
            return redirect('blogs:blogs-list')
            
    
    def delete_blog(request,id):
        blog = Blogs.objects.filter(id=id)
        if blog:
            blog.delete()
            messages.success(request, "News deleted." )
            return redirect('blogs:blogs-list')
        messages.success(request, "Blog doesn't exist." )
        return redirect('blogs:blogs-list')