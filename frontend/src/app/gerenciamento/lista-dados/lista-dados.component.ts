import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Usuario } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';
import { Mensagem } from '../../entidades/Usuarios';
import { ResponderComponent } from '../responder/responder.component';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ShareService } from '../../services/share.service';

@Component({
  selector: 'app-lista-dados',
  standalone: true,
  imports: [CommonModule, ResponderComponent, FormsModule],
  templateUrl: './lista-dados.component.html',
  styleUrl: './lista-dados.component.css'
})
export class ListaDadosComponent {

  usuarios: Usuario[] = [];
  mensagens: Mensagem[] = [];

  responderSelecionado: boolean = false;
  btnResponder: boolean = false;
  usuarioSelecionado: number = -1;

  constructor(
    private httpClient: HttpClient,
    private share: ShareService
  ) { }

  ngOnInit() {
    this.buscarDados()
  }

  buscarDados() {
    this.httpClient.get<Usuario[]>(`http://127.0.0.1:5000/`).subscribe(
      res => {
        this.usuarios = res;
        // console.log(this.usuarios);
      },
      error => {
        console.error('Erro ao buscar dados:', error);
      }
    );
  }

  checkSelecionado(mensagem:Mensagem) {
    mensagem.checkbox = !mensagem.checkbox;
  }

  verMensagens(mensagens: Mensagem[], id: number) {
    this.mensagens = mensagens;
    this.responderSelecionado = false;
    this.btnResponder = true;
    this.usuarioSelecionado = id;
  }

  responderMensagem(usuarios: Usuario[]) {
    this.responderSelecionado = true;
    this.share.shareMensagem(usuarios, this.usuarioSelecionado)
  }

  verUmaMensagem(mensagem: Mensagem) {
    alert(mensagem.texto_msg)
  }
}
