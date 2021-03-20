****************************
Mopidy-VFD
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-VFD
    :target: https://pypi.org/project/Mopidy-VFD/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/github/workflow/status/PeterWurmsdobler/mopidy-vfd/CI
    :target: https://github.com/PeterWurmsdobler/mopidy-vfd/actions
    :alt: CI build status

.. image:: https://img.shields.io/codecov/c/gh/PeterWurmsdobler/mopidy-vfd
    :target: https://codecov.io/gh/PeterWurmsdobler/mopidy-vfd
    :alt: Test coverage

Mopidy extension to display track information on a VFD


Prerequisites
=============

Raspbian and Mopidy installation

Follow the instructions on https://docs.mopidy.com/en/latest/installation/raspberrypi/ to install both the Raspberry PI Debian based operating system as well as Mopidy.

PIP support

Raspberry buster comes with python3.7, but not with pip, so::

    sudo apt install python3-pip

SPI support

First, run::

    sudo raspi-config

and enable SPI. The SPI python driver has to be installed::

    sudo python3.7 -m pip install spidev

Nortitake support

For now, until there is a pypi package available::

    sudo apt install git
    git clone https://github.com/PeterWurmsdobler/noritake.git
    cd noritake
    sudo python3.7 ./setup.py install


Installation
============

For now, until there is a pypi package available::

    sudo apt install git
    git clone https://github.com/PeterWurmsdobler/mopidy-vfd.git
    cd mopidy-vfd
    sudo python3.7 ./setup.py install


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-VFD to your Mopidy configuration file::

    [vfd]
    # TODO: Add example of extension config


Project resources
=================

- `Source code <https://github.com/PeterWurmsdobler/mopidy-vfd>`_
- `Issue tracker <https://github.com/PeterWurmsdobler/mopidy-vfd/issues>`_
- `Changelog <https://github.com/PeterWurmsdobler/mopidy-vfd/blob/master/CHANGELOG.rst>`_


Credits
=======

- Original author: `Peter Wurmsdobler <https://github.com/PeterWurmsdobler>`__
- Current maintainer: `Peter Wurmsdobler <https://github.com/PeterWurmsdobler>`__
- `Contributors <https://github.com/PeterWurmsdobler/mopidy-vfd/graphs/contributors>`_
