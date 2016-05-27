# -*- coding: UTF-8 -*-
# Copyright 2013-2016 Luc Saffre
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

"""Database models for :mod:`lino_welfare.modlib.users`.

"""

from __future__ import unicode_literals

from lino.modlib.users.models import *


class UserDetail(UserDetail):
    """Layout of User Detail in Lino Presto."""

    main = """
    box1
    remarks:40 AuthoritiesGiven:20
    """

    box1 = """
    username profile:20 partner
    first_name last_name initials
    email language timezone team
    id created modified
    """

Users.detail_layout = UserDetail()

