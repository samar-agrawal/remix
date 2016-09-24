from setuptools import setup, find_packages

setup(
    name='remix',
    version='1.0',
    description='Collection of scripts',
    author='Samar',
    author_email='samar@enstino.com',
    packages = find_packages(),
    license = 'MIT',
    package_dir = {'': '.'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development'
    ],
    zip_safe=True,
)
