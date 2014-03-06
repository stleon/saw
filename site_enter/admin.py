from django.contrib import admin
from site_enter.models import Site
from site_enter.models import SiteBaseInformation


class SiteBaseInformationInline(admin.TabularInline):
	model = SiteBaseInformation
	extra = 0

class SiteAdmin(admin.ModelAdmin):
	search_fields = ['site_name']
	list_display = ('site', 'date_created', 'date_updated', 'active')
	list_filter = ['active']
	inlines = [SiteBaseInformationInline]


class SiteBaseInformationAdmin(admin.ModelAdmin):
	search_fields = ['site__site']
	list_display = ('site', 'yandex_tyc', 'google_pr', 'date_created', 'date_updated',)


admin.site.register(Site, SiteAdmin)
admin.site.register(SiteBaseInformation, SiteBaseInformationAdmin)