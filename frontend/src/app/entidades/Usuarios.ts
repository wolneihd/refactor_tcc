// mensagem
export interface Mensagem {
  id: number;
  analise_ia: string;
  categoria: string;
  feedback: string;
  llm: string;
  texto_msg: string;
  timestamp: number;
  tipo_mensagem: string;
  usuario_id: number;
  checkbox: boolean;
  respondido: number;
}

// usuario
export interface Usuario {
  id: number;
  userID_Telegram: number;
  nome: string;
  sobrenome: string;
  mensagens: Mensagem[];
}
