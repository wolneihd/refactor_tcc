import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Mensagem, Usuario } from '../entidades/Usuarios';
import { Observable } from 'rxjs';
import { enviroment } from '../environment/environment';
import { Resposta } from '../entidades/Resposta';

const apiUrl = enviroment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  usuarios: Usuario[] = [];

  constructor(private httpClient: HttpClient) { }

  obterDadosTabela(): Observable<Usuario[]> {
    return this.httpClient.get<Usuario[]>(`${apiUrl}`)
  }

  gerarRespostaIA(texto_adicional: string, mensagens: Mensagem[]): Observable<Resposta>{
    const dados = {
      "texto_adicional": texto_adicional,
      "mensagens": mensagens
    }
    return this.httpClient.post<Resposta>(`${apiUrl}/gerar_resposta`, dados)
  }
}
