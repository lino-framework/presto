# -*- coding: UTF-8 -*-
# Copyright 2013-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


from django.db.models import Q
from django.conf import settings

from lino.api import dd, rt, _
from lino.utils.quantities import ZERO_DURATION
from lino.utils import SumCollector

from lino_xl.lib.contacts.models import *
# from lino_xl.lib.courses.mixins import Enrollable
from lino_xl.lib.beid.mixins import SSIN
# from lino_xl.lib.calview.ui import WeeklyView
# from lino_xl.lib.calview.ui import WeeklyPlanner
from lino_xl.lib.calview.mixins import Plannable
from lino.modlib.printing.actions import DirectPrintAction
from lino.mixins.periods import Monthly

from lino_xl.lib.calview.models import WeeklyPlannerBase, DailyPlannerBase
from lino_xl.lib.calview.models import Navigators, CalendarView, InsertEvent


class PrintRoster(DirectPrintAction):
    help_text = _("Print a roster of calendar events")
    # combo_group = "creacert"
    label = _("Roster")
    tplname = "roster"
    build_method = "weasy2pdf"
    icon_name = None
    show_in_bbar = False
    parameters = Monthly(
        show_remarks=models.BooleanField(
            _("Show remarks"), default=False),
        overview=models.BooleanField(
            _("Overview"), default=True))
    params_layout = """
    start_date
    end_date
    overview
    show_remarks
    """
    keep_user_values = True




class Partner(Partner, mixins.CreatedModified):

    class Meta(Partner.Meta):
        app_label = 'contacts'
        # verbose_name = _("Partner")
        # verbose_name_plural = _("Partners")
        abstract = dd.is_abstract_model(__name__, 'Partner')

    # isikukood = models.CharField(
    #     _("isikukood"), max_length=20, blank=True)
    #
    hidden_columns = 'created modified'

    faculty = None
    """Required by :mod:`lino_xl.lib.working`.
    """

    # def get_overview_elems(self, ar):
    #     # In the base classes, Partner must come first because
    #     # otherwise Django won't inherit `meta.verbose_name`. OTOH we
    #     # want to get the `get_overview_elems` from AddressOwner, not
    #     # from Partner (i.e. AddressLocation).
    #     elems = super(Partner, self).get_overview_elems(ar)
    #     elems += AddressOwner.get_overview_elems(self, ar)
    #     return elems


class PartnerDetail(PartnerDetail):

    main = "general contact #tickets invoicing misc "

    general = dd.Panel("""
    overview:20 general2:20 general3:40
    # notes.NotesByPartner orders.OrdersByPartner
    """, label=_("General"))

    general2 = """
    id language
    url
    """

    # tickets = "tickets.SponsorshipsByPartner"

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    contact = dd.Panel("""
    address_box
    remarks:30 sepa.AccountsByPartner
    """, label=_("Contact"))

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """

    ledger = dd.Panel("""
    vat.VouchersByPartner
    ledger.MovementsByPartner
    """, label=dd.plugins.ledger.verbose_name)

    invoicing = dd.Panel("""
    invoicing_left:30 #orders.OrdersByProject:50
    sales.InvoicesByPartner
    """, label=_("Invoicing"))

    invoicing_left = """
    pf_income
    salesrule__invoice_recipient
    payment_term salesrule__paper_type
    """

    purchases = dd.Panel("""
    purchase_account vat_regime vat_id
    ana.InvoicesByPartner
    """, label=_("Purchases"))

    misc = dd.Panel("""
    created modified
    """, label=_("Miscellaneous"))


class Person(Partner, Person):
    """
    Represents a physical person.
    """

    class Meta(Person.Meta):
        app_label = 'contacts'
        # verbose_name = _("Person")
        # verbose_name_plural = _("Persons")
        #~ ordering = ['last_name','first_name']
        abstract = dd.is_abstract_model(__name__, 'Person')

    print_roster = PrintRoster()

    @dd.displayfield(_("Print"))
    def print_actions(self, ar):
        if ar is None:
            return ''
        elems = [
            ar.instance_action_button(
                self.print_roster)]
        return E.p(*join_elems(elems, sep=", "))

    @classmethod
    def get_user_queryset(cls, user):
        qs = super(Person, cls).get_user_queryset(user)
        return qs.select_related('country', 'city')

    def get_print_language(self):
        "Used by DirectPrintAction"
        return self.language

    def cal_entries_by_guest(self):
        return rt.models.cal.Event.objects.filter(guest__partner=self)

dd.update_field(Person, 'first_name', blank=False)
# dd.update_field(Person, 'last_name', blank=False)

# class PersonDetail(PersonDetail, PartnerDetail):
class PersonDetail(PartnerDetail):

    main = "general contact humanlinks misc cal_tab"

    general = dd.Panel("""
    overview:20 general2:40 #general3:40
    contacts.RolesByPerson:20
    """, label=_("General"))

    contact = dd.Panel("""
    # lists.MembersByPartner
    remarks:30 sepa.AccountsByPartner
    """, label=_("Contact"))

    humanlinks = dd.Panel("""
    humanlinks.LinksByHuman:30
    households.MembersByPerson:20 households.SiblingsByPerson:50
    """, label=_("Human Links"))

    misc = dd.Panel("""
    url
    created modified
    # notes.NotesByPartner
    """, label=_("Miscellaneous"))

    cal_tab = dd.Panel("""
    print_actions
    #cal.GuestsByPartner cal.EntriesByGuest
    """, label=_("Calendar"))

    general2 = """
    title first_name:15 middle_name:15
    last_name
    gender:10 birth_date age:10
    id language
    """

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """


Persons.insert_layout = """
first_name last_name
phone gsm
gender email
"""

# class Persons(Persons):
#
#     detail_layout = PersonDetail()


class Worker(Person, SSIN, Plannable):
    class Meta:
        app_label = 'contacts'
        verbose_name = _("Worker")
        verbose_name_plural = _("Workers")
        abstract = dd.is_abstract_model(__name__, 'Worker')

    plannable_header_row_label = _("All workers")

    def get_weekly_chunks(self, ar, entries, today):
        sums = SumCollector()
        for e in entries:  # .filter(guest__partner=self).distinct():
            yield e.obj2href(ar, ar.actor.get_calview_div(e, ar))
            sums.collect(e.event_type, e.get_duration())
        for k, v in sums.items():
            yield _("{} : {}").format(k, str(v))
            # need to explicitly call str(v) because otherwise __format__() is
            # used, which would render it like a Decimal

    @classmethod
    def get_plannable_entries(cls, obj, ar):

        # The header row in a workers calendar view shows entries that
        # are for everybody, e.g. holidays.  This is when
        # cal.EventType.locks_user is True.
        # print("20200303 get_plannable_entries", cls, obj, ar)
        Event = rt.models.cal.Event
        if obj is None:
            return Event.objects.none()
        User = rt.models.users.User
        qs = Event.objects.all()
        if obj is cls.HEADER_ROW:
            qs = qs.filter(event_type__locks_user=False)
        else:
            # entries where the worker is either a guest or the author
            # qs = qs.filter(event_type__locks_user=True)
            try:
                u = User.objects.get(partner=obj)
                # print(u)
                qs = qs.filter(Q(user=u) | Q(guest__partner=obj)).distinct()
            except Exception:
                qs = qs.filter(guest__partner=obj).distinct()
        return qs
        # return Event.calendar_param_filter(qs, ar.param_values)




class WorkerDetail(PersonDetail):

    main = "general contact"

    general = dd.Panel("""
    overview:20 cal_panel:40
    orders.EnrolmentsByWorker
    """, label=_("General"))

    cal_panel = """
    national_id  print_actions
    cal.EntriesByGuest
    """


class Workers(Persons):
    model = 'contacts.Worker'
    # detail_layout = WorkerDetail()
    detail_layout = 'contacts.WorkerDetail'


class Company(Partner, Company):
    class Meta(Company.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Company')

    # class Meta:
    #     verbose_name = _("Organisation")
    #     verbose_name_plural = _("Organisations")

    # vat_id = models.CharField(_("VAT id"), max_length=200, blank=True)


class CompanyDetail(PartnerDetail):

    main = "general contact invoicing misc"

    ledger = dd.Panel("""
    vat.VouchersByPartner
    ledger.MovementsByPartner
    """, label=dd.plugins.ledger.verbose_name)

    general = dd.Panel("""
    overview:20 general2:40 general3:40
    contacts.RolesByCompany
    """, label=_("General"))

    general2 = """
    prefix:20 name:40
    type vat_id
    url
    """

    general3 = """
    email:40
    phone
    gsm
    fax
    """

    contact = dd.Panel("""
    # lists.MembersByPartner
    remarks:30 sepa.AccountsByPartner
    """, label=_("Contact"))

    address_box = """
    country region city zip_code:10
    addr1
    street_prefix street:25 street_no street_box
    addr2
    """

    # tickets = "tickets.SponsorshipsByPartner"

    misc = dd.Panel("""
    id language
    created modified
    # notes.NotesByPartner
    """, label=_("Miscellaneous"))


Companies.insert_layout = """
name
phone gsm
#language:20 email:40
type #id
"""

class WorkersParameters(dd.Actor):

    abstract = True

    @classmethod
    def class_init(cls):
        cls.params_layout = rt.models.contacts.Workers.params_layout
        super(WorkersParameters, cls).class_init()

    @classmethod
    def setup_parameters(cls, params):
        super(WorkersParameters, cls).setup_parameters(params)
        rt.models.contacts.Worker.setup_parameters(params)

    @classmethod
    def get_calview_chunks(cls, obj, ar):
        pv = ar.param_values
        # if pv.user:
        # if pv.assigned_to:
        # if settings.SITE.project_model is not None and pv.project:
        # if pv.event_type:
        if obj.start_time:
            yield str(obj.start_time)[:5] + " "
        # elif not pv.start_date:
            # t.append(str(self.start_date))
        # if not pv.user and self.user:
        #     t.append(str(self.user))
        if obj.project:
            yield str(obj.project) + " "
            if obj.project.city:
                yield obj.project.city.name + " "
        # if not pv.event_type and self.event_type:
        #     t.append(str(self.event_type))
        if obj.room and obj.room.ref:
            yield obj.room.ref + " "
        if obj.summary:
            yield obj.summary + " "

    def get_header_chunks(obj, ar, entries, today):

        # unlike the library version, this does not have an insert button and
        # does not show only whole-day events.

        # entries = entries.filter(start_time__isnull=True)
        txt = str(today.day)
        if today == dd.today():
            txt = E.b(txt)

        yield E.p(txt, align="center")
        for e in entries:
            yield e.obj2href(ar, ar.actor.get_calview_div(e, ar))


class WeeklyPlanner(WorkersParameters, WeeklyPlannerBase, Workers):
    column_names_template = "name_column:20 {vcolumns}"
    hide_top_toolbar = False


class DailyPlanner(WorkersParameters, DailyPlannerBase, Workers):
    column_names_template = "name_column:20 {vcolumns}"
    # display_mode = "html"
    navigation_mode = 'day'


class WeeklyView(WorkersParameters, CalendarView):
    label = _("Weekly view")
    detail_layout = 'contacts.WeekDetail'
    navigation_mode = "week"
    # params_layout = ""

class DailyView(WorkersParameters, CalendarView):
    label = _("Daily view")
    detail_layout = 'contacts.DayDetail'
    navigation_mode = "day"
    insert_event = InsertEvent()


class WeekDetail(dd.DetailLayout):
    main = "body"
    body = "navigation_panel:15 contacts.WeeklyPlanner:85"

class DayDetail(dd.DetailLayout):
    main = "body"
    body = "navigation_panel:15 contacts.DailyPlanner:85"



add = Navigators.add_item
add("contacts", _("Workers calendar"), "contacts.DailyView", "contacts.WeeklyView", "")
