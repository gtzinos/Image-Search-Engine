import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import {MediaMatcher} from '@angular/cdk/layout';
@Component({
  selector: 'responsive-template',
  templateUrl: './responsive-template.component.html',
  styleUrls: ['./responsive-template.css']
})
export class ResponsiveTemplateComponent {

  mobileQuery: MediaQueryList;

  fillerNav = [
    {
      title: "Insert images",
      url: "/upload"
    },
    {
      title: "Search images",
      url: "/search"
    }
  ]

  private _mobileQueryListener: () => void;

  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListener);
  }

  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListener);
  }

  shouldRun = [/(^|\.)plnkr\.co$/, /(^|\.)stackblitz\.io$/].some(h => h.test(window.location.host));
}