from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
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

def autopay_app(request):
    return render(request, "autopay.html")

def documentation_bot(request):
    return render(request, "bot_doc.html")

def authorize(request):
    return render(request, "auth.html")

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.clean_data.get('password')
            email = form.cleaned_data.get('email')

            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('projects/')
        else:
            form = UserCreationForm()

    return render(request, 'registration.html')
