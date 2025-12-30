import random
from collections import defaultdict

def build_bigram_model(text):
    words = text.lower().split()
    bigram_model = defaultdict(list)

    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        bigram_model[current_word].append(next_word)

    return bigram_model

def generate_text(bigram_model, start_word, length=10):
    current_word = start_word.lower()
    generated_words = [current_word]

    for _ in range(length - 1):
        next_words = bigram_model.get(current_word)
        if not next_words:
            break
        next_word = random.choice(next_words)
        generated_words.append(next_word)
        current_word = next_word

    return " ".join(generated_words)

def main():
   
    text = input("Enter a training text: ")

   
    bigram_model = build_bigram_model(text)

    
    start_word = input("Enter a start word: ")

   
    generated_text = generate_text(bigram_model, start_word, length=10)

    print("\nGenerated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
