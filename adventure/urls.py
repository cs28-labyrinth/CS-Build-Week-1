from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('generate', api.generate),
    url('move', api.move),
    url('say', api.say),
    url('take', api.take), ## WIP
    url('use', api.use) ## WIP
]