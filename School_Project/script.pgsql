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

CREATE table data_student(
    id serial primary KEY,
    firts_name varchar(256) not null,
    last_name varchar(256) not null,
    date_of_birth varchar not null,
    ethnicity varchar,
    gender varchar(1),
    entry_academic_period integer,
    email varchar,
    entry_age integer,
    english_2nd_language BOOLEAN,
    UNIQUE(email)
);