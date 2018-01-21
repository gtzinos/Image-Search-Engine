import { Routes } from '@angular/router';
import { AppComponent } from './app.component';


export const appRoutes: Routes = [
  {
    path: '', component: AppComponent, children: [
      {
        path: '', loadChildren: "./shared/components/responsive-template/responsive-template.module#ResponsiveTemplateComponenModule"
      }
    ]
  }

]
