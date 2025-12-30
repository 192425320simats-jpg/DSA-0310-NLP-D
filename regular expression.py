import re

text = "The quick brown fox jumps over the lazy dog. The fox was quick."

pattern_fox = r"fox"
matches_fox = re.findall(pattern_fox, text)
print(f"Matches for 'fox': {matches_fox}")

pattern_quick = r"quick"
match_quick = re.search(pattern_quick, text)
if match_quick:
    print(f"Found 'quick' at position: {match_quick.start()} - {match_quick.group()}")
else:
    print("'quick' not found.")

pattern_t_words = r"\b[tT]\w+"
matches_t_words = re.findall(pattern_t_words, text)
print(f"Words starting with 't' or 'T': {matches_t_words}")

pattern_lazy = r"lazy"
replaced_text = re.sub(pattern_lazy, "active", text)
print(f"Text after replacement: {replaced_text}")

pattern_start = r"^The"
match_start = re.match(pattern_start, text)
if match_start:
    print("The text starts with 'The'.")
else:
    print("The text does not start with 'The'.")
