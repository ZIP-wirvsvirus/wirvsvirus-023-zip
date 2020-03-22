""" from https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json """
from datetime import datetime
import requests

from crawler.Crawler import Crawler
from database.models import NewsEntry

URL = "https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json"


class BundCrawler(Crawler):
    def __init__(self):
        self.result = []

    def __collect(self):
        resp = requests.get(url=URL)
        return resp.json()

    def __buildNewsEntry(self, json_news_entry):
        # TODO error handling...
        identifier = json_news_entry["identifier"]
        source = "warnung_bund"
        query_url = URL
        # stupid python ignoring rfc 3339... :
        sent = json_news_entry['sent'][:-5] + json_news_entry['sent'][-5:].replace(":", "")
        created = datetime.strptime(sent, '%Y-%m-%dT%H:%M:%S%z')
        last_update = datetime.now()
        content = json_news_entry
        area = ""
        try:
            area = json_news_entry['info'][0]['area']['areaDesc']
        except:
            # TODO
            pass
        category = json_news_entry['info'][0]['category']
        tags = 'TODO'
        return NewsEntry(identifier=identifier, source=source, query_url=query_url, created=created,
                         last_update=last_update, content=content, area=area, category=category, tags=tags)

    def collect_and_commit(self, database):
        try:
            data = self.__collect()
            for entry in data:
                database.session.add(self.__buildNewsEntry(entry))
            database.session.commit()
        except Exception as ex:
            # TODO handle error correctly
            print(ex)  # database commit failed...
            raise ex
