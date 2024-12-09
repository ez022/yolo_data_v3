import os
from collections import Counter

def count_label_combinations_and_individual_labels(directory):
    # Dictionary to store counts of label combinations
    combination_counts = Counter()
    # Dictionary to count occurrences of individual labels
    individual_label_counts = Counter()
    total_files = 0  # To track the total number of files processed
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            total_files += 1
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                # Extract labels from the file
                labels = set()
                for line in file:
                    try:
                        label = int(line.split()[0])  # Extract the label (first column)
                        labels.add(label)
                    except (IndexError, ValueError):
                        # Handle any unexpected line formats
                        continue
            
            # Count individual labels
            for label in labels:
                individual_label_counts[label] += 1
            
            # Convert the set of labels to a sorted tuple (to ensure consistent combinations)
            label_combination = tuple(sorted(labels))
            combination_counts[label_combination] += 1
    
    # Print combination counts
    print("Label Combinations Count:")
    for combination, count in combination_counts.items():
        print(f"{combination}: {count}")
    
    # Print individual label counts
    print("\nIndividual Label Count:")
    for label, count in individual_label_counts.items():
        print(f"Contains {label}: {count}")
    
    # Verify total count
    total_count = sum(combination_counts.values())
    print("\nVerification:")
    print(f"Total combinations counted: {total_count}")
    print(f"Total files processed: {total_files}")
    if total_count == total_files:
        print("Verification successful: Total counts match the total number of files.")
    else:
        print("Verification failed: Counts do not match the total number of files.")

# Example usage
directory = "./labels"
count_label_combinations_and_individual_labels(directory)
