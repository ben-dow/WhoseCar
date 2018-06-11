import { Component, OnInit } from '@angular/core';
import {Carpool, Passenger} from '../_models/Carpool';
import {ActivatedRoute} from '@angular/router';
import {CarpoolInformationService} from '../_services/carpool-information.service';
import {Observable} from 'rxjs';


@Component({
  selector: 'app-carpool-display',
  templateUrl: './carpool-display.component.html',
  styleUrls: ['./carpool-display.component.css']
})
export class CarpoolDisplayComponent implements OnInit {

  CarpoolModel: Carpool;

  loggedin = false;

  title = '';

  loaded = false;

  PersonalData: Passenger;

  constructor(private route: ActivatedRoute,  private informationService: CarpoolInformationService) {

    this.route.params.subscribe(params => localStorage.setItem('CarpoolID', params['id']));
    this.informationService.getCarpoolInformation().subscribe(data => {
      this.CarpoolModel = data;
      this.loaded = true;
    });

  }

  ngOnInit() {
  }

  onLoggedIn(LoggedIn: boolean) {
    this.loggedin = LoggedIn;
  }
  onPersonalInformation(PersonalData: Passenger) {
    this.PersonalData = PersonalData;
  }

  onUpdateCarpoolInfo(Update: boolean) {
    this.informationService.getCarpoolInformation().subscribe(data => {
      this.CarpoolModel = data;
      this.PersonalData = this.CarpoolModel.Users[this.PersonalData.id];
    });


  }
}
