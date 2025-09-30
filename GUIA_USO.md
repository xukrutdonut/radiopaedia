# 📖 Guía de Uso Completa - Radiología Pediátrica

## 🎯 Objetivo del Proyecto

Este proyecto te permite crear tu propio sitio web de radiología pediátrica utilizando casos educativos de tu playlist de Radiopaedia. Es ideal para:
- Crear colecciones personalizadas de casos
- Estudiar casos específicos de radiología infantil
- Compartir casos educativos con colegas o estudiantes
- Tener acceso offline a casos seleccionados

## 🚀 Instalación Paso a Paso

### Opción 1: Instalación Rápida (Recomendada)

#### En Linux/Mac:
```bash
./run.sh
```

#### En Windows:
```bash
run.bat
```

El script automáticamente:
1. Creará el entorno virtual
2. Instalará las dependencias
3. Te preguntará qué quieres hacer (scraper o web app)

### Opción 2: Instalación Manual

1. **Crea un entorno virtual:**
```bash
python -m venv venv
```

2. **Activa el entorno virtual:**

En Linux/Mac:
```bash
source venv/bin/activate
```

En Windows:
```bash
venv\Scripts\activate
```

3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

## 📥 Extracción de Casos

### Paso 1: Encuentra tu Playlist

1. Ve a [Radiopaedia.org](https://radiopaedia.org)
2. Crea una cuenta (si aún no tienes una)
3. Crea una playlist con los casos que te interesan
4. Copia la URL de tu playlist (ejemplo: `https://radiopaedia.org/playlists/85715`)

### Paso 2: Ejecuta el Scraper

#### Usando la playlist por defecto (85715):
```bash
python scraper.py
```

#### Usando tu propia playlist:
```bash
python scraper.py https://radiopaedia.org/playlists/TU_PLAYLIST_ID
```

### Paso 3: Espera a que termine

El scraper:
- Mostrará el progreso de cada caso
- Incluye delays de 1 segundo entre peticiones (¡sé respetuoso con el servidor!)
- Guardará los datos en `data/cases.json`

**Tiempo estimado:** 1-2 segundos por caso + tiempo de descarga

## 🌐 Visualización de Casos

### Iniciar la Aplicación Web

```bash
python webapp.py
```

Luego abre tu navegador en: **http://localhost:5000**

### Características de la Web App

1. **Página Principal**
   - Lista de todos los casos
   - Información básica de cada caso
   - Búsqueda visual rápida

2. **Página de Detalle**
   - Información completa del paciente
   - Tipo de estudio realizado
   - Hallazgos radiológicos
   - Diagnóstico detallado
   - Discusión del caso
   - Imágenes (si están disponibles)
   - Enlace al caso original

3. **API REST**
   - `GET /api/cases` - Lista todos los casos en formato JSON
   - `GET /api/case/<id>` - Obtiene un caso específico

## 🔧 Personalización Avanzada

### Modificar el Diseño

Edita los archivos en `templates/`:

- **`base.html`**: Diseño general, colores, fuentes
- **`index.html`**: Página principal de casos
- **`case.html`**: Página de detalle del caso

### Cambiar el Puerto del Servidor

Edita `webapp.py` y cambia la línea:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Por ejemplo, para usar el puerto 8080:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Ajustar el Delay del Scraper

Edita `scraper.py` en la función `scrape_playlist()`:
```python
def scrape_playlist(self, output_file: str = 'cases.json', delay: float = 1.0):
```

Cambia `delay: float = 1.0` a un valor mayor para ser más conservador.

### Agregar Campos Personalizados

En `scraper.py`, en la función `scrape_case()`, puedes agregar más campos al diccionario `case_data`:

```python
case_data = {
    'url': case_url,
    'title': '',
    'patient_data': {},
    'study': '',
    'findings': '',
    'diagnosis': '',
    'discussion': '',
    'images': [],
    'tu_campo_nuevo': ''  # Agrega tus campos aquí
}
```

## 💡 Casos de Uso

### Uso 1: Estudio Personal
```bash
# 1. Extrae tus casos favoritos
python scraper.py https://radiopaedia.org/playlists/TU_PLAYLIST

# 2. Estudia offline
python webapp.py
```

### Uso 2: Presentaciones Educativas
1. Crea una playlist temática (ej: "Trauma pediátrico")
2. Extrae los casos
3. Usa la web app durante tus presentaciones
4. Los enlaces originales están disponibles para referencias

### Uso 3: Investigación
1. Extrae casos de tu área de interés
2. Usa la API para análisis programático:
```python
import requests
cases = requests.get('http://localhost:5000/api/cases').json()
# Analiza los datos
```

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
**Solución:** Asegúrate de haber activado el entorno virtual e instalado las dependencias:
```bash
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

### Error: "No cases found in playlist"
**Solución:** 
- Verifica que la URL de la playlist sea correcta
- Asegúrate de tener conexión a internet
- Verifica que la playlist no esté vacía

### Error: "Address already in use"
**Solución:** El puerto 5000 está ocupado. Opciones:
1. Cierra la aplicación que usa el puerto
2. Cambia el puerto en `webapp.py`

### Los casos no se muestran en la web
**Solución:**
1. Verifica que existe el archivo `data/cases.json`
2. Verifica que el archivo tiene contenido válido:
```bash
cat data/cases.json  # Linux/Mac
type data\cases.json  # Windows
```

### Imágenes no se cargan
**Nota:** Las imágenes se cargan directamente desde Radiopaedia. Si no se muestran:
- Verifica tu conexión a internet
- Las imágenes requieren que Radiopaedia esté disponible

## ⚖️ Consideraciones Legales

### ✅ Permitido:
- Uso personal para estudio
- Uso educativo en instituciones
- Referencia a casos originales
- Compartir con fines educativos no comerciales

### ❌ No Permitido:
- Uso comercial sin permiso
- Eliminar atribución a Radiopaedia
- Redistribución masiva del contenido
- Uso que viole los términos de servicio de Radiopaedia

### 📝 Atribución Requerida:
Siempre da crédito a:
- Radiopaedia.org como fuente
- Los autores originales de los casos
- Mantén los enlaces a los casos originales

## 🔒 Mejores Prácticas

1. **Respeta el servidor de Radiopaedia:**
   - No reduzcas el delay entre peticiones
   - No hagas scraping masivo
   - Evita scraping en horas pico

2. **Seguridad:**
   - No uses en producción sin HTTPS
   - No expongas el servidor a internet público sin autenticación
   - Mantén las dependencias actualizadas

3. **Ética:**
   - Usa solo para educación
   - No elimines atribuciones
   - Respeta la propiedad intelectual

## 📊 Estructura de Datos

Los casos se guardan en formato JSON:

```json
{
  "url": "https://radiopaedia.org/cases/12345",
  "title": "Título del caso",
  "patient_data": {
    "Age": "5 años",
    "Gender": "Masculino"
  },
  "study": "Radiografía de tórax",
  "findings": "Descripción de hallazgos...",
  "diagnosis": "Diagnóstico final",
  "discussion": "Discusión del caso...",
  "images": ["url1", "url2", ...]
}
```

## 🆘 Soporte

### Documentación Adicional:
- [README.md](README.md) - Documentación general
- [requirements.txt](requirements.txt) - Lista de dependencias
- [config.example.json](config.example.json) - Configuración de ejemplo

### Reportar Problemas:
1. Verifica que tu problema no esté en esta guía
2. Revisa los issues existentes en GitHub
3. Crea un nuevo issue con:
   - Descripción del problema
   - Pasos para reproducirlo
   - Mensajes de error
   - Tu entorno (OS, Python version)

## 🎓 Recursos Adicionales

- [Radiopaedia.org](https://radiopaedia.org) - Fuente original
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/)

---

¡Disfruta aprendiendo radiología pediátrica! 🏥📚
