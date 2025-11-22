
    "!pip install requests\n",
    "!pip install beautifulsoup4\n",
    "!pip install pandas\n",
    "\n"
   
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "url = \"https://quotes.toscrape.com/\"\n",
    "response = requests.get(url)\n",
    "\n",
    "soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "quotes = []\n",
    "authors = []\n",
    "\n",
    "for q in soup.find_all(\"div\", class_=\"quote\"):\n",
    "    text = q.find(\"span\", class_=\"text\").get_text(strip=True)\n",
    "    author = q.find(\"small\", class_=\"author\").get_text(strip=True)\n",
    "    \n",
    "    quotes.append(text)\n",
    "    authors.append(author)\n",
    "\n",
    "df = pd.DataFrame({\"Quote\": quotes, \"Author\": authors})\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30a07178-041b-4c9e-ba5d-a64652928356",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "043e7085-49fe-4c80-8a58-0ecaf944f24d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
