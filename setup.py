import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-codeserver-proxy",
    version='0.1.0',
    url="https://github.com/dragonstyle/jupyter-codeserver-proxy",
    author="Charles Teague",
    description="charles@posit.co",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
	keywords=['jupyter', 'VSCode', 'jupyterhub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=1.5.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'codeserver = jupyter_codeserver_proxy:setup_codeserver',
        ]
    },
    package_data={
        'jupyter_codeserver_proxy': ['icons/vscode.svg'],
    },
)
