from django.shortcuts import render



# Create your views here.

import gmaps

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
import gmaps
import gmaps.datasets
import os
import ipywidgets as widgets
import geopy
# export GOOGLE_API_KEY='AIzaSyBcT_KzlYcyYf-171L7pR6ngBgZHYq24C4'

def fun(request):

	gmaps.configure(api_key = 'AIzaSyBcT_KzlYcyYf-171L7pR6ngBgZHYq24C4')
	dataset = gmaps.datasets.load_dataset_as_df('earthquakes')
	dataset.head()
	location = dataset[['latitude','longitude']]
	weight = dataset['magnitude']
	fig = gmaps.figure()
	fig.add_layer(gmaps.heatmap_layer(location,weights = weight))
	fig = gmaps.figure(map_type='ROADMAP')
	# 'ROADMAP', 'HYBRID', 'TERRAIN', 'SATELLITE'

	return render(request,'index.html',{'fig':fig})


def login_signup(request):
    return render(request,'login.html')

def index(request):
	return render(request,'accounts.html')

def login(request):
	return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "That username is taken")
            return render(request, 'login.html', {'errorr': 'Username is already taken'})
            # return redirect('accounts')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, "That email is been use")
                return render(request, 'login.html', {'errorr': 'Email is in use '+email})
                return redirect('accounts')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                # auth.login(request,user)
                #messages.success(request,'You are now Loged in')
                user.save()
                messages.success(request, 'You are now registered in')
                return redirect('accounts')
    



