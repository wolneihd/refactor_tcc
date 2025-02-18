import { Component } from '@angular/core';
import { Mensagem, Usuario } from '../../entidades/Usuarios';
import { CommonModule } from '@angular/common';
import { ShareService } from '../../services/share.service';

@Component({
  selector: 'app-responder',
  standalone: true,
  imports: [CommonModule],
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

  constructor(private share: ShareService) { }

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
