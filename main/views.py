from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as inbuilt_login
from django.contrib.auth import logout as inbuilt_logout
from .models import Image
from django import forms
from random import randint
from .models import ProfilePic
import re
from random import shuffle

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# HELPER FUNCTIONS
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

def get_profile_pic(email):
    picture = ProfilePic.objects.filter(email=email)
    if len(picture) == 0:
        return None
    return picture[0]

# Create your views here.

def home(request):
    images = list(Image.objects.all().reverse())
    images = images[-1::-1]
    # shuffle(images)
    img_rows = [[], [], [], []]
    for i in range(len(images)):
        img_rows[i % 4].append(images[i])
    pp = None
    if (request.user.is_authenticated):
        pp = get_profile_pic(request.user.email)
    return render(request, "index.html", {'col1': img_rows[0], 'col2': img_rows[1],
                                          'col3': img_rows[2], 'col4': img_rows[3],
                                          'pp': pp})

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        return render(request, "signup.html")
    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        password = request.POST["password"]

        if not re.search(regex, email):
            return render(request, 'signup.html', {'isError': True, 'error': 'Please enter valid email address',
                                                   'name': name, 'email': email})
        if len(User.objects.filter(email=email)) > 0:
            return render(request, 'signup.html', {'isError': True, 'error': 'This email already exists. Login instead?',
                                                   'name': name, 'email': email})
        username = list(email.split("@"))[0] + '-' + str(randint(1, 1000000))
        user = User.objects.create_user(username=username, email=email, password=password)
        img = ProfilePic.objects.create(email=email)
        user.first_name = name
        user.last_name = "Hey there, I am using Kliks."
        user.save()
        img.save()
        inbuilt_login(request, user)
        return redirect('edit-profile')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        return render(request, "login.html", {'isError': False})
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        if (len(user) == 0):
            return render(request, "login.html", {'isError': True, 'email': email})
        user = authenticate(username=user[0].username, password=password)
        if user is None:
            return render(request, "login.html", {'isError': True, 'email': email})
        inbuilt_login(request, user)
        return redirect('home')

def logout(request):
    inbuilt_logout(request)
    return redirect('home')


def upload(request):

    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return render(request, 'upload.html', {'pp': get_profile_pic(request.user.email)})
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            new_image = Image.objects.create()
            new_image.user_email = request.user.email
            new_image.title = (request.POST['title'])
            new_image.img = form.cleaned_data['image']
            new_image.small_img = form.cleaned_data['image']
            new_image.save()
            return redirect('home')


def profile(request, username):
    user = User.objects.filter(username=username)
    if (len(user) == 0):
        return redirect('home')
    user = user[0]
    images = Image.objects.filter(user_email=user.email)
    pp = None
    self = False
    if (request.user.is_authenticated):
        pp = get_profile_pic(request.user.email)
        if (request.user.email == user.email): self = True
    images = list(images)[-1::-1]
    img_rows = [[], [], [], []]
    for i in range(len(images)):
        img_rows[i % 4].append(images[i])

    return render(request, 'profile.html', {'profile_user':user,'profile_pp': get_profile_pic(user.email), 'pp': pp, 'self': self,
                                            'col1': img_rows[0], 'col2': img_rows[1],
                                            'col3': img_rows[2], 'col4': img_rows[3],
                                            'count': len(images)
                                            })

def self_profile(request):
    if (not request.user.is_authenticated):
        return redirect('home')
    return redirect('/profile/' + request.user.username)

def full_page_image(request, id):
    image = Image.objects.filter(id=id)
    if (len(image) == 0):
        return redirect('home')
    image = image[0]
    image_user = User.objects.filter(email=image.user_email)[0]
    count = len(Image.objects.filter(user_email=image.user_email))
    pp = None
    if (request.user.is_authenticated):
        pp = get_profile_pic(request.user.email)



    return render(request, "image_fullpage.html",
                  {'image': image, 'image_user': image_user, 'image_pp': get_profile_pic(image_user.email),
                   'count': count, 'pp': pp})

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        return render(request, 'edit-profile.html', {'pp': get_profile_pic(request.user.email)})
    else:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST['name']
            user.last_name = request.POST['bio']
            user.save()
            profile_object = ProfilePic.objects.filter(email=user.email)[0]
            profile_object.pp = form.cleaned_data['image']
            profile_object.save()
            return redirect('/profile')
        else:
            user = request.user
            user.first_name = request.POST['name']
            user.last_name = request.POST['bio']
            user.save()
            return redirect('/profile')

def search(request, key):

    words = list(key.lower().split('_'))
    images = Image.objects.all()
    filtered_images = []
    for image in images:
        matches = False
        for word in words:
            if word in image.title.lower():
                matches = True
        if matches:
            filtered_images.append(image)
    filtered_images = filtered_images[-1::-1]
    img_rows = [[], [], [], []]
    for i in range(len(filtered_images)):
        img_rows[i % 4].append(filtered_images[i])

    pp = None
    if request.user.is_authenticated:
        pp = get_profile_pic(request.user.email)

    return render(request, 'search.html', {'col1': img_rows[0], 'col2': img_rows[1],
                                            'col3': img_rows[2], 'col4': img_rows[3],
                                            'count': len(filtered_images),
                                           'pp': pp, 'key': " ". join(list(key.split("_"))),
                                           "Key": (" ". join(list(key.split("_")))).capitalize()})