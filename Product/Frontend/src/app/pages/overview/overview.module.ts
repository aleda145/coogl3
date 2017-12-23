import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';
import { OverviewChartjsPieComponent } from './overview-components/rec-chartjs-pie.component';


import { ThemeModule } from '../../@theme/theme.module';
import { OverviewComponent } from './overview.component';
import { OverviewRoutingModule, routedComponents } from './overview-routing.module';
import {ComponentsModule} from '../components/components.module';
import { OverviewD3BarComponent } from './overview-components/overview-d3-bar.component';


const components = [
    OverviewD3BarComponent,
    OverviewChartjsPieComponent,
];
@NgModule({
  imports: [ComponentsModule, ThemeModule, AngularEchartsModule, NgxChartsModule, ChartModule, OverviewRoutingModule,
  ],
  declarations: [OverviewComponent , ...routedComponents, ...components],
  entryComponents: [
  ],
})
export class OverviewModule {}
