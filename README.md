###### Das Projekt ist tot und bevor dieses Repo und die Organisation dahinter komplett gelöscht werden, verweise ich auf den [Clone](https://github.com/ValorNaram/wirvsvirus-023-zip)

Backend for wirvsvirus-023-zip
---
Getting started:
```
npm install
ng build
pip3 install -r requirements.txt
```
danach muss noch die ENV-Variable `DATABASE_URL` auf eine (postgresql) Datenbank gesetzt werden und dann kann die Anwendung entweder über die app.py, über die entsprechenden flask-Befehle oder über gunicorn gestartet werden.

---
### Bis jetzt / TODO:
- Crawler muss über `<url>/do_crawl` angestoßen werden und füllt dann die Datenbank (bisher nur warnung-bund)
- über `<url>/api/query` können die Ergebnisse zurückgegeben werden, filter sind per GET oder POST zu übergeben.
- Datenbankmodel muss noch mal angepackt werden!
- Anbindung Frontend zu query-api fehlt noch

--- 
### Deployment mit Heroku:
- heroku Projekt erstellen
- heroku-postgresql-addon hinzufügen
- sicherstellen, dass im Hauptprojekt `DATABASE_URL` korrekt gesetzt wurde 
- Tabelle erstellen: (ACHTUNG, die Tabellenstruktur ist bisher alles andere als final )
````
create table news_entry
(
    source      text,
    query_url   text      not null,
    created     timestamp not null,
    last_update timestamp not null,
    content     text      not null,
    area        text,
    category    text      not null,
    tags        json,
    identifier  text      not null
        constraint news_entry_pk
            primary key,
    headline    text      not null
);

create unique index news_entry_identifier_uindex
    on news_entry (identifier);

```
- projekt zum entsprechenden heroku git push 
