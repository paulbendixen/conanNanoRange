from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    for bld in builder.builds:
        bld.settings["compiler.cppstd"] = "gnu17"
    builder.run()
