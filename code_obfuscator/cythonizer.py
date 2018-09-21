from distutils.core import setup, Extension
import os
import sys
from glob import glob
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import shutil
from unittest.mock import patch


class Cythonizer(object):

    def __init__(self):
        self.path = ""

    def execute(self, path):
        self.path = os.path.abspath(path)
        python_files = [y for x in os.walk(self.path) for y in glob(os.path.join(x[0], '*.py'))]
        for python_file in python_files:
            if not python_file.endswith('__init__.py'):
                self.build_so(python_file)
                self.clean_up(python_file)

        shutil.rmtree(os.path.realpath('./build'))

    def get_package_name(self, file):
        relative_path = file[len(self.path) + 1:]
        normalized_path = os.path.splitext(relative_path)[0]
        if normalized_path.startswith('./'):
            normalized_path = normalized_path[2:]
        return '.'.join(normalized_path.split('/'))

    def build_so(self, file):
        print('Building : ' + file)
        package_name = self.get_package_name(file)

        with patch.object(sys, 'argv', ["setup.py", "build_ext", "--build-lib=" + self.path]):
            ext_modules = [
                Extension(package_name,
                          [file], )]
            setup(
                cmdclass={'build_ext': build_ext},
                ext_modules=ext_modules
            )

    def clean_up(self, file):
        directory_name = os.path.dirname(file)
        file_name = os.path.basename(file)
        root = os.path.splitext(file_name)[0]
        os.remove(directory_name + '/' + root + '.py')
        os.remove(directory_name + '/' + root + '.c')
