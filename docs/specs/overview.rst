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
- 79 models
- 17 user roles
- 4 user types
- 294 views
- 23 dialog actions
<BLANKLINE>




Don't read me
=============

>>> show_choicelists()
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
=============================== ================= ================================== ================================== ===============================
 name                            preferred_width   de                                 fr                                 en
------------------------------- ----------------- ---------------------------------- ---------------------------------- -------------------------------
 about.TimeZones                 4                 Zeitzonen                          Zeitzonen                          Time zones
 addresses.AddressTypes          20                Adressenarten                      Types d'adresses                   Address types
 addresses.DataSources           24                Datenquellen                       Sources de données                 Data sources
 cal.AccessClasses               31                None                               None                               None
 cal.DisplayColors               7                 None                               None                               None
 cal.DurationUnits               8                 None                               None                               None
 cal.EntryStates                 13                Kalendereintrag-Zustände           Kalendereintrag-Zustände           Entry states
 cal.EventEvents                 8                 Beobachtungskriterien              Évènements observés                Observed events
 cal.GuestStates                 12                Anwesenheits-Zustände              Anwesenheits-Zustände              Presence states
 cal.PlannerColumns              6                 None                               None                               None
 cal.Recurrencies                20                None                               None                               None
 cal.ReservationStates           4                 Zustände                           États                              States
 cal.TaskStates                  9                 Aufgaben-Zustände                  Aufgaben-Zustände                  Task states
 cal.Weekdays                    10                None                               None                               None
 cal.YearMonths                  9                 None                               None                               None
 checkdata.Checkers              54                Datentests                         Tests de données                   Data checkers
 clients.ClientEvents            10                Beobachtungskriterien              Évènements observés                Observed events
 clients.ClientStates            9                 Bearbeitungszustände Klienten      Etats bénéficiaires                Client states
 clients.KnownContactTypes       9                 Standard-Klientenkontaktarten      Types de contact connus            Known contact types
 contacts.CivilStates            27                Zivilstände                        Etats civils                       Civil states
 contacts.PartnerEvents          18                Beobachtungskriterien              Évènements observés                Observed events
 countries.PlaceTypes            16                None                               None                               None
 excerpts.Shortcuts              4                 Excerpt shortcuts                  Excerpt shortcuts                  Excerpt shortcuts
 healthcare.Tariffs              6                 Krankenkassen-Tarife               Krankenkassen-Tarife               Healthcare tariffs
 households.MemberDependencies   15                Haushaltsmitgliedsabhängigkeiten   Dépendances de membres de ménage   Household Member Dependencies
 households.MemberRoles          11                Haushaltsmitgliedsrollen           Rôles de membres de ménage         Household member roles
 humanlinks.LinkTypes            27                Verwandschaftsarten                Types de parenté                   Parency types
 ledger.CommonAccounts           29                Gemeinkonten                       Comptes communs                    Common accounts
 ledger.JournalGroups            26                Journalgruppen                     Groupes de journaux                Journal groups
 ledger.PeriodStates             14                Zustände                           États                              States
 ledger.TradeTypes               18                Handelsarten                       Types de commerce                  Trade types
 ledger.VoucherStates            14                Zustände Beleg                     États Beleg                        Voucher states
 ledger.VoucherTypes             42                Belegarten                         Types de pièce                     Voucher types
 notes.SpecialTypes              4                 Sondernotizarten                   Sondernotizarten                   Special note types
 phones.ContactDetailTypes       8                 Kontaktangabenarten                Kontaktangabenarten                Contact detail types
 presto.IncomeCategories         4                 Einkommenskategorien               Einkommenskategorien               Income categories
 printing.BuildMethods           20                None                               None                               None
 products.DeliveryUnits          5                 Delivery units                     Delivery units                     Delivery units
 products.PriceFactors           19                Price factors                      Price factors                      Price factors
 products.ProductTypes           16                Product types                      Product types                      Product types
 system.Genders                  8                 None                               None                               None
 system.PeriodEvents             9                 Beobachtungskriterien              Évènements observés                Observed events
 system.YesNo                    12                Ja oder Nein                       Oui ou non                         Yes or no
 uploads.Shortcuts               4                 Upload shortcuts                   Upload shortcuts                   Upload shortcuts
 uploads.UploadAreas             7                 Upload-Bereiche                    Domaines de téléchargement         Upload areas
 users.UserTypes                 21                Benutzerarten                      Types d'utilisateur                User types
 vat.DeclarationFieldsBase       4                 Declaration fields                 Declaration fields                 Declaration fields
 vat.VatAreas                    13                MWSt-Zonen                         Zones TVA                          VAT areas
 vat.VatClasses                  31                MwSt.-Klassen                      Classes TVA                        VAT classes
 vat.VatColumns                  4                 MWSt-Kolonnen                      MWSt-Kolonnen                      VAT columns
 vat.VatRegimes                  6                 MwSt.-Regimes                      MwSt.-Regimes                      VAT regimes
 vat.VatRules                    39                MwSt-Regeln                        MwSt-Regeln                        VAT rules
 xl.Priorities                   8                 Prioritäten                        Priorités                          Priorities
=============================== ================= ================================== ================================== ===============================
<BLANKLINE>


Test whether the bootstrap3 user interface works:

>>> url = '/bs3/products/Products'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
