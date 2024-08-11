import {Component, EventEmitter, Output, ViewChild, viewChild} from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar';
import { MatProgressBarModule } from "@angular/material/progress-bar";
import { CommonModule } from '@angular/common';
import {SolveComponent} from "../solve/solve.component";
import {DownloadComponent} from "../download/download.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    FormsModule,
    HttpClientModule,
    MatProgressBarModule,
    MatSnackBarModule,
    CommonModule,
    SolveComponent,
    DownloadComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  formData = new FormData();
  title = 'FrontendAssignmentSolver';
  isLoading = false;

  // @Output() documentReady = new EventEmitter<void>();
  @ViewChild(SolveComponent) solver?: SolveComponent;

  constructor(private http: HttpClient, private snackBar: MatSnackBar) { }

  onFileChange(event: any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.formData.append('file', file);
    }
  }

  onSubmit(form: any) {
    this.formData.append('name', form.value.name);
    this.formData.append('email', form.value.email);
    this.formData.append('subject', form.value.subject);
    this.formData.append('academicLevel', form.value.academicLevel);
    this.formData.append('additionalInfo', form.value.additionalInfo);
    this.formData.append('gradeSemesterYear', form.value.gradeSemesterYear);
    this.formData.append('institutionName', form.value.institutionName);
    this.formData.append('message', form.value.message);

    this.isLoading = true;

    this.http.post('http://localhost:5000/solve-assignment', this.formData).subscribe({
      next: (response: any) => {
        this.isLoading = false;
        this.snackBar.open('Solution document is ready!', 'Close', {
          duration: 30000
        });
        // Handle the response, e.g., trigger file download

        this.solver.fetchFiles();

        // Reset the form and FormData
        form.reset();
        this.formData = new FormData();
      },


      error: (error) => {
        this.isLoading = false;
        this.snackBar.open('Error while solving the assignment.', 'Close', {
          duration: 30000
        });
      }
    });
  }
}

