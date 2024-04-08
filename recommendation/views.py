from django.shortcuts import render

# Create your views here.
def recommendations_view(request):
    return render(request, 'recommendations.html')
