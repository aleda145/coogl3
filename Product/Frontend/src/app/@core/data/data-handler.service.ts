import { Component, OnInit } from '@angular/core';
import { Injectable } from '@angular/core';
import {Http, RequestOptions, Response} from '@angular/http';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { Movie } from './movieClass';
import 'rxjs/add/operator/map';
import { environment } from '../../../environments/environment';
import { AuthenticationService } from '../../pages/authentication/_services';



@Injectable()
export class DataHandlerService {
  authService: AuthenticationService;
  headers: HttpHeaders;
  apiUrl: any = environment.apiUrl;
readonly ROOT_URL = this.apiUrl + '/v1/recommendations';
readonly ROOT_URLtrending = this.apiUrl + '/v1/trending';
readonly ROOT_URLyoutube = this.apiUrl + '/v1/youtubetrending';
readonly ROOT_URLtwitter = this.apiUrl + '/v1/twittertrending';
readonly ROOT_URLsimple = this.apiUrl + 'v1/simple-success';
readonly ROOT_URLaverage = this.apiUrl + 'v1/average-success';

  movies: Observable<Movie[]>;
  trendingMovies: Observable<Movie[]>;
  youtubeMovies: Observable<Movie[]>;
  twitterMovies: Observable<Movie[]>;
  simpleSuccess: Observable<Movie[]>;
  averageSuccess: Observable<Movie[]>;

  constructor(private http: HttpClient, authService: AuthenticationService) {
    this.headers = new HttpHeaders();
    this.authService = authService;
  }
  setHeaders() {
    this.headers = this.headers.set('Authorization', 'JWT ' + this.authService.token);
  }
  getData(): any {
    this.setHeaders();
    return this.http.get(this.ROOT_URL, {headers: this.headers}).map((res: Response) => res);
  }
  getTrendingData(): any {
    this.setHeaders();
    return this.http.get(this.ROOT_URLtrending,  {headers: this.headers}).map((res: Response) => res);
  }
  getYoutubeData(): any {
    this.setHeaders();
    return this.http.get(this.ROOT_URLyoutube,  {headers: this.headers}).map((res: Response) => res);
  }
  getTwitterData(): any {
    this.setHeaders();
    return this.http.get(this.ROOT_URLtwitter,  {headers: this.headers}).map((res: Response) => res);
  }
  getSimpleSuccessrate(): any {
    this.setHeaders();
    return this.http.get(this.ROOT_URLsimple,  {headers: this.headers}).map((res: Response) => res);
  }
  getAverageSuccessrate(): any {
    this.setHeaders();
    return this.http.get(this.ROOT_URLaverage,  {headers: this.headers}).map((res: Response) => res);
  }
  getMetaRecommendationsData(age_lower: number, age_upper: number,
                            male: boolean, female: boolean, other: boolean): any {
    this.setHeaders();
    let filter: string = '';
    filter += 'age_lower=' + age_lower.toString() + '&age_upper=' + age_upper.toString();
    if (male) { filter += '&male=1'; }
    if (other) {filter += '&other=1'; }
    if (female) {filter += '&female=1'; }

    return this.http.get(this.ROOT_URL + '/?' + filter,  {headers: this.headers}).map((res: Response) => res);
  }

}
