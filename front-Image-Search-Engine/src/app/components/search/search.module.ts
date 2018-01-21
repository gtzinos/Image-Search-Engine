import { NgModule } from '@angular/core';
import { SearchComponent } from './search.component';
import { RouterModule } from '@angular/router';
import { FileUploadModule } from 'primeng/primeng';
import { MatSnackBarModule } from '@angular/material';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    SearchComponent
  ],
  imports: [
    FileUploadModule,MatSnackBarModule,CommonModule,FormsModule,
    RouterModule.forChild([{path: '', component: SearchComponent}])
  ],
  providers: [],
  bootstrap: [SearchComponent]
})
export class SearchModule { }
