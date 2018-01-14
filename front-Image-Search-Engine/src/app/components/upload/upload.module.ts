import {FileUploadModule} from 'primeng/primeng';
import { NgModule } from '@angular/core';
import { UploadComponent } from './upload.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    UploadComponent
  ],
  imports: [
      FileUploadModule,
    RouterModule.forChild([{path: '', component: UploadComponent}])
  ],
  providers: [],
  bootstrap: [UploadComponent]
})
export class UploadModule { }
