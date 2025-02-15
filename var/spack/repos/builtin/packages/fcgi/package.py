# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fcgi(AutotoolsPackage):
    """FastCGI is simple because it is actually CGI with only a few extensions.
    Like CGI, FastCGI is also language-independent. For instance, FastCGI
    provides a way to improve the performance of the thousands of Perl
    applications that have been written for the Web."""

    homepage = "https://fastcgi-archives.github.io/"
    url = "https://github.com/FastCGI-Archives/fcgi2/archive/refs/tags/2.4.2.tar.gz"

    license("OML")

    version("2.4.4", sha256="c0e0d9cc7d1e456d7278c974e2826f593ef5ca555783eba81e7e9c1a07ae0ecc")
    version("2.4.3", sha256="5273bc54c28215d81b9bd78f937a9bcdd4fe94e41ccd8d7c991aa8a01b50b70e")
    version("2.4.2", sha256="1fe83501edfc3a7ec96bb1e69db3fd5ea1730135bd73ab152186fd0b437013bc")
    version(
        "2.4.1-SNAP-0910052249",
        sha256="829dc89a0a372c7b0b172303ec9b42e9d20615d6d0e9fc81570fdac6c41a0f30",
        url="https://github.com/FastCGI-Archives/FastCGI.com/raw/master/original_snapshot/fcgi-2.4.1-SNAP-0910052249.tar.gz",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    parallel = False
