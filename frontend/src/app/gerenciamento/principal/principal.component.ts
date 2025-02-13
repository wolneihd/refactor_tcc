import { Component } from '@angular/core';
import { ListaDadosComponent } from "../lista-dados/lista-dados.component";
import { NavbarComponent } from "../navbar/navbar.component";
import { ResponderComponent } from "../responder/responder.component";
import { CommonModule } from '@angular/common';
import { FiltrarComponent } from "../filtrar/filtrar.component";
import { Router } from '@angular/router';

@Component({
  selector: 'app-principal',
  standalone: true,
  imports: [ListaDadosComponent, NavbarComponent, ResponderComponent, CommonModule, FiltrarComponent],
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.css'
})
export class PrincipalComponent {

  btnResponder:boolean = true;
  btnFiltrar:boolean = false;

  filtrar: boolean = false;
  mensagemRecebida: string = ''; // Variável para armazenar a mensagem

  constructor(private router: Router) {}

  ngOnInit() {
    this.filtrar = history.state.filtrar; // Acessa o objeto mensagem
    console.log('Dados recebidos...', this.filtrar);
  }

}
