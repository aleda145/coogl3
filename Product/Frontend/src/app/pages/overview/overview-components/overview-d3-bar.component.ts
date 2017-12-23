import { Component, OnDestroy, OnInit, Input } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { OverviewComponent } from '../overview.component'
import { DataHandlerService} from '../../../@core/data/data-handler.service';


/*
  Author: Anton Bergström, Ariyan Abdulla, Erik Thörngren
  Date: 2017-10-12
  Last update: 2017-11-24 by Ariyan & Anton
  This contains the typescript code for the graphs on the overview page.
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
export class OverviewD3BarComponent implements OnDestroy, OnInit {
  @Input() factor: number;
  movies: string[];
  data: any;
  results = [];
  showLegend = false;
  showXAxis = true;
  showYAxis = true;
  xAxisLabel = 'movies';
  yAxisLabel = 'recommended';
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
    Author: Anton Bergström, Ariyan Abdulla, Erik Thörngren
    Date: 2017-11-24
    Last update: 2017-11-24 by Erik & Ariyan
    This function gets the required data from the APIManager.
  */
  private getData() {
    if (this.factor === 1) {
      this.dataHandlerService.getData().subscribe((data) => {
        this.movies = data.recommendation_list;
        const realName = [];
        for (let i = 0; i < this.movies.length; ++i) {
        const newName = {
          name: this.movies[i]['title'],
          value: this.movies[i]['timesRecommended'],
        };
        realName.push(newName);
      }
      this.results = realName;
      }); // Converts the data making it reachable in the htm file
    }
    if (this.factor === 2) {
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
      }); // Converts the data making it reachable in the htm file
    }
  }
   extractData() {
    return null;
  }


  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }
}
