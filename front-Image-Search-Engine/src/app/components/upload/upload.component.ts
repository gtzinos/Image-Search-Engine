import { Component, OnInit } from '@angular/core';
import {MatSnackBar} from '@angular/material';

@Component({
  selector: 'upload',
  templateUrl: './upload.component.html'
})
export class UploadComponent {

  constructor(public snackBar: MatSnackBar) {}

  uploaded(event) {
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