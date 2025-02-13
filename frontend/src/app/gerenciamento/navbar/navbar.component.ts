import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  constructor(private router: Router) { }

  responderMensagem() {
    this.router.navigate(['/gerenciamento'], {
      state: { filtrar: true, mensagem: "Filtragem ativada" },
    });
    console.log('enviado...')
  }
}
