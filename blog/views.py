# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.conf import settings
import logging

logger = logging.getLogger('blog.views')


# Create your views here.
def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC
            }


def index(request):
    try:
        pass
        # open("sss.txt", "r")
    except Exception as e:
        # 调用日志器,保存进日志错误信息
        logger.error(e)

    return render(request, 'index.html', locals())
