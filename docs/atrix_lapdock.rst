.. _atrix_lapdock:

========================
Atrix Lapdock Other Uses
========================

I bought the Atrix Lapdock since I couldn't find any sub $100 portable HDMI displays. The only affordable displays I
could find were USB only. With the Atrix Lapdock and some adapters, I was able to use it as a portable display for
several devices, which is great for traveling.

It's a good idea to remove the plate on the docking area (underneath where the phone would be). It makes it easier to
plug in the adapters or have to sand/shave them less. You can easily pull it off with your finger nails (the plate
actually has a couple of magnets to keep it in place, and two small plastic clips).

.. image:: https://i.imgur.com/WpsmIm.jpg
    :target: https://imgur.com/WpsmI
    :width: 49%
.. image:: https://i.imgur.com/5HAGwm.jpg
    :target: https://imgur.com/5HAGw
    :width: 49%

Pictures and Videos
===================

.. imgur-embed:: a/zEkwz

.. raw:: html

    <iframe width="560" height="315" src="http://www.youtube.com/embed/VfdKq33WgHw?rel=0" frameborder="0"></iframe>

.. raw:: html

    <iframe width="560" height="315" src="http://www.youtube.com/embed/zCxTTrTZSSM?rel=0" frameborder="0"></iframe>

.. raw:: html

    <iframe width="560" height="315" src="http://www.youtube.com/embed/x_yhJ_QBfaU?rel=0" frameborder="0"></iframe>

.. raw:: html

    <iframe width="560" height="315" src="http://www.youtube.com/embed/P1zKD66GSYo?rel=0" frameborder="0"></iframe>

With a Nexus 4
==============

Works with the Nexus 4 just fine, appears to maintain aspect ratio. Adapters used:

* `HDMI Male to Micro HDMI Female <https://www.dealextreme.com/p/hdmi-male-to-micro-hdmi-female-adapter-66079>`_
* `Micro USB B Male to Female <https://www.ebay.com/itm/ws/eBayISAPI.dll?ViewItem&item=270928425953>`_
* `SlimPort SP1002 (HDMI) <https://www.amazon.com/dp/B009UZBLSG/>`_
* `HDMI Port Saver (Male to Female) 90 Degree <https://www.monoprice.com/products/product.asp?p_id=3733>`_

.. image:: https://i.imgur.com/MJs3n49m.jpg
    :target: https://imgur.com/MJs3n49
    :width: 49%
.. image:: https://i.imgur.com/MUViVQIm.jpg
    :target: https://imgur.com/MUViVQI
    :width: 49%

Using USB OTG
-------------

Using a modified kernel with OTG_USER_CONTROL set, I was able to get the Lapdock's keyboard, mouse, and USB hub working
with my Nexus 4! While I wait for my Miracast adapter to arrive, I had to put something on the Lapdock's HDMI port to
make it turn on, so I used a Raspberry Pi for now. Here are a few observations:

* I'm using an unmodified 5-wire Micro USB B Male to Female.
* The phone **does not charge** even though the lapdock is sending power and data to the phone. Perhaps the kernel
  needs additional modification?
* In the second and third pictures I removed the small WiFi USB adapter that was plugged into the Lapdock to show that
  the phone detected it, confirming the USB hub works.
* Once I get my `PTV3000 <https://www.amazon.com/Netgear-PTV3000-100NAS-Push2TV/dp/B00904JILO>`_ I can try using the
  Lapdock's full potential with my phone.
* No multitouch mouse/touchpad :(

Steps taken to accomplish:

1. `Download <https://forum.xda-developers.com/showpost.php?p=38621573&postcount=121>`_ the modified kernel at the
   bottom of that post.
2. `Boot the new kernel <https://forum.xda-developers.com/showthread.php?t=2151159>`_ following the instructions in the
   original post.
3. Plug and play!

.. note::

    Ignore the Raspberry Pi in the images below, I'm just using it to trick the Lapdock into powering on. Notice the
    mouse cursor on my phone!

    If you can see, I ran ``lsusb`` on the phone, removed the USB WiFi adapter, and ran ``lsusb`` again. Notice the
    shorter "paragraph" on my phone. Definitely working.

.. image:: https://i.imgur.com/qbs7sWgb.jpg
    :target: https://imgur.com/qbs7sWg
    :width: 33%
.. image:: https://i.imgur.com/yNgacICb.jpg
    :target: https://imgur.com/yNgacIC
    :width: 33%
.. image:: https://i.imgur.com/K7glCXNb.jpg
    :target: https://imgur.com/K7glCXN
    :width: 33%

Using USB OTG and Miracast
--------------------------

It works, but it's not really pleasant. If we can get Keyboard/Mouse to Bluetooth working that would be much better.

Comments
========

.. disqus::
