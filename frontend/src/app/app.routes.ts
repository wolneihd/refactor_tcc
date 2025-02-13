import { Routes } from '@angular/router';
import { ListaDadosComponent } from './gerenciamento/lista-dados/lista-dados.component';
import { ResponderComponent } from './gerenciamento/responder/responder.component';
import { LoginComponent } from './login/login/login.component';
import { PrincipalComponent } from './gerenciamento/principal/principal.component';

export const routes: Routes = [
  {
    path: 'main',
    component: ListaDadosComponent
  },
  {
    path: 'main/responder',
    component: ResponderComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'gerenciamento',
    component: PrincipalComponent
  }
];
