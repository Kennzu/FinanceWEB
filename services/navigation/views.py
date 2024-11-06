from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     host = request.META["HTTP_HOST"]
#     user_agent = request.META["HTTP_USER_AGENT"]
#     path = request.path

#     return HttpResponse(f'''
# HOST: {host}
# AGENT: {user_agent}
# PATH: {path}
# ''')


def main_page(request):
    return render(request, "main2.html")

def project_page(request):
    return render(request, "projects.html")

def finance_bot(request):
    return render(request, "finance_bot.html")
