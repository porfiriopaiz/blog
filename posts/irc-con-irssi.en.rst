.. title: IRC con irssi
.. slug: irc-con-irssi
.. date: 2016-11-02 15:26:28 UTC-06:00
.. tags: irc, cli
.. category: floss
.. link: 
.. description: Automatizando la conexión a IRC con irssi.
.. type: text

Desde mis inicios en el Software Libre y GNU/Linux, una de las caracteristicas
que atrapó mi atención es el poder que tiene la linea de comandos en este
sistema operativo. Desde moverse entre los diferentes directorios hasta
instalar un sistema operativo completamente desde cero, son algunas de las
tareas rutinarias que se pueden llevar acabo desde la terminal.

En este post les mostraré como configurar irssi para automatizar algunos de los
pasos que se deben llevar acabo para poder acceder a una sala de chat, como lo
es conectarse al servidor, autenticarse y posteriormente ingresar a los
diferentes canales que sean de nuestro interés.

Instalando irssi
================

Para instalar irssi en fedora, basta con abrir una terminal y escribir el
siguiente comando:

.. code-block:: console

    su -c 'dnf install irssi'

Y para instalar irssi en debian:

.. code-block:: console

    su -c 'apt-get install irssi'

Ejecutando irssi
----------------

Para correr irssi abrimos una terminal y escribimos el siguiente comando:

.. code-block:: console

    irssi

Configuraciones
===============

Configuraciones de Servidor
---------------------------

Todas estos comandos deben ser ejecutadas en una sesión de irssi.

Primero removeremos la configuracion existente del servidor que necesitamos
automatizar. Con ``/server list`` podremos visualizar los servidores existentes:

.. code-block:: console

    /server list

En nuestro caso eliminaremos la configuración existente de Freenode.

.. code-block:: console

    /server remove chat.freenode.net

Y añadiremos la nueva configuración con el siguiente comando:

.. code-block:: console

    /SERVER ADD -auto -network Freenode chat.freenode.net 6667 your_nick_password

Donde ``-auto`` define la conexión al servidor de Freenode como automática y
``your_nick_password`` es tu contraseña de usuario en Freenode.

Añadiendo Canales
-----------------

De igual manera es posible añadir a que canales de este servidor nos queremos
conectar automáticamente en cada inicio de sesión, para ello ejecutamos el
siguiente comando en nuestra sesión de irssi:

.. code-block:: console

    /channel add -auto #fedora Freenode

Donde ``-auto`` permite que ingresemos al canal ``#fedora`` en ``Freenode`` de
forma automática en cada inicio de sesión.

Para terminar, cada vez que hagamos un cambio en nuestra configuración será
necesario salvar los cambios con el comando:

.. code-block:: console

    /save

irssi toma el user name de tu sesión actual como el usuario para tu sesión en
irc, para evitar que esto suceda en caso de que el nombre de tu sesión en el
sistema no coincida con tu usuario en Freenode, deberas ejecutar irssi con el
siguiente parámetro:

.. code-block:: console

    irssi -n nick

Donde ``nick`` es tu usario de IRC en Freenode.

Una vez que hayas añadido todos tus canales de interés que se encuentran en el
servidor de Freenode y guardado los cambios, solo necesitaras ejecutar en una
terminal el comando ``irssi`` y automáticamente te conectarás al servidor y
a todos los canales que hayas añadido sin necesidad de autenticarte manualmente
y sin correr el riesgo que alguien pueda leer tu contraseña mientras la
escribes. Todo esto desde una terminal.
