from django.shortcuts import render

from .models import Post

# Create your views here.

#CRUD - create retrieve update delete

# List all the posts

def post_list_view(request):
	if request.method == 'POST':
		if request.POST.get('name') and request.POST.get('email') and request.POST.get('comment'):
			post=Post()
			post.name= request.POST.get('name')
			post.email= request.POST.get('email')
			post.comment= request.POST.get('comment')
			post.save()

	post_objects = Post.objects.all().order_by("-id")
	context = {
		'post_objects': post_objects
	}
	return render(request, "blog/forum.html", context)


