Bitácora de Diseño UX - Actividad 4

Tema: Accesibilidad (A11y) y Vistas Alternativas
Fecha: 27 de Enero, 2026

1. El Problema de Accesibilidad en Mapas

Los mapas interactivos (como Leaflet o Google Maps) son inherentemente visuales. Un usuario que depende de lectores de pantalla (Screen Readers) o que tiene dificultades motoras finas no puede "arrastrar y explorar" fácilmente.

2. Solución: La Vista de Lista Sincronizada

Para cumplir con las pautas WCAG (Web Content Accessibility Guidelines), se implementó una vista de lista complementaria.

A. Estructura Dual (Responsive)

Escritorio: Barra lateral izquierda fija (w-80) y mapa a la derecha.

Móvil: Diseño apilado (Columna). La lista aparece debajo del mapa (o arriba, dependiendo de la preferencia, aquí usamos order de flexbox) para que sea accesible con scroll.

B. Mejoras Técnicas de A11y (Accessibility)

Se agregaron atributos ARIA y roles específicos en map.html:

aria-label en botones: Se etiquetó explícitamente el botón de "Volver" (aria-label="Volver al inicio") y los botones de acción dentro del popup ("Cancelar", "Guardar").

Navegación por Teclado (tabindex="0"): Los items de la lista no son solo divs, tienen tabindex="0" y escuchan el evento onkeypress (Enter). Esto permite que un usuario navegue la lista usando solo la tecla TAB y seleccione un lugar con ENTER para que el mapa se mueva ahí.

Roles Semánticos: Se usó <aside> para la lista y <main> para el mapa, ayudando a los lectores de pantalla a entender la estructura.

C. Feedback Visual (Sincronización)

Interacción Lista -> Mapa: Al hacer clic en la lista, usamos map.flyTo(). Esta animación suave ayuda al usuario a mantener el contexto espacial (ver cómo nos desplazamos de A a B) en lugar de un teletransporte brusco.

Highlight: El item seleccionado en la lista cambia de color (bg-emerald-50), indicando claramente cuál es el punto activo.

3. Prompt Utilizado (IA)

"Modifica la interfaz map.html para tener dos columnas: 'Mapa' y 'Lista de Lugares Guardados'. Cuando se agregue un marcador en el mapa, debe aparecer dinámicamente en la lista con sus coordenadas. Asegúrate de que los botones tengan 'aria-label' y que la lista sea navegable por teclado (tabindex). Al hacer clic en un item de la lista, el mapa debe hacer un 'FlyTo' hacia ese marcador."

Fin del reporte de Actividad 4