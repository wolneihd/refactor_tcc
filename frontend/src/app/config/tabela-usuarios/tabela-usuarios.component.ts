import { NgFor } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-tabela-usuarios',
  standalone: true,
  imports: [NgFor],
  templateUrl: './tabela-usuarios.component.html',
  styleUrl: './tabela-usuarios.component.css'
})
export class TabelaUsuariosComponent {

  // Array para armazenar os dados da tabela
  tabela = [
    ['João', 'joao@gmail.com', 'ativo'],
    ['Pedro', 'pedro@gmail.com', 'ativo'],
    ['Maria', 'maria@gmail.com', 'ativo'],
    ['Antônio', 'antonio@gmail.com', 'ativo'],
    ['Sérgio', 'sergio@gmail.com', 'ativo']
  ];

  editarUsuario() {
    alert('todo: editar usuario')
  }

  excluirUsuario() {
    alert('todo: excluir usuario')
  }

}
