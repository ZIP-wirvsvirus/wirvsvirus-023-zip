import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SourceService {

  constructor(private http: HttpClient) {}

  filters = 'assets/data/filters.json';

  getFilters() {
    return this.http.get(this.filters);
  }

  getArticle(filename: string) {
    return this.http.get(filename);
  }

}
