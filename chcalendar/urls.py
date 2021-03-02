from django.urls import path

from chcalendar.views import CHView

urlpatterns = [
    path('', CHView.as_view(), name='main')
]