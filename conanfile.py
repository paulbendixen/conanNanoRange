import os
import glob

from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class NanorangeConan(ConanFile):
    name = "nanorange"
    version = "20191001"
    license = "MIT"
    author = "Paul M. Bendixen paulbendixen@gmail.com"
    url = "gitlab.com/paulbendixen/conannanorange"
    website = "https://github.com/tcbrindle/NanoRange"
    description = "NanoRange is a C++17 implementation of the C++20 Ranges proposals (formerly the Ranges TS)."
    topics = ("conan", "NanoRange", "ranges", "C++17", "Ranges TS")
    no_copy_source = True
    settings = "compiler"
    # No settings/options are necessary, this is header only

    def configure(self):
        if self.settings.compiler == "Visual Studio":
            if not any([self.settings.compiler.cppstd == std for std in ["17", "20"]]):
                raise ConanInvalidConfiguration("nanoRange requires at least c++17")
        else:
            if not self.settings.compiler.cppstd in ["17", "20", "gnu17", "gnu20"]:
                raise ConanInvalidConfiguration("nanoRange requires at least c++17")

    def source(self):
        tools.get("https://github.com/tcbrindle/NanoRange/archive/abc34279d71369527e4da43cc4d02cf77446f79a.tar.gz", destination="source_folder", sha256="799431094ab784eb3cdbcd6de6681ff5d8b2b28e1a1e26e0a3a94fbfbfcd7e75" ) 

    def package(self):
        sourceSubfolder = glob.glob("{}/source_folder/NanoRange-*".format(self.source_folder))[0]
        print( sourceSubfolder )
        self.copy("*.hpp", src="{}/include".format(sourceSubfolder), dst="include" )
        self.copy("LICENSE_1_0.txt", src=sourceSubfolder, dst="licenses")

    def package_id(self):
        self.info.header_only()
