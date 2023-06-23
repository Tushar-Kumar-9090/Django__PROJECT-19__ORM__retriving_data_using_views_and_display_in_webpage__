"""
ASGI config for project22_ORM_retriving_data_using_view_and_display_in__webpage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project22_ORM_retriving_data_using_view_and_display_in__webpage.settings')

application = get_asgi_application()
