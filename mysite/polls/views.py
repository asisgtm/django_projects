from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 83f25503 is the polls index.")