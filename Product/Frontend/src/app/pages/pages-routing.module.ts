import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { OverviewComponent } from './overview/overview.component';
import { UsersComponent } from './users/users.component';
import { UserComponent } from './user/user.component';
import { TrendingComponent} from './trending/trending.component';
import { RecommendedComponent } from './recommended/recommended.component';

import { AuthGuard } from './authentication/_guards/index';
import {LoginComponent} from './authentication/login/index';

const routes: Routes = [{
  path: '',
  component: PagesComponent,
    children: [{
    path: 'overview',
    component: OverviewComponent,
    canActivate: [AuthGuard],
  }, {
    path: 'login', component: LoginComponent,
  }, {
    path: 'performance',
    component: RecommendedComponent,
    canActivate: [AuthGuard],
  }, {
    path: 'recommendations',
    component: UsersComponent,
    canActivate: [AuthGuard],
  }, {
    path: 'user',
    component: UserComponent,
    canActivate: [AuthGuard],
  }, {
    path: 'trending',
    component: TrendingComponent,
    canActivate: [AuthGuard],
    }, {
    path: 'content',
    loadChildren: './content/content.module#ContentModule',
  }, {
    path: '',
    redirectTo: 'overview',
    pathMatch: 'full',
  }],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PagesRoutingModule {
}
