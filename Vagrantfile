Vagrant.configure('2') do |config|



  # CONFIGURA EL NOMBRE DE LA "BOX" ESCOGIDA PARA NUESTRA VM
  config.vm.box = 'snowmetiv'

  # URL DONDE SE ENCUENTRA LA BOX
  config.vm.box_url = 'https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box'

  #PATH DE LAS CLAVES SSH GENERADAS PARA LA CONEXION A NUESTRA VM
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  #UTILIZADO PARA LA SINCRONIZACIÓN DIRECTA DE LAS CARPETAS.EN CASO DE NO PONERLO AL EJECUTAR VAGRANT UP , EMPEZARÁ A PREPARAR LAS SMB FOLDERS Y DEBEREMOS INTRODUCIR LAS CREDENCIALES.

  config.vm.synced_folder ".", "/vagrant", disabled: true



  config.vm.provider :azure do |azure, override|

    # VARIABLES DE ENTORNO QUE LE PASAMOS 
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET'] 
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']


    # CONFIGURACION DE LA VM DE AZURE. Nombre / Tamaño / Puerto TCP
    azure.vm_name = 'snowmetiv'
    azure.vm_size = 'Standard_A1'
    azure.tcp_endpoints = '80'
    

  end
    

    
    # PROVISIONAMIENTO CON ANSIBLE. RUTA AL ARCHIVO QUE CONTIENE LOS SCRIPTS QUE EJECUTAMOS PARA EL PROVISIONAMIENTO "PLAYBOOK.YML"
  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end
