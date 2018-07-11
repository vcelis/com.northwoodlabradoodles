#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import BaseHandler
from google.appengine.api import mail
from google.appengine.api import app_identity

import settings
import webapp2
import logging

def validateEmail(email):
  """Function to validate email provided.
  Returns True if the email matched the regex.
  Returns the validation error message specified in settings
  """
  if settings.RE_EMAIL.match(email):
    return True
  else:
    return False

def sendConfirmationEmail(email):
  mail.send_mail(sender=settings.CONFIRMATION_MAIL_SENDER,
                 to=email,
                 subject=settings.CONFIRMATION_MAIL_SUBJECT,
                 body=settings.CONFIRMATION_MAIL_BODY)

class EmailRegistrationPage(BaseHandler):
  """Page handler for the email registration form.

  Page handler to handle the requests for the email registration form.
  Inherits common functionality from BaseHandler.
  """
  def get(self):
    """Handles the GET requests for the email registration page.

    No support for GET requests. Redirect to home page.
    """
    self.redirect(uri_for('home'))

  def post(self):
    """Handles the POST requests for the email registration page.

    When email address validity succeeds, both the registrant and NL will be notified.
    """
    email_input = self.request.get('email')
    params = { 'email': email_input }

    if not settings.RE_EMAIL.match(email_input):
      params['error_email'] = settings.RE_EMAIL_FAIL
      self.render(settings.TEMPLATE_FILENAME['home'], **params)
    else:
      sender_address = (settings.CONFIRMATION_MAIL_SENDER.format(app_identity.get_application_id()))
      subject = settings.CONFIRMATION_MAIL_SUBJECT
      message = mail.EmailMessage(sender=sender_address, subject=subject)
      message.to = email_input
      message.body = settings.CONFIRMATION_MAIL_BODY
      message.html = settings.CONFIRMATION_MAIL_BODY_HTML

      message.send()
      params['success_email'] = settings.RE_EMAIL_SUCCESS
      self.render(settings.TEMPLATE_FILENAME['home'], **params)
