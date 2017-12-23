import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { environment } from '../../../../environments/environment';

import { AuthenticationService } from '../_services/index';


@Component({
    moduleId: module.id,
    templateUrl: 'login.component.html',
})

export class LoginComponent implements OnInit {
    public token: string;
    model: any = {};
    loading = false;
    error = '';

    constructor(
        private router: Router,
        private authenticationService: AuthenticationService,
        private http: HttpClient) {
        // set token if saved in local storage
         }

    ngOnInit() {
        const currentUser = JSON.parse(localStorage.getItem('currentUser'));
        this.token = currentUser && currentUser.token;
        // reset login status
        this.authenticationService.logout();
    }

    login() {
        this.loading = true;
        const body = {'username': this.model.username, 'password': this.model.password}
        this.http.post(environment.apiUrl + 'v1/authenticate/', body).subscribe(
            response => {
                const token = response['token'];
                if (token) {
                    // set token property
                    this.token = token;
                    // store username and jwt token in local storage to keep user logged in between page refreshes
                    localStorage.setItem('currentUser',
                        JSON.stringify({ username: this.model.username, token: token }));
                    this.authenticationService.setToken(token)
                    this.router.navigate(['/']);
                }
            },
            (err: HttpErrorResponse) => {
                this.error = 'Username or password is incorrect';
                this.loading = false;
            },
        );
    }
}
