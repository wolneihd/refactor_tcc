import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { enviroment } from '../../environment/environment';

const minio = enviroment.minio;

@Component({
  selector: 'app-dialog-imagem',
  standalone: true,
  imports: [],
  templateUrl: './dialog-imagem.component.html',
  styleUrl: './dialog-imagem.component.css'
})
export class DialogImagemComponent {

  nome_arquivo: string = '';
  url_imagem: string = '';

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) {
    this.ngOnInit()
   }

  ngOnInit(): void {
    this.nome_arquivo = this.data.url;
    this.url_imagem = `${minio}/${this.nome_arquivo}`;    
    console.log(this.url_imagem);
  }

}
