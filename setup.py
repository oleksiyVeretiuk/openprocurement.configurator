import os
from setuptools import setup, find_packages

entry_points = {
    'openprocurement.api.plugins': [
        'configurator = openprocurement.configurator.set_configurator:set_up'
    ]
}
requires = [
    'openprocurement.api',
]
setup(name='openprocurement.configurator',
      version='0.0.1',
      description='configurator',
      classifiers=[
          "Framework :: Pylons",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      requires=requires,
      include_package_data=True,
      zip_safe=False,
      entry_points=entry_points)
