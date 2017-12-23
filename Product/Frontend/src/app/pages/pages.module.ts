import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { OverviewModule } from './overview/overview.module';
import { UsersModule } from './users/users.module';
import { UserModule } from './user/user.module';
import { TrendingModule } from './trending/trending.module';
import { RecommendedModule } from './recommended/recommended.module';
import { PagesRoutingModule } from './pages-routing.module';
import { ThemeModule } from '../@theme/theme.module';
import { ComponentsModule } from './components/components.module';

import {LoginComponent} from './authentication/login/index';
import { AuthGuard } from './authentication/_guards/index';
import { AuthenticationService, UserService } from './authentication/_services/index';

// used to create fake backend
import { fakeBackendProvider } from './authentication/_helpers/fake-backend';
import { MockBackend, MockConnection } from '@angular/http/testing';
import { BaseRequestOptions } from '@angular/http';

const PAGES_COMPONENTS = [
  PagesComponent,
];

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    OverviewModule,
    RecommendedModule,
    UsersModule,
    TrendingModule,
    UserModule,
    ComponentsModule,
  ],
  declarations: [
    ...PAGES_COMPONENTS,
    LoginComponent,
  ],
  providers: [
        AuthGuard,
        AuthenticationService,
        UserService,
        // providers used to create fake backend
        fakeBackendProvider,
        MockBackend,
        BaseRequestOptions,
    ],
})
export class PagesModule {
}
