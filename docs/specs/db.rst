.. doctest docs/specs/db.rst
.. _presto.specs.db:

=================================
Database structure of Lino Presto
=================================

This document describes the database structure.

.. contents::
  :local:


.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *


>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
43 apps: lino, staticfiles, about, jinja, bootstrap3, extjs, printing, system, users, office, xl, countries, contacts, uploads, contenttypes, gfks, checkdata, cal, weasyprint, ledger, orders, dashboard, calview, clients, households, addresses, phones, humanlinks, topics, healthcare, products, memo, excerpts, vat, sales, invoicing, sepa, notes, appypod, export_excel, tinymce, presto, sessions.
80 models:
=========================== ============================ ========= =======
 Name                        Default table                #fields   #rows
--------------------------- ---------------------------- --------- -------
 addresses.Address           addresses.Addresses          16        145
 cal.Calendar                cal.Calendars                6         1
 cal.Event                   cal.OneEvent                 24        1206
 cal.EventPolicy             cal.EventPolicies            20        6
 cal.EventType               cal.EventTypes               23        8
 cal.Guest                   cal.Guests                   6         1204
 cal.GuestRole               cal.GuestRoles               5         2
 cal.RecurrentEvent          cal.RecurrentEvents          22        16
 cal.RemoteCalendar          cal.RemoteCalendars          7         0
 cal.Room                    cal.Rooms                    13        6
 cal.Subscription            cal.Subscriptions            4         0
 cal.Task                    cal.Tasks                    19        6
 calview.DailyPlannerRow     calview.DailyPlannerRows     7         2
 checkdata.Problem           checkdata.Problems           6         329
 clients.ClientContact       clients.ClientContacts       7         0
 clients.ClientContactType   clients.ClientContactTypes   5         5
 contacts.Company            contacts.Companies           30        31
 contacts.CompanyType        contacts.CompanyTypes        7         14
 contacts.Membership         contacts.Memberships         4         30
 contacts.Partner            contacts.Partners            28        151
 contacts.Person             contacts.Persons             35        106
 contacts.Role               contacts.Roles               4         4
 contacts.RoleType           contacts.RoleTypes           5         5
 contacts.Worker             contacts.Workers             38        9
 contenttypes.ContentType    gfks.ContentTypes            3         80
 countries.Country           countries.Countries          6         8
 countries.Place             countries.Places             9         78
 dashboard.Widget            dashboard.Widgets            5         0
 excerpts.Excerpt            excerpts.Excerpts            12        0
 excerpts.ExcerptType        excerpts.ExcerptTypes        17        7
 gfks.HelpText               gfks.HelpTexts               4         2
 healthcare.Plan             healthcare.Plans             4         5
 healthcare.Rule             healthcare.Rules             6         0
 healthcare.Situation        healthcare.Situations        6         0
 households.Household        households.Households        30        14
 households.Member           households.Members           14        57
 households.Type             households.Types             4         6
 humanlinks.Link             humanlinks.Links             4         56
 invoicing.Area              invoicing.Areas              6         3
 invoicing.Item              invoicing.Items              9         0
 invoicing.Plan              invoicing.Plans              8         1
 invoicing.SalesRule         invoicing.SalesRules         3         17
 invoicing.Tariff            invoicing.Tariffs            7         2
 ledger.Account              ledger.Accounts              18        21
 ledger.AccountingPeriod     ledger.AccountingPeriods     7         3
 ledger.FiscalYear           ledger.FiscalYears           5         11
 ledger.Journal              ledger.Journals              26        8
 ledger.LedgerInfo           ledger.LedgerInfoTable       2         0
 ledger.MatchRule            ledger.MatchRules            3         0
 ledger.Movement             ledger.Movements             11        58
 ledger.PaymentTerm          ledger.PaymentTerms          11        8
 ledger.Voucher              ledger.AllVouchers           8         143
 notes.EventType             notes.EventTypes             8         1
 notes.Note                  notes.Notes                  17        100
 notes.NoteType              notes.NoteTypes              11        3
 orders.Enrolment            orders.Enrolments            5         136
 orders.Order                orders.Orders                32        114
 orders.OrderItem            orders.OrderItems            6         114
 phones.ContactDetail        phones.ContactDetails        7         15
 presto.Client               presto.Clients               43        65
 presto.LifeMode             presto.LifeModes             4         6
 products.PriceRule          products.PriceRules          5         12
 products.Product            products.Products            14        8
 products.ProductCat         products.ProductCats         6         2
 sales.InvoiceItem           sales.InvoiceItems           15        72
 sales.PaperType             sales.PaperTypes             5         3
 sales.VatProductInvoice     sales.Invoices               27        29
 sepa.Account                sepa.Accounts                6         17
 sessions.Session            users.Sessions               3         ...
 system.SiteConfig           system.SiteConfigs           10        1
 tinymce.TextFieldTemplate   tinymce.TextFieldTemplates   5         2
 topics.Interest             topics.Interests             6         0
 topics.Topic                topics.Topics                8         3
 uploads.Upload              uploads.Uploads              19        10
 uploads.UploadType          uploads.UploadTypes          10        11
 uploads.Volume              uploads.Volumes              5         0
 users.Authority             users.Authorities            3         0
 users.User                  users.AllUsers               18        4
 vat.InvoiceItem             vat.InvoiceItemTable         9         0
 vat.VatAccountInvoice       vat.Invoices                 20        0
=========================== ============================ ========= =======
<BLANKLINE>
