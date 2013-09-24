from pybuilder.core import use_plugin, init, Author

use_plugin("python.install_dependencies")
#use_plugin("copy_resources")
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")

authors = [Author('Marco Hoyer', 'marco_hoyer@gmx.de')]
description = """checl_http_yaml: a nagios/icinga check plugin requesting yaml data and checking key-value pairs in response.

for more documentation, visit https://github.com/marco-hoyer/check_http_yaml
"""

name = 'check_http_yaml'
license = 'GNU GPL v3'
summary = 'check_http_yaml - yaml key-value check via http'
url = 'https://github.com/marco-hoyer/check_http_yaml'
version = '1.0'

default_task = ['publish']

@init
def initialize(project):
    
    project.depends_on("requests")

    project.install_file('/usr/lib64/icinga/plugins', 'check_http_yaml.py')
    project.install_file('/etc/icinga/conf.d/commands', 'check_http_yaml.cfg')

    project.set_property('distutils_classifiers', [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Monitoring',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ])


@init(environments='teamcity')
def set_properties_for_teamcity_builds(project):
    import os

    project.version = '%s-%s' % (project.version, os.environ.get('BUILD_NUMBER', 0))
    project.default_task = ['install_dependencies', 'package']
    project.set_property('install_dependencies_use_mirrors', False)
    project.get_property('distutils_commands').append('bdist_rpm')
