# IHKrus
Ein einfaches mitmproxy-Addon, das automatisch die ~besch...~ unpraktischen Checkboxen im IHK Online-Berichtsheft checkt.
Warum? Die Checkboxen sind:
- immer in einer anderen Reihenfolge (manchmal alphabetisch geordnet, manchmal nicht)
- langsam
- mit Text in Schriftgröße 1 oder so beschrieben.

## Wie benutze ich das?
Du musst mitmproxy und sein Zertifikat installieren. Dann routest du deinen HTTP-Traffic durch den Port, auf dem
dein mitmproxy laufen soll (indem du z.B. deine Proxy-Einstellungen änderst). Anschließend startest du mitmproxy
mit dem Addon so: `mitmproxy -s addon.py`

Gegebenenfalls musst du die IDs der Checkboxen anpassen, damit sie auch für dich stimmen.

Hört sich zu schwierig an? Ich sag dir was. Mitmproxy auf meinem Arbeits-PC aufzusetzen, die HTTP-Anfragen anzuschauen
und das Script zu schreiben ging schneller, als eine Woche in dem Berichtsheft manuell abzugeben. Also probier's mal aus.

![](https://i.imgur.com/i4h3LLl.png)
