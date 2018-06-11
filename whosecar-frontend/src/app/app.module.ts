import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { CarpoolDisplayComponent } from './carpool-display/carpool-display.component';
import { CreateCarpoolComponent } from './create-carpool/create-carpool.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';

import { RouterModule, Routes } from '@angular/router';
import { CarpoolViewComponent } from './carpool-display/carpool-view/carpool-view.component';
import { LogInComponent } from './carpool-display/log-in/log-in.component';
import { CarpoolSelectComponent } from './carpool-display/carpool-select/carpool-select.component';
import { DriverSelectComponent } from './carpool-display/carpool-select/driver-select/driver-select.component';

const appRoutes: Routes = [
  {path: '', component: CreateCarpoolComponent},
  {path: ':id', component: CarpoolDisplayComponent}
];


@NgModule({
  declarations: [
    AppComponent,
    CarpoolDisplayComponent,
    CreateCarpoolComponent,
    CarpoolViewComponent,
    LogInComponent,
    CarpoolSelectComponent,
    DriverSelectComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: false } // <-- debugging purposes only
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
