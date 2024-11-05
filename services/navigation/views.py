from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    return HttpResponse(f'''
HOST: {host}
AGENT: {user_agent}
PATH: {path}
''')