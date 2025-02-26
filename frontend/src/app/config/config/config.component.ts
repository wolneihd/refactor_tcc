import { Component } from '@angular/core';
import { NabvarConfigComponent } from '../nabvar-config/nabvar-config.component';

@Component({
  selector: 'app-config',
  standalone: true,
  imports: [NabvarConfigComponent],
  templateUrl: './config.component.html',
  styleUrl: './config.component.css'
})
export class ConfigComponent {

}
