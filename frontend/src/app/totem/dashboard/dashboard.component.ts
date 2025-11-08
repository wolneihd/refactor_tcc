import { Component, OnDestroy } from '@angular/core';
import { NabvarConfigComponent } from '../../config/nabvar-config/nabvar-config.component';
import { ApiService } from '../../services/api.service';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { CommonModule } from '@angular/common';
import { FiltrarTotemComponent } from "../filtrar-totem/filtrar-totem.component";
import { interval, Subscription } from 'rxjs';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    NabvarConfigComponent,
    NgxChartsModule,
    FiltrarTotemComponent
  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnDestroy {

  dadosTotem: any[] | null = null;
  private intervalSub: Subscription | null = null;

  constructor(private api: ApiService) { }

  ngOnInit() {
    // Executa imediatamente
    this.carregarDados();

    // Depois executa a cada 2 segundos
    this.intervalSub = interval(2000).subscribe(() => {
      this.carregarDados();
    });
  }

  carregarDados() {
    this.api.obterDadosTotem().subscribe({
      next: res => {
        this.dadosTotem = res;
        console.log(this.dadosTotem);
      },
      error: erro => {
        console.error(erro);
      }
    });
  }

  ngOnDestroy() {
    // Evita vazamento de memória ao destruir o componente
    this.intervalSub?.unsubscribe();
  }

  // Definindo as opções do gráfico
  showXAxis = true;
  showYAxis = true;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  xAxisLabel = 'Categorias';
  yAxisLabel = 'Quantidade de avaliações';
}
