#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'Andrew Hutchings'
SITENAME = "libAttachSQL"
SITESUBTITLE = "A lightweight C API for MySQL servers"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('libAttachSQL on GitHub', 'http://github.com/libattachsql/libattachsql'),
        ('IRC Channel', 'irc://chat.freenode.net/libAttachSQL'),
         ('Documentation', 'http://docs.libattachsql.org/'),)

# Social widget
#SOCIAL = (('GitHub', 'http://github.com/LinuxJedi'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='notmyidea-lxj'
DEFAULT_DATE_FORMAT = '%a %d %b %Y, %H:%M'

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
# Cleaner Articles
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

DISPLAY_CATEGORIES_ON_MENU=True
