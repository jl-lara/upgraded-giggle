MapStar TJ - EcoRutas y Seguridad Urbana 🌿🛡️

"Explora el lado verde de la ciudad."
Una aplicación de mapas interactiva enfocada en rutas ecológicas y seguras para los ciudadanos de Tijuana.

🚀 Cómo correr el proyecto

Sigue estos pasos para levantar el entorno de desarrollo local:

Prerrequisitos: Asegúrate de tener Python 3.x instalado.

Instalar dependencias:

pip install flask


Ejecutar el servidor:

python main.py


Abrir en el navegador:
Ve a http://127.0.0.1:5000

🛠️ Stack Tecnológico

Backend: Python / Flask (Micro-framework ligero).

Frontend: HTML5 + Tailwind CSS (Estilos utilitarios y responsivos).

Mapas: Leaflet.js + OpenStreetMap (Tiles).

Iconos: Lucide Icons.

🎨 Justificación de Diseño UX

Este proyecto fue diseñado siguiendo principios de Usabilidad y Accesibilidad (A11y):

Ley de Fitts: Los controles de Zoom se movieron a la esquina inferior derecha para ser accesibles con el pulgar en dispositivos móviles.

Feedback del Sistema (Heurística #1):

Latencia: Se implementó "Optimistic UI" (marcador inmediato) y Toasts de notificación ("Guardando...") para informar al usuario del estado de la red.

Prevención de Errores: Confirmación explícita antes de guardar un punto.

Accesibilidad (A11y):

Vista Dual: Se sincronizó el mapa con una lista lateral navegable por teclado (Tab + Enter), permitiendo el uso a personas que dependen de lectores de pantalla.

Contraste: Se eligió un mapa claro (OpenStreetMap Standard) en lugar de oscuro para garantizar la legibilidad bajo la luz del sol.

🤖 Créditos a la IA

Este código y diseño fueron co-creados utilizando Gemini Canvas.

Rol de la IA: Generación de boilerplate (HTML/Flask), sugerencia de estilos Tailwind y scripts de Leaflet.

Rol del Humano: Refinamiento de UX, corrección de accesibilidad (cambio de mapa oscuro a claro) y lógica de negocio.

Prompt Principal:

"Actua como diseñador web, crea una app de mapas llamada MapStar con Flask y Leaflet. Enfócate en accesibilidad (vista de lista sincronizada) y feedback de usuario (toasts de carga). Usa Tailwind CSS para un diseño moderno."

Proyecto desarrollado para el Laboratorio de UX + IA - Enero 2026