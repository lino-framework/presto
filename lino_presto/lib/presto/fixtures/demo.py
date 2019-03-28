# -*- coding: UTF-8 -*-
# Copyright 2018-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Demo data for Lino Presto.

- Create a client MTI child for most persons.

"""
from __future__ import unicode_literals

import datetime
from django.conf import settings

from lino.utils import ONE_DAY
from lino.utils.mti import mtichild
from lino.utils.ssin import generate_ssin
from lino.api import dd, rt, _
from lino.utils import Cycler
from lino.utils import mti
from lino.utils.mldbc import babel_named as named, babeld
from lino.modlib.users.utils import create_user
from lino_xl.lib.cal.choicelists import EntryStates, GuestStates

# from django.conf import settings

# courses = dd.resolve_app('courses')
# cal = dd.resolve_app('cal')
# users = dd.resolve_app('users')

AMOUNTS = Cycler("5.00", None, None, "15.00", "20.00", None, None)

from lino_xl.lib.products.choicelists import DeliveryUnits


def objects():
    Partner = rt.models.contacts.Partner
    Person = rt.models.contacts.Person
    Worker = rt.models.contacts.Worker
    LifeMode = rt.models.presto.LifeMode
    EventType = rt.models.cal.EventType
    Room = rt.models.cal.Room
    GuestRole = rt.models.cal.GuestRole
    Enrolment = rt.models.orders.Enrolment
    DurationUnits = rt.models.cal.DurationUnits
    SalesRule = rt.models.invoicing.SalesRule
    UserTypes = rt.models.users.UserTypes
    Company = rt.models.contacts.Company
    Client = rt.models.presto.Client
    ClientStates = rt.models.presto.ClientStates
    Product = rt.models.products.Product
    Tariff = rt.models.invoicing.Tariff
    ProductTypes = rt.models.products.ProductTypes
    ProductCat = rt.models.products.ProductCat
    Account = rt.models.ledger.Account
    Journal = rt.models.ledger.Journal
    PriceRule = rt.models.products.PriceRule
    User = rt.models.users.User

    # yield skills_objects()

    yield babeld(LifeMode, _("Single"))
    yield babeld(LifeMode, _("Living together"))
    yield babeld(LifeMode, _("Married couple"))
    yield babeld(LifeMode, _("Family with children"))
    yield babeld(LifeMode, _("Three-generation household"))
    yield babeld(LifeMode, _("Single with children"))

    t1 = babeld(Tariff, _("By presence"), number_of_events=1)
    yield t1

    t10 = babeld(Tariff, _("Maximum 10"), number_of_events=1, max_asset=10)
    yield t10

    obj = Company(
        name="Home Helpers",
        country_id="BE", vat_id="BE12 3456 7890")
    yield obj
    settings.SITE.site_config.update(site_company=obj)

    ahmed= Worker(first_name="Ahmed", gender=dd.Genders.male)
    yield ahmed
    maria= Worker(first_name="Maria", gender=dd.Genders.female)
    yield maria

    indacc = named(
        Account, _("Sales on services"),
        # sheet_item=CommonItems.sales.get_object(),
        ref="7010")
    yield indacc

    presence = ProductCat(**dd.str2kw('name', _("Fees")))
    yield presence

    garden_et = EventType(
        force_guest_states=True,
        **dd.str2kw('name', _("Garden works")))
    yield garden_et

    home_et = EventType(
        force_guest_states=True,
        **dd.str2kw('name', _("Home help")))
    yield home_et

    yield Room(**dd.str2kw('name', _("Garden works"), event_type=garden_et))
    yield Room(**dd.str2kw('name', _("House works"), event_type=home_et))
    yield Room(**dd.str2kw('name', _("Office")))

    def product(pt, name, unit, **kwargs):
        return Product(**dd.str2kw('name', name,
                       delivery_unit=DeliveryUnits.get_by_name(unit),
                       product_type=ProductTypes.get_by_name(pt), **kwargs))

    yield product('default', _("Ironing of a shirt"), 'piece')
    yield product('default', _("Ironing of a pair of trousers"), 'piece')
    yield product('default', _("Ironing of a skirt"), 'piece')
    yield product('default', _("Washing per Kg"), 'kg')

    # yield Product(**dd.str2kw('name', _("Ironing of a shirt"), delivery_unit=DeliveryUnits.piece))
    # yield Product(**dd.str2kw('name', _("Ironing of a pair of trousers"), delivery_unit=DeliveryUnits.piece))
    # yield Product(**dd.str2kw('name', _("Ironing of a skirt"), delivery_unit=DeliveryUnits.piece))
    # yield Product(**dd.str2kw('name', _("Washing per Kg"), delivery_unit=DeliveryUnits.kg))


    garden_prod = named(
        Product, _("Garden works"), sales_account=indacc,
        # tariff=t1,
        sales_price=30, cat=presence,
        product_type=ProductTypes.default)
    yield garden_prod
    # group_therapy.tariff.number_of_events = 1
    # yield group_therapy.tariff
    
    home_prod = named(
        Product, _("Home help"),
        # tariff=t1,
        sales_price=60, sales_account=indacc, cat=presence,
        product_type=ProductTypes.default)
    yield home_prod
    # ind_therapy.tariff.number_of_events = 1
    # yield ind_therapy.tariff
   
    yield named(Product, _("Other"), sales_price=35)

    # worker = GuestRole(**dd.str2kw('name', _("Worker")))
    # yield worker
    #
    # student = GuestRole(**dd.str2kw('name', _("Student")))
    # yield student

    # yield create_user("ahmed", UserTypes.worker,
    #                   event_type=garden_et, partner=ahmed)
    # yield create_user("maria", UserTypes.worker, event_type=home_et, partner=maria)
    yield create_user("margarete", UserTypes.secretary)

    yield PriceRule(seqno=1, event_type=garden_et, fee=garden_prod)
    yield PriceRule(seqno=2, event_type=home_et, fee=home_prod)

    invoice_recipient = None
    for n, p in enumerate(Partner.objects.all()):
        if n % 10 == 0:
            yield SalesRule(
                partner=p, invoice_recipient=invoice_recipient)
            # p.salesrule.invoice_recipient = invoice_recipient
            # yield p
        else:
            invoice_recipient = p

    qs = rt.models.cal.Event.objects.filter(
        start_date__lt=dd.today(-10))
    for e in qs:
        if e.id % 5:
            e.state = EntryStates.took_place
        else:
            e.state = EntryStates.missed
        yield e


    def person2client(p, **kw):
        c = mti.insert_child(p, Client)
        for k, v in kw.items():
            setattr(c, k, v)
        c.client_state = ClientStates.active
        c.save()
        return Client.objects.get(pk=p.pk)

    count = 0
    for person in Person.objects.exclude(gender=''):
        if not person.birth_date:  # not those from humanlinks
            if User.objects.filter(partner=person).count() == 0:
                if rt.models.contacts.Role.objects.filter(person=person).count() == 0:
                    birth_date = settings.SITE.demo_date(-170 * count - 16 * 365)
                    national_id = generate_ssin(birth_date, person.gender)

                    client = person2client(person,
                                           national_id=national_id,
                                           birth_date=birth_date)
                    # youngest client is 16; 170 days between each client

                    count += 1
                    if count % 2:
                        client.client_state = ClientStates.active
                    elif count % 5:
                        client.client_state = ClientStates.newcomer
                    else:
                        client.client_state = ClientStates.former

                    # Dorothée is three times in our database
                    if client.first_name == "Dorothée":
                        client.national_id = None
                        client.birth_date = ''

                    client.full_clean()
                    client.save()

    # CLIENTS = Cycler(
    #     Client.objects.filter(client_state=ClientStates.coached))


    JournalGroups = rt.models.ledger.JournalGroups
    Company = rt.models.contacts.Company
    from lino_xl.lib.ledger.utils import DEBIT, CREDIT

    # JOURNALS

    # rt.models.ledger.Journal.objects.get(ref="SLS").delete()
    # rt.models.ledger.Journal.objects.get(ref="SLC").delete()

    kw = dict(journal_group=JournalGroups.sales)
    MODEL = rt.models.sales.InvoicesByJournal
    # MODEL = rt.models.vat.InvoicesByJournal
    kw.update(ref="MAN", dc=CREDIT, trade_type="sales")
    # kw.update(printed_name=_("Mission"))
    kw.update(dd.str2kw('name', _("Manual invoices")))
    yield MODEL.create_journal(**kw)

    # kw.update(ref="GH")
    # kw.update(dd.str2kw('name', _("Garden and hedges")))
    # yield MODEL.create_journal(**kw)
    #
    # kw.update(ref="R")
    # kw.update(dd.str2kw('name', _("Renovation works")))
    # yield MODEL.create_journal(**kw)

    # ORDERS

    kw = dict(journal_group=JournalGroups.orders)
    MODEL = rt.models.orders.OrdersByJournal

    kw.update(ref="ORD", dc=CREDIT, trade_type="sales")
    kw.update(printed_name=_("Orders"))
    kw.update(dd.str2kw('name', _("Orders")))
    yield MODEL.create_journal(**kw)


