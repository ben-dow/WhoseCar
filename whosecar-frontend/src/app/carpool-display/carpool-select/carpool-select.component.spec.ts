import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CarpoolSelectComponent } from './carpool-select.component';

describe('CarpoolSelectComponent', () => {
  let component: CarpoolSelectComponent;
  let fixture: ComponentFixture<CarpoolSelectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CarpoolSelectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CarpoolSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
