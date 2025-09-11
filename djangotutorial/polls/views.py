from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Choice , Question

def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    template=loader.get_template("polls/index.html")
    context={"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context,request))

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

def votes(request, question_id):
    # Get the question object or return 404 if not found
    question = get_object_or_404(Question, pk=question_id)

    try:
        # Get the selected choice from POST data
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # If no choice was selected or choice does not exist,
        # re-render the detail page with an error message
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # Increment the vote count using F() expression (safe for concurrency)
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        selected_choice.refresh_from_db()

        # Redirect to the results page after successful vote submission
        # (Prevents duplicate submissions if user hits Back/Refresh)
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )
    
def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{"question":question})

