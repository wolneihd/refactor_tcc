import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Mensagem, Usuario } from '../entidades/Usuarios';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  usuarios: Usuario[] = [];

  constructor(private httpClient: HttpClient) { }

  obterDadosTabela(): Observable<Usuario[]> {
    return this.httpClient.get<Usuario[]>(`http://127.0.0.1:5000/`)
  }

  gerarRespostaIA(texto_adicional: string, mensagens: Mensagem[]): Observable<any>{
    const dados = { 
      "texto_adicional": texto_adicional,
      "mensagens": mensagens 
    }
    return this.httpClient.post('http://127.0.0.1:5000/gerar_resposta', dados)
  }
}
