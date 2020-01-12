# bauchbinde
Bauchbinden-Generator für den Raspberry-Pi

## Installation

- Die Dateien aus `cgi-bin/` nach `/usr/lib/cgi-bin/` kopieren und .cgi-Dateien ausführbar machen.
- Die Dateien `www/` in den Webroot kopieren (normalerweise /var/www).

Zum Darstellen der Bauchbinde muss ein Browser im Fullscreen automatisch nach dem Login gestartet werden:

```
midori -e Fullscreen -a http://localhost/cgi-bin/showip.cgi
```

Für das LXDE gibt es eine Autostart-Datei (`autostart`), die man nach `/etc/xdg/lxsession/LXDE/autostart` kopieren kann.

