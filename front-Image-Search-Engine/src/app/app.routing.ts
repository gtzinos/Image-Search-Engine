import { Routes } from '@angular/router';
import { AppComponent } from './app.component';


export const appRoutes: Routes = [
  {
    path: '', component: AppComponent, children: [
      { path: '', redirectTo: 'search', pathMatch: "full"},
      { path: 'search', loadChildren: "./search/search.module#SearchModule" },
      { path: '**', redirectTo: 'search' }
    ]
  }
];
