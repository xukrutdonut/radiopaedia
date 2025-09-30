# 🏥 Radiología Pediátrica - Radiopaedia Scraper

Una herramienta para crear tu propia web de radiología pediátrica mediante el scraping de casos seleccionados de Radiopaedia.

## 📋 Descripción

Este proyecto te permite:
- Extraer casos de tu playlist de Radiopaedia
- Crear una base de datos local de casos educativos
- Visualizar los casos en una interfaz web moderna y limpia
- Usar los casos para educación y referencia en radiología pediátrica

## 🚀 Inicio Rápido

### Prerequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clona el repositorio** (o descarga los archivos)

```bash
git clone https://github.com/xukrutdonut/radiopaedia.git
cd radiopaedia
```

2. **Crea un entorno virtual** (recomendado)

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

## 📥 Uso del Scraper

### Scraping de tu playlist

Por defecto, el scraper está configurado para la playlist 85715. Para ejecutarlo:

```bash
python scraper.py
```

Para usar una playlist diferente:

```bash
python scraper.py https://radiopaedia.org/playlists/YOUR_PLAYLIST_ID
```

El scraper:
- Extraerá todos los casos de la playlist
- Guardará la información en `data/cases.json`
- Incluye un delay entre peticiones para ser respetuoso con el servidor

**Nota importante:** Por favor usa esta herramienta de manera responsable. Radiopaedia es un recurso educativo gratuito y debemos respetar sus servidores.

## 🌐 Uso de la Aplicación Web

Una vez que hayas extraído los casos, puedes visualizarlos en una interfaz web:

```bash
python webapp.py
```

Luego abre tu navegador en: `http://localhost:5000`

La aplicación web incluye:
- Vista de lista de todos los casos
- Página de detalle para cada caso
- Información del paciente
- Hallazgos, diagnóstico y discusión
- Imágenes del caso
- API REST para acceso programático

## 📁 Estructura del Proyecto

```
radiopaedia/
├── scraper.py           # Script para extraer casos de Radiopaedia
├── webapp.py            # Aplicación web Flask
├── requirements.txt     # Dependencias de Python
├── templates/           # Plantillas HTML
│   ├── base.html       # Plantilla base
│   ├── index.html      # Página principal
│   └── case.html       # Página de detalle de caso
├── data/               # Directorio para datos (creado automáticamente)
│   └── cases.json     # Casos extraídos
└── README.md          # Este archivo
```

## 🔌 API Endpoints

La aplicación web proporciona una API REST:

- `GET /` - Página principal con lista de casos
- `GET /case/<id>` - Detalle de un caso específico
- `GET /api/cases` - JSON con todos los casos
- `GET /api/case/<id>` - JSON de un caso específico

## 📊 Formato de Datos

Los casos se almacenan en formato JSON con la siguiente estructura:

```json
{
  "url": "URL del caso original",
  "title": "Título del caso",
  "patient_data": {
    "Age": "Edad del paciente",
    "Gender": "Género"
  },
  "study": "Tipo de estudio realizado",
  "findings": "Hallazgos radiológicos",
  "diagnosis": "Diagnóstico",
  "discussion": "Discusión del caso",
  "images": ["URLs de las imágenes"]
}
```

## ⚙️ Personalización

### Modificar el diseño

Las plantillas HTML están en el directorio `templates/`. Puedes modificar:
- `base.html` - Diseño general y estilos
- `index.html` - Página principal
- `case.html` - Página de detalle

### Modificar el scraper

Edita `scraper.py` para:
- Cambiar el delay entre peticiones
- Extraer información adicional
- Modificar el formato de salida

## 🛡️ Consideraciones Legales y Éticas

- Este proyecto es solo para **fines educativos**
- El contenido extraído es propiedad de Radiopaedia.org
- Debes dar crédito apropiado a la fuente original
- No uses esto con fines comerciales sin permiso
- Respeta los términos de servicio de Radiopaedia
- Usa delays apropiados entre peticiones

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Haz commit de tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto para fines educativos. El contenido extraído de Radiopaedia pertenece a sus autores originales.

## 🙏 Agradecimientos

- [Radiopaedia.org](https://radiopaedia.org) - Por proporcionar un excelente recurso educativo gratuito
- Todos los contribuidores de casos a Radiopaedia

## 📞 Soporte

Si tienes problemas o preguntas:
1. Revisa la documentación
2. Busca en los issues existentes
3. Abre un nuevo issue si es necesario

---

**Nota:** Este es un proyecto educativo. Por favor usa esta herramienta de manera responsable y ética.
