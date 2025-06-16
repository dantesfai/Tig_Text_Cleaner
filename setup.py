# setup.py
from setuptools import setup, find_packages

setup(
    name='textcleaner',
    version='0.1.0',
    author='Dani Tesfai',
    author_email='d202361017@xs.ustb.edu.cn',
    description='A Tigrinya text cleaning tool',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    py_modules=['text_cleaner'],
    install_requires=[
        # Only third-party packages; standard libs are excluded
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'textcleaner=text_cleaner:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

