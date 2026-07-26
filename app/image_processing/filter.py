# --- FIX: Move imports to the top level (Main Thread) ---
import torch
from transformers import CLIPProcessor, CLIPModel

from PIL import Image
import os
from app.core.config import settings



MODEL_NAME = "openai/clip-vit-base-patch32"
model = None
processor = None
device = None 

def _load_model():
    """
    Loads the AI model weights into memory.
    """
    global model, processor, device
    if model is not None:
        return

    print("🤖 Loading CLIP model into memory...")
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        # Optional: Add specific support for Mac Apple Silicon (MPS)
        if torch.backends.mps.is_available():
            device = "mps"

        model = CLIPModel.from_pretrained(MODEL_NAME).to(device)
        processor = CLIPProcessor.from_pretrained(MODEL_NAME)
        print(f"✅ CLIP model loaded successfully on {device}.")
    except Exception as e:
        print(f"❌ FAILED to load CLIP model. Error: {e}")
        model = "failed"
        processor = "failed"


def filter_images(image_paths: list[str], query: str, job_id: int) -> list[str]:
    """
    Uses the CLIP model to filter images based on their relevance to a text query.
    """
    _load_model()
    
    if model == "failed" or not image_paths:
        return image_paths

    print(f"[JOB {job_id}] 🧠 Starting AI filtering for {len(image_paths)} images...")
    
    try:
        BATCH_SIZE = 16
        relevant_paths = []
        for i in range(0, len(image_paths), BATCH_SIZE):
            batch_paths = image_paths[i:i + BATCH_SIZE]
            
            images = [Image.open(path).convert("RGB") for path in batch_paths]
            inputs = processor(text=[query], images=images, return_tensors="pt", padding=True).to(device)

            with torch.no_grad():
                outputs = model(**inputs)
            
            logits_per_image = outputs.logits_per_image
            scores = logits_per_image.squeeze().cpu().numpy()
            
            if scores.ndim == 0:
                scores = [scores.item()]

            for path, score in zip(batch_paths, scores):
                if score >= settings.CLIP_FILTER_THRESHOLD:
                    relevant_paths.append(path)
        
        num_removed = len(image_paths) - len(relevant_paths)
        print(f"[JOB {job_id}] ✨ AI filtering complete. Removed {num_removed} images.")
        
        return relevant_paths

    except Exception as e:
        print(f"[JOB {job_id}] ❌ ERROR during AI filtering: {e}")
        return image_paths