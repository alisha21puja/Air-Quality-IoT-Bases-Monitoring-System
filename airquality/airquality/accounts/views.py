from django.shortcuts import render



# Create your views here.

import gmaps


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


def index(request):
	return render(request,'index.html')

def login(request):
	return render(request,'accounts.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirmpassword']
        phone = request.POST['phone']
        type_usr = request.POST['type_usr']
        src = request.POST['profile_img']
        #mobile  = request.POST['mobile']
        #userType = request.POST['usertype']
        if password == password2:
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
                    key = user._get_pk_val()
                    var = UserProfile(id=key, type_usr=type_usr,
                                      phone=phone, profile_img=src)
                    var.save()
                    message = ""
                    if type_usr == 100:
                        message = "User Name :"+email + " PASSWORD :" + password + \
                            " EMAIL : "+email+" PHONE : "+phone+" Role : PARTICIPANT"
                    elif type_usr == 200:
                        message = "User Name :"+email + " PASSWORD :" + password + \
                            " EMAIL : "+email+" PHONE : "+phone+" Role : SPONSER"
                    elif type_usr == 300:
                        message = "User Name :"+email + " PASSWORD :" + password + \
                            " EMAIL : "+email+" PHONE : "+phone+" Role : ORGANISER"

                    send_mail('Subject' + "YOU HAVE NOW REGISTERED TO TECH EVENT",
                              'Message' + message + 'Will Contact your soon',
                              'sachin.thakur9614@gmail.com',
                              [email, 'sachin.thakur@mca.christuniversity.in', ],
                              fail_silently=True)
                    messages.success(request, 'You are now registered in')
                    return redirect('accounts')
        elif first_name == '':
            messages.error(request, 'FirstName  field  is empty')
        elif last_name == '':
            messages.error(request, 'Last Name field  is empty')
        elif username == '':
            messages.error(request, 'Username field  is empty')
        elif email == '':
            messages.error(request, 'Email field   is empty')
        elif password == '':
            messages.error(request, 'Password is empty')
        elif password2 == '':
            messages.error(request, 'Confirm password field is empty')
        else:
            messages.error(request, 'Password do not match')
            return redirect('accounts')
    else:
        return render(request, 'base.html')




