# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xkill(AutotoolsPackage):
    """xkill is a utility for forcing the X server to close connections to
    clients.  This program is very dangerous, but is useful for aborting
    programs that have displayed undesired windows on a user's screen."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xkill"
    url      = "https://www.x.org/archive/individual/app/xkill-1.0.4.tar.gz"

    version('1.0.4', 'b04c15bfd0b619f1e4ff3e44607e738d')

    depends_on('libx11')
    depends_on('libxmu')

    depends_on('xproto@7.0.22:', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
