import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { UserRoutingModule, routedComponents } from './user-routing.module';

const components = [
  /*ExampleComponent*/
];

@NgModule({
  imports: [ThemeModule, UserRoutingModule, AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class UserModule {

}
