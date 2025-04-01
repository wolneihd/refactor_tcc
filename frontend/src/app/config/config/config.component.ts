import { Component } from '@angular/core';
import { NabvarConfigComponent } from '../nabvar-config/nabvar-config.component';
import { TabelaUsuariosComponent } from "../tabela-usuarios/tabela-usuarios.component";

@Component({
  selector: 'app-config',
  standalone: true,
  imports: [NabvarConfigComponent, TabelaUsuariosComponent],
  templateUrl: './config.component.html',
  styleUrl: './config.component.css'
})
export class ConfigComponent {

}
