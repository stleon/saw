from django.shortcuts import render
from site_enter.forms.forms import EnterSiteForm
from django.views.decorators.csrf import csrf_protect
from site_auditor import SiteAuditor
from site_enter.models import Site
from site_enter.models import SiteBaseInformation
import datetime
from django.utils import timezone
from django.contrib import messages


@csrf_protect
def home(request):

	site = None
	two_weeks = None

	def base_inf(site_obj, type_scan):
		s = SiteAuditor(obj.site, type_scan)
		if not s.error:
			SiteBaseInformation.objects.create(site=site_obj, yandex_tyc=s.yad['tyc'], google_pr=s.pr,
								   alexa_all_world=s.alexa['all_world'], alexa_country=s.alexa['country'],
								   alexa_rank_in_country=s.alexa['rank_in_country'],
								   yandex_blog_links=s.yad['blogs'], proindex_google=s.pro_index['google'],
								   proindex_yandex=s.pro_index['yandex_standart'],
								   proindex_yandex_popal=s.pro_index['yandex_in_index'],
								   yahoo_index=s.pro_index['yahoo_index'], bing_outgoing_links=s.bing[0],
								   bing_index=s.bing[1])
		else:
			messages.add_message(request, messages.ERROR, s.error)
			s = None
		return s

	if request.method == 'POST':
		form = EnterSiteForm(request.POST)
		if form.is_valid():
			# TODO: сразу пишет в бд, а сайт может и не пройти валидацию на адрес. Исправить
			obj, created = Site.objects.get_or_create(site=form.cleaned_data['site'].strip().lower(),)
			if created:  # если сайта нет вообще, полный скан
				site = base_inf(obj, 'y')
			else:
				if SiteBaseInformation.objects.all().filter(
						date_created__lt=timezone.now() - datetime.timedelta(days=14), site=obj.id):  # прошло 14 дней, полный скан
					site = base_inf(obj, 'y')
				else:  # не прошло 14 дней, часть из бд, часть из 2w
					site = Site.objects.get(id=obj.id)
					two_weeks = SiteAuditor(obj.site, '2w')
	else:
		form = EnterSiteForm()
	return render(request, 'index.html', {'form': form, 'site':site, 'two_weeks':two_weeks,})