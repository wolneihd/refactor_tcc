import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShareService {

  private valueSource = new BehaviorSubject<string>('');
  value = this.valueSource.asObservable();

  constructor() { }

  changeValue(newValue: string) {
    this.valueSource.next(newValue); 
  }
}
