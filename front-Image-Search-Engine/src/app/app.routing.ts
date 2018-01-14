import { Routes } from '@angular/router';
import { AppComponent } from './app.component';


export const appRoutes: Routes = [
  {
    path: '', component: AppComponent, children: [
      { path: '', redirectTo: 'search', pathMatch: "full"},
      { path: 'search', loadChildren: "./components/search/search.module#SearchModule" },
      { path: 'upload', loadChildren: "./components/upload/upload.module#UploadModule" },
      { path: '**', redirectTo: 'search' }
    ]
  }
];
