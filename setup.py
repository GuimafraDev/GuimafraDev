from setuptools import setup, find_packages

setup(
    name="gods_eye",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "pyyaml",
        "requests",
        "networkx",
        "pandas",
        "numpy",
        "solana",
        "gunicorn"
    ],
    entry_points={
        "console_scripts": [
            "gods_eye=src.backend.app:main"
        ]
    },
)