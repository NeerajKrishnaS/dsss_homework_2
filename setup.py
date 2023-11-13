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
)
