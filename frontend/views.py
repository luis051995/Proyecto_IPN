from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def registro(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())