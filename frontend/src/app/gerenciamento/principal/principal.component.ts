import { Component } from '@angular/core';
import { ListaDadosComponent } from "../lista-dados/lista-dados.component";
import { NavbarComponent } from "../navbar/navbar.component";
import { ResponderComponent } from "../responder/responder.component";
import { CommonModule } from '@angular/common';
import { FiltrarComponent } from "../filtrar/filtrar.component";
import { ShareService } from '../../services/share.service';

@Component({
  selector: 'app-principal',
  standalone: true,
  imports: [ListaDadosComponent, NavbarComponent, ResponderComponent, CommonModule, FiltrarComponent],
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.css'
})
export class PrincipalComponent {

  btnResponder:boolean = false;
  btnFiltrar:boolean = false;
  public boxFiltrarResponder:string = '';

  constructor(private shareService: ShareService) {}

  ngOnInit(): void {
    this.shareService.value.subscribe(texto => {
      console.log('Mensagem recebida:', texto); 
      this.boxFiltrarResponder = texto;
      if (texto === 'filtrar' && this.btnFiltrar === false) {
        this.btnResponder = false;
        this.btnFiltrar = true;
      } else {
        this.btnResponder = false;
        this.btnFiltrar = false;
      }
    });
  }

}
