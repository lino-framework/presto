.. include:: /../docs/shared/include/defs.rst

.. _presto.de.tour:

=================
Besichtigungstour
=================

.. contents::
  :local:


Kontakte
========

Als **Partner** bezeichnen wir allgemein jede Einzelperson oder Gruppe, die als
**Rechnungsempfänger** oder sonstiger Gesprächspartner fungieren kann.
Jeder Partner kann unterschiedliche Rollen oder gar parallele Rollen je
nach Auftragstyp oder Finalität einer Dienstleistung haben.

Lino unterscheidet fünf Partnerarten: **Personen**, **Klienten**, **Arbeiter**,
**Haushalte** und **Organisationen**. Klienten und Arbeiter sind Personen, über
die wir mehr wissen als über eine normale Person.  Ein Klient oder Arbeiter ist
immer auch eine Person.

Damit die Suche und die familiäre Einschätzung einfacher ersichtlich wird,
können für jede Person auch deren Familienzusammensetzungen (generell
Mitgliedschaft in Haushalten) und familiäere Beziehungen erfasst werden.

Pro Partner können mehrere Adressen hinterlegt werden. Mögliche Adressenarten
können definiert werden (z.B. "Referenzadresse" oder "Wohnsitz")

Pro Klient kann ein **Grund der Anfrage** (oder mehrere) angegeben werden im
Panel **Interessen** (Reiter "Klient").  Die **Themen**, für die sich ein
Klient "interessieren" kann, sind konfigurierbar unter
:menuselection:`Konfigurierung --> Themen --> Themen`.
Falls nötig Wortschatz und/oder Einordnung geändert werden.

Aufträge
========

Ein **Auftrag** ist, wenn man eine Serie von
*Einsätzen* plant, bei denen eine Serie von *Arbeitern* eine bestimmte Aufgabe
für einen bestimmten *Klienten* verrichtet.
Die Serie von Einsätzen kann sich auf einen einzigen Einsatz beschränken.
Die Serie von Arbeitern kann sich auf einen einzigen Arbeiter beschränken.

Ein Auftrag muss immer einem *Klienten* zugewiesen sein und kann optional einen
anderen *Partner* als Rechnungsempänger haben.

Jeder einzelne Einsatz hat eine Liste der anwesenden Arbeiter, die prinzipiell
immer die Gleiche ist, sich unter Umständen jedoch von Mal zu Mal ändern kann.

Der Auftrag gilt als Grundlage für die Fakturierung. Ohne Auftrag keine
Rechnung.  Im Auftrag können neben den vorgesehenen Arbeitern auch Fahrtkosten
und sonstige planbare Nebenkosten erfasst werden, die pro Einsatz fakturiert
werden.

Aufträge sind in **Journale** gruppiert. Ein Journal ist eine Serie von
chronologisch geordneten und durchlaufend nummerierten Dokumenten.

Um die verschiedenen **Tätigkeitsbereiche** des Betriebs zu differenzieren, kann
der Systemverwalter **Teams** konfigurieren.

Pro Journal kann man definieren, welches Team für die Aufträge in diesem
Journal zuständig ist. Eventuell können mehrere Journale pro Team angelegt
werden.


Termine
========

Ein **Termin** ist, wenn an einem bestimmten Tag und Uhrzeit ein bestimmter
Arbeiter (oder mehrere) sich an einem bestimmten Ort mit einem bestimmten
Klienten verabredet hat.

Ein Termin wird manchmal auch allgemeiner als **Kalendereintrag** bezeichnet.
Der Unterschied ist, dass z.B. ein Urlaubstag oder ein Feiertag ein
Kalendereintrag sein kann, obwohl es kein Termin ist.

Ein **Einsatz** ist ein Termin im Rahmen eines Auftrags, d.h. ein
Kalendereintrag, der mit einem Auftrag **verknüpft** ist.

Man kann in Lino auch **unfakturierte Termine** verwalten, d.h. die nicht mit
einem Auftrag verknüpft sind (z.B. interne Besprechungen, Urlaubstage, sonstige
Termine der Mitarbeiter, ...).

Der **Autor** eines Kalendereintrags ist der administrative Mitarbeiter, der
den Termin erstellt hat (manuell oder automatisch).

Die **Arbeiter** eines Kalendereintrags stehen im Panel "Anwesenheiten".

Ob ein fakturierbarer Termin bereits fakturiert ist, kann man im Detail dieses
Termins (Reiter "Mehr") sehen. Dort stehen sowohl Dienstleistungen als auch
Nebenkosten,

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


Fakturierungsbereiche
=====================

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




Dienstleistungen, die nicht an den Kunden fakturiert werden, wohl aber ans
ÖSHZ.

Zum Beispiel reine Lagerbesichtungen

Hierfür muss ein Auftrag erstellt und der *Termine* erfasst werden, damit Lino
"weiß", dass die Zeit ans ÖSHZ fakturiert werden soll.


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

Lino kann Terminvorschläge automatisch generieren.
Dabei wird pro Klient ein Auftrag erstellt, in dem die gewünschten Wochentage
und Uhrzeiten festgehalten werden.  Lino generiert daraufhin Terminvorschläge.
Jeder einzelne Termin kann manuell verändert werden.  Die Terminvorschläge
müssen in Lino bestätigt werden, wenn sie stattgefunden haben.

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



