CREATE table Data_School(
    id serial primary KEY,
    school_name varchar(256) not null,
    principal varchar,
    email varchar not null,
    phone integer,
    address1 varchar,
    tstreet varchar,
    UNIQUE(school_name, email)
);

select * from data_school;

COPY data_school (school_name, principal, email, phone, address1, tstreet) from '/home/alessandra-goncalves/Documents/Python/School_Project/Data_School.csv' with delimiter as ',' CSV HEADER;

select * from data_school;