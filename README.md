# Radiopaedia Scraper & Viewer

Una aplicación web para visualizar casos de imágenes médicas de Radiopaedia con un visor similar a la plataforma original.

## Características

- 🔍 **Scraper**: Extrae información de playlists de radiopaedia.org
- 🖼️ **Visor de Imágenes**: Interfaz moderna para visualizar imágenes médicas (RM, CT, etc.)
- 📱 **Responsive**: Diseño adaptable para diferentes dispositivos
- 🎨 **UI Moderna**: Interfaz similar a Radiopaedia con tema oscuro
- ⌨️ **Atajos de Teclado**: Navegación con flechas y ESC para cerrar modal

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/xukrutdonut/radiopaedia.git
cd radiopaedia
```

2. Instalar dependencias de Python:
```bash
pip install -r requirements.txt
```

## Uso

### 1. Scraping de Datos

Para extraer información de una playlist de Radiopaedia:

```bash
# Scraping básico (solo lista de casos)
python scraper.py 85715

# Scraping completo (incluye detalles de cada caso)
python scraper.py 85715 --full
```

Los datos se guardarán en `data/playlist_data.json`.

### 2. Visualización

Iniciar el servidor web:

```bash
python server.py
```

El servidor estará disponible en: http://localhost:8000

Para usar un puerto diferente:
```bash
python server.py 3000
```

## Estructura del Proyecto

```
radiopaedia/
├── scraper.py          # Script de scraping
├── server.py           # Servidor HTTP
├── requirements.txt    # Dependencias Python
├── data/              # Datos extraídos
│   └── playlist_data.json
└── web/               # Aplicación web
    ├── index.html
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── data/          # Datos para el visor
        └── playlist_data.json
```

## Funcionalidades del Visor

### Navegación
- **Búsqueda**: Filtrar casos por título o descripción
- **Lista de Casos**: Sidebar con todos los casos disponibles
- **Click en Caso**: Ver detalles completos del caso

### Visualización de Imágenes
- **Galería**: Vista en miniatura de todas las imágenes
- **Modal**: Visor a pantalla completa al hacer click
- **Zoom**: Controles para acercar/alejar imágenes
- **Navegación**: Flechas para moverse entre imágenes
- **Teclado**: 
  - `←` / `→`: Navegar entre imágenes
  - `ESC`: Cerrar modal

## Características Técnicas

### Scraper
- Extrae títulos, descripciones y diagnósticos
- Identifica enlaces a casos individuales
- Extrae URLs de imágenes médicas
- Respeta rate limiting (1 segundo entre requests)
- Guarda datos en formato JSON

### Visor Web
- HTML5 + CSS3 + JavaScript vanilla (sin frameworks)
- Diseño responsive con CSS Grid y Flexbox
- Tema oscuro optimizado para visualización médica
- Animaciones suaves y transiciones
- Compatible con navegadores modernos

## Desarrollo

El proyecto usa tecnologías estándar web sin dependencias externas para el frontend:
- HTML5 para estructura
- CSS3 para estilos y animaciones
- JavaScript vanilla para funcionalidad

Para desarrollo, el servidor Python sirve los archivos estáticos desde el directorio `web/`.

## Notas

- El scraper incluye datos de ejemplo si no se pueden cargar datos reales
- Las imágenes placeholder se usan como demostración
- El proyecto respeta las políticas de rate limiting de Radiopaedia
- Para uso educativo únicamente

## Licencia

Este proyecto es para fines educativos.
