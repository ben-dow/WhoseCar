import {Component, Input, OnInit} from '@angular/core';
import {Car} from '../../_models/Carpool';

@Component({
  selector: 'app-carpool-view',
  templateUrl: './carpool-view.component.html',
  styleUrls: ['./carpool-view.component.css']
})
export class CarpoolViewComponent implements OnInit {
  @Input() cars: Car[];


  constructor() { }

  ngOnInit() {
  }

}
