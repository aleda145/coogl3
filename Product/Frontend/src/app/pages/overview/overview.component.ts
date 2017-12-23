import { Component, OnInit } from '@angular/core';

import { User } from '../authentication/_models/index';
import { UserService } from '../authentication/_services/index';
import { DataHandlerService} from '../../@core/data/data-handler.service';


/*
  Author: Anton Bergström, Ariyan Abdulla, David Schutzer
  Date: 2017-09-30
  Last update: 2017-11-23 by Anton & Ariyan
  This contains the different components used on the overview page.
*/

@Component({
  selector: 'ngx-overview',
  styleUrls: ['./overview.component.scss'],
  templateUrl: './overview.component.html',
})
export class OverviewComponent implements OnInit {
  users: User[] = [];
  movies: string[];
  trendingMovies: string[];
  data: any;
  dataTrending: any;
  obj: any;
  modalHeader1 = 'Graph for the top recommended content';
  modalHeader2 = 'List for the top recommended content';
  modalHeader3 = 'Graph for the top trending content';
  modalHeader4 = 'List for the top trending content';
  modalContent1 = `This graph shows the number of times a movie has been recommended in total from Coogl3's algorithm.
  Each bar represent the number of times a specific movie has been recommended to all users.
  The movie that has been recommended the most is represented by the highest bar.\n
  A user
  will be recommended to a certain movie based on personal preferences and earlier watched movies
  and based on what content that is trending.`;
  modalContent2 = `This list shows the top recommended movies and their titles.
The first movie in the list is the movie that has been recommended the most.
A user
  will be recommended to a certain movie based on personal preferences and earlier watched movies
  and based on what content that is trending.
  The percentage value shows the rate of success for each movie,
meaning how many times a movie has been watched when recommended.
The higher the percentage, the higher the success rate is for that specific movie.
This can be of interest since it shows whether a recommended movie has been a successful recommendation.`;
  modalContent3 = `This graph shows the top trending movies and the score produced from Coogl3's algorithm.
  This score is normalized from 0 to 1 where 1 is the most trending movie. Each bar shows the score for a specific movie
  which means that the higher the score a movie has the more trending it is.
  Basically this graph shows what movies are trending the most.`;
  modalContent4 = `This list shows the top trending movies and their titles.
The first movie in the list is the one with the highest score.
The first movie on this list has the highest
trending score.`;

    constructor(private userService: UserService, private dataHandlerService: DataHandlerService) { }

    ngOnInit() {
        // get users from secure api end point
        this.userService.getUsers()
            .subscribe(users => {
                this.users = users;
            });
        this.getData();
        this.extractData();
        this.getTrendingData();
        this.extractTrendingData();
    }
    getTrendingData() {
      this.dataHandlerService.getTrendingData().subscribe((data) => {
        this.dataTrending = data;
        // console.log(this.data); not allowed by lint ?
      });
    }
    getData() {
    this.dataHandlerService.getData().subscribe((data) => {
      this.data = data;
      // console.log(this.data); not allowed by lint ?
    }); // Converts the data making it reachable in the htm file
  }
    extractTrendingData() {
      return null;
    }
    extractData() {
    return null;
  }
}
