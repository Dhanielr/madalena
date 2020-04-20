from django.shortcuts import render
from django.views.generic import TemplateView

from .tasks import sleepy_test

class TestView(TemplateView):

    template_name = 'resizer/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data()
        context['test'] = 'Página de Testes'

        sleepy_test.delay(10)

        return context
