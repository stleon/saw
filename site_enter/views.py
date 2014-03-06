from django.shortcuts import render
from site_enter.forms.forms import EnterSiteForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home(request):
	if request.method == 'POST':
		form = EnterSiteForm(request.POST)
		if form.is_valid():
			site = form.cleaned_data['site'].strip()
	else:
		form = EnterSiteForm()
	return render(request, 'index.html', {'form': form})