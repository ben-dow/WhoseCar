import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LogInServiceService {

  constructor(private http: HttpClient) { }

  login(username: string) {
    return this.http.post<any>('http://localhost:5000/Authenticate',
      {'CarpoolID': localStorage.getItem('CarpoolID'), 'PassengerName': username} ).map(user => user);
  }
}
