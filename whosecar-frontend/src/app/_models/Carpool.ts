export interface Carpool {
  id: string;
  Title: string;
  Cars: {};
  Users:  {};
}
export interface Car {
  id: string;
  CarCapacity: number;
  Owner_ID: string;
  Passengers: Passenger[];
  Owner_Name: string;
}

export interface Passenger {
  id: string;
  Car_ID: string;
  Carpool_ID: string;
  Driver: boolean;
  Name: string;
}
