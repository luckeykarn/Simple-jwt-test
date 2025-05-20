# from django.shortcuts import render
# from simple_jwt_test.models import Category,Product

# def api_testing(request):
#     context = {
#         "title":"api_testing"
#     }
#     return render(request,context)

# # Create your views here.

from django.http import HttpResponse

def api_testing(request):
    return HttpResponse("API Testing Endpoint")
