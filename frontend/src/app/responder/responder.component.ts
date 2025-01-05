import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Mensagem } from '../entidades/Usuarios';

@Component({
  selector: 'app-responder',
  standalone: true,
  imports: [],
  templateUrl: './responder.component.html',
  styleUrl: './responder.component.css'
})
export class ResponderComponent {
  mensagem!: Mensagem;

  constructor(private router: Router) {}

  ngOnInit() {
    this.mensagem = history.state.mensagem; // Acessa o objeto mensagem
    console.log('Dados recebidos:', this.mensagem);
  }

}
