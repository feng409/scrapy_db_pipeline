from setuptools import setup


setup(
    name='scrapy_db_pipeline',
    version='1.0',
    description='persist item to the database table',
    long_description=open('readme.rst').read(),
    long_description_content_type='text/markdown',
    keywords='scrapy pipeline',
    license='MIT License',
    author="chemf",
    author_email='eoyohe@gmail.com',
    url='https://github.com/feng409/scrapy_db_pipeline',
    classifiers=[
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
    packages=[
        'scrapy_db_pipeline',
    ],
    install_requires=[
        'DBUtils',
        'pymysql'
    ],
)
