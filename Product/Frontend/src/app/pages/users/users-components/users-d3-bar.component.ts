import { Component, OnDestroy, OnInit, Input, EventEmitter } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { UsersComponent } from '../users.component'
import { DataHandlerService} from '../../../@core/data/data-handler.service';

/*
  Author: Anton Bergström & Ariyan Abdulla
  Date: 2017-09-30
  Last update: 2017-11-22 by Ariyan & Anton
  This contains the typescript code for the graphs on the recommendation page.
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
export class UsersD3BarComponent implements OnDestroy, OnInit {
  movies: string[];
  data: any;
  results = [];
  showLegend = false;
  showXAxis = true;
  showYAxis = true;
  xAxisLabel = 'movies';
  yAxisLabel = 'recomended';
  colorScheme: any;
  themeSubscription: any;
  @Input() args: any = {
    male: true,
    other: true,
    female: true,
    fromAge: 0 ,
    toAge: 200 ,
  };

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
  }

  /*
    Author: Anton Bergström, Ariyan Abdulla, Erik Thörngren
    Date: 2017-10-29
    Last update: 2017-11-23 by Ariyan, Erik
    This contains the code which gets the required data from APIManager to the recommendation page.
  */

  public getData() {
      this.dataHandlerService.getMetaRecommendationsData(
        this.args.fromAge, this.args.toAge, this.args.male,
        this.args.female, this.args.other,
      ).subscribe((data) => {
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

  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }
  public setData(data: any) {
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
  }
}
