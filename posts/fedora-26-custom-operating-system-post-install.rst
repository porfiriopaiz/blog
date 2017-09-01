.. title: Fedora 26 Custom Operating System post install
.. slug: fedora-26-custom-operating-system-post-install
.. date: 2017-08-31 16:26:39 UTC-06:00
.. tags: dnf, fc26, postinstall
.. category: floss
.. link: 
.. description:
.. type: text

En la última publicación expliqué cómo hacer una instalación mínima de Fedora
25, han pasado varios meses desde entonces y Fedora 26 ya salió, siguiendo los
mismos pasos lo instalé en mi laptop y a continuación documentaré mi "post
install".

.. TEASER_END

Dado que esta instalación es mínima, los paquetes instalados no proveen soporte
para tarjetas de redes inalámbricas. Si bien es cierto durante la instalación
Anaconda ofrece dicho soporte, una vez instalados los paquetes mínimos, estos
no incluyen los controladores necesarios, por lo que para esta primera parte
debo conectar mi laptop a una red cableada.

Luego de verificar la conexión de red cableada, lo primero que hice fue editar
el archivo de configuración de ``dnf`` y agregar las siguientes líneas como
root con los siguientes comandos:

.. code-block:: console

   echo 'fastestmirror=true' >> /etc/dnf/dnf.conf
   echo 'deltarpm=false' >> /etc/dnf/dnf.conf
   echo 'keepcache=true' >> /etc/dnf/dnf.conf

De esta forma que aseguro que ``dnf`` siempre use el mirror más eficiente; que
no use use ``*.drpm``'s para realizar las actualizaciones, sino que en su lugar
siempre descargue ``*.rpm``'s; y que guarde cada paquete que se descargue en la
caché.

A continuación reiniciamos.

.. code-block:: console
   
   reboot

``dnf`` tiene un servicio y un timer que me resultan muy molestos, ambos se
aseguran de actualizar la caché de metadatos de paquetes con cierta frecuencia,
esto es algo que me gusta hacer cuando yo quiero y lo necesito, no cuando a
``dnf`` se le antoje así que eso se corrije de la siguiente forma:

.. code-block:: console

   su -c 'systemctl disable dnf-makecache.service'
   su -c 'systemctl disable dnf-makecache.timer'

Reiniciamos.

.. code-block:: console
   
   reboot

Una vez personalizado el archivo de configuración de ``dnf`` y deshabilitados
los molestos servicios y timer, procedo a limpiar la caché y a regenerarla,
esta vez, todos los comandos lo ejecutaré como usuario normal, pasándole dichos
comandos a root como un parámetro:

Este crea la caché de metadatos de paquetes para mi usuario `mortal`:

.. code-block:: console

   dnf clean all
   dnf makecache

Este crea la caché de metadatos de paquetes para mi usuario `dios`:

.. code-block:: console
   
   su -c 'dnf clean all'
   su -c 'dnf makecache'

Existe la posibilidad de que durante la instalación no haya marcado la opción
de descargar las versión más reciente de los paquetes a instalar, para
verificar si hay actualizaciones disponibles:

.. code-block:: console
   
   su -c 'dnf --refresh check-update'

Para descargar e instalar las actualizaciones:

.. code-block:: console
   
   su -c 'dnf upgrade'

Y reiniciamos:

.. code-block:: console
   
   reboot

En mi laptop uso GNOME Shell como entorno de escritorio así que procederé a
instalarlo usando un grupo de paquete especifico que provee las colección de
paquetes necesaria para instalar hacer de mi Fedora Custom Operating System un
Fedora Workstation:

.. code-block:: console
   
   su -c 'dnf groups install workstation-product-environment'

Una vez descargados e instalados los paquetes, cambiamos el `init mode` por
defecto de `multi-user.tarjet` a `graphical.tarjet`, de lo contrario, cuando
reiniciemos no arrancará en modo gráfico.

También debemos habilitar el servicio de `login` gráfico, si no, aunque hayamos
habilitado el modo gráfico el login seguirá siendo en modo texto:

.. code-block:: console
   
   su -c 'systemctl set-default graphical.target'
   su -c 'systemctl enable gdm.service'
   reboot 

Si todo ha salido bien, ya debes estar corriendo Fedora 26 Workstation con
GNOME Shell.

Antes de abrir cualquier aplicación, lo primero es abrir una terminal y
ejecutar el siguiente comando:

.. code-block:: console
   
   gsettings set org.gnome.nautilus.preferences default-sort-order type

De esta forma cuando abra ``Nautilus`` me mostrará todos los archivos ordenados
por externsión.

.. code-block:: console

   su -c 'dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'

Refrescamos la caché, esto solo descargará los metadatos del repositorio de
RPMFusion:

.. code-block:: console

   su -c 'dnf check-update'

Antes de copiar cualquier archivo desde mis respaldos, debo reconfigurar el
molesto ``tracker`` y a todos sus amigos:

.. code-block:: console

   su -c 'dnf install tracker-preferences'
   mkdir ~/.config/autostart
   cp /etc/xdg/autostart/tracker* ~/.config/autostart
   cd ~/.config/autostart
   sed -i 's/X-GNOME-Autostart-enabled=true/X-GNOME-Autostart-enabled=false/' tracker*

Verificamos el estado de ``tracker``:

.. code-block:: console

   tracker status

Y le hacemos un `hard reset`:

.. code-block:: console

   tracker reset --hard

A continuación instalo grupos de paquetes que proveen librerías necesarias para
otros programas como ``vim``, en otro post explicaré por qué es útil tenerlas:

.. code-block:: console

   su -c 'dnf -y groups install c-development'
   su -c 'dnf -y groups install development-libs'
   su -c 'dnf -y groups install development-tools'
   su -c 'dnf -y groups install fedora-packager'
   su -c 'dnf -y groups install rpm-development-tools'
   su -c 'dnf install automake gcc gcc-c++ kernel-devel cmake'
   su -c 'dnf install python-devel python3-devel'
   su -c 'dnf install monodevelop'
   su -c 'dnf install golang'
   su -c 'dnf install nodejs'
   su -c 'dnf install rust'
   su -c 'dnf install cargo'
   su -c 'dnf install python3-virtualenv'
   su -c 'dnf install python3-pip'
