import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: '/o/example-angular-liferay/app/app.component.html'
})
export class AppComponent {
  title = 'app';

  constructor(private router:Router) {
    this.router.navigateByUrl("/test1")
  }
}
