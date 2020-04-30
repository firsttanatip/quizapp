from django.shortcuts import render,redirect
from .models import Questions
from .forms import *
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    cate = Category.objects.all()
    print(cate)
    return render(request,
        'quiz/home.html',
        {'cate':cate})
    
def exam(request,cate_id):
    cate1 = Category.objects.get(id=cate_id)
    exam = Exam.objects.filter(category=cate_id)
    context = {'exam':exam,'cate':cate1}
    return render(request,'quiz/exam1.html',context)

def question(request,quest_id):
    exam1 = Exam.objects.get(id=quest_id)
    quest = Questions.objects.filter(exam=quest_id)
    context = {'exam':exam1,'quest':quest}
    return render(request,'quiz/quest.html',context)
    
  



def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        print(qid)
        print(qans)
        print(ans)
        print(score)
        eff = (score/total)*100
    return render(request,
        'quiz/result.html',
        {'score':score,
        'eff':eff,
        'total':total})
    
def about(request):
    return render(request,
        'quiz/about.html')

def contact(request):
    return render(request,
        'quiz/contact.html')
    

    
    










#
#
#
#
#
#
#
