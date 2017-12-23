import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ModalsComponent} from './modals/modals.component';
import {ModalComponent} from './modals/modal/modal.component';
import {NgbModalModule} from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  imports: [
    CommonModule,
    NgbModalModule,
  ],
  declarations: [ModalsComponent, ModalComponent],
  exports: [ModalsComponent],
  entryComponents: [ModalComponent],
})
export class ComponentsModule {}
