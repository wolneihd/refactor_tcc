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

  constructor(private shareService: ShareService) { }

  filtrarMensagem() {
    this.shareService.mostrarFiltrarResponder(true, false);
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
}
