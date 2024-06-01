"""
ASGI config for djangchan project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangchan.settings')

application = get_asgi_application()


from django.urls import path
from channels.routing import ProtocolTypeRouter , URLRouter
from home.consumers import *
ws_patt=[
    
    path('test/' , TestConsumer ),
    
    
    ]
application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests

      'websocket':URLRouter(ws_patt)
})
