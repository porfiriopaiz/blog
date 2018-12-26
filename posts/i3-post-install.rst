.. title: i3 post-install
.. slug: i3-post-install
.. date: 2018-12-09 21:26:18 UTC-06:00
.. tags: dnf, fc29, fedora, postinstall
.. category: floss
.. link:
.. description: Fedora 29 i3 window manager post-install
.. type: text

Luego de instalar Fedora 29 con i3 window manager, es necesario instalar otros
programas que facilitarán nuestra experiencia de usuario.

.. TEASER_END

El primer problema que debemos resolver es cómo nos vamos a conectar a
Internet, ya habrás notado que no tenemos ningún programa o applet que nos
permita activar nuestra tarjeta de red o gestionar las diferentes redes que
estén a nuestro alcance.

Suponiendo que ya estás logueado y que tu hardware está soportado por Fedora,
la tarjeta de red inalámbrica debería estar activada, pero ¿Cómo nos
conectamos a alguna de las redes que tenemos disponibles?

nmcli
=====

En el post anterior instalamos la colección de paquetes provisto por el grupo
"Soporte de Hardware", este grupo provee una amplia variedad de cotroladores de
red. También instalamos el grupo de paquetes correspondientes a NetworkManager.

``nmcli`` es un programa de línea de comandos que nos permitirá activar por
software el hardware de red de nuestro equipo, escanear las redes que están a
nuestro alrededor y conectarnos a las mismas.

Necesitaremos una terminal, presionando <Inicio> + <Enter> obtenemos una
Terminal.

Si nuestro equipo cuenta con un switch que permite activar o desactivar la
tarjeta de red, nos aseguramos de que esté activado.

Luego en la terminal ejecutamos el siguiente comando para verficar que esté
activado por software:

.. code-block:: console

   nmcli networking on

Esto debería activar la conexión de red cableada de nuestro equipo en caso que
estuvieramos acceso a una y desearamos usarla.

Para activar el hardware de red inalámbrico desde la terminal, ejecutamos el
siguiente comando:

.. code-block:: console

   nmcli radio wifi on

Esto debería activar nuestra tarjeta de red, a continuación verificamos cuáles
son las redes que tenemos disponibles a nuestro alcance:

.. code-block:: console

   nmcli device wifi list

.. code-block:: console

   IN-USE  SSID           MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
           RED_WIFI_2     Infra  5     130 Mbit/s  100     ▂▄▆█  WPA2
           RED_WIFI_2     Infra  1     130 Mbit/s  29      ▂___  WPA2
           RED_WIFI_3     Infra  1     54 Mbit/s   17      ▂___  WPA1

En caso de necesitar escanear nuevamente para verificar otras conexiones:

.. code-block:: console

   nmcli device wifi rescan

Suponiendo que ``RED_WIFI_1`` no requiere contraseña de acceso, para
conectarnos solo debemos ejecutar el siguiente comando:

.. code-block:: console

   nmcli device wifi connect RED_WIFI_1

En caso de requerir una contraseña de acceso:

.. code-block:: console

   nmcli device wifi connect RED_WIFI_1 password 1234567890

Donde:

   ``connect`` es un parámetro.

   ``RED_WIFI_1`` es el argumento que indica a qué red nos queremos conectar.

   ``password`` es un parámetro.

   ``1234567890`` es el argumento que el parámetro anterior recibe como
   contraseña. Debe usar la contraseña de la red a la que desea conectarse.

Ya debería estar conectado a su red. Procedemos a instalar los programas que
nos ayudarán a facilitar nuestra experiencia de usuario con i3.

Redes
=====

nm-applet
---------

``nm-applet`` es un simple applet de NetworkManager que nos permite hacer lo
mismo que hicimos con ``nmcli``, pero de manera gráfica.

.. code-block:: console

   su -c 'dnf install nm-applet'

Para ejecutar ``nm-applet`` presionamos <Inicio> + <d> y escribimos `nm-applet`
y presionamos <Enter>. En la esquina inferior derecha de nuestra pantalla
debería aparecer un ícono correspondiente a este `applet` desde donde podemos
gestionar nuestra conexión a las diferentes redes que tengamos disponibles a
nuestro alrededor.

NetworkManager-tui
------------------

Esta es una alternativa a ``nm-applet`` que hace uso de ``ncurses`` para
generar una `Text User Interface`.

.. code-block:: console

   su -c 'dnf install NetworkManager-tui'

nm-connection-editor
--------------------

`NetworkManager Connection Editor` nos permite editar de manera amigable e
intuitiva la configuración de las diferentes redes a las que hemos accedido, o
bien, crear Hotspots en caso que nuestra tarjeta de red lo soporte.

.. code-block:: console

   su -c 'dnf install nm-connection-editor'

Emulador de Terminal
====================

Ya habrás notado que el emulador que se instala por defecto con i3 es
``rxvt-unicode`` y que no es muy amigable que digamos, no es muy intuitivo a
primera vista y tiene cierta curva de aprendizaje que no queremos recorrer,
posiblemente...

Irónicamente mi emulador de terminal preferido es GNOME Terminal, puedes
instalar el que prefieras.

.. code-block:: console

   su -c 'dnf install gnome-terminal'

``i3`` tiene asignada la combinación de teclas <Inicio> + <Enter> al emulador
``urxvt``, para lanzar GNOME Terminal en su lugar hace falta editar el archivo
de configuración de ``i3`` (``~/.config/i3/config``), buscar la línea:

.. code-block:: console

   bindsym $mod+Return exec i3-sensible-terminal

Y sustituir por el comando que llama a nuestro emulador de terminal, en mi
caso, ``gnome-terminal``:

.. code-block:: console

   bindsym $mod+Return exec gnome-terminal

En los siguientes post iré compartiendo que otros programas uso en mi setup de
Fedora 29 con i3wm. Por el momento ya tienes los necesario para instalar otros
programas de interés como navegador Web y demás.
