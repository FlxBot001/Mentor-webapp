from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'index.html')

def about(request):
   return render(request, 'about.html')

def contact(request):
   return render(request, 'contact.html')

def courseDetails(request):
   return render(request, 'course-details.html')

def courses(request):
   return render(request, 'courses.html')

def events(request):
   return render(request, 'events.html')

def pricing(request):
   return render(request, 'pricing.html')

def starter(request):
   return render(request, 'starter.html')

def trainers(request):
   return render(request, 'trainers.html')