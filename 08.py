# import tkinter as tk
# from tkinter import filedialog
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from nltk.tokenize import sent_tokenize, word_tokenize
# import nltk
# import os
# from gensim.models import KeyedVectors

# nltk.download('punkt')  # Cần thiết cho việc tách câu và từ
# current_directory = os.getcwd()
# bin_path = os.path.join(current_directory, "GoogleNews-vectors-negative300.bin")
# word_vectors = KeyedVectors.load_word2vec_format(bin_path, binary=True)

# def process_text(text):
#     sentences = sent_tokenize(text)
#     return sentences

# def find_matching_sentences(input_text, comparison_text):
#     input_sentences = process_text(input_text)
#     comparison_sentences = process_text(comparison_text)
#     matching_sentences = []

#     for input_sentence in input_sentences:
#         if input_sentence.strip().lower() in (sentence.strip().lower() for sentence in comparison_sentences):
#             matching_sentences.append(input_sentence)

#     return matching_sentences

# def find_matching_words(input_text, comparison_text):
#     input_words = set(word_tokenize(input_text.lower()))
#     comparison_words = set(word_tokenize(comparison_text.lower()))
#     matching_words = list(input_words.intersection(comparison_words))
#     return matching_words

# def calculate_similarity(input_text, comparison_text):
#     input_words = word_tokenize(input_text.lower())
#     comparison_words = word_tokenize(comparison_text.lower())

#     input_vector = []
#     comparison_vector = []

#     for word in input_words:
#         if word in word_vectors:
#             input_vector.append(word_vectors[word])

#     for word in comparison_words:
#         if word in word_vectors:
#             comparison_vector.append(word_vectors[word])

#     if len(input_vector) > 0 and len(comparison_vector) > 0:
#         similarity = word_vectors.n_similarity(input_vector, comparison_vector)
#         return similarity
#     else:
#         return 0.0  # Return 0 if no words found in the Word2Vec model

# def load_text(file_text_area):
#     file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#     if file_path:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
#             file_text_area.delete('1.0', tk.END)
#             file_text_area.insert(tk.END, content)

# def compare_texts():
#     text1 = compare_texts_ui.text1_text_area.get("1.0", tk.END)
#     text2 = compare_texts_ui.text2_text_area.get("1.0", tk.END)

#     similarity_percentage = calculate_similarity(text1, text2) * 100

#     matching_sentences = find_matching_sentences(text1, text2)
#     matching_words = find_matching_words(text1, text2)
    
#     compare_texts_ui.similarity_label.config(text=f"Similarity: {similarity_percentage:.2f}%")
    
#     input_sentences = process_text(text1)
#     total_sentences = len(input_sentences)
    
#     # Thay đổi hiển thị thành số lượng câu tương đồng thay vì phần trăm tương đồng
#     num_matching_sentences = len(matching_sentences)
    
#     if matching_sentences:
#         matching_sentences_text = "Matching sentences:\n" + '\n'.join(matching_sentences)
#         matching_sentences_text = matching_sentences_text.replace(".", "")
#         compare_texts_ui.matching_sentences_label.config(text=matching_sentences_text)
#         compare_texts_ui.similarity_label.config(text=f"Similarity: {similarity_percentage:.2f}%, Matching Sentences: {num_matching_sentences}")
#     else:
#         compare_texts_ui.matching_sentences_label.config(text="No matching sentences found")
    
#     if matching_words:
#         matching_words_text = "Matching words:\n" + ', '.join(matching_words)
#         matching_words_text = matching_words_text.replace(".", "")
#         compare_texts_ui.matching_words_label.config(text=matching_words_text)
#     else:
#         compare_texts_ui.matching_words_label.config(text="No matching words found")

# def compare_texts_ui():
#     root = tk.Tk()
#     root.title("Text Similarity Comparison")

#     text1_frame = tk.Frame(root)
#     text1_frame.pack(padx=10, pady=10)

#     text1_label = tk.Label(text1_frame, text="Text 1:")
#     text1_label.pack()

#     compare_texts_ui.text1_text_area = tk.Text(text1_frame, wrap=tk.WORD, width=40, height=10)
#     compare_texts_ui.text1_text_area.pack()

#     text2_frame = tk.Frame(root)
#     text2_frame.pack(padx=10, pady=10)

#     text2_label = tk.Label(text2_frame, text="Text 2:")
#     text2_label.pack()

#     compare_texts_ui.text2_text_area = tk.Text(text2_frame, wrap=tk.WORD, width=40, height=10)
#     compare_texts_ui.text2_text_area.pack()

#     load_text1_button = tk.Button(root, text="Load Text 1", command=lambda: load_text(compare_texts_ui.text1_text_area))
#     load_text1_button.pack(padx=10, pady=5)

#     load_text2_button = tk.Button(root, text="Load Text 2", command=lambda: load_text(compare_texts_ui.text2_text_area))
#     load_text2_button.pack(padx=10, pady=5)

#     check_button = tk.Button(root, text="Check Similarity", command=compare_texts)
#     check_button.pack(padx=10, pady=10)

#     compare_texts_ui.similarity_label = tk.Label(root, text="Similarity: ")
#     compare_texts_ui.similarity_label.pack(padx=10, pady=5)

#     compare_texts_ui.matching_sentences_label = tk.Label(root, text="Matching sentences:\n", justify=tk.LEFT, wraplength=300)
#     compare_texts_ui.matching_sentences_label.pack(padx=10, pady=5)
    
#     compare_texts_ui.matching_words_label = tk.Label(root, text="Matching words:\n", justify=tk.LEFT, wraplength=300)
#     compare_texts_ui.matching_words_label.pack(padx=10, pady=5)

#     root.mainloop()

# # Gọi hàm để chạy giao diện
# compare_texts_ui()


import tkinter as tk
from tkinter import filedialog
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os
from gensim.models import KeyedVectors

nltk.download('punkt')  # Cần thiết cho việc tách câu và từ
current_directory = os.getcwd()
bin_path = os.path.join(current_directory, "GoogleNews-vectors-negative300.bin")
word_vectors = KeyedVectors.load_word2vec_format(bin_path, binary=True)

def process_text(text):
    sentences = sent_tokenize(text)
    return sentences

def find_matching_sentences(input_text, comparison_text):
    input_sentences = process_text(input_text)
    comparison_sentences = process_text(comparison_text)
    matching_sentences = []

    for input_sentence in input_sentences:
        if input_sentence.strip().lower() in (sentence.strip().lower() for sentence in comparison_sentences):
            matching_sentences.append(input_sentence)

    return matching_sentences

def find_matching_words(input_text, comparison_text):
    input_words = set(word_tokenize(input_text.lower()))
    comparison_words = set(word_tokenize(comparison_text.lower()))
    matching_words = list(input_words.intersection(comparison_words))
    return matching_words

def calculate_similarity(input_text, comparison_text):
    input_words = word_tokenize(input_text.lower())
    comparison_words = word_tokenize(comparison_text.lower())

    input_vector = []
    comparison_vector = []

    for word in input_words:
        if word in word_vectors:
            input_vector.append(word_vectors[word])

    for word in comparison_words:
        if word in word_vectors:
            comparison_vector.append(word_vectors[word])

    if len(input_vector) > 0 and len(comparison_vector) > 0:
        similarity = word_vectors.n_similarity(input_vector, comparison_vector)
        return similarity
    else:
        return 0.0  # Return 0 if no words found in the Word2Vec model

def color_matching_sentences(text_widget, matching_sentences, similarity_threshold=0.8):
    text = text_widget.get("1.0", tk.END)
    for sentence in matching_sentences:
        similarity = calculate_similarity(text, sentence)
        if similarity >= similarity_threshold:
            start_index = text.find(sentence)
            end_index = start_index + len(sentence)
            text_widget.tag_add("match", f"1.{start_index}", f"1.{end_index}")
            text_widget.tag_config("match", background="yellow")  # Màu nền là vàng cho độ tương đồng >80%

def load_text(file_text_area):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            file_text_area.delete('1.0', tk.END)
            file_text_area.insert(tk.END, content)

def compare_texts():
    text1_widget = compare_texts_ui.text1_text_area
    text2_widget = compare_texts_ui.text2_text_area

    text1 = text1_widget.get("1.0", tk.END)
    text2 = text2_widget.get("1.0", tk.END)

    similarity_percentage = calculate_similarity(text1, text2)

    matching_sentences = find_matching_sentences(text1, text2)
    matching_words = find_matching_words(text1, text2)
    
    compare_texts_ui.similarity_label.config(text=f"Similarity: {similarity_percentage:.2f}")
    
    input_sentences = process_text(text1)
    total_sentences = len(input_sentences)
    
    num_matching_sentences = len(matching_sentences)
    
    if matching_sentences:
        matching_sentences_text = "Matching sentences:\n" + '\n'.join(matching_sentences)
        matching_sentences_text = matching_sentences_text.replace(".", "")
        compare_texts_ui.matching_sentences_label.config(text=matching_sentences_text)
        color_matching_sentences(text1_widget, matching_sentences)  # Tô màu các câu giống nhau
        compare_texts_ui.similarity_label.config(text=f"Similarity: {similarity_percentage:.2f}, Matching Sentences: {num_matching_sentences}")
    else:
        compare_texts_ui.matching_sentences_label.config(text="No matching sentences found")
    
    if matching_words:
        matching_words_text = "Matching words:\n" + ', '.join(matching_words)
        matching_words_text = matching_words_text.replace(".", "")
        compare_texts_ui.matching_words_label.config(text=matching_words_text)
    else:
        compare_texts_ui.matching_words_label.config(text="No matching words found")

def compare_texts_ui():
    root = tk.Tk()
    root.title("Text Similarity Comparison")

    text1_frame = tk.Frame(root)
    text1_frame.pack(padx=10, pady=10)

    text1_label = tk.Label(text1_frame, text="Text 1:")
    text1_label.pack()

    compare_texts_ui.text1_text_area = tk.Text(text1_frame, wrap=tk.WORD, width=40, height=10)
    compare_texts_ui.text1_text_area.pack()

    text2_frame = tk.Frame(root)
    text2_frame.pack(padx=10, pady=10)

    text2_label = tk.Label(text2_frame, text="Text 2:")
    text2_label.pack()

    compare_texts_ui.text2_text_area = tk.Text(text2_frame, wrap=tk.WORD, width=40, height=10)
    compare_texts_ui.text2_text_area.pack()

    load_text1_button = tk.Button(root, text="Load Text 1", command=lambda: load_text(compare_texts_ui.text1_text_area))
    load_text1_button.pack(padx=10, pady=5)

    load_text2_button = tk.Button(root, text="Load Text 2", command=lambda: load_text(compare_texts_ui.text2_text_area))
    load_text2_button.pack(padx=10, pady=5)

    check_button = tk.Button(root, text="Check Similarity", command=compare_texts)
    check_button.pack(padx=10, pady=10)

    compare_texts_ui.similarity_label = tk.Label(root, text="Similarity: ")
    compare_texts_ui.similarity_label.pack(padx=10, pady=5)

    compare_texts_ui.matching_sentences_label = tk.Label(root, text="Matching sentences:\n", justify=tk.LEFT, wraplength=300)
    compare_texts_ui.matching_sentences_label.pack(padx=10, pady=5)
    
    compare_texts_ui.matching_words_label = tk.Label(root, text="Matching words:\n", justify=tk.LEFT, wraplength=300)
    compare_texts_ui.matching_words_label.pack(padx=10, pady=5)

    root.mainloop()

# Gọi hàm để chạy giao diện
compare_texts_ui()
