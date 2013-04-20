#!/usr/bin/env python
#-*- coding: utf8 -*-

from core import app

app.run(host=app.config['APPLICATION_HOST'], 
        port=app.config['APPLICATION_PORT'], 
        debug=app.config['DEBUG'])