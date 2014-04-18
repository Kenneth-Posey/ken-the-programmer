#!/usr/bin/env python

import sys

# added extra paths here because pythonanywhere is somewhat screwy about importing properly
site_packages_path = '/usr/local/lib/python2.7/site-packages'
if site_packages_path not in sys.path:
    sys.path.append(site_packages_path)
    
site_packages_path = '/home/mr_pleco/website/svn/website'
if site_packages_path not in sys.path:
    sys.path.append(site_packages_path)
    
pil_path = '/usr/local/lib/python2.7/site-packages/PIL'
if pil_path not in sys.path:
    sys.path.append(pil_path)

from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
