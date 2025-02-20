import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-reset-senha',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './reset-senha.component.html',
  styleUrl: './reset-senha.component.css'
})
export class ResetSenhaComponent {

  reenviarEmail() {
    alert('TODO: enviar e-mail.');
  }

}
