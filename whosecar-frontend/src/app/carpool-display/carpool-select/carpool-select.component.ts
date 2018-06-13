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

  @Input() cars: {};
  @Input() PassengerData: Passenger;
  @Output() UpdateCarpoolInfo = new EventEmitter<boolean>();


  Driver: boolean;

  editMode = false;
  private formInfo: { capacity: number };

  constructor(private carpoolService: CarpoolInformationService) {
  }

  ngOnInit() {
  }

  onMakeSelection(carId: string) {

  }

  OnCreateDriver(form: NgForm) {
    const Capacity = form.value['CarCapacity'];
    this.carpoolService.CreateDriver(Capacity, this.PassengerData.id).subscribe(data => this.UpdateCarpoolInfo.emit(true));


  }

  OnCarChoosenUpdated() {
    this.UpdateCarpoolInfo.emit(true);
  }

  objectKeys(obj) {
    return Object.keys(obj);
  }

  OnSaveChanges(form: NgForm) {
    const value = form.value['capacity'];
    if (value === '')  {
      this.editMode = false;
    } else {

      this.carpoolService.changeCarCapacity(this.PassengerData.Car_ID, value).subscribe(data => {
        this.UpdateCarpoolInfo.emit(true);
        this.editMode = false;

      });
    }

}

  OnRemoveFromCar() {
    this.carpoolService.removePassengerFromCar(this.PassengerData.Car_ID, this.PassengerData.id).subscribe(data => {
      this.UpdateCarpoolInfo.emit(true);
    });
  }


  OnDeleteCar() {
    this.carpoolService.removeCar(this.PassengerData.Car_ID).subscribe(data => {
      this.UpdateCarpoolInfo.emit(true);
      this.editMode = false;
    });

  }

}
