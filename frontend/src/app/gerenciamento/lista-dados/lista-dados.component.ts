import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Usuario } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';
import { Mensagem } from '../../entidades/Usuarios';
import { ResponderComponent } from '../responder/responder.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-lista-dados',
  standalone: true,
  imports: [CommonModule, ResponderComponent],
  templateUrl: './lista-dados.component.html',
  styleUrl: './lista-dados.component.css'
})
export class ListaDadosComponent {
  usuarios: Usuario[] = [];
  mensagens: Mensagem[] = [];
  responderSelecionado: boolean = false;

  constructor(private httpClient: HttpClient, private router: Router) { }

  ngOnInit() {
    this.buscarDados()
  }

  buscarDados() {
    this.httpClient.get<Usuario[]>(`http://localhost:5001`).subscribe(
      res => {
        this.usuarios = res;
        // console.log(this.usuarios);
      },
      error => {
        console.error('Erro ao buscar dados:', error);
      }
    );
  }

  verMensagem(mensagens: Mensagem[]) {
    for (let i = 0; i < mensagens.length; i++) {
      console.log(mensagens[i])
    }
    this.mensagens = mensagens;
    this.responderSelecionado = false;
  }

  responderMensagem(mensagem: Mensagem) {
    this.responderSelecionado = true;
    this.router.navigate(['/app-responder'], {
      state: { mensagem: mensagem }, // Envia o objeto mensagem
    });
  }

  verUmaMensagem(mensagem: Mensagem) {
    alert(mensagem.texto_msg)
  }
}
