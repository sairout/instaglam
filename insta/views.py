from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import InstaUser, Photo, Follower, Likes, Comments
# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            u = InstaUser(user=user)
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return render(request, 'sign-up.html')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Id already Exists')
            return render(request, 'sign-up.html')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            u = InstaUser(user=user)
            u.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'sign-up.html')


def home(request):
    if request.user.is_authenticated:
        users = InstaUser.objects.all()
        for user in users:
            if user.user.username == request.user.username:
                u = user
                break
        followed = Follower.objects.filter(follower=u.user.username)
        followed_list = []
        for follow in followed:
            followed_list.append(follow.username)
        photos = Photo.objects.filter(owner__in=followed_list).order_by('-date_uploaded')
        context = {'instauser': u, 'photofeed': photos}
        return render(request, 'home.html', context)
    else:
        return redirect('index')


def upload(request, pk):
    if request.method == 'POST':
        photo = request.FILES['photo']
        caption = request.POST['caption']
        username = User.objects.get(id=pk).username
        profilepic = InstaUser.objects.get(user=request.user).profilepic
        p = Photo(photo=photo, caption=caption, owner=username, owner_profilepic=profilepic)
        p.save()
        return redirect('home')
    else:
        return render(request, 'upload.html')


def own_profile(request):
    users = InstaUser.objects.all()
    for user in users:
        if user.user == request.user:
            u = user
            break

    photos = Photo.objects.filter(owner=u.user.username)
    context = {'instauser': u, 'photos': photos}
    return render(request, 'own-profile.html', context)



def profile(request, pk):
    instausers = InstaUser.objects.all()
    user = User.objects.get(id=pk)
    for instauser in instausers:
        if instauser.user.username == user.username:
            u = instauser
            break
    photos = Photo.objects.filter(owner=u.user.username)
    f = Follower.objects.filter(username=u.user.username, follower=request.user.username)
    if f:
        following = True
    else:
        following = False
    context = {'instauser': u, 'photos': photos, 'following': following}
    return render(request, 'profile.html', context)


def feed_profile(request, pk):
    id = User.objects.get(username=pk).id
    return profile(request, id)


def profilepic_upload(request, pk):
    if request.method == 'POST':
        profilepic = request.FILES['photo']
        u = InstaUser.objects.get(user=request.user)
        u.profilepic = profilepic
        u.save()
        photos = Photo.objects.filter(owner=request.user.username)
        for photo in photos:
            photo.owner_profilepic = profilepic
            photo.save()
        return redirect('own-profile')
    else:
        return render(request, 'profilepic-upload.html')


def list(requset):
    users = InstaUser.objects.all().exclude(user=requset.user)
    context = {'instausers': users}
    return render(requset, 'list.html', context)


def follow(request, pk):
    username = User.objects.get(id=pk)
    f = Follower(username=username, follower=request.user.username)
    f.save()
    return redirect('/')


def unfollow(request, pk):
    username = User.objects.get(id=pk)
    f = Follower.objects.filter(username=username, follower=request.user.username)[0]
    f.delete()
    return redirect('/')


def post_detail(request, pk):
    post = Photo.objects.get(id=pk)
    likes = Likes.objects.filter(postid=pk).order_by('-date')
    comments = Comments.objects.filter(postid=pk).order_by('-date')
    liked = Likes.objects.filter(postid=pk, liker=request.user.username)
    if liked:
        liked = True
    else:
        liked = False
    context = {'post': post, 'likes': likes, 'comments': comments, 'liked': liked}
    return render(request, 'post-detail.html', context)


def like(request, pk):
    l = Likes.objects.filter(postid=pk, liker=request.user.username)
    if not l:
        Likes.objects.create(postid=pk, liker=request.user.username)
        photo = Photo.objects.get(id=pk)
        photo.likes = photo.likes+1
        photo.save()
    return redirect('home')


def unlike(request, pk):
    l = Likes.objects.filter(postid=pk, liker=request.user.username)
    l.delete()
    photo = Photo.objects.get(id=pk)
    photo.likes = photo.likes-1
    photo.save()
    return redirect('home')


def comment(requset, pk):
    cmt = requset.POST['comment']
    Comments.objects.create(postid=pk, commenter=requset.user.username, comment=cmt)
    photo = Photo.objects.get(id=pk)
    photo.comments = photo.comments+1
    photo.save()
    return redirect('home')


def own_post_detail(request, pk):
    post = Photo.objects.get(id=pk)
    likes = Likes.objects.filter(postid=pk).order_by('-date')
    comments = Comments.objects.filter(postid=pk).order_by('-date')
    liked = Likes.objects.filter(postid=pk, liker=request.user.username)
    if liked:
        liked = True
    else:
        liked = False
    context = {'post': post, 'likes': likes, 'comments': comments, 'liked': liked}
    return render(request, 'own-post-detail.html', context)


def edit(request, pk):
    if request.method == 'POST':
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
        else:
            photo = ''
        caption = request.POST['caption']
        post = Photo.objects.get(id=pk)
        if photo:
            post.photo = photo
        if caption:
            post.caption = caption
        post.save()
        return redirect('own-profile')
    else:
        post = Photo.objects.get(id=pk)
        context = {'post': post}
        return render(request, 'edit-post.html', context)


def delete(request, pk):
    if request.method == 'POST':
        post = Photo.objects.get(id=pk)
        Likes.objects.filter(postid=pk).delete()
        Comments.objects.filter(postid=pk).delete()
        post.delete()
        return redirect('own-profile')
    else:
        return render(request, 'delete-post.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
