import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Usuario } from '../entidades/Usuarios';

@Injectable({
  providedIn: 'root'
})
export class ShareService {


  // Usando BehaviorSubject para armazenar e compartilhar dados
  private usuariosSource = new BehaviorSubject<Usuario[]>([]);
  private idSource = new BehaviorSubject<number>(0);
  private boxFiltrar = new BehaviorSubject<boolean>(false);
  private boxResponder = new BehaviorSubject<boolean>(false);

  // Observáveis para serem usados pelos componentes
  usuarios$ = this.usuariosSource.asObservable();
  id$ = this.idSource.asObservable();
  filtrar$ = this.boxFiltrar.asObservable();
  responder$ = this.boxResponder.asObservable();

  constructor() { }

  mostrarFiltrarResponder(filtrar: boolean, responder: boolean) {
    this.boxFiltrar.next(filtrar);
    this.boxResponder.next(responder);
  }

  // Métodos para atualizar os dados
  shareMensagem(usuarios: Usuario[], id: number): void {
    this.usuariosSource.next(usuarios);
    this.idSource.next(id);
  }
}
