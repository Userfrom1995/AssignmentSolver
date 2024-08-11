import {Component, EventEmitter, Input, OnInit} from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {RouterOutlet} from "@angular/router";
import {FormsModule} from "@angular/forms";
import {NgForOf} from "@angular/common";




interface FileData {
  name: string;
  size: string;
  date: string;
  url: string;
}

@Component({
  selector: 'app-solve',
  standalone: true,
  imports: [RouterOutlet, FormsModule, HttpClientModule, NgForOf ],
  templateUrl: './solve.component.html',
  styleUrl: './solve.component.css'
})
export class SolveComponent implements OnInit {
  files: FileData[] = [];
  // private socket$: WebSocketSubject<any>;
  // @Input() documentReadyEvent: EventEmitter<void>;


  constructor(private http: HttpClient ) {
    // this.socket$ = new WebSocketSubject('ws://localhost:5000' +
    //   '');


  }

  ngOnInit(): void {
    this.fetchFiles();

    // this.socket$.subscribe(
    //   message => {
    //     if (message.event === 'file_ready') {
    //       this.fetchFiles();  // Refresh file list when a new file is ready
    //     }
    //   },
    //   error => console.error('WebSocket error:', error),
    //   () => console.log('WebSocket connection closed')
    // );
    // this.documentReadyEvent.subscribe(() => {
    //   this.fetchFiles();
    // });
  }




  fetchFiles(): void {
    this.http.get<FileData[]>('http://localhost:5000/api/files')
      .subscribe(
        (data: FileData[]) => {
          this.files = data.map(file => ({
            ...file,
            url: `http://localhost:5000/api/files/${file.name}`
          }));
        },
        (error) => {
          console.error('Error fetching files', error);
        }
      );
  }

  downloadFile(file: FileData): void {
    window.open(file.url, '_blank');
  }

  deleteFile(file: FileData): void {
    this.http.delete(`http://localhost:5000/api/files/${file.name}`)
      .subscribe(
        () => {
          this.fetchFiles(); // Refresh the file list after deletion
        },
        (error) => {
          console.error('Error deleting file', error);
        }
      );
  }




}
