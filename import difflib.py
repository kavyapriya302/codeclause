import difflib

def calculate_similarity(text1, text2):
    """
    Calculate the similarity between two texts using the SequenceMatcher from difflib.
    """
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio()

def check_plagiarism(file1_path, file2_path, threshold=0.8):
    """
    Check plagiarism between two files and print the similarity ratio.
    """
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        text1 = file1.read()
        text2 = file2.read()

    similarity_ratio = calculate_similarity(text1, text2)
    print(f"Similarity Ratio: {similarity_ratio * 100:.2f}%")

    if similarity_ratio > threshold:
        print("Potential plagiarism detected!")
    else:
        print("No significant similarity found.")

# Example usage
file1_path = 'path/to/your/file1.txt'
file2_path = 'path/to/your/file2.txt'
check_plagiarism(file1_path, file2_path)
