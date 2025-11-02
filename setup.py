from setuptools import setup, find_packages

setup(
    name="yaraga-commons",
    version="1.0.3",
    author="BB",
    description="Common utilities and models for Yet Another RAG App",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.12.0",
    install_requires=[
        "SQLAlchemy>=2.0.43",
        "pgvector>=0.4.1"
    ],
)
