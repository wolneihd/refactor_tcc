import { Component, Inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-recarregar',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  templateUrl: './recarregar.component.html',
  styleUrl: './recarregar.component.css'
})
export class RecarregarComponent {

  analiseIA: string = ''
  categoria: string = ''
  resumo: string = ''

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) { }

  ngOnInit(): void {
    this.analiseIA = this.data.analiseIA;
    this.categoria = this.data.categoria;
    this.resumo = this.data.resumo;
  }
}
