# -*- coding: UTF-8 -*-
# Copyright 2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino Presto"
    version = "0.1"
    url = "http://presto.lino-framework.org"

    # demo_fixtures = 'std demo minimal_ledger euvatrates demo_bookings payments demo2'.split()
    demo_fixtures = 'std demo minimal_ledger demo_bookings payments demo2'.split()

    languages = 'en de fr et'

    project_model = 'courses.Course'
    workflows_module = 'lino_presto.lib.presto.workflows'
    user_types_module = 'lino_presto.lib.presto.user_types'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.users'
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.properties'
        yield 'lino_presto.lib.contacts'
        yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.lists'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.humanlinks',
        yield 'lino_xl.lib.cal'
        yield 'lino_xl.lib.courses'
        # yield 'lino_xl.lib.products'
        # yield 'lino_noi.lib.products'
        yield 'lino_xl.lib.sales'
        # yield 'lino_xl.lib.vat'
        yield 'lino_xl.lib.sepa'
        yield 'lino_xl.lib.finan'
        yield 'lino_xl.lib.invoicing'
        # 'lino_xl.lib.projects',
        # yield 'lino_xl.lib.blogs'
        yield 'lino_xl.lib.notes'
        # yield 'lino_xl.lib.stars'
        # yield 'lino_xl.lib.meetings'
        # yield 'lino_presto.lib.tickets'
        # yield 'lino_xl.lib.skills'
        # yield 'lino_xl.lib.votes'
        # yield 'lino_presto.lib.working'
        # yield 'lino_xl.lib.working'
        # yield 'lino_xl.lib.deploy'
        yield 'lino.modlib.uploads'
        # yield 'lino_xl.lib.extensible'
        # yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_xl.lib.appypod'
        # yield 'lino_xl.lib.postings'
        # yield 'lino_xl.lib.pages'

        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.checkdata'
        yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.weasyprint'

        yield 'lino_presto.lib.presto'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(country_code='BE')
        # self.plugins.comments.configure(
        #     commentable_model='tickets.Ticket')

