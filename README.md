# PublishYourModel - Fine-Tuning POC

This project provides a proof-of-concept (POC) for fine-tuning a Hugging Face Transformer model for sequence classification.

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the POC

1. **Run the fine-tuning script:**

   ```bash
   python fine_tune.py
   ```

   This script will:
   - Download the IMDb dataset.
   - Load a pre-trained DistilBERT model.
   - Fine-tune the model on a small subset of the IMDb dataset.
   - Save the fine-tuned model to the `./fine_tuned_model` directory.
