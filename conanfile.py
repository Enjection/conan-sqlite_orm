from conans import ConanFile, tools
import os
import glob

class sqlite_ormConan(ConanFile):
    name = "sqlite_orm"
    version = "1.3"
    description = "SQLite ORM light header only library for modern C++."
    #url = "https://github.com/bincrafters/conan-sqlite_orm"
    homepage = "https://github.com/fnc12/sqlite_orm"
    author = "MokinIA <mia@tomsksoft.com>"
    license = "BSD 3-Clause"
    exports = ["LICENSE.md"]
    exports_sources = ["patches/*.diff"]
    requires = "sqlite3/3.21.0@bincrafters/stable"
    source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        source_url = "https://github.com/fnc12/sqlite_orm"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)
        self._apply_patches()

    def _apply_patches(self):
        for filename in sorted(glob.glob("patches/*.diff")):
            self.output.info('applying patch "%s"' % filename)
            tools.patch(base_path=self.source_subfolder, patch_file=filename)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
