import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { TrendingRoutingModule, routedComponents } from './trending-routing.module';


import { TrendingD3BarComponent } from './trending-components/trending-d3-bar.component';

import {ComponentsModule} from '../components/components.module';


const components = [
  TrendingD3BarComponent,
];

@NgModule({
  imports: [ComponentsModule, ThemeModule, TrendingRoutingModule, AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class TrendingModule {}
