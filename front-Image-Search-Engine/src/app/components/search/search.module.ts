import { NgModule } from '@angular/core';
import { SearchComponent } from './search.component';
import { RouterModule } from '@angular/router';
import { FileUploadModule } from 'primeng/primeng';
import { MatSnackBarModule } from '@angular/material';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatSelectModule} from '@angular/material/select';
import {MatInputModule} from '@angular/material/input';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';
@NgModule({
  declarations: [
    SearchComponent
  ],
  imports: [
    FileUploadModule,MatInputModule,MatSlideToggleModule,MatSelectModule,MatSnackBarModule,ReactiveFormsModule,CommonModule,FormsModule,
    RouterModule.forChild([{path: '', component: SearchComponent}])
  ],
  providers: [],
  bootstrap: [SearchComponent]
})
export class SearchModule { }
