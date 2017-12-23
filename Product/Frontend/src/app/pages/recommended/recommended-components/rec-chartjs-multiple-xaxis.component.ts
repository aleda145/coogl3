import { Component, OnDestroy, OnInit, Input } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { DataHandlerService} from '../../../@core/data/data-handler.service';

/*
  Author: Anton Bergström, Ariyan Abdulla & Erik Thörngren
  Date: 2017-09-30
  Last update: 2017-11-23 by Ariyan, Erik
  This contains the typescript code for the graph on the performance page.
*/

@Component({
  selector: 'ngx-chartjs-multiple-xaxis',
  template: `
    <chart type="line" [data]="data" [options]="options"></chart>
  `,
})
export class RecommendedChartjsMultipleXaxisComponent implements OnDestroy, OnInit {
  @Input() factor: number;
  data: {};
  movies: string[];
  movies1: string[];
  options: any;
  themeSubscription: any;

  constructor(private theme: NbThemeService, private dataHandlerService: DataHandlerService) {
    this.themeSubscription = this.theme.getJsTheme().subscribe(config => {

      const colors: any = config.variables;
      const chartjs: any = config.variables.chartjs;

      this.data = {
        labels: [],
        datasets: [{
          label: 'Success over time',
          data: [],
          borderColor: colors.successLight,
          backgroundColor: colors.successLight,
          fill: false,
          pointRadius: 8,
          pointHoverRadius: 10,
        }],
      };

      this.options = {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          position: 'bottom',
          labels: {
            fontColor: chartjs.textColor,
          },
        },
        hover: {
          mode: 'index',
        },
        scales: {
          xAxes: [
            {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Date',
              },
              gridLines: {
                display: true,
                color: chartjs.axisLineColor,
              },
              ticks: {
                fontColor: chartjs.textColor,
              },
            },
          ],
          yAxes: [
            {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Rate(%)',
              },
              gridLines: {
                display: true,
                color: chartjs.axisLineColor,
              },
              ticks: {
                fontColor: chartjs.textColor,
              },
            },
          ],
        },
      };
    });
  }

  ngOnInit() {
    this.getData();
    this.extractData();
  }

  /*
    Author: Anton Bergström, Ariyan Abdulla, Erik Törngren
    Date: 2017-11-24
    Last update: 2017-11-20 by Ariyan & Erik
    This contains the code which gets the required data from APIManager to the performance page.
  */

  getData() {
    if (this.factor === 1) {
      this.dataHandlerService.getAverageSuccessrate().subscribe((data) => {
        this.movies1 = data.averageSuccess;
        this.dataHandlerService.getSimpleSuccessrate().subscribe((data1) => {
          this.movies = data1.simpleSuccess;
          const timeName = [];
          const simpleName = [];
          const averageName = [];
        for (let i = 0; i < this.movies.length; ++i) {
          timeName.push(this.movies[i]['timestamp']);
          simpleName.push(100 * ( this.movies[i]['watched'] / ( this.movies[i]['watched'] + this.movies[i]
            ['not_watched'] ) ) );
          averageName.push(this.movies1[i]['average_user_success_rate']);
        }
          this.data = {
            labels: timeName,
            datasets: [{
              label: 'Success over time simple',
              data: simpleName,
              borderColor: '#FF3DD6',
              backgroundColor: '#ffffff',
              fill: false,
              pointRadius: 8,
              pointHoverRadius: 10,
            }, {
              label: 'Success over time average',
              data: averageName,
              borderColor: '#31ff1e',
              backgroundColor: '#ffffff',
              fill: false,
              pointRadius: 8,
              pointHoverRadius: 10,
            }],
          }
        });
      });
    }

  }
  extractData() {
    return null;
  }

  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }

  private random() {
    return Math.round(Math.random() * 100);
  }
}
