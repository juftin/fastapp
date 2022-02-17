
ml-server
=========

Installation
------------

``ml-server`` isn't ready for PyPi yet. In the meantime you can install directly from GitHub:

.. code-block:: shell

   pip install "ml-server @ git+https://github.com/juftin/ml-server.git@main"

Using Out the Example Server
----------------------------

.. code-block:: shell

   pip install "ml-server[example] @ git+https://github.com/juftin/ml-server.git@main"

.. code-block:: shell

   ml-server serve-debug ml_server.app.example:app

...or via docker:

.. code-block:: shell

   docker run --rm -it \
       --publish 8080:8080 \
       --volume ${PWD}/ml_server:/root/ml_server \
       juftin/ml-server:latest \
       serve-debug ml_server.app.example:app

Using ml-server to build an app
-------------------------------

Create a Python File with Endpoints, we'll call this ``main.py``\ :

.. code-block:: python

   from datetime import datetime

   from ml_server.app import app


   @app.get("/hello")
   def custom_endpoint() -> dict:
       """"
       This is a Custom API Endpoint
       """
       return dict(timestamp=datetime.now(),
                   hello="world")

Then, using the ``ml-server`` CLI we can serve this App:

.. code-block:: shell

   ml-server serve-debug main:app

Test out our new endpoint:

.. code-block:: shell

   curl \
     --request GET \
     --silent \
     --header "Content-Type: application/json" \
     http://localhost:8080/hello

Alternatively, if we want to serve this app using Gunicorn, Nginx, and the UvicornWorker:

.. code-block:: shell

   ml-server serve main:app
