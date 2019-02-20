# -*- coding: UTF-8 -*-
# Copyright 2013-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from __future__ import unicode_literals

from builtins import str
import six

from django.utils.translation import ugettext_lazy as _

from lino_xl.lib.cal.models import *

from lino.modlib.users.choicelists import UserTypes

from lino_xl.lib.courses.choicelists import EnrolmentStates
from lino_xl.lib.invoicing.mixins import InvoiceGenerator

# courses = dd.resolve_app('courses')

# must import this to activate these workflow definitions:
# 20160622 this is now done by workflows_module
# from . import workflows
# from lino_xl.lib.cal.workflows import voga


from lino.modlib.office.roles import OfficeUser


class Room(Room):

    class Meta(Room.Meta):
        abstract = dd.is_abstract_model(__name__, 'Room')
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    event_type = dd.ForeignKey('cal.EventType',blank=True, null=True)


class RoomDetail(dd.DetailLayout):
    main = """
    id name event_type
    company contact_person contact_role
    cal.EntriesByRoom
    """


class Rooms(Rooms):
    column_names = "name event_type *"


# @dd.python_2_unicode_compatible
class Event(Event, InvoiceGenerator):

    class Meta(Event.Meta):
        abstract = dd.is_abstract_model(__name__, 'Event')
        
    # invoiceable_date_field = 'start_date'
    invoiceable_partner_field = 'project'

    def get_invoiceable_product(self, max_date=None):
        if self.project_id is None:
            return None
        return rt.models.products.Product.get_rule_fee(self.project, self.event_type)

    def get_invoiceable_qty(self):
        return self.get_duration()

    def get_event_summary(self, ar):
        # Overrides lino_xl.lib.cal.Event.get_event_summary
        if self.owner is None:
            return self.summary
        else:
            return str(self.owner)

    # def __str__(self):
    #     if self.owner is None:
    #         if six.PY2:
    #             return super(Event, self).__unicode__()
    #         else:
    #             return super(Event, self).__str__()
    #         # a simple super() fails because of
    #         # python_2_unicode_compatible
    #     owner = self.owner._meta.verbose_name + " #" + str(self.owner.pk)
    #     return "%s %s" % (owner, self.summary)

    def suggest_guests(self):
        # print "20130722 suggest_guests"
        for g in super(Event, self).suggest_guests():
            yield g
        order = self.owner
        if not isinstance(order, rt.models.orders.Order):
            # e.g. None or RecorrentEvent
            return
        Guest = settings.SITE.models.cal.Guest
        for obj in order.enrolments_by_order.all():
            if obj.worker:
                yield Guest(event=self,
                            partner=obj.worker,
                            role=obj.guest_role)

    def get_invoice_items(self, info, invoice, ar):
        # TODO : adapt to presto
        # dd.logger.info("20181116a %s", self)
        if info.used_events is None:
            dd.logger.debug("20181126 no used_events for %s", self)
            return
        Product = rt.models.products.Product
        collector = OrderedDict()
        product = Product.get_rule_fee(self.project, self.event_type)
        if product is None:
            raise Exception("20181128 no price rule for {}".format(self))

        fmt = self.get_invoiceable_event_formatter()

        # tariff = self.get_invoiceable_tariff(product)
        title = _("{product} on {date}").format(
            product=product, date=fmt(self, None))
        kwargs = dict(
            invoiceable=self,
            product=product,
            title=title)
        kwargs.update(qty=self.get_duration())
        yield invoice.add_voucher_item(**kwargs)
        # yield model(**kwargs)

dd.update_field(Event, 'description',format="plain")

class EventDetail(EventDetail):
    main = "general more"
    general = dd.Panel("""
    event_type summary user
    start end
    room priority access_class transparent #rset
    owner:30 workflow_buttons:30
    description
    """, _("General"))

    more = dd.Panel("""
    id created:20 modified:20  state
    #outbox.MailsByController cal.GuestsByEvent notes.NotesByOwner
    """, _("More"))


class MyEntries(MyEntries):
    column_names = 'when_text summary room owner workflow_buttons *'


