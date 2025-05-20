Guía para Contribuir a Storyteller-GPT
¡Gracias por tu interés en contribuir al Generador de Cuentos Mágicos! Todas las contribuciones, desde pequeños arreglos de errores hasta nuevas funcionalidades o mejoras en la documentación, son bienvenidas y apreciadas.

Esta guía te ayudará a entender cómo puedes participar en el proyecto.

💡 ¿Cómo puedo Contribuir?
Hay muchas maneras de contribuir, incluso si no eres un experto en código:

Reportando errores (Bugs)
Sugiriendo nuevas características
Mejorando la documentación
Escribiendo código (arreglos, mejoras, nuevas funciones)
Revisando Pull Requests de otros
🐛 Reportar Errores (Bugs)
Si encuentras un error en el generador, ¡por favor repórtalo! Una buena descripción del error nos ayuda a corregirlo rápidamente.

Asegúrate de que el error no haya sido reportado ya buscando en la sección de Issues de GitHub.
Si no lo encuentras, abre un nuevo Issue.
Incluye la siguiente información:
Título claro y conciso (ej. "Error al generar idea con tema largo").
Pasos para reproducir el error: Describe exactamente cómo podemos hacer que el error ocurra.
Comportamiento esperado: ¿Qué debería haber sucedido?
Comportamiento actual: ¿Qué sucedió realmente?
Versión de Python y librerías que estás usando (puedes obtener esto con pip freeze).
Cualquier mensaje de error completo que hayas recibido en la terminal.
✨ Sugerir Nuevas Características
¿Tienes una idea genial para mejorar el generador? ¡Nos encantaría escucharla!

Asegúrate de que la característica no haya sido sugerida ya en la sección de Issues.
Abre un nuevo Issue con la etiqueta enhancement o feature.
Describe tu idea con el mayor detalle posible:
¿Cuál es la característica?
¿Por qué crees que sería útil? (Caso de uso).
¿Cómo esperas que funcione? (Comportamiento deseado).
💻 Contribuir con Código (Pull Requests)
Si quieres enviar código, sigue estos pasos para que tu contribución sea fácil de revisar y fusionar:

1. Haz un "Fork" del Repositorio
Ve a la página principal de Storyteller-GPT en GitHub.
Haz clic en el botón "Fork" en la esquina superior derecha. Esto creará una copia del repositorio en tu propia cuenta de GitHub.
2. Clona tu Fork Localmente
Abre tu terminal.
Clona tu repositorio forkeado a tu máquina local:
Bash

git clone https://github.com/TuUsuario/Storyteller-GPT.git
cd Storyteller-GPT
(Asegúrate de reemplazar TuUsuario con tu nombre de usuario de GitHub).
3. Crea una Rama para tus Cambios
Es crucial trabajar en una rama separada, no directamente en main. Dale un nombre descriptivo a tu rama (ej. feat/nueva-funcion, fix/nombre-del-bug).
Bash

git checkout -b tu-nueva-rama-descriptiva
4. Realiza tus Cambios
Edita los archivos y añade tu código.
Asegúrate de que tus cambios no rompan la funcionalidad existente. Si es posible, prueba tu código.
Estilo de Código: Intentamos seguir las convenciones de estilo de Python (PEP 8). Usa un linter como flake8 o black si puedes, o simplemente trata de mantener el código limpio y legible.
Comentarios: Añade comentarios donde sea necesario para explicar tu lógica, especialmente en funciones complejas o nuevas.
Docstrings: Si creas nuevas funciones o clases, por favor añade docstrings que describan su propósito, argumentos y lo que retornan.
5. Prueba tus Cambios
Antes de enviar tu Pull Request, ejecuta el script principal para asegurarte de que todo funciona como esperas y no has introducido nuevos errores.
6. Confirma y Sube tus Cambios
Añade los archivos que has modificado o creado:
Bash

git add .
Confirma tus cambios con un mensaje claro y conciso:
Bash

git commit -m "feat: añade [nueva función]"
# o "fix: corrige [nombre del bug]"
(Usa prefijos como feat: para nuevas características, fix: para correcciones, docs: para documentación, refactor: para refactorización de código, etc.).
Sube tus cambios a tu repositorio forkeado en GitHub:
Bash

git push origin tu-nueva-rama-descriptiva
7. Abre un Pull Request (PR)
Ve a tu repositorio forkeado en GitHub.
Verás una notificación para comparar y crear un Pull Request desde tu rama a la rama main del repositorio original de Storyteller-GPT. Haz clic en ella.
Título de la PR: Usa un título descriptivo (el mismo que tu mensaje de commit si es apropiado).
Descripción de la PR: Explica en detalle qué problemas resuelve tu código o qué nuevas características añade. Incluye capturas de pantalla o ejemplos si ayudan a entender.
Envía tu Pull Request.
8. Proceso de Revisión
El mantenedor del repositorio (¡ese eres tú, por ahora!) revisará tu Pull Request.
Podemos dejar comentarios, sugerir cambios o hacer preguntas. Por favor, sé paciente y responde a los comentarios. Es posible que te pidamos que realices más cambios en tu rama.
Una vez que los cambios sean aprobados, se fusionarán en el repositorio principal.
🙏 Agradecimientos
¡Cada contribución, grande o pequeña, ayuda a que Storyteller-GPT sea una herramienta mejor! Gracias por ser parte de la comunidad.
