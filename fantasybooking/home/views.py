# Create your views here.

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.http import HttpResponse
from fantasybooking.home.models import Wrestler, Stable, WeeklyStat
from fantasybooking.home.forms import StableForm, WrestlerForm
from django.forms import modelformset_factory
from django.shortcuts import render

from .forms import UserForm


@method_decorator(login_required, name='dispatch')
class ExampleFormView(FormView):
    form_class = UserForm
    template_name = 'example_form.html'
    success_url = "/form"

    def form_valid(self, form):
        form.good_to_go()
        return super(ExampleFormView, self).form_valid(form)


def error(request):
    """Generate an exception. Useful for e.g. configuing Sentry"""
    raise Exception

#Change Stable for Existing Wrestlers
def wrestlers(request):
    wrestler = Wrestler.objects.get(pk=1)
    WrestlerFormSet = modelformset_factory(Wrestler, form=WrestlerForm)

    formset = WrestlerFormSet(request.POST or None)
    if request.method == 'POST':
        if formset.is_valid():
            formset.save(commit=True)
            return create_stable(request)
        else:
            print(form.errors)

    return render(request, 'wrestlers.html', {'formset': formset})

#Create new stable and assign to existing user
def create_stable(request):
    form = StableForm()

    if request.method == 'POST':
        form = StableForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return wrestlers(request)
        else:
            print(form.errors)
    return render(request, 'create_stable.html', {'form': form})

#Create match view
def match(request):
    form = MatchForm()
