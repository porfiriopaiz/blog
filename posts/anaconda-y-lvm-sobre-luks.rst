.. title: Anaconda y LVM sobre LUKS
.. slug: anaconda-y-lvm-sobre-luks
.. date: 2017-02-03 16:59:06 UTC-06:00
.. tags: anaconda, fc25, fedora, luks, lvm
.. category: floss
.. link: 
.. description: Reutilizando LUKS y VG en una instalación cifrada de Fedora.
.. type: text

Previamente había instalado Fedora 22 en mi laptop, desde hace más de 6 meses
Fedora 22 fue declarado `EOL <https://fedoramagazine.org/fedora-22-end-life/>`_
, algo que me preocupaba era como reutilizar las particiones creadas para fc22
de forma que en ellas pudiera instalar la nueva versión de Fedora 25 y
conservar todos los archivos contenidos en el Volumen Lógico que sirve como
``/home``.

En el siguiente post explicaré como lograr esto sin comprometer la integridad
de nuestra información ni los demás sistemas operativos instalados en nuestro
equipo.

.. TEASER_END

A como vimos en el post anterior, también es posible hacer un upgrade, es
genial tener la posibilidad de poder hacer esto, pero la idea de descargar
todos paquetes, para luego actualizarlos de una vez, es algo que no sé si
quiera hacer, francamente hacer fresh installs y configurar todo a como
estaba es algo que me gusta y disfruto hacer. También representa menor carga
para el equipo, ya que solo descarga los paquetes mínimos para tener un
sitema funcional, todo lo demás que eventualmente pueda necesitar lo puedo
instalar en demanda.

Considerando que todos los archivos contenidos en tus sistemas cuentan con su
su debido respaldo, podemos empezar con el proceso de instalación sin miedo a
que algo salga mal, nunca se sabe que podría salir mal hasta que sale mal XD.


