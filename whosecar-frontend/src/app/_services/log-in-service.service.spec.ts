import { TestBed, inject } from '@angular/core/testing';

import { LogInServiceService } from './log-in-service.service';

describe('LogInServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LogInServiceService]
    });
  });

  it('should be created', inject([LogInServiceService], (service: LogInServiceService) => {
    expect(service).toBeTruthy();
  }));
});
