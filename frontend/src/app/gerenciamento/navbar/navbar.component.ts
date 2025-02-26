import { Component, inject } from '@angular/core';
import { ShareService } from '../../services/share.service';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { ContatoComponent } from '../../login/contato/contato.component';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [MatDialogModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

  readonly dialog = inject(MatDialog);
  isFiltrarSelecionado: boolean = false;

  constructor(private shareService: ShareService) { }

  responderMensagem() {
    this.isFiltrarSelecionado = !this.isFiltrarSelecionado;
    this.shareService.mostrarFiltrarResponder(this.isFiltrarSelecionado, false);
  }

  abrirDialogContato() {
    const dialogRef = this.dialog.open(ContatoComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  abrirConfigurar() {
    window.location.href = 'http://localhost:4200/configurar';
  }
}
