# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
#
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

"""
The settings package.

.. autosummary::
   :toctree:

   demo
   doctests
   memory



"""

from __future__ import print_function
from __future__ import unicode_literals

from lino_presto.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino for psychologists"

    demo_fixtures = 'std demo novat minimal_ledger demo_bookings payments demo2'.split()
    project_model = 'contacts.Partner'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino_presto.projects.psico.lib.teams'

    def get_apps_modifiers(self, **kw):
        kw = super(Site, self).get_apps_modifiers(**kw)
        # remove whole plugin:
        # kw.update(tickets=None)
        # alternative implementations:
        # kw.update(tickets='lino_noi.projects.care.lib.tickets')
        kw.update(clocking='lino_presto.projects.psico.lib.clocking')
        kw.update(contacts='lino_presto.projects.psico.lib.contacts')
        kw.update(lists='lino_presto.projects.psico.lib.lists')
        kw.update(users='lino_presto.projects.psico.lib.users')
        return kw

    def setup_plugins(self):
        """Change the default value of certain plugin settings.

        """
        super(Site, self).setup_plugins()
        self.plugins.clocking.configure(ticket_model='contacts.Partner')

# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
