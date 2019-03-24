from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def user_authenticate(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return redirect('https://www.google.co.in/')
            else:
                return render(request, 'user_authenticate.html', {'message': 'Password is Incorrect!!'})
        except User.DoesNotExist:
            return render(request, 'user_authenticate.html', {'message': 'No such user exists!! Try again'})

    return render(request, 'user_authenticate.html', {'message': 'Welcome to Screenly Login'})
