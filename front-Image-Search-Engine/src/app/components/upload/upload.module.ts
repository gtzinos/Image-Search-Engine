import {FileUploadModule} from 'primeng/primeng';
import { NgModule } from '@angular/core';
import { UploadComponent } from './upload.component';
import { RouterModule } from '@angular/router';
import {MatSnackBarModule} from '@angular/material/snack-bar';

@NgModule({
  declarations: [
    UploadComponent
  ],
  imports: [
      FileUploadModule,MatSnackBarModule,
    RouterModule.forChild([{path: '', component: UploadComponent}])
  ],
  providers: []
})
export class UploadModule { }
