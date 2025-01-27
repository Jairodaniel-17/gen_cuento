# Generador de Cuentos con Imágenes

Este proyecto permite generar cuentos cortos acompañados de imágenes generadas automáticamente utilizando inteligencia artificial.

## Requisitos

- Python 3.10+
- CUDA (opcional, para aceleración GPU, para un procesado más rápido en las imágenes)
- Dependencias listadas en `pyproject.toml`
- Stable Diffusion Automatic1111 activado para consumir mediante API `--api` y tener descargado el modelo lametta_v2012.safetensors
- Modelo de generación de imagen: [Lametta_v2012.safetensors](https://civitai.com/models/158643/lametta)

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Jairodaniel-17/gen_cuento.git
   cd gen_cuento
   ```

2. Crear un entorno virtual:

   ```bash
   pip install uv
   ```

3. Sincronizar el entorno virtual:

   ```bash
   - Windows: `uv sync`
   - Linux/MacOS: `uv sync`
   ```

4. Cambiar el nombre de archivo `example.env` a `.env`:

   ```bash
   mv example.env .env
   ```

5. Editar el archivo `.env` con tus credenciales de API, compatible con OpenAI, DeepSeek. Groq, etc. que usen el SDK de OpenAI.

## Uso

Ejecutar el generador principal:

   ```bash
   uv run streamlit run main.py
   ```

## Estructura del Proyecto

```plaintext
gen_cuento/
├── src/
│   ├── generators/
│   │   ├── story_generator.py
│   │   └── image_generator.py
│   ├── api/
│   │   └── stable_diffusion_api.py
│   └── utils/
│       └── config.py
├── example.env
├── pyproject.toml
├── uv.lock
├── main.py
└── README.md
```

## Contribución

1. Haz un fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -am 'Añade nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

- Para el público: [AGPL](LICENSE)
- Para uso comercial: [Contactar](<mailto:jairodaniel.mt@gmail.com>)

Este software se ofrece bajo dos tipos de licencia:

1. **Licencia de Código Abierto (para uso no comercial) - AGPL-3.0:**

   Este software se distribuye bajo los términos de la **Licencia Pública General Affero (AGPL) versión 3.0**. Puedes usar, copiar, modificar y distribuir este software **para fines no comerciales**, siempre que cumplas con los requisitos de la AGPL-3.0. Esto incluye:

   - Hacer disponible el **código fuente** de cualquier modificación realizada.
   - Proveer acceso al código fuente si el software es usado remotamente (por ejemplo, en servidores).

   **El texto completo de la AGPL-3.0 está disponible en:**  
   <https://www.gnu.org/licenses/agpl-3.0.html>

2. **Licencia Comercial (para uso comercial):**

   Si eres una empresa o deseas usar este software con fines comerciales (por ejemplo, en producción, servidores comerciales, o como parte de un producto o servicio de pago), necesitas obtener una **licencia comercial**.

   - La **licencia comercial** te permite utilizar el software de manera **exclusiva** y **cerrada**, sin la obligación de liberar el código fuente de ninguna modificación.
   - Para obtener una licencia comercial, por favor, contacta a **Jairo Daniel Mendoza Torres** a través del correo electrónico **<jairodaniel.mt@gmail.com>**.

**Exclusión de responsabilidad:**

Este software se distribuye **"tal cual"**, sin garantías de ningún tipo, ya sean expresas o implícitas, incluyendo pero no limitado a las garantías de comercialización o adecuación a un propósito particular. En ningún caso los autores o titulares del copyright serán responsables por daños de cualquier tipo, ya sean directos, indirectos, incidentales o consecuentes, que surjan del uso de este software.

## Contacto

### **Instrucciones para obtener la licencia comercial**

Para obtener una licencia comercial, por favor, contacta a **Jairo Daniel Mendoza Torres** en **<jairodaniel.mt@gmail.com>** para discutir los términos específicos de la licencia.
