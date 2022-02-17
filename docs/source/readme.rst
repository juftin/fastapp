
FastApp
=======

HTTP Apps Made Easier with FastApp

Installation
------------

``FastApp`` isn't ready for PyPi yet. In the meantime you can install directly from GitHub:

.. code-block:: shell

   pip install "fastapp @ git+https://github.com/juftin/fastapp.git@main"

Using Out the Example Server
----------------------------

.. code-block:: shell

   pip install "fastapp[example] @ git+https://github.com/juftin/fastapp.git@main"

.. code-block:: shell

   fastapp serve-debug fastapp.app.example:app

...or via docker:

.. code-block:: shell

   docker run --rm -it \
       --publish 8080:8080 \
       --volume ${PWD}/fastapp:/root/fastapp \
       juftin/fastapp:latest \
       serve-debug fastapp.app.example:app

Using FastApp to build an app
-----------------------------

Create a Python File with Endpoints, we'll call this ``main.py``\ :

.. code-block:: python

   from datetime import datetime

   from fastapp.app import app


   @app.get("/hello")
   def custom_endpoint() -> dict:
       """"
       This is a Custom API Endpoint
       """
       return dict(timestamp=datetime.now(),
                   hello="world")

Then, using the ``FastApp`` CLI we can serve this App:

.. code-block:: shell

   fastapp serve-debug main:app

Test out our new endpoint:

.. code-block:: shell

   curl \
     --request GET \
     --silent \
     --header "Content-Type: application/json" \
     http://localhost:8080/hello

Alternatively, if we want to serve this app using Gunicorn, Nginx, and the UvicornWorker:

.. code-block:: shell

   fastapp serve main:app
