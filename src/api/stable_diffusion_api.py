import json
import requests
import base64
import os
import io
from PIL import Image
from typing import Dict, Any, List
import datetime
import logging

logging.basicConfig(
    filename="stable_diffusion.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class StableDiffusionAPI:
    """
    Clase para interactuar con la API de Stable Diffusion.
    """

    def __init__(
        self,
        api_url: str,
        output_folder: str = "imagenes_generadas",
        default_payload: Dict[str, Any] = None,
    ):
        """
        Inicializa la clase StableDiffusionAPI.
        """
        self.api_url = api_url
        self.output_folder = os.path.abspath(output_folder)
        os.makedirs(self.output_folder, exist_ok=True)
        self.default_payload = default_payload or {
            "prompt": "un cachorro con un sombrero de mago",
            "negative_prompt": "(worst quality, low quality:1.4), monochrome, zombie, (interlocked fingers:1.2), monster, watermark, text",
            "steps": 20,
            "width": 768,
            "height": 768,
            "sampler_index": "Euler a",
            "scheduler": "Automatic",
            "cfg_scale": 9,
            "save_images": False,
            "override_settings": {},
        }
        logging.info(
            f"Instancia de StableDiffusionAPI creada. Carpeta de salida: {self.output_folder}"
        )

    def generate_images(self, payload_overrides: Dict[str, Any] = None) -> List[str]:
        """
        Genera imágenes utilizando la API de Automatic 1111 force Stable Diffusion
        """
        payload = self.default_payload.copy()
        if payload_overrides:
            payload.update(payload_overrides)

        endpoint_url = f"{self.api_url}/sdapi/v1/txt2img"

        try:
            response = requests.post(endpoint_url, json=payload, timeout=600)
            response.raise_for_status()
            data = response.json()
            logging.debug(f"Respuesta de la API: {data}")

            if "images" in data and data["images"]:
                saved_images = []
                for i, image_base64 in enumerate(data["images"]):
                    try:
                        image = Image.open(io.BytesIO(base64.b64decode(image_base64)))
                        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                        filename = os.path.join(
                            self.output_folder, f"imagen_{timestamp}_{i}.png"
                        )
                        image.save(filename)
                        logging.info(f"Imagen guardada en: {filename}")
                        saved_images.append(filename)
                    except (ValueError, OSError) as e:
                        logging.error(
                            f"Error al decodificar o guardar la imagen {i}: {e}"
                        )
                        logging.debug(
                            f"Datos base64 (primeros 100 caracteres): {image_base64[:100]}..."
                        )
                return saved_images
            else:
                logging.warning("No se encontraron imágenes en la respuesta de la API.")
                if "info" in data:
                    logging.info(f"Información adicional de la API: {data['info']}")
                else:
                    logging.info(f"Respuesta completa de la API: {data}")
                return []

        except requests.exceptions.RequestException as e:
            logging.error(f"Error en la solicitud a la API: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error al decodificar la respuesta JSON: {e}")
            logging.error(
                f"Respuesta cruda del servidor: {response.text if 'response' in locals() else 'No hay respuesta del servidor'}"
            )
            raise
        except Exception as e:
            logging.exception(f"Un error inesperado ha ocurrido: {e}")
            raise
