import os, sys

sys.path.append('D:\\Sunil\\Python\\StayForShop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'StayForShop.settings'

path = 'D:\\Sunil\\Python\\StayForShop'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


'''
import os, sys
#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)

os.environ['DJANGO_SETTINGS_MODULE'] = 'StayForShop.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

'''