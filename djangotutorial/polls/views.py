from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice , Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ Return the last five published questions (not including those set to be
        published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request, question_id):
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


class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"



