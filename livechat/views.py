from django.shortcuts import render , HttpResponse

# Create your views here.
def chat(request):
    return render(request , 'livechat.html')
