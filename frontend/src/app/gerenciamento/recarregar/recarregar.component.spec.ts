import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecarregarComponent } from './recarregar.component';

describe('RecarregarComponent', () => {
  let component: RecarregarComponent;
  let fixture: ComponentFixture<RecarregarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RecarregarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RecarregarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
