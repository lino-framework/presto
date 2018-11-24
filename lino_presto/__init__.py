# -*- coding: UTF-8 -*-
# Copyright 2012-2015 Rumma & Ko Ltd
# This file is part of Lino Presto.
#
# Lino Presto is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Presto is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Presto.  If not, see
# <http://www.gnu.org/licenses/>.

"""See :ref:`presto`.

.. autosummary::
   :toctree:

   lib
   projects


"""

from os.path import join, dirname

SETUP_INFO = dict()
# execfile(join(dirname(__file__), 'setup_info.py'))
with open(join(dirname(__file__), 'setup_info.py')) as setup_info:
    exec(setup_info.read())
__version__ = SETUP_INFO['version']
intersphinx_urls = dict(docs="http://presto.lino-framework.org")
srcref_url = 'https://github.com/lsaffre/presto/blob/master/%s'
doc_trees = ['docs']


