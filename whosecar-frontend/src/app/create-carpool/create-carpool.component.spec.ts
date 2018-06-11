import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateCarpoolComponent } from './create-carpool.component';

describe('CreateCarpoolComponent', () => {
  let component: CreateCarpoolComponent;
  let fixture: ComponentFixture<CreateCarpoolComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateCarpoolComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateCarpoolComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
