import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Usuario } from '../entidades/Usuarios';

@Injectable({
  providedIn: 'root'
})
export class ShareService {

  private valueSource = new BehaviorSubject<string>('');
  value = this.valueSource.asObservable();

  // Usando BehaviorSubject para armazenar e compartilhar dados
  private usuariosSource = new BehaviorSubject<Usuario[]>([]);
  private idSource = new BehaviorSubject<number>(0);

  // Observáveis para serem usados pelos componentes
  usuarios$ = this.usuariosSource.asObservable();
  id$ = this.idSource.asObservable();

  constructor() { }

  changeValue(newValue: string) {
    this.valueSource.next(newValue);
  }

  // Métodos para atualizar os dados
  shareMensagem(usuarios: Usuario[], id: number): void {
    this.usuariosSource.next(usuarios);
    this.idSource.next(id);
  }
}
