{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0a009e33-a888-4d12-89eb-45145da968ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting openai==0.28\n",
      "  Downloading openai-0.28.0-py3-none-any.whl.metadata (13 kB)\n",
      "Requirement already satisfied: requests>=2.20 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from openai==0.28) (2.32.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from openai==0.28) (4.66.5)\n",
      "Requirement already satisfied: aiohttp in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from openai==0.28) (3.10.5)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (2024.8.30)\n",
      "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (2.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (1.2.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (23.1.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (1.4.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (6.0.4)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (1.11.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\qcc\\anaconda3\\lib\\site-packages (from tqdm->openai==0.28) (0.4.6)\n",
      "Downloading openai-0.28.0-py3-none-any.whl (76 kB)\n",
      "Installing collected packages: openai\n",
      "  Attempting uninstall: openai\n",
      "    Found existing installation: openai 1.98.0\n",
      "    Uninstalling openai-1.98.0:\n",
      "      Successfully uninstalled openai-1.98.0\n",
      "Successfully installed openai-0.28.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install openai==0.28\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dacf651b-905a-484a-bdd7-bef855090289",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading Hugging Face OPT model on CPU. This may take a while...\n",
      "WARNING:tensorflow:From C:\\Users\\Qcc\\anaconda3\\Lib\\site-packages\\tf_keras\\src\\losses.py:2976: The name tf.losses.sparse_softmax_cross_entropy is deprecated. Please use tf.compat.v1.losses.sparse_softmax_cross_entropy instead.\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Device set to use cpu\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generating article from tweets...\n",
      "✅ Article generated and saved to: articles\\article_20250821_043026.txt\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from datetime import datetime\n",
    "from transformers import pipeline\n",
    "\n",
    "# --- Configuration ---\n",
    "TWEETS_FILE = \"tweets_sample.txt\"\n",
    "ARTICLES_DIR = \"articles\"\n",
    "MODEL_NAME = \"facebook/opt-350m\"  # smaller CPU-friendly model\n",
    "\n",
    "os.makedirs(ARTICLES_DIR, exist_ok=True)\n",
    "\n",
    "# --- Load tweets ---\n",
    "with open(TWEETS_FILE, \"r\", encoding=\"utf-8\") as f:\n",
    "    tweet_texts = [line.strip() for line in f if line.strip()]\n",
    "\n",
    "# Combine tweets into a single prompt\n",
    "prompt = \"Write a short sports article based on these tweets:\\n\\n\" + \"\\n\".join(tweet_texts)\n",
    "\n",
    "# --- Load Hugging Face model ---\n",
    "print(\"Loading Hugging Face OPT model on CPU. This may take a while...\")\n",
    "generator = pipeline(\"text-generation\", model=MODEL_NAME, device=-1)  # device=-1 for CPU\n",
    "\n",
    "# --- Generate article ---\n",
    "print(\"Generating article from tweets...\")\n",
    "article = generator(prompt, max_new_tokens=256, do_sample=True)[0]['generated_text']\n",
    "\n",
    "# --- Save article ---\n",
    "timestamp = datetime.now().strftime(\"%Y%m%d_%H%M%S\")\n",
    "article_file = os.path.join(ARTICLES_DIR, f\"article_{timestamp}.txt\")\n",
    "with open(article_file, \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(article)\n",
    "\n",
    "print(f\"✅ Article generated and saved to: {article_file}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "439110d6-5fcb-4e28-9c3d-0a6346da5c35",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa825eb0-3627-4293-9dc5-f322d237d3ce",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
