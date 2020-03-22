Backend for wirvsvirus-023-zip
---
enthält angular sourcecode von `git@github.com:nbartel/team023zip.git` als submodule

Einbindung:
```
git submodule init
git submodule update
npm install
ng build
pip3 install -r requirements.txt
```
danach muss noch die ENV-Variable `DATABASE_URL` auf eine (postgresql) Datenbank gesetzt werden und dann kann die Anwendung entweder über die app.py, über die entsprechenden flask-Befehle oder über gunicorn gestartet werden.

---
### Bis jetzt / TODO:
- Crawler muss über `<url>/do_crawl` angestoßen werden und füllt dann die Datenbank (bisher nur warnung-bund und bei mehrfachem aufruf auch entsprechend doppelt / mit Fehlern)
- über `<url>/api/query` können die Ergebnisse zurückgegeben werden, filter sind per GET oder POST zu übergeben.
- Datenbankmodel muss noch mal angepackt werden!
- Anbindung Frontend zu query-api fehlt noch

--- 
### Deployment mit Heroku:
- heroku projekt erstellen
- heroku-postgresql-addon hinzufügen
- sicherstellen, dass im Hauptprojekt `DATABASE_URL` korrekt gesetzt wurde 
- tabelle erstellen: (ACHTUNG, die Tabellenstruktur ist bisher alles andere als final )
````
create table news_entry
(
    news_id     serial    not null
        constraint news_entry_pk
            primary key,
    source      text,
    query_url   text      not null,
    created     timestamp not null,
    last_update timestamp not null,
    content     json,
    area        text,
    category    text      not null,
    tags        json,
    identifier  text
);

create unique index news_entry_news_id_uindex
    on news_entry (news_id);

```
- projekt zum entsprechenden heroku git push 