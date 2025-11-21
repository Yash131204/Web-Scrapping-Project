{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4748089e-0ead-46e1-aa67-be1ed2977b85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in c:\\users\\admin\\anaconda3\\lib\\site-packages (2.32.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests) (2025.1.31)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\users\\admin\\anaconda3\\lib\\site-packages (4.12.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from beautifulsoup4) (2.5)\n",
      "Requirement already satisfied: pandas in c:\\users\\admin\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install requests\n",
    "!pip install beautifulsoup4\n",
    "!pip install pandas\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "67c36f6a-6442-4317-99f2-1e7b9ea4e951",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                               Quote             Author\n",
      "0  “The world as we have created it is a process ...    Albert Einstein\n",
      "1  “It is our choices, Harry, that show what we t...       J.K. Rowling\n",
      "2  “There are only two ways to live your life. On...    Albert Einstein\n",
      "3  “The person, be it gentleman or lady, who has ...        Jane Austen\n",
      "4  “Imperfection is beauty, madness is genius and...     Marilyn Monroe\n",
      "5  “Try not to become a man of success. Rather be...    Albert Einstein\n",
      "6  “It is better to be hated for what you are tha...         André Gide\n",
      "7  “I have not failed. I've just found 10,000 way...   Thomas A. Edison\n",
      "8  “A woman is like a tea bag; you never know how...  Eleanor Roosevelt\n",
      "9  “A day without sunshine is like, you know, nig...       Steve Martin\n"
     ]
    }
   ],
   "source": [
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
