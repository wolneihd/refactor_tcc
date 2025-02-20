import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { ContatoComponent } from '../contato/contato.component';
import { ResetSenhaComponent } from '../reset-senha/reset-senha.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  readonly dialog = inject(MatDialog);

  abrirDialogContato() {
    const dialogRef = this.dialog.open(ContatoComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirDialogResetSenha() {
    const dialogRef = this.dialog.open(ResetSenhaComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirTelaPrincipal() {
    window.location.href = 'http://localhost:4200/gerenciamento';
  }
}
