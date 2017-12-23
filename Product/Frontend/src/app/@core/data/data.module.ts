import { NgModule, ModuleWithProviders } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserService } from './users.service';
import { ElectricityService } from './electricity.service';
import { StateService } from './state.service';
import { SmartTableService } from './smart-table.service';
import { ContentTableService } from './content-table.service';
import { DataHandlerService } from './data-handler.service';
import { AuthenticationService } from '../../pages/authentication/_services';

const SERVICES = [
  UserService,
  StateService,
  SmartTableService,
  ContentTableService,
  ElectricityService,
  DataHandlerService,
  AuthenticationService,
];

@NgModule({
  imports: [
    CommonModule,
  ],
  providers: [
    ...SERVICES,
  ],
})
export class DataModule {
  static forRoot(): ModuleWithProviders {
    return <ModuleWithProviders>{
      ngModule: DataModule,
      providers: [
        ...SERVICES,
      ],
    };
  }
}
