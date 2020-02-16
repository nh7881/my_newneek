from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.utils import timezone
# Create your views here.

def home_page(request) :
    # 이름 이메일 관심분야 등 입력 받는 페이지
    # 입력받고 제출 시 submit 페이지 실행
    # submit - post
    return HttpResponse('sucess')

def add_user(request) :
    # 동의서 작성(생략)
    # 입력 받은 값 db의 저장 후 다시 home_page로 콜백
    # request 안에 이름 이메일 관심분야 들어있어야함
    user = User.objects.create(name = request.POST['name'], email = request.POST['email'], major = request.POST['major'], create_date = timezone.now())
    user.save()