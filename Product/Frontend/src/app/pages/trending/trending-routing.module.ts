import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TrendingComponent } from './trending.component';

const routes: Routes = [{
  path: '',
  component: TrendingComponent,
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TrendingRoutingModule { }

export const routedComponents = [
  TrendingComponent,
];
