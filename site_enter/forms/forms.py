# -*- coding: utf-8 -*-
from django import forms


class EnterSiteForm(forms.Form):
	site_label = 'Введите название сайта'
	site = forms.CharField(label=site_label, max_length=255, min_length=4, required=True, help_text = site_label,
		widget=forms.TextInput(attrs={'class':'', 'title': site_label, 'placeholder': site_label, 'required': 'true',
		'pattern':'.{4,}'}))