from django.shortcuts import render, redirect
from django.template.response import TemplateResponse



from django.views.generic import ListView, TemplateView
from apps.discuss.models import Question, Tag

from apps.users.models import User





class OraculoList(ListView):


	template_name = 'oraculo/oraculo.html'
	queryset = Question.objects.all()[:5]

	def get_queryset(self, *args, **kwargs):
		tags = [ question.tag.all() for question in self.queryset ]
		return zip(self.queryset, tags)

	def get_context_data(self, **kwargs):
		context = super(OraculoList, self).get_context_data(**kwargs)
		context['total_questions'] = Question.objects.count()
		context['total_users'] = User.objects.exclude(is_superuser=True).count()
		return context




def oraculo(request):
	return TemplateResponse(request, 'oraculo/oraculo.html')


