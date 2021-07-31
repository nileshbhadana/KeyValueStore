from setuptools import setup


def read(fname):
    return open(fname).read()


setup_requires = [
    'click',
    'flask',
    'python-socketio',
    'requests'
]


setup(
    
    name="KeyValueStore",
    version="0.1",
    author="Nilesh Bhadana",
    author_email="nileshbhadana3@gmail.com",
    description="Key-Value Store",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/nileshbhadana/KeyValueStore",
    project_urls={
        "Bug Tracker": "https://github.com/nileshbhadana/KeyValueStore/issues",
    },
    license=read("LICENSE"),
    classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.9", 
    ],
    python_requires=">=3.9",
    setup_requires=setup_requires
)