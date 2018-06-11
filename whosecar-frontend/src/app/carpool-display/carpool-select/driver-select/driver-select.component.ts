import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Car, Passenger} from '../../../_models/Carpool';
import {CarpoolInformationService} from '../../../_services/carpool-information.service';

@Component({
  selector: 'app-driver-select',
  templateUrl: './driver-select.component.html',
  styleUrls: ['./driver-select.component.css']
})
export class DriverSelectComponent implements OnInit {

  @Input() car: Car;
  @Input() passengerData: Passenger;
  @Output() DriverChosen = new EventEmitter();


  constructor(private informationService: CarpoolInformationService) { }

  ngOnInit() {
  }


  onClick() {
    if (this.car.CarCapacity == this.car.Passengers.length ) {
      return;
    }
    this.informationService.setPassengerCar(this.passengerData.id, this.car.id).subscribe( data => this.DriverChosen.emit());
  }

}
