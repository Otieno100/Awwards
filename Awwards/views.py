from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewAwwardsForm, NewAwwardsForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import User


from Awwards.models import Post
import datetime as dt
from .forms import AwwardsLetterForm
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm,UpdateUserProfileForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  AwwardsMerch
from .serializer import MerchSerializer
from rest_framework import status
from .forms import PostForm,UpdateUserForm,UpdateUserProfileForm,RatingsForm,SignupForm
from .models import Post,Profile,Rating



# def post(request):
#       awward = Post.objects.all()

#       return render(request,'awwards/post.html', {"awwards":awward})



def post_item(request):
    
    post = Post.objects.all()
    return render(request, 'awwards/post.html', {"post":post})




        


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'awwards/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awwards/search.html',{"message":message})



@login_required(login_url='/accounts/login/')
def signUp(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"awwards/post.html", {"post":post})




@login_required(login_url='/accounts/login/')
def updateUser(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewAwwardsForm(request.POST, request.FILES)
        if form.is_valid():
            updateUser = form.save(commit=False)
            updateUser.editor = current_user
            updateUser.save()
        return redirect('postToday')

    else:
        form = NewAwwardsForm()
    return render(request, 'updateUser.html', {"form": form})



def updateProfile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'profile.html', params)





class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = AwwardsMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)  

    # permission_classes = (IsAdminOrReadOnly,) 
    def post(self, request, format=None):
            serializers = MerchSerializer(data=request.data)
            if serializers.is_valid():
                  serializers.save()
                  return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

 

def project(request, id):
    post = Post.objects.get(id=id)
    ratings = Rating.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Rating.objects.filter(post=post)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'project.html', params)              