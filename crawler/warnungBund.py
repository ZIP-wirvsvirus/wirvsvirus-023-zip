""" from https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json """
from datetime import datetime
import requests
from crawler.utils import Keywordgeneration
from crawler.Crawler import Crawler
from database.models import NewsEntry

URL = "https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json"
SOURCE_NAME = "Bundesamt für Bevölkerungsschutz und Katastrophenhilfe"


class BundCrawler(Crawler):
    def __init__(self):
        self.keywordgenerator = Keywordgeneration()
        self.result = []

    def __collect(self):
        resp = requests.get(url=URL)
        return resp.json()

    def __buildNewsEntry(self, json_news_entry):
        # TODO error handling...
        identifier = json_news_entry["identifier"]
        source = SOURCE_NAME
        query_url = URL
        # stupid python ignoring rfc 3339... :
        sent = json_news_entry["sent"][:-5] + json_news_entry["sent"][-5:].replace(":", "")
        created = datetime.strptime(sent, "%Y-%m-%dT%H:%M:%S%z")
        last_update = datetime.now()
        content = json_news_entry["info"][0]["description"]
        area = ""
        try:
            area = json_news_entry["info"][0]["area"][0]["areaDesc"]
        except:
            # TODO
            pass
        category = json_news_entry["info"][0]["category"]
        tags = self.keywordgenerator.generateKeyWords([content])
        headline = json_news_entry["info"][0]["headline"]
        return NewsEntry(identifier=identifier, source=source, query_url=query_url, created=created, headline=headline,
                         last_update=last_update, content=content, area=area, category=category, tags=tags)

    def collect_and_commit(self, database):
        try:
            data = self.__collect()
            for entry in data:
                database.session.merge(self.__buildNewsEntry(entry))
            database.session.commit()
        except Exception as ex:
            # TODO handle error correctly
            print(ex)  # database commit failed...
            raise ex
