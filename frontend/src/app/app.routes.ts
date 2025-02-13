import { Routes } from '@angular/router';
import { ListaDadosComponent } from './lista-dados/lista-dados.component';
import { ResponderComponent } from './responder/responder.component';
import { LoginComponent } from './login/login/login.component';

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
  }
];
