# Despliegue desde 0 de un microservicio en la nube

Vamos a dividir en 3 partes el despliegue de este microservicio desde 0 en la nube :

- 1.Provisionamiento
- 2.Creación maquinas virtuales
- 3.Despliegue

## Provisionamiento

En esta parte , hemos utilizado el software Ansible para poder satisfacer todos los requisitos necesarios para que nuestro microservicio funcione correctamente en la maquina virtual que desplegaremos en el siguiente punto. 

Primero instalamos Ansible y modificamos el archivo de hosts , en mi caso creado en el mismo directorio del microservicio ( Proyecto-IV/provision/hosts ).

El archivo hosts : 

    - [snowmetiv]
    - 104.42.74.87 ansible_ssh_user=vagrant

He puesto "ansible_ssh_user=vagrant" para forzar a utilizar el usuario "vagrant" para el acceso a nuestra maquina virtual en azure. 

El archivo que vamos a ejecutar desde Ansible es **playbook.yml**, lo ejecutaremos mediante el comando ***ansible-playbook playbook.yml*** el cual posteriormente incluiremos en el Vagrantfile.

Archivo playbook.yml : [Playbook.yml](https://github.com/vaderrama/Proyecto-IV/blob/master/provision/playbook.yml)

Destacamos del archivo las 3 primeras lineas : 

    hosts: all
    become: yes
    remote_user: vagrant

La primera , se refiere a coger del archivo **hosts** todos los disponibles.
La segunda , sustituye al comando **sudo** en las siguientes lineas para no tener que utilizarlo
La tercera usa como usuario remoto siempre el que indicamos , en este caso "vagrant"

El resto de las instrucciones son referidas a su "name". Utilizandolas para diferentes propositos como instalar pip , o clonar el repositorio de GitHub.

Ejecución de Ansible-playbook playbook.yml : 

![Ansible](img/n7.png)


## Creación maquinas virtuales

En este punto , he utilizado Vagrant para la orquestación en la creación de las maquinas virtuales , ademas de Azure para el despliegue en la nube de las mismas. 

Para ello , es necesario crear un archivo llamado Vagrantfile.
Archivo  Vagranfile : [Vagrantfile](https://github.com/vaderrama/Proyecto-IV/blob/master/Vagrantfile)

En este archivo se han utilizado unas reglas específicas para el uso y despliegue de una máquina virtual con Vagrant y Azure. 
Ademas , se necesita exportar las variables de entorno que podemos observar en el archivo , como son : **TenantID , ClientID, ClientSecret , SubscriptionID**

**tenant_id:** El  Tenant ID de tu directorio activo de Azure.
**client_id:** El Client ID de la aplicacion de tu directorio activo de Azure.
**client_secret:** El Client Secret de la aplicacion de tu directorio activo de Azure.
**subscription_id:** La  "Azure Subscription ID"  que has elegido usar.

Para su obteción hemos necesitado hacer "login" en Azure desde nuestro terminal , asi como crear un directorio activo de azure.  
    
    - az login
    - az ad sp create-for-rbac --name snowmetiv
    
Lo que nos devuelve 

![login](img/n1.png)
![creardirectorio](img/n2.png)

En el archivo "Vagrantfile" disponemos de varias lineas comentadas y explicadas. En concreto esta linea    :
-       config.vm.synced_folder ".", "/vagrant", disabled: true

He decidido dejarla debido a la necesidad de introducir las credenciales del SMB en caso de no existir en el Vagrantfile. Puede verse en la siguiente imagen : 

![vagrantfileLinea](img/vr1.png)


Tambien disponemos de 3 lineas donde podemos configurar caracteristicas de la maquina virtual , como su nombre , tamaño o puerto ( Se pueden utilizar muchas mas configuraciones opcionales , pero con estas es suficiente para nuestro proyecto ) : 

    azure.vm_name = 'snowmetiv'
    azure.vm_size = 'Standard_A1'
    azure.tcp_endpoints = '80'

Al final del archivo se puede ver la ejecución del script creado anteriormente para el provisionamiento. 


    - config.vm.provision :ansible do |ansible|
        ansible.playbook = "provision/playbook.yml"
    end
    
    
    

Una vez hemos exportado las variables de entorno y hemos configurado correctamente vagrant y ansible , procedemos a hacer ; 

    vagrant up --provider=azure
    

![vagrantUp](img/n3.png)

Una vez terminada la ejecución del comando anterior , podemos ir a Azure para ver como se han creado todos los recursos necesarios automaticamente 

![Azure](img/n4.png)


## Despliegue


En el despliegue he utilizado Fabric , un software para poder llevar a acabo ordenes de manera automática a traves de ssh.

Para su instalación hemos utilizado esta orden :

    - pip install "fabric<2"

Ya que otras versiones no funcionan correctamente con nuestras necesidades.

Para ello necesitamos crear un archivo ***fabfile.py***

Archivo fabfile.py : [Fabfile.py](https://github.com/vaderrama/Proyecto-IV/blob/master/despliegue/fabfile.py)
Este archivo consta de diferentes funciones que utilizamos para ejecutar en nuestra maquina , como por ejemplo Iniciar el servicio. 

En el archivo , vienen comentadas las diferentes lineas utilizadas para la creacion de las funciones necesarias. En este caso disponemos de 3 funciones : 

- Iniciar : Inicia el microservicio
- Actualizar : Actualiza el repositorio desde Github. Primero lo borra y luego vuelve a descargarlo 
- Borrar : Borra el proyecto guardado. 


La orden que necesitamos utilizar para realizar alguna de las funciones de despliegue , por por ejemplo iniciar el servicio seria :

    - fab -f fabfile.py -H vagrant@157.56.166.183 Iniciar
    


La dirección donde podemos acceder a la maquina : 

    - http://snowmetiv.westus.cloudapp.azure.com
   


