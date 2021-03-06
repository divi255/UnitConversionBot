# -*- coding: utf-8 -*-
import os
import webapp2
from controller.WebHook import WebHook
from controller.UpdateRates import UpdateRates

debug = os.path.exists('./tests')
os.environ['DEBUG'] = '1' if debug else ''

app = webapp2.WSGIApplication([
    ('/api/webhook', WebHook),
    ('/api/rates/update', UpdateRates)
], debug=debug)
