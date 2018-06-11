import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DriverSelectComponent } from './driver-select.component';

describe('DriverSelectComponent', () => {
  let component: DriverSelectComponent;
  let fixture: ComponentFixture<DriverSelectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DriverSelectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DriverSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
