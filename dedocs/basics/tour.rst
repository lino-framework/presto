.. doctest dedocs/basics/tour.rst
.. include:: /../docs/shared/include/defs.rst
.. _presto.de.tour:

=================
Besichtigungstour
=================

.. contents::
  :local:



Wir melden uns an als Rolf. Der ist Systemverwalter und darf deshalb alles. Wer
es lieber in Französisch hat, wählt Romain.

Hauptbildschirm
===============

Im Hauptbildschirm haben wir das **Hauptmenü**, eventuelle
Willkommensnachrichten und dann das **Dashboard**, d.h. eine Serie von Tabellen
mit diversen Daten. Das Dashboard ist konfigurierbar pro Benutzer.

Die Menüs "Buchhaltung" und "Berichte" kommen wahrscheinlich noch raus, weil
Presto voraussichtlich nur VKR generiert und diese dann in einer externe
Buchhaltung verarbeitet werden.  Es wäre kein technischer Aufwand, die
Buchhaltung mal kurz auszuprobieren (dazu müsste ich lediglich noch
:mod:`lino_xl.lib.finan` und :mod:`lino_xl.lib.bevats`  aktivieren)

Kontakte
========

Als **Partner** bezeichnen wir allgemein jede Einzelperson oder Gruppe, die als
Geschäftspartner, Rechnungsempfänger, Klient, Arbeiter oder sonstiger Kontakt
fungieren kann. Jeder Partner kann unterschiedliche Rollen oder gar parallele
Rollen je nach Auftragstyp oder Finalität einer Dienstleistung haben.

Die Datenbankstruktur unterscheidet fünf Partnerarten: **Personen**,
**Klienten**, **Arbeiter**, **Haushalte** und **Organisationen**. Klienten und
Arbeiter sind eigentlch eine Unterart von Personen. Ein Klient oder Arbeiter
ist immer auch eine Person.  Eine gleiche physische Person kann theoretisch
zugleich Kontaktperson einer Firma, Arbeiter und auch Klient sein.
Der Unterschied zwischen Person, Arbeiter und Klient ist also lediglich
**Ansichtssache** und man kann von einer Ansicht zur anderen wechseln ("Ansicht
als Person, Arbeiter [❌], Klient [❌]").

Jede Person kann **Kontaktperson** für eine oder mehrere Organisationen sein
und kann dort jeweils eine **Funktion** ausüben.

Pro Partner können mehrere **Adressen** hinterlegt werden. Eine davon sollte
als **primär** markiert sein (nur diese Adresse wird tatsächlich benutzt).
Mögliche Adressenarten können definiert werden (z.B. "Referenzadresse" oder
"Wohnsitz"). Auf "Adressen verwalten" klicken, um diese Adressen zu bearbeiten.

Idem für **Kontaktangaben** (Telefon, GSM und E-Mail).

Die **Einkommenskategorie** eines Klienten bestimmt den Tarif, der für Arbeiten
fakturiert wird.  Siehe Fakturierung_.

Haushaltszusammensetzung und familiäre Beziehungen
==================================================

Damit die Suche und die familiäre Einschätzung einfacher ersichtlich wird,
können für jeden Klienten auch deren Haushaltszusammensetzungen und familiäre
Beziehungen erfasst werden.

Ein **Haushalt** ist eine informale Gruppe von Personen, die zusammen wohnen.
Eine Person kann im Laufe der Zeit mehreren Haushalten als **Mitglied** angehören.
Ein Haushalt sollte als **primär** markiert sein.  Die
**Haushaltszusammensetzung** zeigt alle Mitglieder des primären Haushalts.

**Familiäre Beziehungen** sind Beziehungen von Person zu Person, die unabhängig
von der Wohnung existieren.

- Beispiel : :menuselection:`Kontakte --> Personen` und nach *Hubert Frisch*
  suchen.  Dennis Frisch Beziehungen anschauen und Mitgliedschaften korrigieren:
  Dennis ist *Pflegekind* (nicht Kind) in zwei Haushalten.

Termine
========

Ein **Kalendereintrag** ist, wenn zu einem bestimmten Zeipunkt (Datum und
Uhrzeit Beginn und Ende) etwas stattfindet, das in unserem Kalender erwähnt
werden soll.

Ein **Termin** ist ein Kalendereintrag, den ein bestimmter
Mitarbeiter mit einem bestimmten Klienten verabredet hat. Zum Beispiel sind
Urlaubstage oder Feiertage zwar Kalendereinträge, aber keine Termine.

Ein **Einsatz** ist ein Termin im Rahmen eines Auftrags (siehe Einsätze_).
Man kann in Lino auch Termine verwalten, die keine Einsätze sind, also nicht mit
einem Auftrag verknüpft sind (z.B. interne Besprechungen, Urlaubstage, sonstige
Termine der Mitarbeiter, ...).

Der **Autor** eines Kalendereintrags ist der administrative Mitarbeiter, der den
Kalendereintrag erstellt hat (manuell oder automatisch). Generell kann man für
jeden Kalendereintrag **Anwesenheiten** erfassen (Gruppenkalender, Versammlungen
oder Veranstaltungen planen...).



Aufträge
========

Ein **Auftrag** ist, wenn man eine Serie von *Einsätzen* plant, bei denen eine
Serie von *Arbeitern* eine bestimmte Aufgabe für einen bestimmten *Klienten*
verrichtet. Die Serie von Einsätzen kann sich auf einen einzigen Einsatz
beschränken. Die Serie von Arbeitern kann sich auf einen einzigen Arbeiter
beschränken.

Ein Auftrag muss immer einem *Klienten* zugewiesen sein und kann optional einen
anderen *Partner* als Rechnungsempfänger haben.

Jeder einzelne Einsatz hat eine Liste der anwesenden Arbeiter, die prinzipiell
immer die Gleiche ist, sich unter Umständen jedoch von Mal zu Mal ändern kann.

Im Auftrag können neben den vorgesehenen Arbeitern auch Fahrtkosten
und sonstige planbare Nebenkosten erfasst werden, die pro Einsatz fakturiert
werden.

Aufträge sind in **Journale** gruppiert. Ein Journal ist eine Serie von
chronologisch geordneten und durchlaufend nummerierten Dokumenten.

Um die verschiedenen **Tätigkeitsbereiche** des Betriebs zu differenzieren, kann
der Systemverwalter **Teams** konfigurieren.  Menü
:menuselection:`Konfigurierung --> Kalender --> Teams`.

Pro Journal kann man definieren, welches Team für die Aufträge in diesem Journal
zuständig ist. Ein Team kann für mehrere Journale zugleich zuständig sein.   Was
man nicht sagen kann: "für dieses Journal ist mal dieses und mal jenes Team
zuständig".


Einsätze
========

Ein **Einsatz** ist ein Termin im Rahmen eines Auftrags, d.h. ein
Kalendereintrag, der mit einem Auftrag verknüpft ist.

Bei einem Einsatz ist normalerweise ein Arbeiter **anwesend**.
Gegebenenfalls auch mehrere Arbeiter (z.B. Umzüge, Haushaltshilfe).
Gegebenenfalls auch niemand (z.B. in einem stornierten Einsatz).

Die bei einem Einsatz anwesenden Arbeiter stehen im Panel "Anwesenheiten" und
werden dort automatisch auf Basis des Auftrags eingetragen.

Der Einsatz gilt als Grundlage für die Fakturierung. Ohne Einsatz keine
Rechnung. Ob ein Einsatz bereits fakturiert ist, kann man im Detail dieses
Einsatzes (Reiter "Mehr") sehen. Dort stehen sowohl Dienstleistungen als auch
Nebenkosten,

Aufgaben
========

Eine Aufgabe ist eine Notiz über etwas, das erledigt werden muss. Und zwar
normalerweise von einer bestimmten Person für ein bestimmtes Datum.   Eventuell
auch einem bestimmten Auftrag zugeordnet

Kalenderansichten
=================

Über :menuselection:`Kalender --> Kalenderansicht` kann man alle Kalendereinträge
global einsehen (pro Tag, Woche oder pro Monat).

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


Fakturierung
============

Siehe :menuselection:`Konfigurierung --> Produkte --> Preisregeln`.

Jedes Team unterliegt einem **Fakturierungsbereich**.
Diese können konfiguriert werden und bis auf weiteres gibt es deren zwei:

- Für **punktuelle Arbeiten** füllt
  der Arbeiter oder die Mannschaft nach jedem Einsatz
  eine **handgeschriebene Rechnung** aus
  und gibt sie dem Kunden.

  Die Durchschläge der Rechnungen (= Arbeitsberichte) werden im Büro
  gesammelt.
  Jeder Einsatz wird ausgehend von dieser Rechnung erfasst.
  Diese Einsätze müssen nicht unbedingt in Lino geplant werden.
  Dies betrifft die meisten Arbeitsbereiche (Garten, Umzug, ....)

  In der Praxis können auch die bisher punktuellen Einsätze schon in Lino
  geplant werden.  In diesem Fall muss nach dem Einsatz lediglich die Rechnung
  vom Auftrag aus erstellt werden.

- Für **regelmäßige Dienstleistungen** (sh. `Auftrag mit regelmäßigen Terminen`_)
  wird die Terminplanung in Lino gemacht, und auch
  Rechnungen werden von Lino automatisch erstellt (siehe
  :doc:`/invoicing/index`).
  Dies betrifft momentan die Arbeiten im Bereich
  *Haushaltshilfe*.

Einfachen Einsatz nachträglich erfassen
=======================================

Erfassung eines einfachen einmaligen Einsatzes ausgehend von der händisch
ausgefüllten Rechnung:

- Klient erstellen

  - :menuselection:`Kontakte --> Klienten` und dort auf |insert| klicken.

  - Dubletten vermeiden: vorher suchen, ob er nicht schon existiert.

  - NB Das Layout des Detail-Fensters (welche Reite, und welche Elemente wo
    angezeigt werden) ist ein Vorschlag, der leicht
    anpassbar ist und bei dem der Kunde mitreden sollte (was am
    einfachsten direkt auf den Daten im Prototypen geht).

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


Aufträge drucken
================

Auf den Button `printer` klicken.  Lino öffnet dann das druckbare PDF-Dokument
in einem neuen Browserfenster. Beim ersten Mal muss der Browser gesagt
bekommen, dass Lino neue enster öffnen darf.

Inhalt und Layout des gedruckten Dokuments sind noch zu besprechen.

Grund der Anfrage
=================

Pro Klient kann ein **Grund der Anfrage** (oder mehrere) angegeben werden im
Panel **Interessen** (im Reiter "Klient").  Die **Themen**, für die sich ein
Klient interessieren kann, sind konfigurierbar unter
:menuselection:`Konfigurierung --> Themen --> Themen`. Falls nötig können diese
Bezeichnungen und/oder ihre Einordnung geändert werden.

Bin nicht sicher, wozu diese Information gebraucht wird.


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

Dienstleistungen ohne Auftrag
=============================

Zum Beispiel reine Lagerbesichtungen sind  Dienstleistungen, die nicht an den
Kunden fakturiert werden, wohl aber ans ÖSHZ.

Hierfür muss ein Auftrag erstellt und der *Termin* als *Einsatz* erfasst werden,
damit Lino "weiß", dass die Zeit ans ÖSHZ fakturiert werden soll.

Ist noch nicht definitiv.


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
