from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import ml 

def home(request):
    # If the user is logged in, show only the Get Started and Logout buttons
    context = {'user': request.user}
    return render(request, 'app/home.html', context)
def get_started(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not logged in
    return redirect('predict')  # Redirect to the prediction form if the user is logged in
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'app/login.html')
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.objects.create_user(username=username, password=password)
#         login(request, user)
#         return redirect('home')
#     return render(request, 'app/signup.html')
def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already exists. Please try logging in.')
            return redirect('signup')

        user = User.objects.create_user(username=email, password=password)
        user.save()
        messages.success(request, 'Signup successful! Please log in.')
        return redirect('login')

    return render(request, 'app/signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def house_predict(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        # Handle form submission and display a random price
        # In reality, a machine learning model would predict the price
        
        locality_name = request.POST.get('locality')
        bhk = request.POST.get('bhk')
        predicted_price = ml.predict_price({'locality_name':locality_name,'bhk':int(bhk)})

        return render(request, 'app/result.html', {'price': predicted_price})

    return render(request, 'app/predict.html')
