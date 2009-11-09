from setuptools import setup, find_packages

setup(
    name = "rapid-download",
    version = "0.0.1",
    url = 'http://github.com/xando/rapid-download',
    description = "Rapidshare download script",

    include_package_data = True,
    packages = find_packages('.'),

    install_requires = ['setuptools','pycurl' ],
        
    author = 'xando',
    author_email = '',
)
