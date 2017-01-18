.. title: Anaconda y LVM sobre LUKS
.. slug: anaconda-y-lvm-sobre-luks
.. date: 2016-12-30 18:10:00 UTC-06:00
.. tags: anaconda, lvm, luks, fedora, fc25
.. category: floss
.. link: 
.. description: Reutilizando LUKS y VG en una instalación cifrada de Fedora.
.. type: text

Previamente había instalado Fedora 22 en mi laptop, desde hace más de 6 meses
Fedora 22 fue declarado `EOL <https://fedoramagazine.org/fedora-22-end-life/>`_
, algo que me preocupaba era como reutilizar las particiones creadas para fc22
de forma que en ellas pudiera instalar la nueva versión de Fedora 25 y conservar
todos los archivos contenedios en el Volumen Lógico que sirve como ``/home``

En el siguiente post explicaré un como lograr esto sin comprometer la integridad
de nuestra información ni los demás sistemas operativos que se pueden encontrar
en nuestro equipo.

.. TEASER_END


