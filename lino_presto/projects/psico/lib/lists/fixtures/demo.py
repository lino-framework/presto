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
"""The `demo` fixture for this plugin."""

from lino.api import rt, dd, _


def objects():
    List = rt.models.lists.List
    for y in (2014, 2015, 2016):
        yield List(**dd.str2kw('name', _("Women's group {0}").format(y)))
        yield List(**dd.str2kw('name', _("Men's group {0}").format(y)))
        yield List(**dd.str2kw('name', _("Children's group {0}").format(y)))

