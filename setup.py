from setuptools import setup

setup(
    name = 'browserium',
    version = '1.1.0',
    description = 'A single endpoint for your browser driver configuration',
    author = [
        'Soumyajit Basu',
        'Bony Roopchandani'
    ],
    author_email = [
        'soumyajit.basu62@gmail.com',
        'broopchandani@datalicious.com'
    ],
    classifiers = [
        'Intended Audience :: QA Developers',
        'Intended Audience :: SDET'
    ],
    install_requires = [
        'requests',
        'wget',   
        'selenium'
    ],
    packages = ['browserium', 'browserium.utility', 'browserium.configurations', 'browserium.generic_functions'],
    package_data= {'browserium.configurations': ['*.ini']},
    include_package_data=True,
    zip_safe = False,
    entry_points={
        'console_scripts': [
            'browserium = browserium.utility.main:main'
        ]
    }
)
