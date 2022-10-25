## Disturbed Window Monsters
## Roster: David Chen, William Guo, Marc Jiang
## K17: Shell Game
## 2022-Oct-24
## Time Spent: 1 hour
---  

# SQLITE BASIC INFO
- Data types that can be inserted into tables include:
    1. TEXT (a string)
    2. INTEGER 
    3. REAL
    4. NUMERIC (defaults to integer but can be floats)
    5. BLOB (no specific data type)
- Attributes for columns:
    1. PRIMARY KEY (each column value has to be unique and can't be NULL)
    2. NOT NULL (no entry can be null)
    - EX:
        ```
        CREATE TABLE duckies (name TEXT NOT NULL, period INTEGERY PRIMARY KEY)
        ```

# SQLITE SHELL BASIC COMMANDS
- Start sqlite shell by creating database with: 
    ```
    sqlite3 <name>.db
    ```
- Create a table with:
    ```
    CREATE TABLE <table_name> (<column_name> <data type>);
    ```

- Add values to table with:
    ```
    INSERT INTO <table_name> (<value>);
    ```
    - If your table has more than one value, you should denote with:
        ```
        INSERT INTO <table_name> VALUES (<value1>, <value2>...);
        ```
- To view tables created:
    ```
    .table
    ```
- To view values within table:
    ```
    SELECT * FROM <table_name>;
    ```
    - You can also be more specific with filters such as:
        ```
        SELECT <field_name> FROM <table_name>
        ```

        OR

        ```
        SELECT <field_name> FROM <table_name> WHERE insert_value_filter
        ```
- Helpful commands:

    ```
    .help 
    ```
    - gives you a whole list of different shell commands and descriptions of what each commands does 
