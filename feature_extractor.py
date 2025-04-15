import numpy as np

def extract_features(text_series):
    features = []
    for text in text_series:
        chars = [ord(c) for c in text]
        char_counts = np.bincount(chars, minlength=256)[:256]
        length = len(text)
        unique_chars = len(set(text))
        mean_ascii = np.mean(chars) if chars else 0
        std_ascii = np.std(chars) if chars else 0
        features.append(np.concatenate([char_counts, [length, unique_chars, mean_ascii, std_ascii]]))
    return np.array(features)
