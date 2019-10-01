import os

from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class NanorangeConan(ConanFile):
    name = "nanoRange"
    version = "0.1"
    license = "Boost 1.0"
    author = "Paul M. Bendixen paulbendixen@gmail.com"
    url = "gitlab.com/paulbendixen/conannanorange"
    description = "NanoRange is a C++17 implementation of the C++20 Ranges proposals (formerly the Ranges TS)."
    topics = ("ranges", "C++17", "Ranges TS")
    no_copy_source = True
    settings = "compiler"
    # No settings/options are necessary, this is header only

    def configure(self):
        if not self.settings.compiler.cppstd in ["17", "20", "gnu17", "gnu20"]:
            raise ConanInvalidConfiguration("nanoRange requires at least c++17")

    def source(self):
        self.run("git clone https://github.com/tcbrindle/NanoRange.git")

    def package(self):
        self.copy("*.hpp", src="NanoRange/include", dst="include" )

    def package_id(self):
        self.info.header_only()
