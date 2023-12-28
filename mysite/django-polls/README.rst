=====
Polls
=====

Polls es una aplicacion de Django para realizar encuestas basadas en web. Para cada pregunta, los visitantes pueden elegir entre un numero fijo de respuestas

La documentacion detallada se encuentra en el directorio "docs"

Quick start
-----------

1. Agrege polls a tu INSTALLED_APPS en settings como esto::

    INSTALLED_APPS = [
        ...,
        "polls",
    ]

2. Incluye las encuestas URLconf en tu proyecto urls.py asi::
    path("polls", include("polls.urls")),

3. Corre "python manage.py migrate" para crear un modelo de polls

4. Inicie el servidor de desarrollo y visite http://127.0.0.1:8000/admin/ para crear una encuesta (necesitara que la aplicacion de adminitracion este habilitada).

5. Vitite http://127.0.0.1:8000/polls/ para ser participe de las encuestas