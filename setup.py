from distutils.core import setup

setup(
  name = 'pmake',
  packages = ['pmake'], # this must be the same as the name above
  version = '1.0.8',
  description = 'A python build script with support for custom output and parallel builds',
  author = 'Eric Marshall',
  author_email = 'ericmarshall715@gmail.com',
  url = 'https://github.com/emm035/pmake', # use the URL to the github repo
  download_url = 'https://github.com/emm035/pmake/archive/1.0.8.tar.gz', # I'll explain this in a second
  keywords = ['build', 'logging', 'parallel'], # arbitrary keywords
  classifiers = [],
  scripts = ['pmake/pmake'],
  install_requires = ['pyyaml']
)