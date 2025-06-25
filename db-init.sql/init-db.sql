DROP TABLE IF EXISTS BankUser, Account, BankTransaction;

CREATE TABLE BankUser (
	email varchar(255),
	bank_password varchar(255) NOT NULL,
	PRIMARY KEY (email)
);

CREATE TABLE Account (
	email varchar(255) NOT NULL,
	account_name varchar(100) NOT NULL,
	account_type varchar(20) NOT NULL,
	balance decimal(10, 2) NOT NULL,
	interest decimal(5, 2) NOT NULL,
	PRIMARY KEY (email, account_name, account_type),
	FOREIGN KEY (email) REFERENCES User(email)
);

CREATE TABLE BankTransaction (
	transaction_id int NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	account_name varchar(100) NOT NULL,
	account_type varchar(20) NOT NULL,
	transaction_type varchar(20) NOT NULL,
	amount decimal(10, 2) NOT NULL,
	transaction_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	description varchar(255) NULL,
	PRIMARY KEY (transaction_id), 
	FOREIGN KEY (email) REFERENCES User(email),
	FOREIGN KEY (account_name) REFERENCES Account(account_name),
	FOREIGN KEY (account_type) REFERENCES Account(account_type)
);
