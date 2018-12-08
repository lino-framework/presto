# -*- coding: UTF-8 -*-
# Copyright 2014-2016 Rumma & Ko Ltd
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
An extension of :mod:`lino_xl.lib.contacts`
"""

from lino_xl.lib.contacts import Plugin


class Plugin(Plugin):
    extends_models = ['Partner', 'Person', 'Company']

    # Override to add Workers Menu
    def setup_main_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        # We use the string representations and not the classes because
        # other installed applications may want to override these tables.
        for a in ('contacts.Workers', 'contacts.Companies', 'contacts.Persons'):
            m.add_action(a)
