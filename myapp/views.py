from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects #Blog 클래스 안에 있는 객체를 받아준다.
    #모델로부터 객체 목록을 전달 받는다.
    #.object : 모델로부터 객체 목록을 전달 받을 수 있게 함.
    #쿼리셋 : 모델로부터 전달 받은 객체 목록
    return render(request, 'home.html', {'blogs':blogs})
