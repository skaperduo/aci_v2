from django.shortcuts import render

# Create your views here.


def programs(request):
    return render(request, 'programs.html', {})


def program_beed(request):
    return render(request, 'program_beed.html', {})


def program_bsed(request):
    return render(request, 'program_bsed.html', {})


def program_bsba(request):
    return render(request, 'program_bsba.html', {})


def program_bsais(request):
    return render(request, 'program_bsais.html', {})


def program_bsit(request):
    return render(request, 'program_bsit.html', {})


def program_maed(request):
    return render(request, 'program_maed.html', {})


def program_mba(request):
    return render(request, 'program_mba.html', {})


