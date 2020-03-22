import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SearchComponent } from './search/search.component';
import { MissionComponent } from './mission/mission.component';


const routes: Routes = [
  { path: 'search', component: SearchComponent },
  { path: 'mission', component: MissionComponent },
  { path: '',   redirectTo: '/search', pathMatch: 'full' },
  { path: '**',   redirectTo: '/search', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
