import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {appRoutes} from './app.routing';

import { AppComponent } from './app.component';
import { RouterModule } from '@angular/router/';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
