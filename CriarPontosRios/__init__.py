# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CriarPontosRios
                                 A QGIS plugin
 Cria pontos de inicio, fim e confluentes dos Rios.
                             -------------------
        begin                : 2018-05-09
        copyright            : (C) 2018 by Antônio Teles
        email                : antoniot.leandro@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CriarPontosRios class from file CriarPontosRios.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .criar_pontos_rios import CriarPontosRios
    return CriarPontosRios(iface)
