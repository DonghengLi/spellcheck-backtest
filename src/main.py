import csv
import json
import os
import sys
import itertools

def process_csv(input_file_path: str, output_file_path: str, word_excluded: set[str]):
    with open(input_file_path, mode='r', encoding='utf-8-sig') as infile, \
         open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:

        outfile.write('\ufeff') # Adding BOM to the beginning of the file to support Excel

        reader = csv.DictReader(infile)
        fieldnames = ['Encounter ID', '#Words Highlighted', '#Words Corrected', '% Words Corrected', 'Highlighted Words', 'Corrected Words']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            highlighted_words = json.loads(row['highlightedWords'])
            corrected_words = json.loads(row['correctedWords'])

            # Post-process
            highlighted_words = [word for word in itertools.chain(highlighted_words, corrected_words) if word not in word_excluded]
            corrected_words = [word for word in corrected_words if word not in word_excluded]
            
            # Calculating the metrics
            num_highlighted = len(highlighted_words)
            num_corrected = len(corrected_words)
            percent_corrected = (num_corrected / num_highlighted * 100) if num_highlighted else 0

            # Concatenating the words
            highlighted_words_str = ', '.join(highlighted_words)
            corrected_words_str = ', '.join(corrected_words)
            
            writer.writerow({
                'Encounter ID': row['encounterId'],
                '#Words Highlighted': num_highlighted,
                '#Words Corrected': num_corrected,
                '% Words Corrected': f"{percent_corrected:.2f}",
                'Highlighted Words': highlighted_words_str,
                'Corrected Words': corrected_words_str,
            })

def load_medical_abbreviations(target: set[str]):
    for root, dirs, files in os.walk('./dictionary_data/medical_abbreviations/CSVs'):
        for file in files:
            if not file.endswith(".csv"):
                continue

            with open(os.path.join(root, file), mode='r', encoding='utf-8-sig') as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    target.add(row['Abbreviation/Shorthand'])

def load_wordlist_medicalterms_en(target: set[str]):
    with open('./dictionary_data/wordlist-medicalterms-en/wordlist.txt', mode='r', encoding='utf-8-sig') as infile:
        for line in infile:
            line = line.strip()
            if line:
                target.add(line.strip())

def load_dsat_case(target: set[str]):
    with open('./dictionary_data/dsat_case.txt', mode='r', encoding='utf-8-sig') as infile:
        for line in infile:
            line = line.strip()
            if line:
                target.add(line.strip())

DICTIONARY = {
    'medical_abbreviations': load_medical_abbreviations,
    'wordlist_medicalterms_en': load_wordlist_medicalterms_en,
    'dsat_case': load_dsat_case,
}
if __name__ == "__main__":
    if len(sys.argv) not in [3, 4]:
        print("Usage: script.py <input_file_path> <output_file_path> [dictionary_names]")
    else:
        word_excluded = set()

        if len(sys.argv) == 4:
            for dictionary_name in sys.argv[3].split('+'):
                if dictionary_name not in DICTIONARY:
                    print(f"Unknown dictionary name: {dictionary_name}")
                    sys.exit(1)

                DICTIONARY[dictionary_name](word_excluded)
                print('Loaded', dictionary_name)

        process_csv(sys.argv[1], sys.argv[2], word_excluded)
