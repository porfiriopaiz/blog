.. title: Anaconda y LVM sobre LUKS
.. slug: anaconda-y-lvm-sobre-luks
.. date: 2017-02-03 16:59:06 UTC-06:00
.. tags: anaconda, fc25, fedora, luks, lvm
.. category: floss
.. link:
.. description: Reutilizando LUKS y VG en una instalación cifrada de Fedora.
.. type: text

Previamente había actualizado mi laptop de Fedora 22 a Fedora 23 cuando fc22 ya
tenía más de 6 meses de haber alcanzado su final vida, también es posible
reutilizar las particiones creadas para fc22 de forma que en ellas se pueda
instalar la nueva versión de Fedora y conservar todos los archivos contenidos
en el Volumen Lógico que sirve como ``/home``.

En el siguiente post explicaré como lograr esto sin comprometer la integridad
de nuestra información ni los demás sistemas operativos instalados en nuestro
equipo.

.. TEASER_END

Como vimos en el post anterior, también es posible hacer un upgrade, es genial
tener la posibilidad de poder hacer esto, pero la idea de descargar todos
paquetes, para luego actualizarlos de una vez, es algo que no sé si quiera
hacer, francamente hacer fresh installs y configurar todo a como estaba es algo
que me gusta y disfruto hacer. También representa menor carga para el equipo,
ya que solo descarga los paquetes mínimos para tener un sistema funcional, todo
lo demás que eventualmente pueda necesitar lo puedo instalar en demanda.

Considerando que todos los archivos contenidos en tus sistemas cuentan con su
debido respaldo, podemos empezar con el proceso de instalación sin miedo a que
algo salga mal, nunca se sabe que podría salir mal hasta que sale mal XD.

Creando un medio de instalación
===============================

El primer paso es crear un medio de instalación, para ello debemos decargar el
archivo ISO de Fedora 25. Desde Fedora 21 he estado usando la imagen netinstall
, de acuerdo con el capítulo 2 de la `Guía de Instalación de Fedora
<https://docs.fedoraproject.org/en-US/Fedora/25/html/Installation_Guide/chap-downloading-fedora.html>`_:

    "La imagen iso netinstall se inicia directamente en el entorno de
    instalación y utiliza los repositorios de paquetes Fedora en línea como
    fuente de instalación. Con una imagen netinstall, se puede seleccionar una
    amplia variedad de paquetes para crear una instalación personalizada de
    Fedora. La imagen de Netinstall de Fedora Server es universal y puede
    utilizarse para instalar cualquier sabor de Fedora o su propio conjunto de
    paquetes favoritos."

Descargando la imagen Everything netinstall
-------------------------------------------

Yo prefiero usar la imagen ISO netinstall de `Fedora Everything <https://alt.fedoraproject.org/es/>`_.

Aparentemente, la imagen Everything netinstall no cuenta con servidor de
torrents para su descarga:

https://torrent.fedoraproject.org/

Por lo que deberemos usar el método convencional de descarga directa, para ello
nos auxiliaremos de la línea de comandos.

Para sistemas de 32 bits descargar la siguiente imagen:

.. code-block:: console

   wget -N -t 0 -c https://download.fedoraproject.org/pub/fedora/linux/releases/25/Everything/i386/iso/Fedora-Everything-netinst-i386-25-1.3.iso

Para sistemas de 64 bits descargar la siguiente imagen:

.. code-block:: console

   wget -N -t 0 -c https://download.fedoraproject.org/pub/fedora/linux/releases/25/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-25-1.3.iso

Donde:
    `-N` descarga el archivo con las misma marca de tiempo de dia y hora con la
    que fue subido a los servidores.

    `-t 0` en caso de que la descarga se vea interrumpida por problemas de
    conexión hará un intento automático de reconexión, si dejamos el tiempo en
    `0` hará la reconexión de forma inmediata.

    `-c` indica que la descarga debe ser continuada en el byte que quedó
    pendiente al momento que la descarga se viera interrumpida.

Esta es una pequeña medida de contingencia en caso que no contemos con acceso a
una red lo suficiente estable.

También podemos verificar la integridad de la imagen descargada usando el
archivo checksum. Solo tenemos que descargar el archivo y guardarlo en el mismo
directorio que contiene a la imagen ISO:

.. code-block:: console

   wget -N -t 0 -c https://alt.fedoraproject.org/es/static/checksums/Fedora-Everything-25-1.3-x86_64-CHECKSUM

Luego ejecutamos el siguiente comando:

.. code-block:: console

   sha256sum -c Fedora-Everything-25-1.3-x86_64-CHECKSUM

Grabando la imagen ISO en una USB
---------------------------------

Para grabar la imagen ISO en una USB usaremos la herramienta **Fedora Media
Writer**. Si estás usando Windows puedes instalar Fedora Media Writer usando el
siguiente enlace:

https://getfedora.org/fmw/FedoraMediaWriter-win32-4.0.7.exe

Para MacOS:

https://getfedora.org/fmw/FedoraMediaWriter-osx-4.0.7.dmg

Si estás usando Fedora 23 o superior puedes instalar Fedora Media Writer con el
siguinete comando:

.. code-block:: console

   su -c 'dnf install mediawriter'

Antes de ejecutar Fedora Media Writer es recomendable desconectar cualquier
otro dispositivo de almacenamiento extraible que pueda estar conectado en
nuestro equipo, esto para evitar posibles confusiones. Conectamos la memoria
USB que usaremos y ejecutamos Fedora Media Writer.

Los pasos a seguir son muy sencillos, seleccionamos:

1. Custom image.
2. Navegamos hasta el directorio dónde se encuentre la imagen ISO previamente
   descargada.
3. Seleccionamos la USB.
4. Damos clic en `Write to disk`.
5. Ingresamos nuestra contraseña de usuario si estamos en el grupo `wheel` o la
   de `root` en caso de que no seamos admins.
6. Listo.

Arrancando desde la USB
-----------------------

En mi caso tengo configurada mi laptop para iniciar en `UEFI mode` y con
`Secure Boot` activado.

Crear nuestro medio de instalación con Fedora Media Writer nos garantiza que el
medio de instalación funcionará en cualquier posible escenario.

Para acceder al Administrador de arranque de mi laptop solo debo presionar la
tecla **Enter** mientras se muestra el logo de **Lenovo**, este es un
indicador, en mi caso, de que la máquina está arrancando en UEFI mode.

Iniciando el proceso de instalación de Fedora 25
================================================

Para esta sección del post haré uso de capturas de pantallas y una breve
descripción de las mismas.

Lo primero, la conexión a Internet.

Los medios de instalación creados a partir de imágenes netinstall dependen
exclusivamente de una conexión a Internet, ya sea cableada vía puerto RJ45
(Ethernet) o vía Wireless (Usando nuestra tarjeta WiFi), en mi caso el medio de
instalación netinstall detecta ambas tarjetas de red. Los netinstall de Fedora
contienen un conjunto de driveres que nos permiten hacer uso de ciertos
periféricos, en caso de no ser detectada nuestra tarjeta de red WiFi puede que
nuestro dispositivo no sea soportado por Fedora, esto es por razones legales.
Fedora solo incluye controladores libres o que sus fabricantes hacen explícita
mención sobre su política de uso y distribución.

Mi T440p viene equipada con una tarjeta red cableada `Intel® Ethernet
Connection I217-LM
<https://ark.intel.com/products/60019/Intel-Ethernet-Connection-I217-LM>`_ y
una tarjeta de red inalámbrica `Intel® Wireless-N 7260
<http://ark.intel.com/products/75174/Intel-Wireless-N-7260>`_ , ambas tarjetas
fueron detectadas durante la instalación, en la oficina solo tengo acceso a
redes WiFi por lo que usé la tarjeta Wireless.

.. image:: /images/anaconda-screenshots/0000.png
   :align: center

En esta primer imagen del resumen de instalación, lo primero que debemos hacer
es conectarnos a alguna de las redes disponibles ya sea que usemos una red
cableada o una red WiFi, para ello damos clic en la opción `NETWORK & HOST
NAME`.

A continuación, selecionando Wireless y activando la tarjeta; seleccionamos una
red de las que estén disponibles; cambiamos el nombre de nuestro equipo y damos
clic en Apply...

.. image:: /images/anaconda-screenshots/0002.png
   :align: center

damos clic en `Done`.

En la sección de `LOCALIZATION` añadí la distribución de teclado `French
(English (International AltGr dead keys))` y removí `English (US)`.

.. image:: /images/anaconda-screenshots/0005.png
   :align: center

Se puede apreciar una pequeña verificación, donde presionando la tecla `AltGr +
a` y otras vocales, el resultado es las vocales acentuadas.

En la sección `TIME & DATE` siempre habilito la opción `Network Time`...

.. image:: /images/anaconda-screenshots/0007.png
   :align: center

también seleccionamos la `Región` y `Ciudad` en la que nos encontramos, ya que
en base a ello se ajusta la hora y la fecha.

Hasta este momento ya tenemos configuradas las siguientes secciones:

.. image:: /images/anaconda-screenshots/0008.png
   :align: center

Ahora debemos configurar la sección `SOFTWARE`, especificamente `INSTALLATION
SOURCE`...

En esta sección marcamos `On the Network:` y seleccionamos `Closest mirror`,
también nos aseguramos de desmarcar la opción `Updates`...

.. image:: /images/anaconda-screenshots/0009.png
   :align: center

de esta forma el instalador usará los repositorios en línea para descargar los
paquetes necesarios para la instalación, usando el servidor más cercano que por
lo general no es el más cercano geográficamente, pero el más eficiente y con
mejores tiempos en términos de transferencia de datos. Al desmarcar `Updates`
le estamos diciendo al instalador que use los paquetes más recientes que estén
disponibles en el repo.

Esperamos que se descarguen los metadatos de grupos de paquetes, del cual
depende la sección `SOFTWARE SELECTION`:

.. image:: /images/anaconda-screenshots/0011.png
   :align: center

En `SOFTWARE SELECTION` yo escogí `Fedora Custom Operating System`, el cual
representa una selección de paquetes muy mínima, sin entorno gráfico, solo unos
pocos grupos de paquetes que son los siguientes:

.. code-block:: console

   Environment Group: Fedora Custom Operating System
    Environment-Id: custom-environment
    Description: Basic building block for a custom Fedora system.
    Mandatory Groups:
      Core
    Optional Groups:
      Guest Agents
      Standard

Finalmente hemos llegado a la sección `SYSTEM`, seleccionamos `INSTALLATION
DESTINATION`. En `Device Selection`, en `Local Stardard Disk` selecionamos el
disco duro en el que tenemos la instalación de Fedora del cual queremos
reutilizar las particiones existentes.

En la sección `Other Storage Options`, en `Partitioning` seleccionamos `I will
configure partitioning`.

A continuación se muestra el siguiente menú, en el cual daremos clic en
`Unknown`:

.. image:: /images/anaconda-screenshots/0013.png
   :align: center

Una vez que damos clic en `Unknown` se mostrarán las demás particiones
existentes. Nos enfocaremos en las particiones **sda2**, **sda9** y **sda10**:

.. image:: /images/anaconda-screenshots/0014.png
   :align: center

Donde:

    **sda2** es la partición ESP (EFI Partition System), esta partición
    contiene los demás archivos \*.efi, cada OS que haya sido instalado en
    nuestro equipo en UEFI mode tiene un archivo \*.efi que será enlazado a
    nuestro GRUB, el cual nos permite escoger que OS arrancar durante los
    primeros segundos luego de haber encendido nuestro equipo. Por nada del
    mundo esta partición debe ser marcada para ser formateada. **sda2** será
    montada en `/boot/efi`.

    **sda9** es la partición que montaré en `/boot`, esta partición no debe
    estar cifrada, ya que ahí se almacenan archivos necesarios para que el OS
    sea cargado, por ejemplo el kernel. Si estuviera cifrada no podriamos
    acceder al kernel.

    **sda10** es la partición que fue cifrada usando LUKS, la cual contiene el
    `Volume Group` que contiene los demás volúmenes lógicos que sirven de `/`,
    `/home` y `swap`.

Al seleccionar **sda10** se nos solicita la contraseña de cifrado que nos
permitirá acceder al `Volume Group` que contiene las particiones mencionadas.
Se muestra como la instalación existente de Fedora 23, que originalmente era el
fc22 que actualizamos en el post anterior.

.. image:: /images/anaconda-screenshots/0015.png
   :align: center

Damos clic en `Fedora Linux 23 for x86_64` y podremos ver los volúmenes lógicos
que reciclaremos.

Dando clic `/home`, nos aseguramos de asignar un `Mount Point` o punto de
montaje para este Volumén Lógico. Nos aseguramos que el checkbox `Reformat`
**no** esté marcado, y damos clic en `Update Settings`.

.. image:: /images/anaconda-screenshots/0017.png
   :align: center

En la siguiente imagen podemos apreciar que el volumen lógico
`fedora_lilit-home` fue reasignado a `New Fedora 25 Installation`.

.. image:: /images/anaconda-screenshots/0018.png
   :align: center

Seleccionamos `/boot/efi`, que no es más que la partición ESP ubicada en
**sda2**, nos aseguramos de asignar un `Mount Point` o punto de montaje para
este Volumén Lógico, que en este caso sería `/boot/efi`. Nos aseguramos que el
checkbox `Reformat` **no** esté marcado, y damos clic en `Update Settings`.

.. image:: /images/anaconda-screenshots/0019.png
   :align: center

Seleccionamos `/`, este volumen lógico servía como `/` de fc23, por lo que para
poder reutilizarlo debemos marcarlo para formatear. Asignamos `/` como punto de
montaje, asignamos un sistema de archivos (ext4), nos aseguramos que el
checkbox `Reformat` **esté** marcado, y damos clic en `Update Settings`.

.. image:: /images/anaconda-screenshots/0023.png
   :align: center

Seleccionamos `swap`, marcamos el checkbox y damos clic en `Update Settings`.

.. image:: /images/anaconda-screenshots/0025.png
   :align: center

Seleccionamos `/boot`, acá es donde se almacenaban los kernels de fc23, para
poder reutilizar es partición es necesario formatearla. Asignamos un punto de
montaje `/boot`, damos clic en `Reformat`, en mi caso le asigno un sistema de
archivos `ext4` y clic en `Update Settings`.

.. image:: /images/anaconda-screenshots/0030.png
   :align: center

Damos clic en `Done` y aceptamos los cambios que serán efectuados.

Para finalizar solo damos clic en `Begin Installation`.

.. image:: /images/anaconda-screenshots/0032.png
   :align: center

Asignamos una contraseña de usuario y la contraseña de ROOT. Y listo, ahora
solo debemos esperar que la descarga de los paquetes y su instalación finalice:

.. image:: /images/anaconda-screenshots/0037.png
   :align: center

Y listo, damos clic en `Reboot`.

.. image:: /images/anaconda-screenshots/0053.png
   :align: center

En mi caso tuve que hacer una serie de pasos luego de la instalación que los
veremos en el siguiente post.
