ES // EN

MovieBlog Project - Sebastian Moreno y Sebastian Munoz
Final stage of CoderHouse python course

En resumen, desde el día uno nos conectamos en simultaneo gracias al plugin "Share" the VSCODE asignandonos tareas mutuamente y enfocandonos en cada error que fue surgiendo resolviendolo juntos para ser mas eficaces. Fuimos progresando a pasos firmes hasta llegar al cometido.
//
From the beginning we connected simultaneously from "Share", the VSCODE plugin. Assigning tasks to each other and focusing on each error that arose, solving it together to be more effective. We progressed steadily until we reached the goal.

1) Abrir Git Bash para Windows o una terminal para Linux/Unix. // Open Git Bash for Windows or a new terminal for Linux/Unix   Crear directorio de trabajo para el proyecto de curso // Create a new directory of work for the actual project
   >>>
   cd
   mkdir -p Documents/movieblog_project
   cd Documents/movieblog_project
   ls 
   >>>


2) Clonar el proyecto y cambiar de rama // Clone the project and change the branch

   >>>git clone https://github.com/sealmoar/MovieBlog-coder.git

   >>>cd MovieBlog-coder

   >>>git checkout master

3) Crear y activar entorno virtual (Windows)
   Windows // Create and activate the VENV (Virtual enviroment)

   -Windows

   >>>python -m venv venv
   >>>.\venv\Scripts\activate

   -Linux

   >>>python3 -m venv venv
   >>>source venv/bin/activate

4) Instalar las dependencias del proyecto // Install the project requirements
   
   >>>pip install -r requirements.txt

5) Crear base de datos a partir de las migraciones // Create the data base from migrates

   >>>python manage.py makemigrations
   >>>python manage.py migrate

6) Crear super-usuario // Create super-user

   >>>python manage.py createsuperuser
   (Ingrese Username, Email address y Password // Log Username, Emmail addres and Password)

7)Crear estáticos // Create Statics

   >>>python manage.py collectstatic

8) Ejecutar proyecto, el servidor de Django expone el servicio por el localhost en el puerto 8000 por defecto "http://127.0.0.1:8000/" // Execute the project, the Django server shows the service from the localhost in "8000" by default "http://127.0.0.1:8000/"

   >>> python manage.py runserver
