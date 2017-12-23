import { Component, OnInit } from '@angular/core';

import { DataHandlerService} from '../../@core/data/data-handler.service';

/*
  Author: Anton Bergström, Ariyan Abdulla, David Schutzer, Elvin Granat
  Date: 2017-09-30
  Last update: 2017-11-17 by Anton & Ariyan
  This contains the different components used on the trending page.
*/

@Component({
  selector: 'ngx-trending',
  styleUrls: ['./trending.component.scss'],
  templateUrl: './trending.component.html',
})
export class TrendingComponent implements OnInit {
  trendingMovies: string[];
  youtubeMovies: string[];
  twitterMovies: string[];
  dataTrending: any;
  dataYoutube: any;
  dataTwitter: any;
  modalHeader1 = 'Graph for the combined trending content';
  modalHeader2 = 'Graph for the Youtube trending content';
  modalHeader3 = 'Graph for the Twitter trending content';
  modalContent1 = `This graph shows the top trending movies and their score produced by Coogl3's algorithm.
  This score is the sum of the normalized Youtube and Twitter scores. This score is normalized from 0 to
  1 where 1 is the most trending movie. Each bar shows the score for a specific movie
  which means that the higher the score a movie has the more trending it is.
  Basically this graphs shows what movies are trending the most.`;
  modalContent2 = `This graph shows the top Youtube trending movies and their score produced by Coogl3's algorithm.
  By looking at this graph one
  can determine how much a movie is trending on Youtube
  however these values are not normalized.
  `;
  modalContent3 = `This graph shows the top Twitter trending movies and their score produced by Coogl3's algorithm.
  By looking at this graph one
  can determine how much a movie is trending on Twitter
  however these values are not normalized.`;

    constructor(private dataHandlerService: DataHandlerService) { }

    ngOnInit() {
        this.getTrendingData();
        this.extractTrendingData();
        this.getYoutubeData();
        this.extractYoutubeData();
        this.getTwitterData();
        this.extractTwitterData();

    }
    getTrendingData() {
      this.dataHandlerService.getTrendingData().subscribe((data) => {
        this.dataTrending = data;
        // console.log(this.data); not allowed by lint ?
      });
    }
    getYoutubeData() {
    this.dataHandlerService.getYoutubeData().subscribe((data) => {
      this.dataYoutube = data;
      // console.log(this.data); not allowed by lint ?
    }); // Converts the data making it reachable in the htm file
  }
  getTwitterData() {
    this.dataHandlerService.getTwitterData().subscribe((data) => {
      this.dataTwitter = data;
      // console.log(this.data); not allowed by lint ?
    }); // Converts the data making it reachable in the htm file
  }
    extractTrendingData() {
      return null;
    }
    extractYoutubeData() {
    return null;
  }
   extractTwitterData() {
    return null;
  }
}
