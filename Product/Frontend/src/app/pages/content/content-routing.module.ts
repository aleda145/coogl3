import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ContentComponent } from './content.component';
import { ContentTableComponent } from './content-table/content-table.component';

const routes: Routes = [{
  path: '',
  component: ContentComponent,
  children: [{
    path: 'content-table',
    component: ContentTableComponent,
  }],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ContentRoutingModule { }

export const routedComponents = [
  ContentComponent,
  ContentTableComponent,
];
