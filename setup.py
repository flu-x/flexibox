from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'browserium',
    version = '1.1.2',
    description = 'A single endpoint for your browser driver configuration',
    author = [
        'Soumyajit Basu',
        'Bony Roopchandani'
    ],
    author_email = 'soumyajit.basu62@gmail.com',
    classifiers = [
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License'
    ],
    install_requires = [
        'requests',
        'wget',
        'selenium',
        'python-daemon'
    ],
    packages = [
        'browserium',
        'browserium.utility',
        'browserium.configurations',
        'browserium.generic_functions',
        'browserium.logstashRunner'
    ],
    package_data= {
        'browserium.configurations': ['*.ini'],
        'browserium.logstashRunner': ['*.conf']
    },
    include_package_data=True,
    zip_safe = False,
    entry_points={
        'console_scripts': [
            'browserium = browserium.utility.main:main'
        ]
    },
    url = "https://github.com/browserium/Browserium",
    download_url = "https://github.com/browserium/Browserium/archive/1.1.2.tar.gz",
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)