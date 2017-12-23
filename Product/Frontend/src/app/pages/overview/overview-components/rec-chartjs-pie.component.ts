import { Component, OnDestroy } from '@angular/core';
import { NbThemeService } from '@nebular/theme';


/*
  Author: Anton Bergström & Ariyan Abdulla
  Date: 2017-10-08
  Last update: 2017-11-24 by Anton & Ariyan
  This contains the typescript code for the piechart on the overview page.
*/

@Component({
  selector: 'ngx-chartjs-pie',
  template: `
    <chart type="pie" [data]="data" [options]="options"></chart>
  `,
})
export class OverviewChartjsPieComponent implements OnDestroy {
  data: any;
  options: any;
  themeSubscription: any;

  constructor(private theme: NbThemeService) {
    this.themeSubscription = this.theme.getJsTheme().subscribe(config => {

      const colors: any = config.variables;
      const chartjs: any = config.variables.chartjs;

      this.data = {
        labels: ['5', '4', '3', '2', '1'],
        datasets: [{
          data: [50, 20, 10, 10, 10],
          backgroundColor: [colors.successLight, colors.dangerLight, '#FF3DD6', '#FFFE0F', '#4A5DFF'],
        }],
      };

      this.options = {
        maintainAspectRatio: false,
        responsive: true,
        scale: {
          pointLabels: {
            fontSize: 14,
            fontColor: chartjs.textColor,
          },
        },
        scales: {
          xAxes: [
            {
              display: false,
            },
          ],
          yAxes: [
            {
              display: false,
            },
          ],
        },
        legend: {
          labels: {
            fontColor: chartjs.textColor,
          },
        },
      };
    });
  }

  ngOnDestroy(): void {
    this.themeSubscription.unsubscribe();
  }
}
