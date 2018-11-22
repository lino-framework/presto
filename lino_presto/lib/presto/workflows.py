import lino_xl.lib.cal.workflows.voga

"""The default activity are **courses**.  a **hike** usually includes
a bus travel. One enrolment can mean several participants (seats).  A
**journey** also includes a room in a hotel.

"""
from lino_xl.lib.courses.choicelists import CourseAreas
from lino.api import _

CourseAreas.clear()
add = CourseAreas.add_item
add('H', _("House help"), 'default')
add('G', _("Garden"), 'garden', 'courses.GardenContracts')
add('J', _("Journeys"), 'journeys', 'courses.Journeys')


