🏀 EuroLeague Pulse — Agregador Multilingüe de Noticias y Rumores 24/7

EuroLeague Pulse es una aplicación web 100% estática y sin servidor (serverless) diseñada para ejecutarse gratuitamente sobre GitHub Pages, recolectando en tiempo real todas las noticias oficiales, rumores de mercado y fichajes de los principales medios especializados en la Euroliga, con traducción instantánea a Español, Inglés, Turco y Griego.

✨ Características Principales

🌐 Multilingüe en Tiempo Real (ES, EN, TR, EL): Cambio instantáneo de toda la interfaz, etiquetas, calendarios y titulares/resúmenes de cada noticia mediante pretraducción automática en backend y motor de traducción en vivo con caché local en el navegador.

📰 Cobertura Total de 8 Medios de Referencia:

🇪🇺 Eurohoops (eurohoops.net)

🇱🇹 BasketNews (basketnews.com)

🇪🇸 Gigantes del Basket (gigantes.com)

🇪🇸 Encestando (encestando.es)

🇬🇷 SDNA (sdna.gr)

🇬🇷 Gazzetta.gr (gazzetta.gr)

🇹🇷 TrendBasket (trendbasket.net)

🏆 Euroleague.net (euroleaguebasketball.net)

🔥 Clasificación Inteligente (Oficial vs. Rumores): Detección automática mediante palabras clave multilingües para separar comunicados oficiales de rumores y movimientos del mercado de fichajes.

📊 Barra Lateral Deportiva Completa:

Calendario y Resultados por Jornada: Navegación entre jornadas disputadas y próximos encuentros con horarios en zona CET.

Clasificación Oficial (20 Equipos): Tabla actualizada con indicadores visuales de zonas de Playoff directo (Top 6), Play-In (7-10) y Eliminación (11-20).

📱 Diseño Fluido a Pantalla Completa y Responsive: Adaptado desde teléfonos móviles (con navegación táctil por pestañas) hasta monitores panorámicos en cuadrícula de 3 columnas.

🤖 Automatización 24/7 con GitHub Actions: Sin necesidad de servidores ni bases de datos externas.

🏗️ Arquitectura del Proyecto

├── index.html                          # Aplicación web completa (HTML5 + Tailwind CSS + JS Vanilla)
├── scripts/
│   └── fetch_news.py                   # Recolector RSS, clasificador y traductor automático (ES/EN/TR/EL)
├── data/
│   └── news.json                       # Base de datos JSON generada y actualizada cada 30 min
├── .github/
│   └── workflows/
│       └── update-news.yml             # Flujo automático de GitHub Actions (Cron cada 30 minutos)
└── README.md                           # Documentación del proyecto


🚀 Cómo Desplegarlo en tu Cuenta de GitHub

Clona o haz Fork de este repositorio en tu cuenta de GitHub.

Ve a Settings → Pages en tu repositorio.

En el apartado Build and deployment, selecciona la rama main y la carpeta / (root), y pulsa Save.

Para activar la recolección automática de noticias:

Ve a la pestaña Actions y habilita los flujos de trabajo (workflows).

Selecciona Actualizar Noticias y Rumores Euroliga (24/7) y pulsa Run workflow para ejecutar la primera actualización al instante.

A partir de ese momento, el robot actualizará data/news.json automáticamente cada 30 minutos.

🛠️ Tecnologías Utilizadas

Frontend: HTML5, Tailwind CSS (CDN), JavaScript ES6+ Vanilla, Lucide Icons.

Automatización & Scraping: Python 3.11 (feedparser, deep-translator), GitHub Actions.

Alojamiento: GitHub Pages.
