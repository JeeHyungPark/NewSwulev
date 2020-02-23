from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

def main(request):

    board = Board.objects.all
    lecture = Lecture.objects.all
    

    return render(request, 'main.html', {'board':board, 'lecture':lecture})


def detail(request, lectureid):

    current_lecture = get_object_or_404(Lecture, pk=lectureid)
    boards = Board.objects.filter(lecture = current_lecture)

    return render(request, 'detail.html', {'current_lecture' : current_lecture, 'boards': boards})


def mypage(request):
    return render(request, 'mypage.html')


##################### about accounts #####################

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password'] == request.POST['password2']:
            # try: # if Username is overlap
            #     user_name = request.POST['id']
            #     # user = User.objects.get(username=user_name)
            #     return render(request, 'signup.html', {'error': '이미 사용 중인 이름입니다.'})
            # except User.DoesNotExist:
            user_id = request.POST['id']
            user = User.objects.create_user(username = user_id, password = request.POST['password'])
            email = request.POST['email']
            student_id = request.POST['hakbun']
            nickname = request.POST['name']
            profile = Profile(user= user, nickname=nickname ,student_id = student_id, email = email)
            profile.save_user_profile(user)
            student = Student_User(userid=user_id)
            student.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'signup.html', {'error': '아이디 또는 비밀번호 가 올바르지 않습니다.'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호 가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


#검색
def post_list(request):
    qs = Lecture.objects.all()
    q = request.GET.get('q', '')
    lectures=[]
    
    if q:
        ql = qs.filter(lecturename__icontains=q)
        qp = qs.filter(professor__icontains=q)
        if( not ql and not qp):
            return render(request, 'main.html',{'popup':True})
        else:
            for object in ql:
                lectures.append(object)
            for object in qp:
                lectures.append(object)
            return render(request, 'main_search.html', {'lectures' : lectures,'q' : q,})
