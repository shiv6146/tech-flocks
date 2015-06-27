from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django import forms
from django.contrib.auth.models import User
from blog.forms import UserForm, PostForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    post_list = Post.objects.order_by('-date')
    paginator = Paginator(post_list, 7)  #Show 10 posts per page

    page_num = request.GET.get('page')

    try:
    	posts = paginator.page(page_num)
    except PageNotAnInteger:
    	posts = paginator.page(1)
    except EmptyPage:
    	posts = paginator.page(paginator.num_pages)

    context_dict = {'posts':posts}

    # Return a rendered response to send to the client.
    return render(request, 'blog/index.html', context_dict)

def register(request):

    registered = False

    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()

            registered = True

        # Invalid forms
        else:
            print user_form.errors

    # Not a Post request
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'blog/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login credentials
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login credentials")

    #Not a Post request, so display the login form.
    else:
        return render(request, 'blog/login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})

@login_required
def like_post(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']

    likes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            likes = post.likes + 1
            post.likes =  likes
            post.save()

    return HttpResponse(likes)