# KI-Lehrling v2.2 – Extended 1 (TESTVERSION)

Adaptiver Lernassistent für Elektrotechnik mit **optionalem LEO-Konferenzmodus**.

## Enthalten

- `app.py`: Hauptanwendung mit Diagnose, Hilfe-Stufen, Lehrlingskarte und begrenztem Chat
- `topics.py`: vier voneinander getrennte Lernmodule aus dem öffentlichen 2.1-Repository
- `conference_mode.py`: Konferenzregie, Beameransicht, Offline-Ersatzantworten, optional Live-KI
- `requirements.txt`: Python-Abhängigkeiten
- `secrets.example.toml`: Platzhalter für Streamlit-Secrets – niemals echte Schlüssel committen
- `tests/test_structure.py`: einfache Offline-Prüfung von Syntax und Modulstruktur

## Installation auf GitHub + Streamlit Cloud

1. **Neuen Branch** `v2.2-extended-1` im bestehenden Repository erstellen. `main` unverändert lassen.
2. Alle Dateien aus diesem Verzeichnis **in die Wurzel** des Branches hochladen; Verzeichnisstruktur beibehalten.
3. In Streamlit Community Cloud **eine eigene Test-App** aus diesem Branch mit `app.py` als Entry-Point anlegen.
4. Im Streamlit-Cloud-Menü unter **Secrets** den Inhalt aus `secrets.example.toml` mit echten Werten (insbesondere `API_KEY`, `CONFERENCE_KEY`) hinterlegen. Nicht in das Repository hochladen.
5. Normale App über die Standard-URL öffnen und alle vier Themen testen.
6. Konferenzregie über `?conference=1&key=DEIN_CONFERENCE_KEY` öffnen.
7. Beamer über `?conference=1&view=beamer&key=DEIN_CONFERENCE_KEY` in einem zweiten Fenster öffnen. Beide Fenster müssen dieselbe App-Instanz und denselben `room` verwenden.
8. Vor dem Vortrag mehrere vollständige Probedurchläufe durchführen; währenddessen nicht neu deployen.

## Lokaler Start

```bash
python -m pip install -r requirements.txt
mkdir -p .streamlit
# secrets.example.toml als .streamlit/secrets.toml kopieren und echte Werte einsetzen
streamlit run app.py
```

## Sicherheit und Grenzen

- Der Konferenzmodus ist standardmäßig **gesperrt**, bis `CONFERENCE_KEY` gesetzt ist.
- Die Zugangsdaten in der URL können in Browserhistorie oder beim Teilen von Links sichtbar werden. Für produktive Zugriffsverwaltung wäre eine echte Anmeldung bzw. separate Autorisierung nötig.
- Alle Personen mit dem Konferenzschlüssel können derzeit die Regie öffnen. Beameransicht ist nicht auf eine eigene Leseberechtigung begrenzt.
- Der gemeinsame Konferenzzustand liegt im Serverarbeitsspeicher und geht bei Neustart/Redeploy verloren; mehrere getrennte Server-Replikate können getrennte Zustände besitzen.
- Die Offline-Option bezieht sich ausschließlich auf vorbereitete Konferenzantworten; die reguläre Lernanwendung benötigt `API_KEY` und eine Verbindung zum Modellanbieter.
- Lernstände sind nur sitzungsbezogen und nicht als überprüfte Noten oder formelle Kompetenznachweise zu verwenden.
- `MODEL`, `REASONING_EFFORT` und Groq-Kompatibilität müssen im laufenden Betrieb überprüft werden.
- Kein Lehrkräfte-Upload, Schülerlogin, dauerhafte Speicherung oder Dashboard enthalten.

## Stand der Prüfung

**Statischer Syntax- und Strukturtest bestanden**; ein echter Live-Test auf Streamlit Cloud, inklusive Groq-Anbindung und gleichzeitiger Bedienung von Regie/Beamer, steht noch aus. Nicht ungeprüft als produktive Schulplattform einsetzen.

## Änderungen gegenüber Claude-Code

- `app.py`: Bei `?conference=1` ist nun ein gesetztes `CONFERENCE_KEY` verpflichtend; die ursprüngliche Konferenzschlüssel-Prüfung ließ andernfalls jeden Besucher zu.
- `topics.py`: anhand der öffentlichen Version 2.1 vom 29.10.2026 übernommen.
- `conference_mode.py`: unverändert aus dem vom Nutzer bereitgestellten Claude-Code.
