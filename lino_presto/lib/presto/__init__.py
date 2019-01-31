# -*- coding: UTF-8 -*-
# Copyright 2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The main plugin for Lino Presto.

See :doc:`/specs/presto/presto`.

.. autosummary::
   :toctree:

    migrate
    user_types
    layouts
    choicelists

"""


from lino.api import ad, _


class Plugin(ad.Plugin):
    "See :class:`lino.core.plugin.Plugin`."

    verbose_name = _("Master")

    needs_plugins = ['lino_xl.lib.countries']

    municipality_type = '50'

    def setup_main_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        # m.add_separator()
        m.add_action('presto.Clients')
        # m.add_action('presto.MyClients')
        # m.add_action('presto.Translators')
        # m.add_action('courses.CourseProviders')
        # m.add_action('coachings.CoachedClients')
        # m.add_action('coachings.MyCoachings')

    def setup_config_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        # mg = self.get_menu_group()
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('presto.Categories')
        m.add_action('presto.EndingReasons')

    def setup_explorer_menu(self, site, user_type, m):
        mg = site.plugins.contacts
        # mg = self.get_menu_group()
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('presto.AllClients')



