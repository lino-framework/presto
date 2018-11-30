# Copyright 2013-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Extends :mod:`lino_xl.lib.courses` for :ref:`presto`.

.. autosummary::
   :toctree:

    fixtures.demo

"""


from lino_xl.lib.courses import Plugin
from lino.api import _


class Plugin(Plugin):

    verbose_name = _("Contracts")

    teacher_model = 'users.User'
    teacher_label = _("Worker")
    
    # pupil_model = 'tera.Client'
    pupil_model = 'contacts.Person'
    # pupil_name_fields = "pupil__client__name"
    extends_models = ['Enrolment', 'Course', 'Line']
    
    # remove dependencies so that courses can come as the first item
    # in main menu:
    needs_plugins = []

