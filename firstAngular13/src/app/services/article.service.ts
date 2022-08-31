import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Article } from '../models/article.model';
const baseUrl = 'http://localhost:8080/articles';

@Injectable({
  providedIn: 'root'
})
export class ArticleService {
  constructor(private http: HttpClient) { }
  getAll(): Observable<Article[]> {
    return this.http.get<Article[]>(`${baseUrl}`);
  }

  get(id: any): Observable<Article> {
    return this.http.get<Article>(`${baseUrl}/${id}`);
  }
  create(data: any): Observable<Article[]> {
    return this.http.post<Article[]>(`${baseUrl}`, data);
  }
  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }
  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }
  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }
  findByTitle(title: any): Observable<Article[]> {
    return this.http.get<Article[]>(`${baseUrl}?title=${title}`);
  }
}
