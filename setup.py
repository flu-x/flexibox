from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='flexibox',
    version='1.0.0',
    description='A single box of functionalities for a selenium project',
    author=['Soumyajit Basu'],
    author_email='soumyajit.basu62@gmail.com',
    classifiers=[
        'Intended Audience :: Information Technology', 'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable', 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6', 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7', 'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X', 'Operating System :: POSIX',
        'Topic :: Software Development :: Quality Assurance', 'Topic :: Software Development :: Testing'
    ],
    install_requires=['requests', 'wget', 'selenium'],
    packages=[
        'flexibox', 'flexibox.core', 'flexibox.utility', 'flexibox.configurations', 'flexibox.generic_functions',
        'flexibox.standalonedriverobject'
    ],
    package_data={'flexibox.configurations': ['*.ini']},
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': ['flexibox = flexibox.utility.main:main']},
    url="https://github.com/flu-x/Flexibox",
    download_url="https://github.com/flu-x/Flexibox/archive/1.0.0.tar.gz",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
