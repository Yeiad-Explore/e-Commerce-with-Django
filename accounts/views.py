from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User #import user


# Create your views here.
def login_page(request):
    return render(request ,'accounts/login.html')



def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        #If user already exists
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.') # An error message
            return HttpResponseRedirect(request.path_info) #Redirect to same page
        print(email)    

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()


     


    return render(request ,'accounts/register.html')    

