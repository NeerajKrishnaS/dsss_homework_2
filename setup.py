from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Replace with your actual project name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
        ],
    },
    url='https://github.com/NeerajKrishnaS/dsss_homework_2',
    license='Apache License',  # Choose an appropriate license
    author='NeerajKrishnaS',
    author_email='neerajKrishnabs@gmail.com',
    description='A simple math quiz game',
    long_description='A Python package for a simple math quiz game.',
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License v2.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

