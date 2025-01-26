import json
import logging
import requests
from src.api.stable_diffusion_api import StableDiffusionAPI
from src.utils.config import API_URL_STABLE_DIFFUSION, DEFAULT_PAYLOAD_STABLE_DIFFUSION


class ImageGenerator:
    def __init__(self):
        self.sd_api = StableDiffusionAPI(
            API_URL_STABLE_DIFFUSION, default_payload=DEFAULT_PAYLOAD_STABLE_DIFFUSION
        )

    def generate_images(self, image_configs: list[dict]) -> list[str]:
        generated_images = []
        for config in image_configs:
            try:
                result = self.sd_api.generate_images(config)
                if isinstance(result, str):
                    generated_images.extend(result.split(","))
                else:
                    generated_images.extend(result)
            except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                logging.error(f"Error de red o JSON: {e}")
            except Exception as e:
                logging.error(f"Error inesperado: {e}")

        return generated_images

    def print_results(self, images):
        for i, path in enumerate(images):
            print(f"Imagen {i + 1}: {path.strip()}")
        print(f"Total: {len(images)}")
