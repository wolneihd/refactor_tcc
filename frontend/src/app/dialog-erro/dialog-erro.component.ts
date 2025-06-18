import { Component, Inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-dialog-erro',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './dialog-erro.component.html',
  styleUrl: './dialog-erro.component.css'
})
export class DialogErroComponent {

  titulo: string = '';
  erro: string = '';

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) { }

  ngOnInit(): void {
    this.titulo = this.data.titulo;
    this.erro = this.data.erro;
  }

}
