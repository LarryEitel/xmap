import os
from setuptools import setup, find_packages


def read_file(name):
    return open(os.path.join(os.path.dirname(__file__),
                             name)).read()

readme = read_file('README.rst')
changes = read_file('HISTORY.rst')

setup(name='djangoprojectrecipe',
      version="0.1",
      description="simple buildout recipe for django projects",
      long_description='\n\n'.join([readme, changes]),
      classifiers=[
        'Framework :: Buildout',
        'Framework :: Django',
        'Topic :: Software Development :: Build Tools',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        ],
      packages=find_packages(),
      keywords='',
      author='Stefan Foulis',
      author_email='stefan.foulis@gmail.com',
      url='http://github.com/stefanfoulis/djangoprojectrecipe',
      license='BSD',
      zip_safe=False,
      install_requires=[
        'zc.buildout',
        'zc.recipe.egg',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [zc.buildout]
      default = djangoprojectrecipe.recipe:Recipe
      """,
      )
