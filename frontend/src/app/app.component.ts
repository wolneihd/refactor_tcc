import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ListaDadosComponent } from './lista-dados/lista-dados.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ListaDadosComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
}
