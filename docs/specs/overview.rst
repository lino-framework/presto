.. doctest docs/specs/overview.rst
.. include:: /../docs/shared/include/defs.rst

.. _lino.tested.presto:
.. _presto.specs.overview:

========
Overview
========

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *


Some vocabulary
===============

================ ================================
English          German
================ ================================
Furniture        Möbel
Used furniture   Gebrauchtmöbel
Renovation       Renovierungsarbeiten
Bicycle studio   Fahrradwerkstatt
Furniture store  Möbellager
Garden services  Gartenarbeiten
Home help        Haushaltshilfe
Small repair     Kleinreparaturen im Haushalt
Laundry service  Wäschedienst (Waschbären)
Transport        Transport
Moving           Umzüge
Delivery note    Lieferschein
================ ================================


- Managed as contracts : Garden contracts, Home help
- Managed as delivery notes  : Bicycle, Transport, Small repair, Moving, Furniture store, Renovation


Complexity factors
==================

>>> print(analyzer.show_complexity_factors())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 43 plugins
- 81 models
- 4 user types
- 308 views
- 24 dialog actions
<BLANKLINE>




Don't read me
=============

>>> show_choicelists()
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
=============================== ======== ================= ================================== ================================== ===============================
 name                            #items   preferred_width   de                                 fr                                 en
------------------------------- -------- ----------------- ---------------------------------- ---------------------------------- -------------------------------
 about.TimeZones                 1        4                 Zeitzonen                          Zeitzonen                          Time zones
 addresses.AddressTypes          6        20                Adressenarten                      Types d'adresses                   Address types
 addresses.DataSources           2        24                Datenquellen                       Sources de données                 Data sources
 cal.AccessClasses               3        31                Zugriffsklassen                    Classes d'accès                    Access classes
 cal.DisplayColors               16       7                 Display colors                     Display colors                     Display colors
 cal.DurationUnits               7        8                 None                               None                               None
 cal.EntryStates                 5        13                Kalendereintrag-Zustände           Kalendereintrag-Zustände           Entry states
 cal.EventEvents                 2        8                 Beobachtungskriterien              Évènements observés                Observed events
 cal.GuestStates                 3        15                Anwesenheits-Zustände              Anwesenheits-Zustände              Presence states
 cal.PlannerColumns              5        14                Tagesplanerkolonnen                Colonnes planificateur             Planner columns
 cal.Recurrencies                7        20                None                               None                               None
 cal.ReservationStates           0        4                 Zustände                           États                              States
 cal.TaskStates                  5        9                 Aufgaben-Zustände                  Aufgaben-Zustände                  Task states
 cal.Weekdays                    7        10                None                               None                               None
 cal.YearMonths                  12       9                 None                               None                               None
 calview.Planners                2        17                None                               None                               None
 checkdata.Checkers              15       54                Datentests                         Tests de données                   Data checkers
 clients.ClientEvents            3        10                Beobachtungskriterien              Évènements observés                Observed events
 clients.ClientStates            3        9                 Bearbeitungszustände Klienten      Etats bénéficiaires                Client states
 clients.KnownContactTypes       2        9                 Standard-Klientenkontaktarten      Types de contact connus            Known contact types
 contacts.CivilStates            7        27                Zivilstände                        Etats civils                       Civil states
 contacts.PartnerEvents          1        18                Beobachtungskriterien              Évènements observés                Observed events
 countries.PlaceTypes            23       16                None                               None                               None
 excerpts.Shortcuts              0        4                 Excerpt shortcuts                  Excerpt shortcuts                  Excerpt shortcuts
 healthcare.Tariffs              3        6                 Krankenkassen-Tarife               Krankenkassen-Tarife               Healthcare tariffs
 households.MemberDependencies   3        15                Haushaltsmitgliedsabhängigkeiten   Dépendances de membres de ménage   Household Member Dependencies
 households.MemberRoles          9        11                Haushaltsmitgliedsrollen           Rôles de membres de ménage         Household member roles
 humanlinks.LinkTypes            13       27                Verwandschaftsarten                Types de parenté                   Parency types
 ledger.CommonAccounts           21       29                Gemeinkonten                       Comptes communs                    Common accounts
 ledger.DC                       2        6                 Booking directions                 Booking directions                 Booking directions
 ledger.JournalGroups            7        26                Journalgruppen                     Groupes de journaux                Journal groups
 ledger.PeriodStates             2        14                Zustände                           États                              States
 ledger.TradeTypes               6        18                Handelsarten                       Types de commerce                  Trade types
 ledger.VoucherStates            4        14                Belegzustände                      Belegzustände                      Voucher states
 ledger.VoucherTypes             4        42                Belegarten                         Types de pièce                     Voucher types
 notes.SpecialTypes              0        4                 Sondernotizarten                   Sondernotizarten                   Special note types
 orders.OrderStates              5        14                Belegzustände                      Belegzustände                      Voucher states
 phones.ContactDetailTypes       6        8                 Kontaktangabenarten                Kontaktangabenarten                Contact detail types
 presto.IncomeCategories         4        4                 Einkommenskategorien               Einkommenskategorien               Income categories
 printing.BuildMethods           9        20                None                               None                               None
 products.DeliveryUnits          3        5                 Delivery units                     Delivery units                     Delivery units
 products.PriceFactors           1        19                Price factors                      Price factors                      Price factors
 products.ProductTypes           2        16                Product types                      Product types                      Product types
 system.Genders                  2        8                 None                               None                               None
 system.PeriodEvents             3        9                 Beobachtungskriterien              Évènements observés                Observed events
 system.YesNo                    2        12                Ja oder Nein                       Oui ou non                         Yes or no
 uploads.Shortcuts               2        26                Upload shortcuts                   Upload shortcuts                   Upload shortcuts
 uploads.UploadAreas             1        7                 Upload-Bereiche                    Domaines de téléchargement         Upload areas
 users.UserTypes                 4        21                Benutzerarten                      Types d'utilisateur                User types
 vat.DeclarationFieldsBase       0        4                 Declaration fields                 Declaration fields                 Declaration fields
 vat.VatAreas                    3        13                MWSt-Zonen                         Zones TVA                          VAT areas
 vat.VatClasses                  8        31                MwSt.-Klassen                      Classes TVA                        VAT classes
 vat.VatColumns                  0        4                 MWSt-Kolonnen                      MWSt-Kolonnen                      VAT columns
 vat.VatRegimes                  1        6                 MwSt.-Regimes                      MwSt.-Regimes                      VAT regimes
 vat.VatRules                    1        39                MwSt-Regeln                        MwSt-Regeln                        VAT rules
 xl.Priorities                   5        8                 Prioritäten                        Priorités                          Priorities
=============================== ======== ================= ================================== ================================== ===============================
<BLANKLINE>

Test whether the bootstrap3 user interface works:

>>> url = '/bs3/products/Products'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
