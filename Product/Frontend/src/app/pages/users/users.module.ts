import { NgModule } from '@angular/core';
import { AngularEchartsModule } from 'ngx-echarts';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ChartModule } from 'angular2-chartjs';

import { ThemeModule } from '../../@theme/theme.module';

import { UsersRoutingModule, routedComponents } from './users-routing.module';
import { UsersD3BarComponent } from './users-components/users-d3-bar.component';
import { UsersD3LineComponent } from './users-components/users-d3-line.component';
import { UsersD3PieComponent } from './users-components/users-d3-pie.component';
import { UsersD3AreaStackComponent } from './users-components/users-d3-area-stack.component';
import { UsersD3PolarComponent } from './users-components/users-d3-polar.component';
import { UsersD3AdvancedPieComponent } from './users-components/users-d3-advanced-pie.component';

import {ComponentsModule} from '../components/components.module';



const components = [
  UsersD3BarComponent,
  UsersD3LineComponent,
  UsersD3PieComponent,
  UsersD3AreaStackComponent,
  UsersD3PolarComponent,
  UsersD3AdvancedPieComponent,
];

@NgModule({
  imports: [ComponentsModule, ThemeModule, UsersRoutingModule, AngularEchartsModule, NgxChartsModule, ChartModule],
  declarations: [...routedComponents, ...components],
})
export class UsersModule {}
