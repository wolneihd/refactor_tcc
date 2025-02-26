import { Component } from '@angular/core';
import { enviroment } from '../../environment/environment';

const frontEndUrl = enviroment.frontEndUrl;

@Component({
  selector: 'app-nabvar-config',
  standalone: true,
  imports: [],
  templateUrl: './nabvar-config.component.html',
  styleUrl: './nabvar-config.component.css'
})
export class NabvarConfigComponent {

  voltarGerenciamento() {
    window.location.href = `${frontEndUrl}/gerenciamento`;
  }

}
