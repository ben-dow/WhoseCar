import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Car, Carpool} from '../_models/Carpool';
import 'rxjs/add/operator/map';
import 'rxjs-compat/add/operator/catch';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CarpoolInformationService {

  constructor(private http: HttpClient) { }

  private handleError(error: Response | any) {
    location.href = '/';
    return null;
  }

  getCarpoolInformation() {
    return this.http.get<any>('http://localhost:5000/Carpool/' +
      localStorage.getItem('CarpoolID')).map(carpool => carpool).catch((error: any ) => this.handleError(error));

  }

  CreateDriver(CarCapacity: number, Passenger: string ) {
    const urlString: string = 'http://localhost:5000/Carpool/' + localStorage.getItem('CarpoolID') + '/AddCar/' + Passenger;
    return this.http.post<any>(urlString, {'car_capacity': CarCapacity } ).map(response => response);
  }

  getPassengerInformation(Passenger: string){
    const urlString: string = 'http://localhost:5000/Passengers/' + Passenger;
    return this.http.get<any>(urlString ).map(response => response);
  }

  setPassengerCar(Passenger: string, car: string) {
    const urlString: string = 'http://localhost:5000/Cars/' + car + '/Passengers/AddPassenger/' + Passenger;
    return this.http.post<any>(urlString, {} ).map(response => response);
  }
}
