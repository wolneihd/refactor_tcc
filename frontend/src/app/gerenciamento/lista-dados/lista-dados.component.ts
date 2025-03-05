import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Usuario } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';
import { Mensagem } from '../../entidades/Usuarios';
import { FormsModule } from '@angular/forms';
import { ShareService } from '../../services/share.service';
import { ApiService } from '../../services/api.service';
import { MatDialog } from '@angular/material/dialog';
import { DialogImagemComponent } from '../dialog-imagem/dialog-imagem.component';

@Component({
  selector: 'app-lista-dados',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './lista-dados.component.html',
  styleUrl: './lista-dados.component.css'
})
export class ListaDadosComponent {

  usuarios: Usuario[] = [];
  mensagens: Mensagem[] = [];

  isResponderSelecionado: boolean = false;
  btnResponder: boolean = false;
  usuarioSelecionado: number = -1;

  constructor(
    private share: ShareService,
    private api: ApiService
  ) { }

  ngOnInit(){
    this.api.obterDadosTabela().subscribe({
      next: res => {
        this.usuarios = res; 
        // console.log(this.usuarios);
      },
      error: erro => {
        console.error(erro)
      }
    })
  }

  informarStatus(codigo: number): String {
    if (codigo === 0) {
      return "Em aberto";
    } else {
      return "Respondido"
    }
  }

  informarTipo(tipo: string): String {
    if (tipo === "text") {
      return "Texto";
    } else if (tipo === "audio") {
      return "Audio"
    } else {
      return "Imagem"
    }
  }

  checkSelecionado(mensagem:Mensagem) {
    mensagem.checkbox = !mensagem.checkbox;
  }

  verMensagens(mensagens: Mensagem[], id: number) {
    this.mensagens = mensagens;
    this.btnResponder = true;
    this.usuarioSelecionado = id
  }

  responderMensagem(usuarios: Usuario[]) {
    this.share.shareMensagem(usuarios, this.usuarioSelecionado);
    this.isResponderSelecionado = !this.isResponderSelecionado;
    this.share.mostrarFiltrarResponder(false, this.isResponderSelecionado);
  }

  verUmaMensagem(mensagem: Mensagem) {
    alert(mensagem.texto_msg)
  }

  converterTimestampData(timestamp: number): string {
    const data = new Date(timestamp * 1000);
    const dia = data.getDate().toString().padStart(2, '0');
    const mes = (data.getMonth() + 1).toString().padStart(2, '0'); // Mês começa do 0
    const ano = data.getFullYear();
    return `${dia}/${mes}/${ano}`;
  }

  converterTimestampHora(timestamp: number): string {
    const data = new Date(timestamp * 1000);
    const horas = data.getHours().toString().padStart(2, '0');
    const minutos = data.getMinutes().toString().padStart(2, '0');
    return `${horas}:${minutos}`;
  }

  readonly dialog = inject(MatDialog);

  abrirDialogImagem(nome_arquivo: string) {
    const dialogRef = this.dialog.open(DialogImagemComponent, {
      data: {
        url: nome_arquivo
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }  
}
