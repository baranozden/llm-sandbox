from django.shortcuts import redirect, render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Chat index.")


def send_message(request):
    pass


def return_response(request):
    pass