from transformers import pipeline

# Load the BERT-Emotions-Classifier
classifier = pipeline("text-classification", model="ayoubkirouane/BERT-Emotions-Classifier")

# Input text
text = "I have a headache and I feel very tired. I don't know what to do... I should contunue working and its being actually really grate the results, but its late..."

# Perform emotion classification
results = classifier(text)

# Display the classification results
print(results)