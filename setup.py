from setuptools import setup, find_packages

setup(
    name='CalculatorApp',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calculator = calc:main',  
        ],
    },
    install_requires=[
        
    ],
    author='AlinaV, Kamila_A',
    author_email='alinav2048@gmail.com',
    description='Simple calculator app',
    license='MIT',
    keywords='calculator app',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)