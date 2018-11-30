# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import dd, rt, _

from lino_xl.lib.courses.choicelists import *

CourseAreas.clear()
add = CourseAreas.add_item
add('10', _("Home help"), 'default')
add('20', _("Garden contracts"), 'garden')


# Stand der Beratung:
# 01 dauert an                                
# 03 abgeschlossen                            
# 05 automatisch abgeschlossen                
# 06 Abbruch der Beratung                     
# 09 Weitervermittlung                        
# 12 nur Erstkontakt
CourseStates.clear()
add = CourseStates.add_item
add('01', _("Active"), 'active',
    is_editable=True, is_invoiceable=True, is_exposed=True,
    auto_update_calendar=False)
add('03', _("Closed"), 'closed',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('05', _("Inactive"), 'inactive',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('06', _("Cancelled"), 'cancelled',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('09', _("Forwarded"), 'forwarded',
    is_editable=False, is_invoiceable=False, is_exposed=False,
    auto_update_calendar=False)
add('12', _("Draft"), 'draft',
    is_editable=True, is_invoiceable=False, is_exposed=True,
    auto_update_calendar=False)

# EnrolmentStates.default_value = 'confirmed'
EnrolmentStates.clear()
add = EnrolmentStates.add_item
add('01', _("Confirmed"), 'confirmed', invoiceable=True, uses_a_place=True)
add('03', _("Closed"), 'closed', invoiceable=False, uses_a_place=False)
add('05', _("Inactive"), 'inactive', invoiceable=False, uses_a_place=False)
add('06', _("Cancelled"), 'cancelled', invoiceable=False, uses_a_place=False)
add('09', _("Forwarded"), 'forwarded', invoiceable=False, uses_a_place=False)
add('12', _("First contact"), 'requested', invoiceable=False, uses_a_place=False)
add('00', _("Trying"), 'trying', invoiceable=False, uses_a_place=False)
add('02', _("Active"), 'active', invoiceable=True, uses_a_place=True)
# add('04', _("04"), invoiceable=False, uses_a_place=False)
# add('08', _("08"), invoiceable=False, uses_a_place=False)
# add('11', _("11"), invoiceable=False, uses_a_place=False)
# add('99', _("99"), invoiceable=False, uses_a_place=False)


class InvoicingPolicies(dd.ChoiceList):
    verbose_name = _("Invoicing policy")
    verbose_name_plural = _("Invoicing policies")

add = InvoicingPolicies.add_item
add('00', _("By calendar event"), 'by_event')
add('10', _("By presence"), 'by_guest')


class Residences(dd.ChoiceList):
    verbose_name = _("Residence")
    verbose_name_plural = _("Residences")

class HouseholdCompositions(dd.ChoiceList):
    verbose_name = _("Household composition")
    verbose_name_plural = _("Household compositions")

class IncomeCategories(dd.ChoiceList):
    verbose_name = _("Income category")
    verbose_name_plural = _("Income categories")

class PriceFactor(dd.Choice):
    field_cls = None
    def __init__(self, value, cls, name):
        self.field_cls = cls
        super(PriceFactor, self).__init__(value, cls.verbose_name, name)

class PriceFactors(dd.ChoiceList):
    item_class = PriceFactor
    verbose_name = _("Price factor")
    verbose_name_plural = _("Price factors")



add = PriceFactors.add_item
add("10", Residences, "residence")
add("20", HouseholdCompositions, "composition")
add("30", IncomeCategories, "income")


add = Residences.add_item
add("10", _("Inside"), "inside")
add("20", _("Outside"), "ouside")

add = HouseholdCompositions.add_item
add("10", _("Alone"))
add("20", _("2 members"))
add("30", _("3 members"))

add = IncomeCategories.add_item
add("10", _("Below 900"))
add("20", _("900-1100"))
add("30", _("1100-1300"))
add("40", _("1300-1800"))
add("90", _("Above 1800"))
