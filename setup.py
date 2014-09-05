
from distutils.core import setup, Extension
import os
import shutil
import sys

amberhome = os.getenv('AMBERHOME')

if amberhome is None:
    raise RuntimeError('AMBERHOME is not set! Cannot compile pysander')

packages = ['sander', 'sanderles']

os.system('/bin/rm -fr sanderles')
shutil.copytree('sander', 'sanderles')

try:
    pysander = Extension('sander.pysander',
                         sources=['sander/src/pysandermodule.c'],
                         include_dirs=[os.path.join(amberhome, 'include')],
                         library_dirs=[os.path.join(amberhome, 'lib')],
                         libraries=['sander'])
    pysanderles = Extension('sanderles.pysander',
                            sources=['sanderles/src/pysandermodule.c'],
                            include_dirs=[os.path.join(amberhome, 'include')],
                            library_dirs=[os.path.join(amberhome, 'lib')],
                            libraries=['sanderles'],
                            define_macros=[('LES', None)])
    setup(name='sander', ext_modules=[pysander, pysanderles], packages=packages)
finally:
    os.system('/bin/rm -fr sanderles')
