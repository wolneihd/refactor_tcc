import { Component } from '@angular/core';
import { Mensagem, Usuario } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';
import { ShareService } from '../../services/share.service';
import { ApiService } from '../../services/api.service';
import { FormsModule } from '@angular/forms';
import { Resposta } from '../../entidades/Resposta';

@Component({
  selector: 'app-responder',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './responder.component.html',
  styleUrl: './responder.component.css'
})
export class ResponderComponent {

  divResponder: boolean = false;
  mensagem!: Mensagem;

  usuarios: Usuario[] = [];
  mensagensSelecionadas: Mensagem[] = [];
  id: number = 0;

  isResponderSelecionado: boolean = false;
  promptAdicionalUsuario: string = '';
  respostaIA!: Resposta;

  constructor(
    private share: ShareService,
    private api: ApiService
  ) { }

  ngOnInit(): void {
    this.share.usuarios$.subscribe(usuarios => {
      this.usuarios = usuarios
    })
    this.share.id$.subscribe(id => {
      this.id = id;
    })
    for (const usuario of this.usuarios) {
      if (usuario.id === this.id) {
        for (const mensagem of usuario.mensagens) {
          if (mensagem.checkbox === true) {
            this.mensagensSelecionadas.push(mensagem)
          }
        }
      }
    }
  }

  gerarResposta() {
    this.divResponder = !this.divResponder;
    this.api.gerarRespostaIA(this.promptAdicionalUsuario, this.mensagensSelecionadas).subscribe({
      next: (resposta) => {
        this.respostaIA = resposta;
        this.limparQuebrasLinha(this.respostaIA.resposta);
        console.log(this.respostaIA)
      },
      error: erro => {
        console.error(erro)
        alert("Erro ao carregar os jogos");
      }
    })
  }

  limparQuebrasLinha(texto: string) {
    this.respostaIA.resposta = texto.replace(/\n{3,}/g, '');
  }

  retornoEnvio: string = '';
  enviarResposta() {
    this.isResponderSelecionado = false;
    this.share.mostrarFiltrarResponder(this.isResponderSelecionado, false);
    this.api.enviarResposta(this.mensagensSelecionadas, this.respostaIA.resposta).subscribe({
      next: (resposta) => {
        this.retornoEnvio = resposta;
      },
      error: erro => {
        console.error(erro)
        alert("Erro ao carregar os jogos");
      }
    })
  }

  fecharResposta() {
    this.isResponderSelecionado = false;
    this.share.mostrarFiltrarResponder(this.isResponderSelecionado, false);
  }
}
