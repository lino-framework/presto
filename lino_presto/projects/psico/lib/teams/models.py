# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
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
"""Database models for this plugin."""

from __future__ import unicode_literals

from lino.api import _

from lino_xl.lib.teams.models import *


class Team(Team):
    
    class Meta(Team.Meta):
        app_label = 'teams'
        abstract = dd.is_abstract_model(__name__, 'Team')
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


dd.inject_field(
    'contacts.Partner', 'team',
    dd.ForeignKey('teams.Team', blank=True, null=True))

# dd.inject_field(
#     'clocking.Session', 'team',
#     dd.ForeignKey('teams.Team', blank=True, null=True))

dd.inject_field(
    'ledger.Journal', 'team',
    dd.ForeignKey('teams.Team', blank=True, null=True))


