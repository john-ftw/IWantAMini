from django.http import HttpResponse

def index(request):
    return HttpResponse("Windows Azure, I'd like a Mini please!")
