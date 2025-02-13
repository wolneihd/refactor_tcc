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

  constructor(private shareService: ShareService) { }

  responderMensagem() {
    console.log('Abrir caixa de filtro:'); // Depuração
    this.shareService.changeValue('filtrar');
  }

  abrirDialogContato() {
    const dialogRef = this.dialog.open(ContatoComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}
