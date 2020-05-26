from django.shortcuts import render

def home(request):
    return render(request, 'public/home.html')

def about(request):
    return render(request, 'public/about.html', {'title':'About'})

def staff(request):
    return render(request, 'public/staff.html', {'title':'Staff'})
