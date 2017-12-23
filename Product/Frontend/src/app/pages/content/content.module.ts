import { NgModule } from '@angular/core';
import { Ng2SmartTableModule } from 'ng2-smart-table';

import { ThemeModule } from '../../@theme/theme.module';
import { ContentRoutingModule, routedComponents } from './content-routing.module';
import { ContentTableService } from '../../@core/data/content-table.service';

@NgModule({
  imports: [
    ThemeModule,
    ContentRoutingModule,
    Ng2SmartTableModule,
  ],
  declarations: [
    ...routedComponents,
  ],
  providers: [
    ContentTableService,
  ],
})
export class ContentModule { }
