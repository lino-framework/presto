.. doctest docs/specs/menu.rst
.. include:: /../docs/shared/include/defs.rst

.. _presto.specs.menu:

========
The menu
========

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *


>>> rt.login('rolf').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Kontakte : Arbeiter, Organisationen, Personen, Haushalte, Klienten
- Kalender : Meine Termine, Überfällige Termine, Meine unbestätigten Termine, Meine Aufgaben, Meine Gäste, Meine Anwesenheiten, Meine überfälligen Termine, Kalenderansicht
- Aufträge : Garten (Garten), Umzüge (Umzüge), Renovierung (Renovierung), Haushaltshilfe (Haushaltshilfe), Heimpflege (Heimpflege), Büro (Büro)
- Verkauf : Verkaufsrechnungen (SLS), Gutschriften Verkauf (SLC), Händische Rechnungen (MAN), Rechnungen erstellen
- Buchhaltung :
  - Einkauf : Einkaufsrechnungen (PRC)
- Büro : Meine Auszüge, Meine Uploads
- Berichte :
  - Buchhaltung : Schuldner, Gläubiger
  - Verkauf : Offene Rechnungen, Journal für Verkaufsrechnungen
  - MwSt. : Purchase journal, Intra-Community purchases, Intra-Community sales
- Konfigurierung :
  - System : Benutzer, Site-Parameter, Hilfetexte
  - Kontakte : Organisationsarten, Funktionen, Klientenkontaktarten, Haushaltsarten, Themen, Krankenkassen, Krankenkassen-Regeln, Lebensweisen
  - Kalender : Kalenderliste, Teams, Regelmäßige Ereignisse, Gastrollen, Kalendereintragsarten, Wiederholungsregeln, Externe Kalender, Tagesplanerzeilen
  - Buchhaltung : Konten, Journale, Geschäftsjahre, Buchungsperioden, Zahlungsbedingungen
  - Produkte : Dienstleistungen, Möbel, Produktkategorien, Preisregeln
  - Verkauf : Papierarten, Pauschalen, Fakturationsbereiche
  - Büro : Notizarten, Ereignisarten, Auszugsarten, Meine Einfügetexte, Dateibibliotheken, Upload-Arten
  - Orte : Länder, Orte
- Explorer :
  - System : Vollmachten, Benutzerarten, Benutzerrollen, All dashboard widgets, Datenbankmodelle, Datentests, Datenprobleme
  - Kontakte : Kontaktpersonen, Partner, Klientenkontakte, Standard-Klientenkontaktarten, Haushaltsmitgliedsrollen, Mitglieder, Adressenarten, Adressen, Kontaktangabenarten, Kontaktangaben, Verwandtschaftsbeziehungen, Verwandschaftsarten, Interessen, Krankenkassen-Tarife, Krankenkassen-Situationen, Klienten
  - Kalender : Kalendereinträge, Aufgaben, Anwesenheiten, Abonnements, Termin-Zustände, Gast-Zustände, Aufgaben-Zustände
  - Buchhaltung : Gemeinkonten, Begleichungsregeln, Belege, Belegarten, Bewegungen, Handelsarten, Journalgruppen
  - Aufträge : Aufträge, Einschreibungen
  - Produkte : Price factors
  - Verkauf : Verkaufsrechnungen, Sales invoice items, Fakturationspläne, Verkaufsregeln
  - SEPA : Bankkonten
  - Büro : Auszüge, Einfügetexte, Uploads, Upload-Bereiche
  - MwSt. : VAT areas, MwSt.-Regimes, VAT classes, VAT columns, Rechnungen, MwSt-Regeln
- Site : Info



