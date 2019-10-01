from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    builder.update_build_if( lambda build : build.settings["compiler.cppstd"] == None , new_settings={"compiler.cppstd":"gnu17"}  )
    builder.run()
