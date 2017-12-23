import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { RecommendedRoutingModule, routedComponents } from './recommended-routing.module';
import { RecommendedChartjsBarComponent } from './recommended-components/rec-chartjs-bar.component';
import { RecommendedChartjsLineComponent } from './recommended-components/rec-chartjs-line.component';
import { RecommendedChartjsPieComponent } from './recommended-components/rec-chartjs-pie.component';
import { RecommendedChartjsMultipleXaxisComponent} from './recommended-components/rec-chartjs-multiple-xaxis.component';
import { RecommendedChartjsBarHorizontalComponent} from './recommended-components/rec-chartjs-bar-horizontal.component';
import { RecommendedChartjsRadarComponent } from './recommended-components/rec-chartjs-radar.component';
// imports components
import {ComponentsModule} from '../components/components.module';
// Modals

const components = [
  RecommendedChartjsBarComponent,
  RecommendedChartjsLineComponent,
  RecommendedChartjsPieComponent,
  RecommendedChartjsMultipleXaxisComponent,
  RecommendedChartjsBarHorizontalComponent,
  RecommendedChartjsRadarComponent,
];

@NgModule({
  imports: [ ComponentsModule, ThemeModule, RecommendedRoutingModule,
    AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class RecommendedModule {}
