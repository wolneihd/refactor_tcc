import { Component, Inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-user-config',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './user-config.component.html',
  styleUrl: './user-config.component.css'
})
export class UserConfigComponent {

  titulo: string = '';
  nome: string = '';
  email: string = '';

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) {
      this.ngOnInit()
     }
  
    ngOnInit(): void {
      this.titulo = this.data.titulo;
      this.nome = this.data.nome;   
      this.email = this.data.email;
    }

}
