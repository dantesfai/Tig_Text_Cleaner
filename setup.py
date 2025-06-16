# setup.py
from setuptools import setup

setup(
    name='tigrinya_cleaner',
    version='1.0',
    py_modules=['cleaned_text'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'tigrinya-cleaner=cleaned_text:main',
        ],
    },
    author='Daniel Tesfai',
    author_email='d202361017@xs.ustb.edu.cn',
    description='A CLI tool for cleaning and little normalizing Tigrinya text',
    url='https://github.com/dantesfai/Tig_Text_Cleaner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
