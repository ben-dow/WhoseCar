import {Component, OnInit, ViewChild} from '@angular/core';
import {NgForm} from '@angular/forms';
import * as $ from 'jquery';
import {HttpClient} from '@angular/common/http';


@Component({
  selector: 'app-create-carpool',
  templateUrl: './create-carpool.component.html',
  styleUrls: ['./create-carpool.component.css']
})
export class CreateCarpoolComponent implements OnInit {
  loading = false;

  constructor() {
  }

  ngOnInit() {
  }

  newCarpoolSubmit(form: NgForm) {
    const carpoolTitle = form.value['carpoolName'];
    this.loading = true;

    $.ajax({
      url: 'http://localhost:5000/Carpool/NewCarpool/' + carpoolTitle,
      type: 'POST',
      'success': function(data) {
        location.href = '/' + data['url'];
      },
      'error': function(data) {
        this.loading = false;
        location.href = '/';
      }
      }
    );
  }

}

