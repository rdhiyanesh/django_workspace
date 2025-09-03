from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import question

def index(request):
    return HttpResponse("hello world , you are at the polls index")


def details(request,question_id):
    return HttpResponse("your looking at a question  %s."  % question_id)

def results (request,question_id):
    response="you are looking at the results of the question %s."
    return HttpResponse(response % question_id )

def votes(request,question_id):
    return HttpResponse("you're voting question is %s." % question_id)

def index(request):
    latest_question_list=question.objects.order_by("-pub_date")[:5]
    output=", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    latest_question_list=question.objects.order_by("-pub_date")[:5]
    template=loader.get_template("polls/index.html")
    context={"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    try:
        question=question.object.get(pk=question_id)
    except question.DoesNotExist:
        raise Http404("question does not exist")
    return render( request, "polls/details.html",{"question:question"})
    



