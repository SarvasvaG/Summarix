from transformers import pipeline, set_seed
model_ckpt = "google/flan-t5-base"
pipe = pipeline('summarization', model=model_ckpt)