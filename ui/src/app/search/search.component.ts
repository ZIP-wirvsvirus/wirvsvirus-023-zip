import { Component, OnInit } from '@angular/core';
import { SourceService } from '../source.service';

import FuzzySearch from 'fuzzy-search';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  filters: string[] = [];
  selectedFilters: string[] = [];

  loadedFilters: string[] = [];
  loadedArticles: {}[] = [];

  previewArticles: {}[] = [];

  constructor(private sourceService: SourceService) { }

  ngOnInit(): void {
    this.loadFilters();
    this.loadArticles();
  }

  loadFilters() {
    this.sourceService.getFilters().subscribe((resp: any) =>
      {
          this.loadedFilters = resp['filters'];
          this.initFilters();
      }
    );
  }

  initFilters() {
    let me = this;
    this.loadedFilters.forEach(function (value: string) {
        me.filters.push(value);
    });

    this.filters = this.filters.filter((item, i, ar) => ar.indexOf(item) === i); //make it unique
    this.filters.sort(); // make it sorted
  }

  loadArticles() {
    this.loadArticle('assets/data/content/DE-BB-EW-SE079-20200318-79-001.json');
    this.loadArticle('assets/data/content/DE-BB-EW-SE079-20200318-79-002.json');
    this.loadArticle('assets/data/content/DE-BW-FR-W022-20200310-000.json');
    this.loadArticle('assets/data/content/DE-BW-FR-W022-20200317-000.json');
    this.loadArticle('assets/data/content/DE-BW-KN-W131-20200316-000.json');
    this.loadArticle('assets/data/content/DE-BW-RT-SE050-20200320-50-000.json');
    this.loadArticle('assets/data/content/DE-BW-S-SE018-20200321-18-000.json');
    this.loadArticle('assets/data/content/DE-BY-A-W083-20200317-000.json');
    this.loadArticle('assets/data/content/DE-BY-CO-W141-20200320-001.json');
    this.loadArticle('assets/data/content/DE-BY-M-W060-20200316-000.json');
    this.loadArticle('assets/data/content/DE-BY-M-W060-20200320-000.json');
    this.loadArticle('assets/data/content/DE-BY-M-W150-20200319-000.json');
    this.loadArticle('assets/data/content/DE-BY-TS-W135-20200316-000.json');
    this.loadArticle('assets/data/content/DE-BY-WEN-W130-20200313-000.json');
    this.loadArticle('assets/data/content/DE-BY-WEN-W130-20200318-000.json');
    this.loadArticle('assets/data/content/DE-MV-SN-SE024-20200320-24-000.json');
    this.loadArticle('assets/data/content/DE-MV-SN-SE024-20200320-24-001.json');
    this.loadArticle('assets/data/content/DE-MV-SN-SE024-20200320-24-002.json');
    this.loadArticle('assets/data/content/DE-NI-BS-W091-20200313-000.json');
    this.loadArticle('assets/data/content/DE-NI-STD-SE029-20200318-29-000.json');
    this.loadArticle('assets/data/content/DE-NW-BN-SE030-20200320-30-001.json');
    this.loadArticle('assets/data/content/DE-NW-BN-SE030-20200320-30-003.json');
    this.loadArticle('assets/data/content/DE-NW-BN-SE030-20200320-30-004.json');
    this.loadArticle('assets/data/content/DE-NW-BO-SE077-20200319-77-001.json');
    this.loadArticle('assets/data/content/DE-NW-DU-SE038-20200314-38-000.json');
    this.loadArticle('assets/data/content/DE-NW-DU-SE038-20200318-38-001.json');
    this.loadArticle('assets/data/content/DE-NW-EN-SE069-20200320-69-000.json');
    this.loadArticle('assets/data/content/DE-NW-ERK-SE056-20200303-56-000.json');
    this.loadArticle('assets/data/content/DE-NW-LIP-SE041-20200314-41-002.json');
    this.loadArticle('assets/data/content/DE-NW-MH-SE065-20200316-65-000.json');
    this.loadArticle('assets/data/content/DE-NW-OE-SE086-20200320-86-001.json');
    this.loadArticle('assets/data/content/DE-NW-SO-SE089-20200314-89-000.json');
    this.loadArticle('assets/data/content/DE-NW-SO-SE089-20200320-89-000.json');
    this.loadArticle('assets/data/content/DE-NW-ST-SE032-20200320-32-000.json');
    this.loadArticle('assets/data/content/DE-NW-UN-SE068-20200314-68-000.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200314-97-000.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200316-97-000.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200317-97-000.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200317-97-001.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200318-97-001.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200318-97-004.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200319-97-000.json');
    this.loadArticle('assets/data/content/DE-NW-WES-SE097-20200321-97-000.json');
    this.loadArticle('assets/data/content/DE-RP-LU-SE005-20200320-5-000.json');
    this.loadArticle('assets/data/content/DE-RP-MZ-SE003-20200320-3-000.json');
    this.loadArticle('assets/data/content/DE-SH-EH-SE028-20200315-28-000.json');
    this.loadArticle('assets/data/content/DE-SL-SB-SE023-20200316-23-000.json');
    this.loadArticle('assets/data/content/DE-ST-MD-SE022-20200320-22-000.json');
    this.loadArticle('assets/data/content/DE-TH-HIG-W111-20200321-001.json');
  }

  loadArticle(name: string) {
    this.sourceService.getArticle(name).subscribe((resp: any) =>
      {
          resp.sourceName = name.split("assets/data/content/")[1];
          this.loadedArticles.push(resp);
          this.previewArticles.push(resp);
      }
    );
  }

  toggleFilter(filter: string): void {
    if(this.selectedFilters.includes(filter)) {
        this.selectedFilters = this.selectedFilters.filter(item => item !== filter)
        this.filters.push(filter);
    } else {
        this.filters = this.filters.filter(item => item !== filter)
        this.selectedFilters.push(filter);
    }
    this.filters = this.filters.filter((item, i, ar) => ar.indexOf(item) === i); //make it unique
    this.filters.sort(); // make it sorted

    this.selectedFilters = this.selectedFilters.filter((item, i, ar) => ar.indexOf(item) === i); //make it unique
    this.selectedFilters.sort(); // make it sorted
  }

  onKey(event: any): void {
    this.previewArticles = [];
    const searcher = new FuzzySearch(this.loadedArticles, ['headline', 'content'], {
      caseSensitive: true,
    });
    const result = searcher.search(event.target.value);

    setTimeout(() => {  this.previewArticles = result; }, 1000); //simulate loading

  }

}
