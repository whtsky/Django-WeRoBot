# -*- coding: utf-8 -*-
"""
Django-WeRoBot
---------------

Adds WeRoBot support to Django.

:copyright: (c) 2013 by whtsky.
:license: BSD, see LICENSE for more details.

Links
`````

* `documentation <https://django-werobot.readthedocs.org/>`_
"""

__version__ = '0.1.2'
__all__ = ['make_view']

from werobot.robot import BaseRoBot
from werobot.parser import parse_user_msg
from werobot.reply import create_reply
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


def make_view(robot):
    """
    为一个 BaseRoBot 生成 Django view。

    :param robot: 一个 BaseRoBot 实例。
    :return: 一个标准的 Django view
    """
    assert isinstance(robot, BaseRoBot),\
        "RoBot should be an BaseRoBot instance."

    @csrf_exempt
    def werobot_view(request):
        timestamp = request.GET.get("timestamp", "")
        nonce = request.GET.get("nonce", "")
        signature = request.GET.get("signature", "")
        if not robot.check_signature(
            timestamp=timestamp,
            nonce=nonce,
            signature=signature
        ):
            return HttpResponseForbidden()
        if request.method == "GET":
            return HttpResponse(request.GET.get("echostr", ""))
        elif request.method == "POST":
            body = request.body
            message = parse_user_msg(body)
            reply = robot.get_reply(message)
            return HttpResponse(
                create_reply(reply, message=message),
                content_type="application/xml;charset=utf-8"
            )
        return HttpResponseNotAllowed(['GET', 'POST'])

    return werobot_view
