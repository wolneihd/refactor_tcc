import { Component } from '@angular/core';
import { Mensagem } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-responder',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './responder.component.html',
  styleUrl: './responder.component.css'
})
export class ResponderComponent {

  divResponder:boolean = true;
  mensagem!: Mensagem;

  ngOnInit() {
    this.mensagem = history.state.mensagem; // Acessa o objeto mensagem
    console.log('Dados recebidos:', this.mensagem);
  }

  gerarResposta() {
    this.divResponder = !this.divResponder;
  }

  enviarResposta() {
    alert('Enviar resposta!');
  }

  fecharResposta() {
    alert('Fechar janela de fechar!')
  }

}
