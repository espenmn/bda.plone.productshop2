import os
from setuptools import (
    setup,
    find_packages,
)


version = '0.3dev'
shortdesc = "Product shop extension for bda.plone.shop"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'CHANGES.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(name='bda.plone.productshop',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      author='Bluedynamics Alliance',
      author_email='dev@bluedynamics.com',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bda', 'bda.plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'plone.app.dexterity',
          'plone.app.relationfield',
          'bda.plone.shop',
          'collective.instancebehavior',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'bda.plone.productshop',
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
