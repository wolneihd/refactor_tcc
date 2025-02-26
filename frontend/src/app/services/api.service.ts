import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Mensagem, Usuario } from '../entidades/Usuarios';
import { Observable } from 'rxjs';
import { enviroment } from '../environment/environment';
import { Resposta } from '../entidades/Resposta';
import { Busca } from '../entidades/Busca';

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

  enviarResposta(mensagens: Mensagem[], resposta: string): Observable<any>{
    const dados = {
      "mensagens": mensagens,
      "resposta": resposta
    }
    return this.httpClient.post<any>(`${apiUrl}/responder`, dados)
  }

  filtrarBusca(busca: Busca): Observable<Busca>{
    return this.httpClient.post<Busca>(`${apiUrl}/filtrar`, busca);
  }
}
