# Flask Web with MYSQL Database

This project is about create a flask web and mysql with docker compose and show the result of the table in the web 

## Project Overview 

The stages for the project : 

1. **Flask server**: I create a flask server with the function and the api GET methods for the connection and to show the table .
2. **MYSQL init.sql**: I create the file with the config inside of createing the table and the employees .
3. **Dockerfile**: Image for the flask server to use in the docker-compose 
4. **Docker Compose up**: Config the file and then `docker-compose.yml up --build`.


### Stage 1 : Flask server 
- At the start i install the modules i need for the webapp : 'Flask' , 'mysql.connector' , 'jsonfy' 

    ```bash
    from flask import Flask, jsonify
    import mysql.connector
    
    ```
- After that i need to create the connection fo the mysql database `def connection_to_mysql()` , so i check on the internet ways to do that and i found a way to make a function with directory in python for enter the info to connect to the database . 
    
- I start createing the `def employees()` and before that i needed to add the API Call to show the table result and i use GET methods :
        
    ```bash
    @app.route('/' ,methods=['GET'])
    ```
- In the function of the `employees()` i start work on the pull of the table and to show it in the web , 
    1. I call to the function `def connection_to_mysql()` to get the info of the connection and enter the vlaue to the connection function for the import i add (mysql.connector).

    2.  I use the `cursor` object for create a query  ( cursor is the intermediary between the falsk server and the mysql database). the query i use it to show all the values i have in the table employees :
        ```bash
        con = connection.cursor()
        con.execute("SELECT * FROM employees")
        ```
    3. The `fetchall()` object is to return all the rows i have from that query i ask to show and close the query. 

    4. Create a list of all the employees and print it in a rows with useing a for loop to enter all the rows i have in the table 
        ```bash 
        employees_list  =   [{"id": row[0], "name": row[1], "role": row[2]} for row in show_rows]
        ```
    5. The list is return in html : (photo)

- Start the Flask Server in localhost `app.run()` .

- I run the flask server local on my compuer just to see if i get errors form the logs (i create a function with "Hello world response" in /hello_world) . Use : 
    ```bash
    cd webapp/
    python3 app.py
    ```


### Stage 2 : MYSQL init.sql File 

- First i create the table for enter the values i need , the table i called **employees** with a 3 parametes : 
    1. **ID**: type int and it all the time grow when i enter new value and make the id a primary key(you cant change and add by your self a id ).

    2. **Name**: type VARCHAR and can get max 100 letters .

    3. **Role**: type VARCHAR and can get max 100 letters .

- After that i need to enter a values to the table and i use the `INSERT INTO` commend to enter the values to the **employees** table . 
    ```bash
    INSERT INTO employees (name , role )
    VALUES 
    ('Bar' , 'DevOps'),
    ('Gal' , 'Network Engineer'),
    ('Yaniv' , 'Junior Network Engineer');
    ```

### Stage 3 : Dockerfile 

- To streamline my workflow, I created a Dockerfile to directly install my Python code along with all the necessary libraries.

- I take python slim image for my Dockerfile `python:3.10-slim ` , i dont need large configuration of a large python image , the slim image is more lightweight and efficient, reducing the overall size of the container and focusing only on the essentials required for my application.

- Create a directory and copy the webapp directory to the directory i create that called webapp . 
- I export the continer when it need to be run to port 5000 for the flask server . 
- Install all the libery i need for the code in the `requirements.txt` file and make a cmd commend for start the flask server :
    ```bash 
    CMD ["python3" , "app.py"]
    ```

### Stage 4 : Docker Compose up

- Now i need to enter create two continer that need to communicate with each other and set on the same network . 

- at the first i create the flask service , i make a build for the Dockerfile (`build: ./webapp/`)  it know to find the Dockerfile and make a build to the image . 

- I need to enter a name for the continer **"flask-web"** and export the continer to port 5000 and connect the continer to the network that i create leter.(for make a clean upload i make a depends_on call that with for the mysql service to get up and after that start the flask service).  
    ```bash 
    container_name: flask-web
    ports:
      - "5000:5000"
    depends_on:
      - 'mysql'
    networks:
      - flask-web
    ```

- now i make the mysql service , enter the image for the mysql `image: mysql:latest` and call the continer **"mysql-flask"** . i need to enter the same env i make in the flask server image (with the same password and username .): 
    ```bash 
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_USER: admin 
      MYSQL_PASSWORD: admin
      MYSQL_ROOT_HOST: 0.0.0.0
      MYSQL_DATABASE: employees
    ```
- export the mysql service to port 3306 ("3306" is the port that the mysql know to lisen to) , add the service to the same network that the flask-web is in . 

- for the SQL Script i create earlier i take the path of the `init.sql` file and copy it to the docker entrypoint (any file i put in this folder will start automatically) the path is : 
    ```bash
    volumes:
    - ./init-db/init.sql:/docker-entrypoint-initdb.d/init.sql
    ```

- after all that i create the network with the default driver that create a separate network : 
    ```bash 
    networks:
        flask-web:
            driver: bridge
    ```

- now i need to make all the commend docker compose up and see if the web is working . i do the next commend for that : 
    ```bash 
    docker-compose up --build 
    ```
- the `docker-compose up` make all the continers get up and the flag `--build` for the Dockerfile i install in the flask service . 


## Bonus -  K8s app 






    