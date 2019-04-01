from distutils.core import setup
from io import open

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='deepvec',
    packages=['deepvec'],
    version='0.1',
    license='MIT',
    description='Tensorflow wrapper for classification',
    long_description=long_description,
    author='Nuha Almozaini',
    author_email='nuha.mozaini@gmail.com',
    url='https://github.com/nuhamozaini',
    download_url='https://github.com/nuhamozaini/deepvec/archive/v_01.tar.gz',
    keywords=['classification', 'deep learning', 'tensorflow', 'keras', 'pandas'],
    install_requires=[
        'tensorflow',
        'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
