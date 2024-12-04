This directory contains the necessary SQL files for constructing my database.

00_packtrackDB.sql
SQL script to create and use our database, create the tables, and populate those tables

README.md
README file written in markdown that intruduces the project to the user and outlines the file structure.

reset.sql
SQL script to delete all created tables and reset the database. Helpful for testing during development.

How to re-bootstrap our database
1. run the reset.sql file to drop all existing tables
2. run the 00_packtrackDB.sql file to recreate and repopulate the tables
