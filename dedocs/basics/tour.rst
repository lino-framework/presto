.. doctest dedocs/basics/tour.rst
.. include:: /../docs/shared/include/defs.rst
.. _presto.de.tour:

======================
Eine Besichtigungstour
======================

.. contents::
  :local:


Wir melden uns an als Rolf. Der ist Systemverwalter und darf deshalb alles. Wer
es lieber in Französisch hat, wählt Romain.


Klient erstellen
================

- :menuselection:`Kontakte --> Klienten`

- Dubletten vermeiden: vorher suchen, ob der Klient nicht schon existiert.

- Auf |insert| klicken, um das Dialogfenster "Einfügen" zu öffnen.

- Nach Bestätigung des Dialogfensters erstellt Lino den Datensatz und zeigt den
  neuen  Klient im Detail an.

- Das Layout des Detail-Fensters (welche Reiter, und welche Elemente wo
  angezeigt werden) ist ein Vorschlag, der leicht anpassbar ist und bei dem der
  Kunde mitreden sollte (was am einfachsten direkt auf den Produktionsdaten
  geht).


Kalenderansichten
=================

Über :menuselection:`Kalender --> Kalenderansicht` kann man alle Kalendereinträge
global einsehen (pro Tag, Woche oder pro Monat).

Hier kann man auch Filter setzen: z.B. nur ein bestimmtes Team.

Die Termine eines bestimmten Auftrags kann man im Detail des Auftrags (Reiter
"Kalender") sehen.

Alle Termine eines bestimmten Klienten (für alle Aufträge dieses Klienten,
sowie unfakturierte Termine) kann man im Detail des Klienten (Reiter
"Kalendereinträge") sehen.

Die Termine eines bestimmten Arbeiters kann man im Detail des Arbeiters
(Reiter "Anwesenheiten") sehen.

Die Termine eines bestimmten Teams kann man im Detail des Teams
(Panel "Kalendereinträge") sehen.

Im Menü :menuselection:`Kalender` gibt es noch weitere Kalenderansichten. Zum
Beispiel "Überfällig Termine" sind Termine, die älter als eine Woche sind und
bei denen man noch nicht bestätigt hat, ob sie stattgefunden haben oder nicht.
Manche dieser Ansichten können vielleicht raus, und manche fehlen vielleicht
noch.


Ersatzsuche
===========

Ein Arbeiter sagt an, dass er an einem bestimmten Tag fehlen wird und deshalb
bei einem geplanten Einsatz ersetzt werden muss.

- Finde den Termin, um den es geht (über den Arbeiter oder über den Auftrag).

- Im Panel "Anwesenheiten" steht der Arbeiter.

- In der Kolonne "Workflow" gibt es verschiedene Aktionen:
  Wenn du noch nicht weißt, welcher Arbeiter ihn ersetzen wird, dann klicke auf :guilabel:`⚕`.
  Ansonsten klicke auf "Ersatz suchen", wähle den Arbeiter aus und bestätige das Dialogfenster.

- Arbeiter, die auf :guilabel:`⚕` gesetzt wurden, erscheinen automatisch im
  Dashboard unter "Einsätze auf Ersatzsuche" bis auch hier auf "Ersatz suchen"
  geklickt wurde.


Einfachen Einsatz nachträglich erfassen
=======================================

Erfassung eines einfachen einmaligen Einsatzes ausgehend von der händisch
ausgefüllten Rechnung:

- `Klient erstellen`_

- Auftrag erstellen:

  - vom Klienten aus:

     - Reiter "Fakturierung", Panel "Aufträge", Doppelklick auf überletzter Zeile
     - Journal auswählen, Erfassungsdatum bestätigen, :kbd:`Ctrl-S`

  - vom Hauptmenü aus:

     - :menuselection:`Aufträge --> (Auftragsjournal)` und dort |insert|
     - Klient auswählen, Erfassungsdatum, :kbd:`Ctrl-S`

- Auftrag detaillieren:

  - ggf. Rechnungsempfänger angeben
  - Arbeiter erfassen

  - Fahrtkosten eintragen in "Kosten pro Einsatz". Hier können ausser
    Fahrtkosten auch z.B. Verbrauchsprodukte angegeben werden.  Die hier
    angegebenen Kosten werden für jeden stattgefundenen Termin zusätzlich zur
    Arbeitszeit fakturiert.

  - ggf. Beschreibung der Arbeiten

- Auftrag ausdrucken (noch nicht programmiert)

- Termin erfassen:

  - einzelne Termine mit |insert| im Panel "Termine" im Reiter "Kalender"

  - Siehe auch `Auftrag mit regelmäßigen Terminen`_

  - Beachte, dass der oder die im Auftrag erfassten Arbeiter automatisch in den
    **Anwesenheiten** des Termins stehen.

  - Beachte das Feld **Workflow** : jeder Termin steht zunächst im Status "Vorschlag" bzw.
    "Geplant", und man muss auf :guilabel:`☑` klicken, damit er in den Zustand
    "Stattgefunden" wechselt. Ansonsten erstellt Lino keine Rechnung.

- :kbd:`Escape` um auf den Auftrag zurück zu springen.

- Auf |basket| klicken um einen **Fakturierungsplan** für diesen Auftrag zu
  starten. Ein Fakturierungsplan ist, wenn ein Benutzer plant, eine Serie
  on Rechnungen erstellen zu lassen.

  Lino zeigt nun genau einen Vorschlag an, weil es nur einen Termin gibt.

- Vergleiche den von Lino vorgeschlagenen Betrag der Rechnung mit der händisch
  erstellten Rechnung.  Falls ein Unterschied ist: entweder :kbd:`Escape` und den
  Auftrag überprüfen oder Rechnung trotzdem erstellen lassen und dann manuell
  bearbeiten.

- Im Fakturierungsplan auf |money| klicken, um die vorgeschlagenen
  Rechnungen zu generieren.

- Wenn eine Rechnung generiert wurde, steht im betreffenden Vorschlag nicht
  mehr ein |money|, sondern die anklickbare Nummer der erstellten Rechnung.  Auf
  diese Nummer kann man klicken, um die Rechnung im Detail anzuzeigen.

Rechnung manuell bearbeiten
===========================

Man kann eine erstellte Rechnung jederzeit manuell bearbeiten:

- Die Rechnung im Detail anzeigen (z.B. über den Fakturierungsplan, oder über
  :menuselection:`Verkauf --> (Journal)` und dann Doppelklick auf der
  gewünschten Rechnung).

- Im Feld :guilabel:`Workflow` auf "Entwurf" klicken falls die Rechnung auf
  "Registriert" steht.

- Inhalt bearbeiten

- Im Feld :guilabel:`Workflow` auf "Registriert" klicken, um sie wieder zu
  registrieren.

Auftrag mit regelmäßigen Terminen
=================================

Lino kann Terminvorschläge automatisch generieren. Dabei wird pro Klient ein
Auftrag erstellt, in dem die Wiederholungsregeln festgehalten werden (gewünschte
Wochentage und Uhrzeiten, Wiederholungsrate, Anzahl Einsätze und/oder Enddatum,
...).  Lino generiert daraufhin Terminvorschläge. Jeder einzelne Termin kann
manuell verändert werden.  Die Terminvorschläge müssen in Lino bestätigt werden,
wenn sie stattgefunden haben.

- Gehe auf den Auftrag und aktiviere den Reiter "Kalender"

- Fülle die Felder aus, die die Kriterien definieren zum Erstellen der Terminserie:

  - "Beginnt am", "Beginnt um" und "Endet um" : wann der erste Einsatz stattfinden soll
  - "Enddatum" sollte immer frei sein ausser bei Terminen, die mehrere Tage dauern
  - "Wiederholung" und "... alle"

  - "Anzahl Termine" und "Termine generieren bis" : normalerweise wird nur
    eines dieser beiden Felder ausgefüllt.  Lino hört auf, wenn die erste der
    beiden Grenzen erreicht ist. Falls beide Felder leer sind, wird ein
    konfigurierbarer Höchstwert angenommen
    (:menuselection:`Konfigurierung --> System --> Site-Parameter`).

  - Wenn **kein** Wochentag angekreuzt ist, gilt der Wochentag nicht als Kriterium

- Klicke auf |lightning| und beobachte das Panel Kalendereinträge

Den Button |lightning| kannst du so oft betätigen wie du willst (und nach jeder
Änderung in den Kriterien musst du dies selber tun). Lino verändert nur
Terminvorschläge, die noch nicht manuell bearbeitet wurden.

Der Button :guilabel:`☷` dient dazu, die Anwesenheitslisten der erstellten
Terminvorschläge zu aktualisieren. Also wenn du
einen Arbeiter im Auftrag auswechselst, nachdem du schon auf |lightning|
geklickt hattest, möchtest du wahrscheinlich auch auf :guilabel:`☷` klicken.
Auch hier werden natürlich nur Termine aktualisiert, die noch nicht
stattgefunden haben


Rechnungen an die ÖSHZ
======================

Rechnungen an die ÖSHZ werden auf Basis der erfassten Termine erstellt,
unabhängig der tatsächlich an den Kunden fakturierten Dienstleistungen.
Nullrechnungen sind also nicht nötig. Wohl aber ist ein Auftrag nötig, denn
sonst hat Lino ja keine Ahnung, wer der Klient ist.

Der Rechnungsinhalt könnte automatisch von Lino generiert werden.

Momentan gilt die pragmatischse Vorgehensweise, dass man pro Gemeinde pro
Quartal folgendes macht:

- In das Journal gehen (z.B. :menuselection:`Buchhaltung -->
  Gemeinderechnungen`)

- |insert| um eine neue Rechnung zu erstellen. Als Partner die
  Gemeindeverwaltung (das ÖSHZ) auswählen.

- Papierart muss sein "Dienstleistungsbericht" (das kann man schon in den
  Stammdaten der Gemeinde eintragen).

- **Fakturierbare von / bis** aufüllen

- Leere Rechnung ausdrucken (auf den Button `printer` klicken).

  Der Dienstleistungsbericht zeigt automatisch alle Klienten, die im gleichen
  Ort wie die Verwaltung oder einem untergeordneten Ort wohnen. Siehe
  :menuselection:`Konfigurierung --> Orte --> Orte`, Kolonne "Teil von".

- Eventuell die tatsächlich fakturierten Zahlen manuell eingeben.

Beispiele
=========

Hier einige Tests auf den Demo-Daten.

>>> from lino import startup
>>> startup('lino_presto.projects.noereth.settings.doctests')
>>> from lino.api.doctest import *

Liste der Teams:

>>> show_menu_path(cal.AllRooms)
Konfigurierung --> Kalender --> Teams

>>> rt.show(cal.AllRooms, column_names="name event_type")
================ ================== ================== =====================
 Bezeichnung      Bezeichnung (fr)   Bezeichnung (en)   Kalendereintragsart
---------------- ------------------ ------------------ ---------------------
 Garten           Garten             Garden             Außenarbeiten
 Umzüge           Umzüge             Moves              Außenarbeiten
 Renovierung      Renovierung        Renovation         Innenarbeiten
 Haushaltshilfe   Haushaltshilfe     Home help          Innenarbeiten
 Heimpflege       Heimpflege         Home care          Innenarbeiten
 Büro             Bureau             Office             Büroarbeiten
================ ================== ================== =====================
<BLANKLINE>

>>> rt.show(ledger.Journals, column_names="ref name room voucher_type")
================ ====================== ====================== ================== ================ ============================================
 Referenz         Bezeichnung            Bezeichnung (fr)       Bezeichnung (en)   Team             Belegart
---------------- ---------------------- ---------------------- ------------------ ---------------- --------------------------------------------
 SLS              Verkaufsrechnungen     Factures vente         Sales invoices                      Verkaufsrechnung (sales.InvoicesByJournal)
 MAN              Händische Rechnungen   Händische Rechnungen   Manual invoices                     Verkaufsrechnung (sales.InvoicesByJournal)
 Garten           Garten                                                           Garten           Auftrag (orders.OrdersByJournal)
 Umzüge           Umzüge                                                           Umzüge           Auftrag (orders.OrdersByJournal)
 Renovierung      Renovierung                                                      Renovierung      Auftrag (orders.OrdersByJournal)
 Haushaltshilfe   Haushaltshilfe                                                   Haushaltshilfe   Auftrag (orders.OrdersByJournal)
 Heimpflege       Heimpflege                                                       Heimpflege       Auftrag (orders.OrdersByJournal)
 Büro             Büro                                                             Büro             Auftrag (orders.OrdersByJournal)
================ ====================== ====================== ================== ================ ============================================
<BLANKLINE>
