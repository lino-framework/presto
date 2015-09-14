# -*- coding: UTF-8 -*-
# Copyright 2012-2015 Luc Saffre
# License: BSD (see file COPYING for details)

"""See :ref:`presto`.

.. autosummary::
   :toctree:

   lib
   projects


"""

from os.path import join, dirname

SETUP_INFO = dict()
execfile(join(dirname(__file__), 'setup_info.py'))
__version__ = SETUP_INFO['version']
intersphinx_urls = dict(docs="http://presto.lino-framework.org")
srcref_url = 'https://github.com/lsaffre/presto/blob/master/%s'


