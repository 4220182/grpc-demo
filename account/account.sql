/*
https://www.postgresqltutorial.com/postgresql-create-table/
createdb demo -U postgres -h 192.168.5.4
psql -h 192.168.5.4 -U postgres demo -f ~/PycharmProjects/grpc-demo/account/account.sql
*/
CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	info VARCHAR ( 50 ) NOT NULL
);