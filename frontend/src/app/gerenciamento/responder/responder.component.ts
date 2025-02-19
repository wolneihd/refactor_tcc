import { Component } from '@angular/core';
import { Mensagem, Usuario } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';
import { ShareService } from '../../services/share.service';
import { ApiService } from '../../services/api.service';
import { FormsModule } from '@angular/forms';

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
      next: () => { },
      error: erro => {
        console.error(erro)
        alert("Erro ao carregar os jogos");
      }
    })
  }

  enviarResposta() {
    this.isResponderSelecionado = false;
    this.share.mostrarFiltrarResponder(this.isResponderSelecionado, false);
    alert('TODO: Enviar resposta!');
  }

  fecharResposta() {
    this.isResponderSelecionado = false;
    this.share.mostrarFiltrarResponder(this.isResponderSelecionado, false);
  }
}
