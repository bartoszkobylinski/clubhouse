from django.shortcuts import render
from django.views.generic import TemplateView
from chcalendar.ch_link_scraper import get_clubhouse_room_info
# Create your views here.

class CHView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['form'].is_valid():
            #save your model here
            clubhouse = get_clubhouse_room_info()
            print(clubhouse)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        



