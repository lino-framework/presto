# -*- coding: UTF-8 -*-
# Copyright 2012-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""See :ref:`presto`.

.. autosummary::
   :toctree:

   lib
   projects


"""

from os.path import join, dirname

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO['version']
intersphinx_urls = dict(
    docs="https://presto.lino-framework.org",
    dedocs="https://de.presto.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/presto/blob/master/%s'
doc_trees = ['docs', 'dedocs']
