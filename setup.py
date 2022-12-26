# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Corona-19-API",
    author_email="dhlife09@gmail.com",
    url="",
    keywords=["Swagger", "Corona-19-API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    &lt;b&gt;굿바이코로나에서 제공하는 코로나바이러스감염증-19 API 입니다.&lt;/b&gt;&lt;br&gt;코로나바이러스감염증-19 API 서비스 제공 - 코로나19 관련 API를 무제한 무료로 사용하세요! 🇰🇷 South Korea&#x27;s COVID-19 API service provided - Use COVID-19 related API for free for unlimited !
    """
)
