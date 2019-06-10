.. title: Chromium
.. slug: chromium
.. date: 2019-01-08 14:14:51 UTC-06:00
.. tags: debian, fc29, fedora, web-browser
.. category:floss
.. link:
.. description: Mi configuración personal para navergar en Internet.
.. type: text

Después de instalar Fedora 29 con i3wm y de sortear las limitancias de conexión
a Internet desde la línea de comandos, lo más escencial es poder navegar en
Internet. A continuación documento paso a paso mi configuración personal de
Chromium Web Browser.

.. TEASER_END

Instalar Chromium
=================

Muchas cosas han cambiado desde que decidí escribir este post, por ejemplo, Google planea remover algunas funcionalidades que permiten hacer uso de bloqueadores de publicidad y otras formas de seguimiento que violan el derecho a la privacidad del usuario. Ojalá que esto no afecte a Chromium, para que los cambios tengan efecto en Google Chrome primeramente tienen que llegar a Chromium, espero que sea algo que los desarrolladores de Google puedan agregar más tarde a su versión de Google Chrome sin que tenga que afectar primeramente a Chromium.

Para Fedora está empaquetado ``chromium`` y ``chromium-vaapi``, la diferencia es que el segundo cuenta con acelaración y decodificiación por hardware, lo que hace la repoducción de audio y video más eficiente. Por esa razón instalo el segundo:
