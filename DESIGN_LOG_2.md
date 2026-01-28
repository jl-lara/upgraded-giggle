Bitácora de Diseño UX - Actividad 2

Tema: Arquitectura de Información y Ley de Fitts
Fecha: 27 de Enero, 2026

1. Configuración del "Lienzo" (El Mapa)

A. Elección del TileLayer (Estilo del Mapa)

Decisión Final: Se eligió OpenStreetMap Standard (Tema Claro).

Iteración de Diseño (Pivot): Inicialmente se implementó un mapa en modo oscuro ("Dark Matter") para coincidir estéticamente con la Landing Page.

Corrección basada en Feedback: Se detectó que el mapa oscuro presentaba problemas de legibilidad y accesibilidad (bajo contraste), dificultando la visualización de calles para algunos usuarios.

Justificación UX: Se aplicó la Ley de Jakob (los usuarios prefieren que tu sitio funcione como los que ya conocen). Al usar el estilo estándar de mapas, reducimos la carga cognitiva y mejoramos la visibilidad en condiciones de mucha luz (ej. caminando por la calle bajo el sol).

B. Ley de Fitts y Controles

La Ley de Fitts establece que el tiempo para alcanzar un objetivo depende del tamaño y la distancia.

Decisión: Se movieron los controles de Zoom a la posición bottomright (inferior derecha).

Por qué: En dispositivos móviles, la esquina inferior derecha es la zona más accesible para el pulgar de un usuario diestro (la mayoría). La posición por defecto (arriba izquierda) es la zona más difícil de alcanzar ("Hard to reach zone").

Mejora de Tamaño: Se aumentó el tamaño de los botones de zoom a 44px (mínimo recomendado por Apple/Google para touch targets) mediante CSS personalizado.

C. Navegación

Se actualizó la barra de navegación flotante a un estilo claro (bg-white/90) con texto oscuro para mantener el contraste adecuado sobre el nuevo mapa claro.

2. Prompt Utilizado (IA)

"Genera un archivo HTML que incluya la librería Leaflet.js (vía CDN) y Tailwind CSS. Crea un contenedor div 'map' que ocupe el 100% del ancho y 500px de alto (o 'h-screen'). Inicializa el mapa centrado en tijuana con un tilelayer de OpenStreetMap. Asegúrate de que los botones de zoom estén en una posición fácil de alcanzar"

"Modifica el archivo map.html. Cambia el estilo del mapa a OpenStreetMap estándar (claro) para mejorar la accesibilidad y el contraste. Ajusta también los colores de la barra de navegación flotante para que sean legibles (texto oscuro sobre fondo blanco) acorde al nuevo fondo claro del mapa."

Fin del reporte de Actividad 2