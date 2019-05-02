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

Ein **Auftrag** ist, wenn man für einen bestimmten Klienten eine Serie von
Terminen plant, bei denen ein bestimmter Arbeiter arbeitet.  Die Serie von
Terminen kann sich auf einen einzigen Einsatz beschränken. Aufträge sind in
*Journale** gruppiert. Der Auftrag gilt als Grundlage für die Fakturierung.
Ohne Auftrag keine Rechnung.  Im Auftrag können neben den vorgesehenen
Arbeitern auch Fahrtkosten und sonstige planbare Nebenkosten erfasst werden,
die pro Einsatz fakturiert werden.

Ein Auftrag muss immer einem Klienten zugewiesen sein und kann optional einen
anderen Partner als Rechnungsempänger haben.

Termine
========

Ein **Termin** ist, wenn an einem bestimmten Tag und Uhrzeit ein bestimmter
Arbeiter (oder mehrere) zu einem bestimmten Klienten gehen.

Ein Termin wird manchmal auch allgemeiner als **Kalendereintrag** bezeichnet.
Der Unterschied ist, dass z.B. ein Urlaubstag oder ein Feiertag ein
Kalendereintrag sein kann, obwohl es kein Termin ist.

**Fakturierbare Termine** sind mit einem Auftrag **verknüpft**. Man kann in Lino
auch **unfakturierte Termine** verwalten (z.B. interne Besprechungen,
Urlaubstage, sonstige Termine der Mitarbeiter, ...).

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


Teams
=====

Um die verschiedenen Tätigkeitsbereiche eines Betriebs zu differenzieren, kann
der Systemverwalter **Teams** und entsprechende **Auftragsjournale** konfigurieren.
Pro Auftragsjournal kann man definieren, welches Team für Aufträge in diesem Journal zuständig ist.
Eventuell können mehrere Auftragsjournale pro Team angelegt werden.

Fakturierungsbereiche
=====================

Jedes Team unterliegt einem **Fakturierungsbereich**.
Diese können konfiguriert werden
Laut Lastenheft gibt es deren zwei:

- **handwerkliche Arbeiten** werden nach jedem Einsatz ausgehend von der händisch
  bereits ausgefüllten und dem Kunden bereits ausgehändigten Rechnung erfasst.

- Für **regelmäßige Dienstleistungen** (sh. `Auftrag mit regelmäßigen Terminen`_)
  werden die Rechnungen für alle Aufträge auf einmal erstellt mit
  :menuselection:`Verkauf --> Rechnungen erstellen`


Beispiel 1 : Einfachen Einsatz nachträglich erfassen
====================================================

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

- Termin(e) erfassen:

  - einzelne Termine mit |insert| im Panel "Termine" im Reiter "Kalender"
  - Siehe auch `Auftrag mit regelmäßigen Terminen`_

  - Beachte, dass die Arbeiter des Auftrags automatisch in den **Anwesenheiten**
    des Termins stehen.
    Jeder einzelne Termin hat eine Liste der
    anwesenden Arbeiter, die unter Umständen von Einsatz zu Einsatz ändern kann.

  - Beachte das Feld **Workflow** : jeder Termin steht zunächst im Status "Vorschlag" bzw.
    "Geplant", und man muss auf :guilabel:`☑` klicken, damit er in den Zustand
    "Stattgefunden" wechselt. Ansonsten erstellt Lino keine Rechnung.

- :kbd:`Escape` um auf den Auftrag zurück zu springen.

- Auf |basket| klicken um einen **Fakturierungsplan** für diesen Auftrag zu
  starten.
  Ein Fakturierungsplan ist, wenn ein Benutzer plant, eine Serie von Rechnungen erstellen zu lassen.
  Lino zeigt hier normalerweise einen Vorschlag an.

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

Lino kann Terminvorschläge automatisch generieren lasen.

- Gehe auf den Auftrag und aktiviere den Reiter "Kalender"

- Fülle die Felder aus, die die Kriterien definieren zum Erstellen der Terminserie:

  - "Beginnt am", "Beginnt um" und "Endet um" : wann der erste Einsatz stattfinden soll
  - Achtung: "Enddatum" sollte immer frei sein ausser bei Terminen, die mehrere Tage dauern
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

Automatikfakturierung
=====================

Lino fakturiert immer alle stattgefundenen Termine eines Auftrags (die noch
nicht fakturiert sind).

Falls ein Termin nicht fakturiert werden soll:

- Den Termin löschen
- Status auf "Abgesagt" (⚕) oder "Verpasst" (☉) setzen

Falls nötig könnten wir einen globalen Parameter definieren "Termine vor diesem
Datum nicht fakturieren"


Aufträge drucken
================

Auf den Button `printer` klicken.  Lino öffnet dann das druckbare PDF-Dokument
in einem neuen Browserfenster. Beim ersten Mal muss der Browser gesagt
bekommen, dass Lino neue enster öffnen darf.

Inhalt und Layout des gedruckten Dokuments sind noch zu besprechen.