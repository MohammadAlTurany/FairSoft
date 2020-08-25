# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os


class G4particlexs(Package):
    """Geant4 data files for evaluated particle cross-sections on natural composition
       of elements"""
    homepage = "http://geant4.web.cern.ch"
    url = "http://geant4-data.web.cern.ch/geant4-data/datasets/G4PARTICLEXS.1.1.tar.gz"

    version('2.1', sha256='094d103372bbf8780d63a11632397e72d1191dc5027f9adabaf6a43025520b41')
    version('1.1', sha256='100a11c9ed961152acfadcc9b583a9f649dda4e48ab314fcd4f333412ade9d62')

    def install(self, spec, prefix):
        mkdirp(join_path(prefix.share, 'data'))
        dest = 'G4PARTICLEXS' + '{0}'.format(self.version)
        install_path = join_path(prefix.share, 'data', dest)
        install_tree(self.stage.source_path, install_path)

    def url_for_version(self, version):
        """Handle version string."""
        return "http://geant4-data.web.cern.ch/geant4-data/datasets/G4PARTICLEXS.%s.tar.gz" % version
