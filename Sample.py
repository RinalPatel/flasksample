#!/usr/bin/env python
# coding: utf-8

# In[5]:


import flask


# In[6]:



import werkzeug
import time
import numpy as np
import urllib
import urllib.request
import cv2
import scipy.ndimage
from flask import Flask,redirect,url_for,render_template
from flask import send_file
from flask import request
import requests
import base64
import os
import webbrowser
from pathlib import Path
from flask import send_from_directory


# In[2]:


app = flask.Flask(__name__)


# In[3]:


#to display the connection status
@app.route('/', methods=['GET', 'POST'])
def handle_call():
    return "Hello you are Successfully Connected....."


# In[4]:


app.run()


# In[ ]:




