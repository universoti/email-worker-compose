create  database email_sender ;

\c email_sender

create TABLE emails(
    id serial not null,
    data TIMESTAMP not null DEFAULT
)