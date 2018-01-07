import { NgModule } from '@angular/core';
import { SearchComponent } from './search.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    SearchComponent
  ],
  imports: [
    RouterModule.forChild([{path: '', component: SearchComponent}])
  ],
  providers: [],
  bootstrap: [SearchComponent]
})
export class SearchModule { }
