from django.conf.urls import patterns, include, url
from apps.oraculo.views import OraculoList
from django.contrib import admin
from .views import QuestionListView, QuestionCreateView, QuestionDetailView



admin.autodiscover()

urlpatterns = patterns('',

	url(r'^preguntas/$', QuestionListView.as_view(), name='questions'),
	url(r'^buscar-ajax/$', 'apps.discuss.views.BuscarAjax', name='buscar'),
	url(r'^preguntar/$', QuestionCreateView.as_view(), name='preguntar'),
	url(r'pregunta/(?P<slug>[-\w]+)/$', 
		QuestionDetailView.as_view(), name = 'detail_question'),
	 )