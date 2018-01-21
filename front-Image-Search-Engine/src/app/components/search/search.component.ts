import { Component, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material';

@Component({
  selector: 'search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  images = [];
  metrics = [{id: 0, title: "Euclidean"}, {id: 1, title: "Taxicab"}, {id: 2, title: "Chebyshev"}]

  selectedMetric = this.metrics[0].id;
  selectedNumber = 1;

  constructor(public snackBar: MatSnackBar) { }

  onBeforeUpload(event) {
    if(!event.formData) {
      event.formData = {};
    }
    event.formData.selectedMetric = this.selectedMetric;
    event.formData.selectedNumber = this.selectedNumber;
  }

  uploaded(event) {

    this.images = JSON.parse(event.xhr.responseText).message;

    console.log(this.images);

    this.snackBar.open("File uploaded", "Great!", {
      duration: 4000,
    });
  }

  error(event) {
    let message = "";
    if(event && event.xhr && event.xhr.responseText && JSON.parse(event.xhr.responseText)) {
      message = JSON.parse(event.xhr.responseText).message;
    }
    else {
      message = "Upload failed";
    }

    this.snackBar.open("Error: " + message, "OK", {
      duration: 4000,
    });
  }
}
