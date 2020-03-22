import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { SourceService } from '../source.service';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss']
})
export class DetailComponent implements OnInit {

  article: {} = {};

  constructor(private sourceService: SourceService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
      this.route.paramMap.subscribe(params => {
        this.loadArticle(params.get('id'));
      });
  }

  loadArticle(name: string) {
    this.sourceService.getArticle('assets/data/content/' + name).subscribe((resp: any) =>
      {
          this.article = resp;
      }
    );
  }

}
