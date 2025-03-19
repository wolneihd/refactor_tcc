import { Component } from '@angular/core';
import { NabvarConfigComponent } from '../../config/nabvar-config/nabvar-config.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [NabvarConfigComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {

}
