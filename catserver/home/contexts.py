#-*- coding:utf-8 -*-

"""
Context processor
"""

def g_context(request):
    """ 
    This context can be used only for server
    """
    __context = {
                 "G_TITLE":"Cat Robot Monitoring System",
                 "G_TITLE_LOGO":"CAT Robot",
                 "G_TITLE_MINI":"CAT",
                 "G_VERSION":"0.1",
                 "G_RELEASE_DATE":"",
                 "G_DESCRIPTION":"",
                 "G_AUTHOR":"Byunghun Hwang",
                 "G_COMPANY":"Nsynapse Inc.",
                 "G_URL":"http://www.nsynapse.com",
                 "G_AUTHOR_EMAIL":"bhhwang@nsynapse.com",
                 }
    return __context