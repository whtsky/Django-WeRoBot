.. module:: django_werobot

Django-WeRoBot
===========================================
Django-WeRoBot 是一个帮助你将 WeRoBot 集成进 Django 的插件。
你可以通过调用 :func:`make_view` 轻松的在你的 Django 应用中集成 `WeRoBot <http://werobot.readthedocs.org/en/latest/>`_ 。

入门
---------
首先，在一个文件中写好你的微信机器人 ::

    # Filename: robot.py

    from werobot import WeRoBot

    robot = WeRoBot(token='token')


    @robot.handler
    def hello(message):
        return 'Hello World!'

然后，在你 Django 项目中的 ``urls.py`` 中调用 :func:`make_view` ，将 WeRoBot 集成进 Django ::

    from django.conf.urls import patterns, include, url
    from django_werobot import make_view
    from robot import robot

    urlpatterns = patterns('',
        url(r'^robot/', make_view(robot)),
    )


大功告成。


API
----------

.. autofunction:: make_view

ChangeLog
-----------

Version v0.1.0
~~~~~~~~~~~~~~~~

+ 框架可用。
