import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

nltk.download('punkt')  # Cần thiết cho việc tách câu và từ

def tru(a,b):
    return a-b
def process_text(text):
    sentences = sent_tokenize(text)
    return sentences

def find_matching_sentences(input_text, comparison_text):
    input_sentences = process_text(input_text)
    comparison_sentences = process_text(comparison_text)
    matching_sentences = []

    for input_sentence in input_sentences:
        # Kiểm tra xem có câu nào trong input_text giống với câu nào trong comparison_text không
        if input_sentence.strip().lower() in (sentence.strip().lower() for sentence in comparison_sentences):
            matching_sentences.append(input_sentence)

    return matching_sentences

def find_matching_words(input_text, comparison_text):
    input_words = set(word_tokenize(input_text.lower()))
    comparison_words = set(word_tokenize(comparison_text.lower()))
    matching_words = list(input_words.intersection(comparison_words))
    return matching_words

def calculate_similarity(input_text, comparison_text):
    corpus = [input_text, comparison_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf_matrix)
    return similarities[0][1]

def compare_texts():
    input_text = compare_texts_ui.input_text_area.get("1.0", tk.END)
    comparison_text = compare_texts_ui.comparison_text_area.get("1.0", tk.END)

    similarity_percentage = calculate_similarity(input_text, comparison_text) * 100

    matching_sentences = find_matching_sentences(input_text, comparison_text)
    matching_words = find_matching_words(input_text, comparison_text)
    
    compare_texts_ui.similarity_label.config(text=f"Similarity: {similarity_percentage:.2f}%")
    
    # Tính phần trăm câu tương đồng
    input_sentences = process_text(input_text)
    total_sentences = len(input_sentences)
    percentage_matching_sentences = (len(matching_sentences) / total_sentences) * 100
    
    # Hiển thị các câu giống nhau nếu có
    if matching_sentences:
        matching_sentences_text = "Matching sentences:\n" + '\n'.join(matching_sentences)
        matching_sentences_text = matching_sentences_text.replace(".", "")
        compare_texts_ui.matching_sentences_label.config(text=matching_sentences_text)
        compare_texts_ui.similarity_label.config(text=f"Similarity: {similarity_percentage:.2f}%, Similarity with Corpus: {percentage_matching_sentences:.2f}%")
    else:
        compare_texts_ui.matching_sentences_label.config(text="No matching sentences found")
    
    # Hiển thị các từ giống nhau nếu có
    if matching_words:
        matching_words_text = "Matching words:\n" + ', '.join(matching_words)  # Loại bỏ khoảng trắng
        matching_words_text = matching_words_text.replace(".", "")
        compare_texts_ui.matching_words_label.config(text=matching_words_text)
    else:
        compare_texts_ui.matching_words_label.config(text="No matching words found")

def compare_texts_ui():
    root = tk.Tk()
    root.title("!!!Text Similarity TADoubleH!!!")

    # Text entry areas
    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=10)

    input_label = tk.Label(input_frame, text="Input Text:")
    input_label.pack()

    compare_texts_ui.input_text_area = tk.Text(input_frame, wrap=tk.WORD, width=40, height=10)
    compare_texts_ui.input_text_area.pack()

    comparison_frame = tk.Frame(root)
    comparison_frame.pack(padx=10, pady=10)

    comparison_label = tk.Label(comparison_frame, text="Corpus:")
    comparison_label.pack()

    compare_texts_ui.comparison_text_area = tk.Text(comparison_frame, wrap=tk.WORD, width=40, height=10)
    compare_texts_ui.comparison_text_area.pack()

    # Check button
    check_button = tk.Button(root, text="Check Similarity", command=compare_texts)
    check_button.pack(padx=10, pady=10)

    # Labels for displaying information
    compare_texts_ui.similarity_label = tk.Label(root, text="Similarity: ")
    compare_texts_ui.similarity_label.pack(padx=10, pady=5)

    compare_texts_ui.matching_sentences_label = tk.Label(root, text="Matching sentences:\n", justify=tk.LEFT, wraplength=300)
    compare_texts_ui.matching_sentences_label.pack(padx=10, pady=5)
    
    compare_texts_ui.matching_words_label = tk.Label(root, text="Matching words:\n", justify=tk.LEFT, wraplength=300)
    compare_texts_ui.matching_words_label.pack(padx=10, pady=5)

    root.mainloop()

# Gọi hàm để chạy giao diện
compare_texts_ui()