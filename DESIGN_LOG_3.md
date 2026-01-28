Bitácora de Diseño UX - Actividad 3

Tema: Micro-interacciones y Feedback del Sistema
Fecha: 27 de Enero, 2026

1. Estrategia de Feedback (Visibilidad del Estado)

A. El Problema de la Latencia

En una aplicación de mapas móviles, la conexión a internet puede ser inestable. Si el usuario toca el mapa y no pasa nada hasta que el servidor responde (2-3 segundos después), pensará que la app se trabó.

B. Solución: Optimistic UI + Toast Notification

Se implementó un patrón de interacción de tres estados:

Estado Inicial (Input Mode): Al hacer clic, se coloca un marcador inmediatamente (JavaScript local). Esto confirma que la app registró el toque.

Prevención de Errores: Se abre un popup con un botón explícito de "Guardar". Esto evita llenar la base de datos de clics accidentales al hacer scroll o zoom (Ley de Murphy).

Estado de Carga (Loading): Al confirmar, aparece un "Toast" flotante con un icono de carga (loader-2 animado).

Decisión de Diseño: Se eligió un Toast inferior en lugar de un alert() del navegador o bloquear toda la pantalla, para no interrumpir la experiencia inmersiva.

Estado Final (Éxito/Error): * Si es éxito: El Toast cambia a "¡Guardado!" con un check verde y desaparece solo.

Si es error: El marcador se elimina automáticamente para no engañar al usuario.

2. Decisiones de Accesibilidad en el Feedback

Iconos + Texto: El Toast no depende solo del color (rojo/verde) para comunicar el estado, sino que usa iconos (check-circle vs alert-circle) y texto descriptivo, ayudando a usuarios con daltonismo.

3. Prompt Utilizado (IA)

"Escribe un script en JS para Leaflet dentro de map.html. Cuando el usuario haga clic en el mapa: 1. Ponga un marcador temporal inmediatamente. 2. Abra un popup que pregunte '¿Guardar este punto?'. 3. Al confirmar, envíe las coordenadas (lat, long) a un endpoint Flask /guardar_punto usando fetch. Muestra un 'toast' o notificación flotante visual que diga 'Guardando...' con un spinner mientras se procesa, y que cambie a 'Guardado' al finalizar."

Fin del reporte de Actividad 3