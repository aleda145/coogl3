import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RecommendedComponent } from './recommended.component';

const routes: Routes = [{
  path: '',
  component: RecommendedComponent,
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class RecommendedRoutingModule { }

export const routedComponents = [
  RecommendedComponent,
];
