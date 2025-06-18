import { Component, inject, Inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialog, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { DialogErroComponent } from '../../dialog-erro/dialog-erro.component';

@Component({
  selector: 'app-excluir-usuario',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './excluir-usuario.component.html',
  styleUrl: './excluir-usuario.component.css'
})
export class ExcluirUsuarioComponent {

  nome: string = '';

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) {
    this.ngOnInit()
  }

  ngOnInit(): void {
    this.nome = this.data.nome;
  }

  readonly dialog = inject(MatDialog);
  inativarUsuario() {
    const dialogRef = this.dialog.open(DialogErroComponent, {
      data: {
        titulo: "Funcionalidade ainda não implementada...",
        erro: "Por ser uma versão teste, esta funcionalidade ainda não está disponivel."
      }
    });
  }

}
