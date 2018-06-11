import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {NgForm} from '@angular/forms';
import {LogInServiceService} from '../../_services/log-in-service.service';
import {Passenger} from '../../_models/Carpool';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {

  @Output() LoggedIn = new EventEmitter<boolean>();
  @Output() LoggedInUser = new EventEmitter<Passenger>();

  private PersonData: Passenger;

  constructor(private loginservice: LogInServiceService) { }

  ngOnInit() {
  }

  LogIn(form: NgForm) {
    const name = form.value['name'];
    this.loginservice.login(name).subscribe(data => {
      this.PersonData = data;
      localStorage.setItem('PersonID', this.PersonData['id']);
      this.LoggedIn.emit(true);
      this.LoggedInUser.emit(this.PersonData);
    });

  }
}
