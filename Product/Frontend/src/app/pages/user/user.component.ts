import { Component, OnInit } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';
import { Observable } from 'rxjs/Observable';
import { Movie } from '../../@core/data/movieClass'
@Component({
  selector: 'ngx-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss'],
})
export class UserComponent implements OnInit {
  data: any;
  movies: string[];
  obj: any;
  test: string= 'test';
  constructor(private dataHandlerService: DataHandlerService) {
   }

  ngOnInit() {
    this.getData();
    this.extractData();

  }
  getData() {
    this.dataHandlerService.getData().subscribe((data) => {
      this.data = data;
      // console.log(this.data); not allowed by lint ?
    }); // Converts the data making it reachable in the htm file
  }
  extractData() {
    return null;
  }

}
