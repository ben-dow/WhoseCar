import {Component, OnInit, Input, EventEmitter, Output} from '@angular/core';
import {Car, Passenger} from '../../_models/Carpool';
import {NgForm} from '@angular/forms';
import {CarpoolInformationService} from '../../_services/carpool-information.service';

@Component({
  selector: 'app-carpool-select',
  templateUrl: './carpool-select.component.html',
  styleUrls: ['./carpool-select.component.css']
})
export class CarpoolSelectComponent implements OnInit {

  @Input() cars: Car[];
  @Input() PassengerData: Passenger;
  @Output() UpdateCarpoolInfo = new EventEmitter<boolean>();

  Driver: boolean;


  constructor(private carpoolService: CarpoolInformationService) {
  }

  ngOnInit() {
  }

  onMakeSelection(carId: string) {

  }

  OnCreateDriver(form: NgForm) {
    const Capacity = form.value['CarCapacity'];
    this.carpoolService.CreateDriver(Capacity, this.PassengerData.id).subscribe( data => this.UpdateCarpoolInfo.emit(true));


  }

  OnCarChoosenUpdated() {
    this.UpdateCarpoolInfo.emit(true);
  }
}
