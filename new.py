import tkinter as tk
from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

def summarize():
    url = utext.get('1.0', "end").strip()
    if not url:
        # Handle the case where the URL is empty
        return

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', ', '.join(article.authors) if article.authors else 'N/A')

    publication.delete('1.0', 'end')
    publication.insert('1.0', str(article.publish_date) if article.publish_date else 'N/A')

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary if article.summary else 'N/A')

    blob = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {blob.polarity}, Sentiment: {"positive" if blob.polarity > 0 else "negative" if blob.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    utext.delete('1.0', 'end')  # Clear the URL text widget

    print(blob.polarity)
    print(f'Sentiment: {"positive" if blob.polarity > 0 else "negative" if blob.polarity < 0 else "neutral"}')

root = tk.Tk()
root.title("News Summarizer")

# Color theme
bg_color = "#FFFFFF"  # White
fg_color = "#000000"  # Black
widget_bg_color = "#F0F0F0"  # Light Gray
btn_bg_color = "#4CAF50"  # Green
btn_fg_color = "#FFFFFF"  # White

# Configure grid
for i in range(13):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

# Define font
font_style = ("Helvetica", 12)

root.configure(bg=bg_color)  # Set window background color

tlabel = tk.Label(root, text="Title", font=font_style, bg=bg_color, fg=fg_color)
tlabel.grid(row=0, column=0, sticky="w")

title = tk.Text(root, height=1, width=140, font=font_style, bg=widget_bg_color)
title.config(state='disabled')
title.grid(row=1, column=0, sticky="ew", padx=5)

alabel = tk.Label(root, text="Authors", font=font_style, bg=bg_color, fg=fg_color)
alabel.grid(row=2, column=0, sticky="w")

author = tk.Text(root, height=1, width=140, font=font_style, bg=widget_bg_color)
author.config(state='disabled')
author.grid(row=3, column=0, sticky="ew", padx=5)

plabel = tk.Label(root, text="Publication Date", font=font_style, bg=bg_color, fg=fg_color)
plabel.grid(row=4, column=0, sticky="w")

publication = tk.Text(root, height=1, width=140, font=font_style, bg=widget_bg_color)
publication.config(state='disabled')
publication.grid(row=5, column=0, sticky="ew", padx=5)

slabel = tk.Label(root, text="Summary", font=font_style, bg=bg_color, fg=fg_color)
slabel.grid(row=6, column=0, sticky="w")

summary = tk.Text(root, height=10, width=140, font=font_style, bg=widget_bg_color)
summary.config(state='disabled')
summary.grid(row=7, column=0, sticky="ew", padx=5)

selabel = tk.Label(root, text="Sentiment Analysis", font=font_style, bg=bg_color, fg=fg_color)
selabel.grid(row=8, column=0, sticky="w")

sentiment = tk.Text(root, height=1, width=140, font=font_style, bg=widget_bg_color)
sentiment.config(state='disabled')
sentiment.grid(row=9, column=0, sticky="ew", padx=5)

ulabel = tk.Label(root, text="URL", font=font_style, bg=bg_color, fg=fg_color)
ulabel.grid(row=10, column=0, sticky="w")

utext = tk.Text(root, height=1, width=140, font=font_style, bg=widget_bg_color)
utext.grid(row=11, column=0, sticky="ew", padx=5)

btn = tk.Button(root, text='Summarize', command=summarize, font=font_style, bg=btn_bg_color, fg=btn_fg_color)
btn.grid(row=12, column=0, pady=10)

root.mainloop()
