from django.shortcuts import render

# Create your views here.
def submit_feedback(request):
    return render(request , 'feedback.html')

