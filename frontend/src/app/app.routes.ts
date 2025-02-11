import { Routes } from '@angular/router';
import { ListaDadosComponent } from './lista-dados/lista-dados.component';
import { ResponderComponent } from './responder/responder.component';

export const routes: Routes = [
  { path: 'app-lista-dados', component: ListaDadosComponent },
  { path: 'app-responder', component: ResponderComponent },
  // { path: '', redirectTo: '/app-lista-dados', pathMatch: 'full' },
];
