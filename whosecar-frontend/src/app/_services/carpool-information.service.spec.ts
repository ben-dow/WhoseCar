import { TestBed, inject } from '@angular/core/testing';

import { CarpoolInformationService } from './carpool-information.service';

describe('CarpoolInformationService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CarpoolInformationService]
    });
  });

  it('should be created', inject([CarpoolInformationService], (service: CarpoolInformationService) => {
    expect(service).toBeTruthy();
  }));
});
