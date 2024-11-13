# Braille Vision Chatbot

This repository contains code for a chatbot designed to assist users with Braille Vision-related queries. Using a fine-tuned language model, the chatbot answers frequently asked questions (FAQ) on Braille Vision setup, usage, troubleshooting, and maintenance. This README file explains the setup, data preparation, model configuration, training, and deployment instructions.

---

## Table of Contents

1. [Data Preparation and Preprocessing](#data-preparation-and-preprocessing)
2. [Model Configuration](#model-configuration)
3. [Training](#training)
4. [Deployment](#deployment)
5. [Usage](#usage)

---

## Data Preparation and Preprocessing

1. **Data Collection**: The dataset comprises frequently asked questions about Braille Vision, each with a corresponding answer. This data is saved in CSV format (`cleaned_faq_questions_answers.csv`).
2. **Preprocessing**: 
   - The data is formatted into a prompt-response format compatible with language model fine-tuning. 
   - Text cleaning steps include tokenization, removing irrelevant characters, and formatting each question-answer pair into a structure the model can interpret.
3. **Dataset Formatting**: The formatted dataset is saved as `formatted_dataset.txt`, ready for model training.

---

## Model Configuration

The model configuration involves using a pre-trained **Llama-2** model, optimized for text generation tasks. Key configurations include:
- **LoRA (Low-Rank Adaptation)**: To reduce memory requirements, we use LoRA adapters, allowing for efficient task-specific training.
- **4-Bit Quantization**: With `bitsandbytes`, the model is loaded in 4-bit precision, further reducing computational cost while maintaining performance.

Dependencies:
```bash
pip install accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7
```

## Training

The training process is managed by `SFTTrainer` (Supervised Fine-Tuning Trainer) and is configured with custom parameters to optimize model performance and resource efficiency.

### Training Configuration
- **Batch Size**: 4 (per device)
- **Learning Rate**: 2e-4 with a cosine learning rate scheduler
- **Number of Epochs**: 10
- **Gradient Accumulation**: Steps set to 1 to optimize training efficiency

### Running the Training Process

To start the training, use the following code:

```python
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    tokenizer=tokenizer,
    args=training_arguments,
)
trainer.train()
```

### Training Progress Tracking

Training progress is tracked with **TensorBoard**, allowing for real-time visualization of key metrics such as **loss**, **learning rate**, and other performance indicators. This facilitates effective monitoring and adjustment of the training process as needed.

---

## Deployment

After fine-tuning, the model can be deployed for inference using a **text-generation pipeline**. To prepare the model for deployment, save both the model and tokenizer:

```python
model.save_pretrained('Llama-2-7b-chat-finetune')
tokenizer.save_pretrained('Llama-2-7b-chat-finetune')
```
