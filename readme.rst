scrapy database pipeline
========================

Introduction
------------

Use pipeline to persist item to the database, just provide the tablename

INSTALL
-------

.. code:: shell

    pip install scrapy_db_pipeline

Usage
-----

configure on setting.py

.. code:: python

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'password'
    DB_NAME = 'db_name

    ITEM_PIPELINES = {
       #...
       'scrapy_db_pipeline.pipelines.DBStorePipeline': 300,
       #...
    }

write your item

.. code:: python

    class CalendarItem(scrapy.Item):
        __table_name__ = 'your_table_name'
        some_item = scrapy.Field()  

**tips**: You must create the table before running Scrapy. Because I
can't know what the type of your field on the database table.

TODO:
-----

database support (if I have time):

-  [x] mysql
-  [ ] ....

