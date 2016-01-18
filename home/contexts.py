#-*- coding:utf-8 -*-

"""
Context processor
"""

def g_context(request):
    """ 
    This context can be used only for server
    """
    __context = {
                 "G_TITLE":"",
                 "G_VERSION":"",
                 "G_DESCRIPTION":"",
                 "G_AUTHOR":"Byunghun Hwang <bhhwang@nsynapsecom>",
                 "G_URL":"http://www.nsynapse.com",
                 "G_AUTHOR_EMAIL":"bhhwang@nsynapse.com",
                 }
    return __context