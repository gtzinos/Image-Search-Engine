import { FileUploadModule } from 'primeng/primeng';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ResponsiveTemplateComponent } from './responsive-template.component';
import {MatDividerModule} from '@angular/material/divider';
import { MatIconModule, MatToolbarModule } from '@angular/material';
import { MatListModule } from '@angular/material/list';
import { MediaMatcher } from '@angular/cdk/layout';
import { MatSidenavModule } from '@angular/material/sidenav';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@NgModule({
  declarations: [
    ResponsiveTemplateComponent
  ],
  imports: [
    MatSidenavModule,MatDividerModule, MatListModule, MatIconModule, MatToolbarModule,
    FileUploadModule, FormsModule,CommonModule,
    RouterModule.forChild([{
      path: '', component: ResponsiveTemplateComponent, children: [
        { path: '', redirectTo: 'search', pathMatch: "full" },
        { path: 'search', loadChildren: "../../../components/search/search.module#SearchModule" },
        { path: 'upload', loadChildren: "../../../components/upload/upload.module#UploadModule" },
        { path: '**', redirectTo: 'search' }]
    }]
    )
  ],
  providers: [MediaMatcher]
})
export class ResponsiveTemplateComponenModule { }
