from django.shortcuts import render
from blogs.models import Blogs

# Create your views here.

def home(request):
    blogs = Blogs.objects.filter(publish=1, status=1)
    context = {"blogs": blogs}
    return render(request, template_name='frontend/pages/index.html', context=context)

def about(request):
    return render(request, template_name='frontend/pages/about.html', context={})
