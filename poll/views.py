from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.core.urlresolvers import reverse
from . models import Poll, Choice

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:6]
    return render(request, 'poll/index.html', {'latest_poll_list':latest_poll_list})

def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return  render(request, 'poll/detail.html', {'poll':poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(id=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {
            'poll':poll,
            'error_message':"You didn't select a choice"
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('poll:result', args=str(poll.id)))

def result(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'poll/result.html', {
        'poll':poll
    })