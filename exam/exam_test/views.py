from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Question,Answer
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from django.http import JsonResponse
from django.core.cache import cache
from .serializer import QuestionsSerializers

def index(request):
    # Önbelleği temizle

    return render(request,'index.html')

@login_required
def warning(request):
    return render(request,'warning.html')

def register(request):
    if request.POST:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, account is created')
            return redirect('/register/')
        else:
            messages.error(request,'Try Again')
    form=UserCreationForm()
    return render(request,'register.html',{'form':form})


@login_required
def show_question(request, question_id):

    question = Question.objects.get(pk=question_id)
    next_question_id = question_id + 1  # Increment the question_id
    
    cache_key = f'question_{next_question_id}'

    # # veriyi json atmak Mehmet Halil MUNGAN
    # serializer = QuestionsSerializers(question)
    # veriyiGor = JsonResponse(serializer.data)
    # # cache.set("json",veriyiGor,300)

    deneme = Question.objects.all()

    for veri in deneme:
        serializer = QuestionsSerializers(veri)
        veriyiJson = JsonResponse(serializer.data)
        cache.set(f'{veri.id}',veriyiJson,300)

    try:
        answer = Answer.objects.get(question=question, user=request.user)
        answer_text = answer.answer_text
        # cevap=cache.set(f'{cache_key}',answer_text,15)
        # json_data == True dönüyor
        # json_data=json.dumps(cevap)
        
    except Answer.DoesNotExist:
        answer = None
    
    
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        


        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()

            messages.success(request, f'Soru {question_id} için cevabınız başarıyla kaydedildi.')
            form = AnswerForm()


            try:
                next_question = Question.objects.get(pk=next_question_id)
                answer_text = answer.answer_text
                response = HttpResponse(render(request, 'questions.html', {'form': form, 'question': next_question, 'next_question_id': next_question_id}))
                response.set_cookie('last_question_id', next_question_id)
                return response

            except Question.DoesNotExist:
                return redirect('completion_page')
    else:
        form = AnswerForm(instance=answer)    
    return render(request, 'questions.html', {'form': form, 'question': question, 'next_question_id': question_id})


def completion_page(request):
       return render(request,'completion.html')

def view_answers(request):
    answers=Answer.objects.filter(user=request.user)
    answered_questions = [answer.question for answer in Answer.objects.filter(user=request.user)]
    return render(request,'answers.html',{'answers':answers,'questions':answered_questions})