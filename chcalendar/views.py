from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from chcalendar.ch_link_scraper import get_clubhouse_room_info
from chcalendar.forms import CHForm
from chcalendar.models import CHRoom,Host
# Create your views here.

class CHView(TemplateView, FormMixin):
    template_name = 'index.html'
    form_class = CHForm
    success_url = 'index.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            clubhouse_url = form.data['url']
            clubhouse_event_info = get_clubhouse_room_info(clubhouse_url)
            chroom = CHRoom(title=clubhouse_event_info.get('title',''), date=clubhouse_event_info.get('room_date',''), description=clubhouse_event_info.get('description',''))
            chroom.save()
            host_information = list(zip(clubhouse_event_info.get("hosts",''), clubhouse_event_info.get('avatars','')))
            for host in host_information:
                room_host = Host(name=host[0], avatar=host[1], room=chroom)
                room_host.save()
            return self.form_valid(form)
        else:
            form = self.get_form(form_class)
            return self.form_invalid(form)
    

    def get_context_data(self, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = super().get_context_data(*args, **kwargs)
        context['room'] = CHRoom.objects.all()
        context['hosts'] = Host.objects.all()
        return context
        



