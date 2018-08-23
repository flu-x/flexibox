from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'browserium',
    version = '1.1.0',
    description = 'A single endpoint for your browser driver configuration',
    author = [
        'Soumyajit Basu',
        'Bony Roopchandani'
    ],
    author_email = 'soumyajit.basu62@gmail.com',
    classifiers = [
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'License :: MIT License'
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
        'browserium.elkStackConfigurer',
        'browserium.elkStackConfigurer.darwin',
        'browserium.elkStackConfigurer.debian',
        'browserium.elkStackConfigurer.rpm'
    ],
    package_data= {
        'browserium.configurations': ['*.ini'],
        'browserium.elkStackConfigurer': ['*.conf'],
        'browserium.elkStackConfigurer.darwin':['*.yml','*.sh'],
        'browserium.elkStackConfigurer.debian':['*.yml','*.sh'],
        'browserium.elkStackConfigurer.rpm':['*.yml','*.sh','*.repo']
    },
    include_package_data=True,
    zip_safe = False,
    entry_points={
        'console_scripts': [
            'browserium = browserium.utility.main:main'
        ]
    },
    scripts = ['browserium/elkStackConfigurer/elk_configure.py'],
    url = "https://github.com/browserium/Browserium",
    download_url = "https://github.com/browserium/Browserium/archive/1.1.0.tar.gz"
)