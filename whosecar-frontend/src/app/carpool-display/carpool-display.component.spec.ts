import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CarpoolDisplayComponent } from './carpool-display.component';

describe('CarpoolDisplayComponent', () => {
  let component: CarpoolDisplayComponent;
  let fixture: ComponentFixture<CarpoolDisplayComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CarpoolDisplayComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CarpoolDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
