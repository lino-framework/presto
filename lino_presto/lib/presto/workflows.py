# -*- coding: UTF-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
The default :attr:`workflows_module
<lino.core.site.Site.workflows_module>` for the :ref:`presto` applications.

"""

from lino.api import _

# If we want to change the text and/or button_text of a state, we must
# do this *before* workflow modules are loaded because transition
# actions would otherwise get the unchanged text or button_text.

from lino_xl.lib.cal.choicelists import EntryStates, GuestStates
EntryStates.ignore_required_states = True

add = EntryStates.add_item
add('60', _("Missed"), 'missed', fixed=True,
    help_text=_("Guest missed the appointment."),
    button_text="☉", noauto=True)  # \u2609 SUN

EntryStates.cancelled.button_text = "⚕"
EntryStates.cancelled.text = _("Called off")
EntryStates.draft.text = _("Scheduled")

# print("20181107a", EntryStates.draft.button_text)


from lino_xl.lib.cal.workflows.voga import *
from lino_xl.lib.courses.workflows import *

# EntryStates.override_transition(
#     "cancel",
#     required_states='missed suggested draft took_place')
EntryStates.missed.add_transition(
    required_states='cancelled suggested draft took_place')

# EntryStates.took_place.guest_state = GuestStates.planned
# EntryStates.cancelled.guest_state = GuestStates.excused
# EntryStates.missed.guest_state = GuestStates.missing

# print("20181107b", EntryStates.draft.button_text)

GuestStates.clear()
add = GuestStates.add_item
# add('10', _("Suggested"), 'suggested', button_text="?")
# add('10', _("Invited"), 'invited', button_text="☐")
add('20', _("Planned"), 'invited', afterwards=True, button_text="☑")
# add('30', _("Done"), 'done', afterwards=True, button_text="☑")
# add('40', _("Cancelled"), 'cancelled', button_text="C")
add('50', _("Needs replacement"), 'needs', afterwards=True, button_text="⚕")
add('60', _("Found replacement"), 'found', button_text="☉")
# add('10', "☐", 'invited')
# add('40', "☑", 'present', afterwards=True)
# add('50', "☉", 'missing', afterwards=True)
# add('60', "⚕", 'excused')


# @dd.receiver(dd.pre_analyze)
# def my_event_workflows(sender=None, **kw):
GuestStates.ignore_required_states = True
GuestStates.invited.add_transition(required_states='needs found')
GuestStates.needs.add_transition(required_states='invited found')
GuestStates.found.add_transition(required_states='invited needs')
