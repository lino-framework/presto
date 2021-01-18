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


>>> show_menu('rolf')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Kontakte : Arbeiter, Organisationen, Personen, Haushalte, Klienten
- Büro : Meine ablaufenden Upload-Dateien, Meine Upload-Dateien, Meine Auszüge
- Kalender : Meine Termine, Überfällige Termine, Meine unbestätigten Termine, Meine überfälligen Termine, Meine Aufgaben, Einsätze auf Ersatzsuche, Kalender, Mitarbeiterplaner
- Aufträge : Garten (Garten), Umzüge (Umzüge), Renovierung (Renovierung), Haushaltshilfe (Haushaltshilfe), Heimpflege (Heimpflege), Büro (Büro), Wartende Aufträge, Aktive Aufträge, Dringende Aufträge
- Verkauf : Verkaufsrechnungen (SLS), Händische Rechnungen (MAN), Rechnungen erstellen
- Berichte :
  - Verkauf : Journal für Verkaufsrechnungen
- Konfigurierung :
  - System : Benutzer, Site-Parameter, Hilfetexte
  - Kontakte : Organisationsarten, Funktionen, Klientenkontaktarten, Haushaltsarten, Themen, Krankenkassen, Krankenkassen-Regeln, Lebensweisen
  - Büro : Dateibibliotheken, Upload-Arten, Notizarten, Ereignisarten, Meine Einfügetexte, Auszugsarten
  - Kalender : Kalenderliste, Teams, Regelmäßige Ereignisse, Gastrollen, Kalendereintragsarten, Wiederholungsregeln, Externe Kalender, Tagesplanerzeilen
  - Buchhaltung : Konten, Journale, Geschäftsjahre, Buchungsperioden, Zahlungsbedingungen
  - Produkte : Dienstleistungen, Möbel, Produktkategorien, Preisregeln
  - Verkauf : Papierarten, Pauschalen, Fakturationsbereiche
  - Orte : Länder, Orte
- Explorer :
  - System : Vollmachten, Benutzerarten, Benutzerrollen, All dashboard widgets, Datenbankmodelle, Datentests, Datenprobleme
  - Kontakte : Kontaktpersonen, Partner, Klientenkontakte, Standard-Klientenkontaktarten, Haushaltsmitgliedsrollen, Mitglieder, Adressenarten, Adressen, Kontaktangabenarten, Kontaktangaben, Verwandtschaftsbeziehungen, Verwandschaftsarten, Interessen, Krankenkassen-Tarife, Krankenkassen-Situationen, Klienten
  - Büro : Upload-Dateien, Upload-Bereiche, Einfügetexte, Auszüge
  - Kalender : Kalendereinträge, Aufgaben, Anwesenheiten, Abonnements, Kalendereintrag-Zustände, Anwesenheits-Zustände, Aufgaben-Zustände, Tagesplanerkolonnen, Zugriffsklassen, Display colors
  - Buchhaltung : Gemeinkonten, Begleichungsregeln, Belege, Belegarten, Bewegungen, Handelsarten, Journalgruppen
  - Aufträge : Aufträge, Einschreibungen
  - Produkte : Price factors
  - Verkauf : Verkaufsrechnungen, Sales invoice items, Fakturationspläne, Verkaufsregeln
  - SEPA : Bankkonten
  - MwSt. : MWSt-Zonen, MwSt.-Regimes, MwSt.-Klassen, MWSt-Kolonnen, Rechnungen, MwSt-Regeln
- Site : Info, Benutzersitzungen
