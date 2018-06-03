drop table if exists grids;
create table grids (
  id integer primary key autoincrement,
  name text not null UNIQUE,
  grid text not null
);