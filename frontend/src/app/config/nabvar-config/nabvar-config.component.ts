import { Component } from '@angular/core';

@Component({
  selector: 'app-nabvar-config',
  standalone: true,
  imports: [],
  templateUrl: './nabvar-config.component.html',
  styleUrl: './nabvar-config.component.css'
})
export class NabvarConfigComponent {


  voltarGerenciamento() {
    window.location.href = 'http://localhost:4200/gerenciamento';
  }

}
