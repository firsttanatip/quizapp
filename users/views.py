from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from quiz.models import *
from quiz.forms import *
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'quiz/profile.html', context)


def createquiz(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:reviewquiz')
    context = {'form':form}
    return render(request, 'quiz/createquiz.html', context)


def updatequiz(request, pk1):
    
	quiz = Questions.objects.get(id=pk1)
	form = QuestionForm(instance=quiz)

	if request.method == 'POST':
		form = QuestionForm(request.POST, instance=quiz)
		if form.is_valid():
			form.save()
			return redirect('users:reviewquiz')#name url

	context = {'form':form}
	return render(request, 'quiz/createquiz.html', context)

def reviewquiz(request):
    context = {
        'quiz':Questions.objects.all().order_by('-id')
    }
    return render(request, 'quiz/reviewquiz.html',context)


def deletequiz(request, pk):
    quiz = Questions.objects.get(id=pk)
    if request.method == "POST":
        quiz.delete()
        return redirect('users:reviewquiz')
    context = {'quiz':quiz}
    return render(request, 'quiz/deletequiz.html', context)

def index(request):
    return render(request,
        'quiz/index.html')
    
def kemail(request):
    return render(request,
        'quiz/kemail.html')
    
def exam(request):
    cate = Category.objects.all()
    print(cate)
    return render(request,
        'quiz/exam.html',
        {'cate':cate})
    
def k7solution(request):
    return render(request,
        'quiz/k7solution.html')
    
def kbye(request):
    return render(request,
        'quiz/kbye.html')
    
def createexam(request):
    form = ExamForm()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:reviewexam')
    context = {'form':form}
    return render(request, 'quiz/createexam.html', context)

def reviewexam(request):
    context = {
        'exam':Exam.objects.all().order_by('-id')
    }
    return render(request, 'quiz/reviewexam.html',context)

def updateexam(request, pk1):
    
	quiz = Exam.objects.get(id=pk1)
	form = ExamForm(instance=quiz)

	if request.method == 'POST':
		form = ExamForm(request.POST, instance=quiz)
		if form.is_valid():
			form.save()
			return redirect('users:reviewexam')#name url

	context = {'form':form}
	return render(request, 'quiz/createexam.html', context)

def deleteexam(request, pk):
    exam = Exam.objects.get(id=pk)
    if request.method == "POST":
        exam.delete()
        return redirect('users:reviewexam')
    context = {'exam':exam}
    return render(request, 'quiz/deleteexam.html', context)



    