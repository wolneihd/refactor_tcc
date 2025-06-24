import { Component, Inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { Mensagem } from '../../entidades/Usuarios';
import { ApiService } from '../../services/api.service';
import { Reanalise } from '../../entidades/Reanalise';

@Component({
  selector: 'app-recarregar',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './recarregar.component.html',
  styleUrl: './recarregar.component.css'
})
export class RecarregarComponent {

  mensagem: Mensagem = {} as Mensagem;

  constructor(@Inject(MAT_DIALOG_DATA) public data: { mensagem: Mensagem }, private api: ApiService) { }

  ngOnInit(): void {
    this.mensagem = this.data.mensagem;
  }

  reavaliarMensagem() {
    this.api.reprocessarMensagem(this.mensagem.texto_msg, this.mensagem.id).subscribe({
      next: (reanalise: Reanalise) => {
        this.mensagem.analise_ia = reanalise.feedback;
        this.mensagem.categoria = reanalise.categoria;
        this.mensagem.feedback = reanalise.resumo;
        console.log('reanalisado...')
      },
      error: erro => {
        console.error(erro)
      }
    })
  }

  captarDadosCampos() {
    let analise_ia = ((<HTMLInputElement>document.getElementById("analise_ia")).value);
    let categoria = ((<HTMLInputElement>document.getElementById("categoria")).value);
    let resumo = ((<HTMLInputElement>document.getElementById("resumo")).value);

    this.api.salvarReprocesso(resumo, analise_ia, categoria, this.mensagem.id).subscribe({
      next: (resposta) => {
        console.log(resposta)
      },
      error: erro => {
        console.error(erro)
      }
    })
  }
}
