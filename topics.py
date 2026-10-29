# Fachmodule aus KI-Lehrling_v2.1, Stand 29.10.2026
TOPICS = {
    "Elektrotechnikrecht": {
        "icon":"⚖️",
        "subtitle":"Grundzüge des Elektrotechnikrechts",
        "competencies":[
            "Fünf Sicherheitsregeln korrekt anwenden",
            "Laie, elektrotechnisch unterwiesene Person und Elektrofachkraft unterscheiden",
            "ETG, ETV und ESV grundsätzlich einordnen",
            "TAEV und Normen voneinander abgrenzen",
            "Praxisfälle sicherheits- und rollenbezogen beurteilen",
        ],
        "module_prompt": """
FACHMODUL: ELEKTROTECHNIKRECHT
Behandle fünf Sicherheitsregeln, ETG, ETV, ESV, TAEV, Personenrollen und relevante Grundlagen aus EN 50110-1.
Keine reale Arbeitsfreigabe. Keine konkrete Anlage als sicher erklären.
DIAGNOSE: Sicherheitsregeln, Personenrollen, Elektrofachkraft, ETG/ETV/ESV, kurzer Praxisfall.
Nutze realistische Fälle aus Werkstatt, Schaltschrank, Teamarbeit und Netzanschluss.
"""
    },
    "Ohmsches Gesetz": {
        "icon":"🔌",
        "subtitle":"Spannung, Strom und Widerstand",
        "competencies":[
            "U, I und R unterscheiden",
            "Ohmsches Gesetz korrekt anwenden",
            "Formeln umstellen",
            "Einheiten korrekt verwenden",
            "Ergebnisse plausibilisieren",
            "Praxisfälle übertragen",
        ],
        "module_prompt": """
FACHMODUL: OHMSCHES GESETZ
Behandle U=R*I, Formelzeichen, Einheiten, Umstellen, mA/A, kOhm/Ohm und Plausibilität.
DIAGNOSE: Größen, Einheiten, einfache Berechnung, Formel umstellen, Plausibilität.
Immer zuerst eigenen Rechenansatz verlangen.
"""
    },
    "Reihen- und Parallelschaltung": {
        "icon":"🧩",
        "subtitle":"Widerstände in Schaltungen",
        "competencies":[
            "Reihen- und Parallelschaltung unterscheiden",
            "Gesamtwiderstand bestimmen",
            "Stromverteilung verstehen",
            "Spannungsverteilung verstehen",
            "Formel passend auswählen",
            "Ergebnisse plausibilisieren",
        ],
        "module_prompt": """
FACHMODUL: REIHEN- UND PARALLELSCHALTUNG
Behandle Schaltungsart, Gesamtwiderstand, Strom, Spannung und Ohmsches Gesetz im Zusammenhang.
DIAGNOSE: Schaltungsart, gleiche/verteilte Größen, Gesamtwiderstand qualitativ, einfache Berechnung, Praxiswirkung.
Zuerst Schaltung verstehen, dann rechnen.
"""
    },
    "Elektrische Messtechnik": {
        "icon":"📏",
        "subtitle":"Spannung, Strom und Widerstand messen",
        "competencies":[
            "Messgröße passend auswählen",
            "Spannungsmessung korrekt einordnen",
            "Strommessung korrekt einordnen",
            "Widerstandsmessung sicher einordnen",
            "Messbereich und Einheit beachten",
            "Messfehler erkennen",
        ],
        "module_prompt": """
FACHMODUL: ELEKTRISCHE MESSTECHNIK
Behandle Spannungs-, Strom- und Widerstandsmessung, Anschlussart, Messbereich, Einheit und typische Fehler.
Keine reale Arbeitsfreigabe.
DIAGNOSE: Spannung messen, Strom messen, Widerstand messen, Fehlanschluss, Messfall beurteilen.
"""
    },
}
