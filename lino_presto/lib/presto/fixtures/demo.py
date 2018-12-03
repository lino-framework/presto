# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
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
from lino.utils.mldbc import babel_named as named, babeld
from lino.modlib.users.utils import create_user
from lino_xl.lib.cal.choicelists import EntryStates, GuestStates
from lino_presto.lib.courses.choicelists import InvoicingPolicies

# from django.conf import settings

# courses = dd.resolve_app('courses')
# cal = dd.resolve_app('cal')
# users = dd.resolve_app('users')

AMOUNTS = Cycler("5.00", None, None, "15.00", "20.00", None, None)

from lino_xl.lib.products.choicelists import DeliveryUnits


def objects():
    Partner = rt.models.contacts.Partner
    Worker = rt.models.contacts.Worker
    # Pupil = dd.plugins.courses.pupil_model
    Teacher = dd.plugins.courses.teacher_model
    Line = rt.models.courses.Line
    EventType = rt.models.cal.EventType
    GuestRole = rt.models.cal.GuestRole
    Course = rt.models.courses.Course
    Enrolment = rt.models.courses.Enrolment
    DurationUnits = rt.models.cal.DurationUnits
    SalesRule = rt.models.invoicing.SalesRule
    UserTypes = rt.models.users.UserTypes
    Company = rt.models.contacts.Company
    Product = rt.models.products.Product
    Tariff = rt.models.invoicing.Tariff
    ProductTypes = rt.models.products.ProductTypes
    ProductCat = rt.models.products.ProductCat
    Account = rt.models.ledger.Account
    CommonItems = rt.models.sheets.CommonItems
    CourseAreas = rt.models.courses.CourseAreas
    PriceRule = rt.models.courses.PriceRule

    # yield skills_objects()

    presence = ProductCat(**dd.str2kw('name', _("Fees")))
    yield presence

    yield Product(**dd.str2kw('name', _("Ironing of a shirt"), delivery_unit=DeliveryUnits.piece))
    yield Product(**dd.str2kw('name', _("Ironing of a pair of trousers"), delivery_unit=DeliveryUnits.piece))
    yield Product(**dd.str2kw('name', _("Ironing of a skirt"), delivery_unit=DeliveryUnits.piece))
    yield Product(**dd.str2kw('name', _("Washing per Kg"), delivery_unit=DeliveryUnits.kg))


    obj = Company(
        name="Home Helpers",
        country_id="BE", vat_id="BE12 3456 7890")
    yield obj
    settings.SITE.site_config.update(site_company=obj)

    ahmed= Worker(first_name="Ahmed")
    yield ahmed
    maria= Worker(first_name="Maria")
    yield maria

    indacc = named(
        Account, _("Sales on services"),
        sheet_item=CommonItems.sales.get_object(), ref="7010")
    yield indacc

    t1 = babeld(Tariff, _("By presence"), number_of_events=1)
    yield t1

    t10 = babeld(Tariff, _("Maximum 10"), number_of_events=1, max_asset=10)
    yield t10

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

    worker = GuestRole(**dd.str2kw('name', _("Worker")))
    yield worker

    garden_et = EventType(
        force_guest_states=True,
        **dd.str2kw('name', _("Garden works")))
    yield garden_et

    home_et = EventType(
        force_guest_states=True,
        **dd.str2kw('name', _("Home help")))
    yield home_et

    yield create_user("ahmed", UserTypes.worker,
                      event_type=garden_et, partner=ahmed)
    yield create_user("maria", UserTypes.worker, event_type=home_et, partner=maria)
    yield create_user("margarete", UserTypes.secretary)

    yield PriceRule(seqno=1, event_type=garden_et, fee=garden_prod)
    yield PriceRule(seqno=2, event_type=home_et, fee=home_prod)

    for a in CourseAreas.get_list_items():
        kw = dict(
            name=a.text, course_area=a, guest_role=worker)
        # kw.update(fees_cat=presence)
        # kw.update(guest_role=attendee)
        # if a.name in('therapies', 'life_groups'):
        #     kw.update(fee=ind_therapy, event_type=ind_et)
        # else:
        #     kw.update(fee=group_therapy, event_type=group_et)
        a.line_obj = Line(**kw)
        yield a.line_obj  # temporary cache used below
        
    invoice_recipient = None
    for n, p in enumerate(Partner.objects.all()):
        if n % 10 == 0:
            yield SalesRule(
                partner=p, invoice_recipient=invoice_recipient)
            # p.salesrule.invoice_recipient = invoice_recipient
            # yield p
        else:
            invoice_recipient = p

    # LINES = Cycler(Line.objects.all())
    USERS = Cycler(rt.models.users.User.objects.all())
    PLACES = Cycler(rt.models.cal.Room.objects.all())
    TEACHERS = Cycler(Teacher.objects.all())
    SLOTS = Cycler(rt.models.courses.Slot.objects.all())
    TARIFFS = Cycler(rt.models.invoicing.Tariff.objects.all())

    date = settings.SITE.demo_date(-200)
    qs = Worker.objects.all()
    if qs.count() == 0:
        raise Exception("Oops, no Partner!")
    PUPILS = Cycler(qs)
    kw = dict(state='active', line=CourseAreas.garden.line_obj)
    for i, obj in enumerate(qs):
        if i % 6:
            kw.update(
                user=USERS.pop(),
                # client=obj,
                partner=obj,
                teacher=TEACHERS.pop(),
                # line=LINES.pop(),
                room=PLACES.pop(),
                start_date=date,
                every=2,
                max_events=10,
                every_unit=DurationUnits.weeks,
                slot=SLOTS.pop())
            kw.update(tariff=TARIFFS.pop())
            c = Course(**kw)
            yield c
            yield Enrolment(pupil=obj, course=c, state='confirmed')
            c.save()  # fill presences
            ar = rt.login(c.user.username)
            c.update_reminders(ar)
            date += ONE_DAY
            
    qs = rt.models.cal.Event.objects.filter(
        start_date__lt=dd.today(-10))
    for e in qs:
        if e.id % 5:
            e.state = EntryStates.took_place
        else:
            e.state = EntryStates.missed
        yield e

