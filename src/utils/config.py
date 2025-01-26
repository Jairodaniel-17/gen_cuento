import dotenv
import os

dotenv.load_dotenv()

LLM_API_MODEL = os.getenv("LLM_API_MODEL")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL")

API_URL_STABLE_DIFFUSION = "http://127.0.0.1:7860"
CHECKPOINT = "lametta_v2012.safetensors"

DEFAULT_PAYLOAD_STABLE_DIFFUSION = {
    "override_settings": {
        "sd_model_checkpoint": CHECKPOINT,
        "CLIP_stop_at_last_layers": 2,
    }
}
