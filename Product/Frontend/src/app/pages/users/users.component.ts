import { Component, OnDestroy, OnInit, Input, ViewChild } from '@angular/core';
import { DataHandlerService} from '../../@core/data/data-handler.service';
import { UsersD3BarComponent } from './users-components/users-d3-bar.component'
/*
  Author: Anton Bergström, Ariyan Abdulla, David Schutzer, Bamse
  Date: 2017-09-30
  Last update: 2017-11-23 by Bamse & David
  This contains the different components used on the recommendation page.
*/

@Component({
  selector: 'ngx-users',
  styleUrls: ['./users.component.scss'],
  templateUrl: './users.component.html',
})

export class UsersComponent implements OnInit {

  @ViewChild( UsersD3BarComponent ) usersD3BarComponent: any;
  model = {
    male: true,
    other: true,
    female: true,
    fromAge: 0 ,
    toAge: 200 ,
  };

  movies: string[];
  data: any;
  value: any= '0 - 200';
  modalHeader1 = 'Graph displaying the number of times a movie has been recommended';
  modalHeader2 = 'List for the top recommended content';
  modalHeader3 = 'Demographic settings';
  modalContent1 = `This graph shows the number of times a movie has been recommended in total from Coogl3's algorithm.
  Each bar represent the number of times a specific movie has been recommended to all users.
  The movie that has been recommended the most is represented by the highest bar.
  This graph reveals the movies that have been recommended the most for all users
  based on the demographic settings that have been set.`;
  modalContent2 = `This list shows the top recommended movies and their titles.
  The first movie in the list is the movie that has been recommended the most according
  to the demographic settings that have been set.`;
  modalContent3 = `Default setting: all users in the database are taken into consideration.
 Use the numbered buttons to change the age interval.
 Use the gender buttons to change the gender demographic.
 By toggling between different ages and genders one can see which movies are
 recommended to different users based on these factors.`;

  paginationModel = 1;

  iconToolbarModel = {
    one: false,
    two: false,
  };
  constructor(private dataHandlerService: DataHandlerService) {}

  ngOnInit() {
    this.getDemoData();

  }
  public getData() {
      this.dataHandlerService.getData().subscribe((data) => {
      this.data = data;
    }); // Converts the data making it reachable in the htm file
  }
  getDemoData() {
    this.dataHandlerService.getMetaRecommendationsData(
      this.model.fromAge, this.model.toAge, this.model.male,
      this.model.female, this.model.other,
    ).subscribe((data) => {
       this.data = data;
    });
    this.usersD3BarComponent.getData();
  }
   setAge(fromAge: number, toAge: number) {
    this.model.fromAge = fromAge;
    this.model.toAge = toAge;
    this.getDemoData();
  }
   enableGender() {
     return null;
   }
}
