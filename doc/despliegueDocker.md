# Despliegue Microservicio con Docker y Heroku


## Despliegue con DockerHub

Hemos utilizado el sistema Docker por su versatilidad a la hora de desplegar aplicaciones web de pequeña capacidad , así como su perfecta integración con GitHub y Travis-CI.

Para ello , necesitamos registrarnos en la web : [DockerHub](https://hub.docker.com/)

- Una vez registrados , podemos crear un repositorio.
- Para poder configurarlo , utilizaremos la documentación de Docker , ya que es sencilla de entender y seguir  [Documentación](https://docs.docker.com/get-started/#docker-concepts)
 
 ### Dockerfile
 - El archivo de configuración de DockerHub , es necesario para la automatización de la creación de una imagen que contiene todo lo necesario para la ejecución de nuestra aplicación. 

### Construcción de la imagen 

- Para la construcción de la imagen de nuestra app , utilizaremos el siguiente comando : 
            
            - docker build -t vaderrama/proyecto-iv .

- Despues de construirla en local , asignamos a nuestra imagen un "Tag" y seguidamente la subimos a DockerHub

            - docker tag vaderrama/proyecto-iv vaderrama/proyecto-iv:deploy
        
- Seguidamente , la subimos con el siguiente comando ;
        
            - docker push vaderrama/proyecto-iv:deploy
            


### Ejecución de la aplicación 

Para poder ejecutar nuestra aplicación ya subida al repositorio creado en Docker , necesitamos tener instalado Docker y utilizar el siguiente comando : 

    - docker run -p 4000:80 vaderrama/proyecto-iv:deploy

Si no encuentra la imagen localmente , la descargará de nuestro repositorio Docker. 

Una vez ejecutada , la aplicación estaria corriendo en la dirección :     http://localhost:4000/


## Despliegue contenedor en Heroku 

Una vez realizados los pasos anteriores , desplegaremos nuestra aplicación como hicimos anteriormente pero esta vez en forma de contenedor. 

 - Creamos una nueva app en la web de heroku ( snowmet-docker ).
 - Creamos el archivo ***heroku.yml*** en nuestro proyecto , este será el encargado de hacer funcionar el despliegue de nuestro contenedor. 
 - Tenemos que decirle a Heroku , que nuestra aplicación será un contenedor , por lo tanto utilizamos : 
                         
            - heroku stack:set container -a snowmet-docker
            
- Subimos nuestra imagen a la aplicación de Heroku 
            
            - heroku container:push web --app snowmet-docker
            
- Finalmente , la desplegamos 

            - heroku container:release web --app snowmet-docker
            
**Despliegue : https://snowmet-docker.herokuapp.com/**
