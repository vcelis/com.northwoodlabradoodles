#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import urllib

# Force dev mode even on deployed app.
# Caching and error reporting use this setting.
# Only use while debugging!
FORCE_DEV = True

# Application title and meta settings
APP_TITLE = 'Northwood Labradoodles'
APP_DESCRIPTION = 'Genuine Australian Labradoodle Breeder located in North Texas. Breeding healthy, beautiful, non-shedding, and well-socialized family companions through the utilization of Puppy Culture and Early Neurological Stimulation.'
APP_KEYWORDS = 'Australian Labradoodle, Australian Labradoodle Breeder, Texas, North Texas, Dallas, breeders, Puppies, ALCA, ALAA, Puppy Culture, biosensor, Labradoodle, For Sale, Doodle, ALD, USA, Puppy, Best Australian Labradoodle Breeder, Non-Shedding, No Shed, Caramel, Red, Parti, Available Puppies, Health Tested, Rutland Manor, Tegan Park, Therapy Dog, Service Dog'
APP_AUTHOR = 'Northwood Labradoodles'

# The directory where the templates live
TEMPLATE_DIR = 'templates'
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), TEMPLATE_DIR)
# Enable/Disable jinja2 auto escape
TEMPLATE_ESCAPE = True
# Jinja2 cache timeout
JINJA2_BYTECODE_TIMEOUT = 3600

# URLS
APP_URLS = {
  'canonical': 'http://localhost:8080',
  'canonical_secure': 'https://localhost:8080'
}

# Template filenames
TEMPLATE_FILENAME = {
  'home': 'home.html'
}

# Regex for form fields
RE_EMAIL = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
#RE_EMAIL = re.compile(r'[^@]+@[^@]+\.[^@]+')

# Form validation error messages
RE_EMAIL_FAIL = 'That\'s not a valid email. Please try again.'
RE_EMAIL_SUCCESS = 'You will be the first to be updated!'

# Email settings
CONFIRMATION_MAIL_SENDER = 'Northwood Labradoodles <northwoodlabradoodles@gmail.com>'
CONFIRMATION_MAIL_SUBJECT = 'Northwood welcomes you!'
CONFIRMATION_MAIL_BODY = urllib.urlopen("templates/email.txt").read()
CONFIRMATION_MAIL_BODY_HTML = urllib.urlopen("templates/email.html").read()
