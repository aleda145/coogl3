import { Component, OnDestroy, OnInit, Input } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { TrendingComponent } from '../trending.component'
import { DataHandlerService} from '../../../@core/data/data-handler.service';

/*
  Author: Anton Bergström & Ariyan Abdulla
  Date: 2017-09-30
  Last update: 2017-11-17 by Ariyan & Anton
  This contains the typescript code for the graphs on the trending page.
*/

@Component({
  selector: 'ngx-d3-bar',
  template: `
    <ngx-charts-bar-vertical
      [scheme]="colorScheme"
      [results]="results"
      [xAxis]="showXAxis"
      [yAxis]="showYAxis"
      [legend]="showLegend"
      [xAxisLabel]="xAxisLabel"
      [yAxisLabel]="yAxisLabel">
    </ngx-charts-bar-vertical>
  `,
})
export class TrendingD3BarComponent implements OnDestroy, OnInit {
  @Input() factor: number;
  movies: string[];
  data: any;
  results = [];
  showLegend = false;
  showXAxis = true;
  showYAxis = true;
  xAxisLabel = 'Title';
  yAxisLabel = 'Score';
  colorScheme: any;
  themeSubscription: any;

  constructor(private theme: NbThemeService, private dataHandlerService: DataHandlerService) {
    this.themeSubscription = this.theme.getJsTheme().subscribe(config => {
      const colors: any = config.variables;
      this.colorScheme = {
        domain: [colors.primaryLight, colors.infoLight, colors.successLight, colors.warningLight, colors.dangerLight],
      };
    });
  }

  ngOnInit() {
    this.getData();
    this.extractData();
  }

  /*
    Author: Anton Bergström & Ariyan Abdulla
    Date: 2017-10-29
    Last update: 2017-11-17 by Ariyan & Anton
    This contains the code which gets the required data from APIManager to the trending page.
  */

  public getData() {
      if (this.factor === 1) {
        this.dataHandlerService.getTrendingData().subscribe((data) => {
      this.movies = data.trendingMovies;

      const realName = [];
        for (let i = 0; i < this.movies.length; ++i) {
        const newName = {
          name: this.movies[i]['title'],
          value: this.movies[i]['score'],
        };
        realName.push(newName);
      }
      this.results = realName;
    });

      }
      if (this.factor === 2) {
        this.dataHandlerService.getYoutubeData().subscribe((data) => {
      this.movies = data.youtubeMovies;

      const realName = [];
        for (let i = 0; i < this.movies.length; ++i) {
        const newName = {
          name: this.movies[i]['title'],
          value: this.movies[i]['score'],
        };
        realName.push(newName);
      }
      this.results = realName;
    });

      }
      if (this.factor === 3) {
        this.dataHandlerService.getTwitterData().subscribe((data) => {
      this.movies = data.twitterMovies;

      const realName = [];
        for (let i = 0; i < this.movies.length; ++i) {
        const newName = {
          name: this.movies[i]['title'],
          value: this.movies[i]['score'],
        };
        realName.push(newName);
      }
      this.results = realName;
    });

      }
      // Converts the data making it reachable in the htm file
  }
   extractData() {
    return null;
  }


  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }
}
