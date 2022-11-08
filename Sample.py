#!/usr/bin/env python
# coding: utf-8

# In[5]:


import flask




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




