create database leavedatabase;
use leavedatabase;

create table roles (
    role_id int auto_increment primary key,
    role varchar(100)
);

insert into roles (role) values
("SDE I"),
("Tech Manager"),
("Senior Manager"),
("HR"),
("Software Tester");
select * from roles;

create table department (
    dept_id int auto_increment primary key,
    departments varchar(250)
);

insert into department (departments) values
("Engineering Department"),
("Technical Department"),
("Operations Department"),
("Human Resource Department"),
("Testing Department");
select * from department;

create table user (
    userid int auto_increment primary key,
    username varchar(50) not null,
    password varchar(255) not null,
    email varchar(100) not null,
    fname varchar(50) not null,
    lname varchar(50) not null,
    firstlevelmanager_id int,
    secondlevelmanager_id int,
    role_id int,
    dept_id int,
    foreign key (firstlevelmanager_id) references user(userid),
    foreign key (secondlevelmanager_id) references user(userid),
    foreign key (role_id) references roles(role_id),
    foreign key (dept_id) references department(dept_id)
);
insert into user (username, password, email, fname, lname, firstlevelmanager_id, secondlevelmanager_id, role_id, dept_id) values
('sant', 'password12', 'santosh360@gmail.com', 'santosh', 'kumar', null, null, 3, 3),  -- senior manager 
('rk', 'password123', 'rakesh324@gmail.com', 'rakesh', 'chaudhary', 1, null, 2, 2),  -- tech manager 
('ak', 'password1234', 'akash123@gmail.com', 'akash', 'patil', 2, 1, 1, 1),  -- sde 1 
('kt', 'password12345', 'ketan500@gmail.com', 'ketan', 'gupta', 2, 1, 5, 5),  -- software tester
('chir', 'password123456', 'chirag400@gmail.com', 'chirag', 'saksena', 1, null, 4, 4);  -- hr
select * from user;

create table leave_type (
    leave_id int auto_increment primary key,
    type_of_leave varchar(255)
);

insert into leave_type (type_of_leave) values
("sick leave"),
("casual leave"),
("vacation leave"),
("maternity leave"),
("paternity leave"),
("emergency leave");

select * from leave_type;

create table leave_requests (
    requestid int auto_increment primary key,
    userid int,
    leave_type_id int,
    leave_creation_time datetime default current_timestamp,
    start_date date not null,
    end_date date not null,
    status enum('pending', 'approved', 'rejected') not null,
    approver_id int,
    remark varchar(255),
    approval_time timestamp null,
    foreign key (userid) references user(userid),
    foreign key (leave_type_id) references leave_type(leave_id),
    foreign key (approver_id) references user(userid)
);

insert into leave_requests (userid, leave_type_id, start_date, end_date, status, approver_id, remark) values
(1, 1, '2024-01-01', '2024-01-03', 'pending', 2, 'medical leave request'),  
(2, 2, '2024-02-05', '2024-02-07', 'pending', 3, 'vacation request'); 

select * from leave_requests; 
