# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRestrictedPython(PythonPackage):
    pypi = "RestrictedPython/restrictedpython-7.4.tar.gz"

    version("7.4", sha256="81b62924713dbd280917fceaecaf210fef7a49dddf1a08c8c214a3613fbeb425")
    version("7.3", sha256="8888304c7858fdcfd86c50b58561797375ba40319d2b6ffb5d24b08b6a2dcd61")

    depends_on("py-setuptools", type="build")
