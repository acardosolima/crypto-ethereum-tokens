#!/bin/bash

DB_NAME=$1
DB_USER=$2
TABLE_NAME=$4

# Check if the table exists
TABLE_EXISTS=$(psql -U $DB_USER -d $DB_NAME -tAc "SELECT 1 FROM pg_tables WHERE tablename='$TABLE_NAME'")

if [ "$TABLE_EXISTS" != "1" ]; then

  psql -U $DB_USER -d $DB_NAME -c "
    CREATE TABLE $TABLE_NAME (
	address TEXT NOT NULL,
	symbol TEXT,
	name TEXT,
	decimals TEXT,
	total_supply TEXT,
	block_timestamp TIMESTAMP NOT NULL,
	block_number INTEGER NOT NULL,
	block_hash TEXT NOT NULL
    );
  "
  echo "Table $TABLE_NAME created."
else
  echo "Table $TABLE_NAME already exists."
fi
