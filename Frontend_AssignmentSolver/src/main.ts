import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { DownloadComponent} from "./download/download.component";
import { SolveComponent} from "./solve/solve.component";

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));

bootstrapApplication(DownloadComponent, appConfig)
  .catch((err) => console.error(err));

bootstrapApplication(SolveComponent, appConfig)
  .catch((err) => console.error(err));
