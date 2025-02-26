import { Component } from '@angular/core';
import { Busca } from '../../entidades/Busca';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-filtrar',
  standalone: true,
  imports: [],
  templateUrl: './filtrar.component.html',
  styleUrl: './filtrar.component.css'
})
export class FiltrarComponent {

  constructor(private api: ApiService) {}

  captarDadosBusca() {

    let nome = ((<HTMLInputElement>document.getElementById("texto-busca")).value);
    let categoria = ((<HTMLInputElement>document.getElementById("categoria")).value);
    let status = ((<HTMLInputElement>document.getElementById("status")).value);
    let tipo = ((<HTMLInputElement>document.getElementById("tipo")).value);
    let ia = ((<HTMLInputElement>document.getElementById("ia")).value);
    let dataDe = ((<HTMLInputElement>document.getElementById("data-de")).value);
    let dataAte = ((<HTMLInputElement>document.getElementById("data-ate")).value);
  
    let busca: Busca = {
      categoria: categoria,
      dataDe: dataDe,
      DataAte: dataAte,
      ia: ia,
      nome: nome,
      status: status,
      tipo: tipo
    };

    console.log("Realizar busca de:", busca);

    this.api.filtrarBusca(busca).subscribe({
      next: res => {
        console.log("Retorno POST: ", res);
      },
      error: erro => {
        console.error(erro)
      }
    })
  }

}
