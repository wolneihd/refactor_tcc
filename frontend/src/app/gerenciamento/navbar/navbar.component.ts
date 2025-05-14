import { Component, inject } from '@angular/core';
import { ShareService } from '../../services/share.service';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { ContatoComponent } from '../../login/contato/contato.component';
import { enviroment } from '../../environment/environment';

const frontEndUrl = enviroment.frontEndUrl;

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [MatDialogModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  readonly dialog = inject(MatDialog);
  mostrarFiltrar: boolean = false;

  constructor(private shareService: ShareService) { }

  filtrarMensagem() {
    this.mostrarFiltrar = !this.mostrarFiltrar;
    this.shareService.mostrarFiltrarResponder(this.mostrarFiltrar, false);
  }

  abrirDialogContato() {
    const dialogRef = this.dialog.open(ContatoComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirConfigurar() {
    window.location.href = `${frontEndUrl}/configurar`;
  }

  abrirDashboardTotem() {
    window.location.href = `${frontEndUrl}/totem`;
  }

  sair() {
    window.location.href = `${frontEndUrl}/login`;
  }
}
