import pandas as pd
import re
import warnings
warnings.filterwarnings("ignore")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

benchmark_llama = [
    "responses/benchmarks/llama 3.1 responses/LLAMA-3.1-CoT-RESPONSES-ARC.csv",
    "responses/benchmarks/llama 3.1 responses/LLAMA-3.1-CoT-RESPONSES-TRUTHFUL.csv",
    "responses/benchmarks/llama 3.1 responses/LLAMA-3.1-CoT-RESPONSES-WINO.csv",
    "responses/benchmarks/llama 3.1 responses/LLAMA-3.1-NON-CoT-RESPONSES-ARC.csv",
    "responses/benchmarks/llama 3.1 responses/LLAMA-3.1-NON-CoT-RESPONSES-TRUTHFUL.csv",
    "responses/benchmarks/llama 3.1 responses/LLAMA-3.1-NON-CoT-RESPONSES-WINO.csv"
]

benchmark_phi = [
    "responses/benchmarks/phi3/PHI3-CoT-RESPONSES-ARC.csv",
    "responses/benchmarks/phi3/PHI3-CoT-RESPONSES-TRUTHFUL.csv",
    "responses/benchmarks/phi3/PHI3-CoT-RESPONSES-WINO.csv",
    "responses/benchmarks/phi3/PHI3-NON-CoT-RESPONSES-ARC.csv",
    "responses/benchmarks/phi3/PHI3-NON-CoT-RESPONSES-TRUTHFUL.csv",
    "responses/benchmarks/phi3/PHI3-NON-CoT-RESPONSES-WINO.csv"
]

tampered_llama = [
    "responses/tampered/llama 3.1 responses/LLAMA-3.1-TAMPERED-CoT-RESPONSES-ARC.csv",
    "responses/tampered/llama 3.1 responses/LLAMA-3.1-TAMPERED-CoT-RESPONSES-TRUTHFUL.csv",
    "responses/tampered/llama 3.1 responses/LLAMA-3.1-TAMPERED-CoT-RESPONSES-WINO.csv"
]

tampered_phi = ["responses/tampered/phi responses/PHI-TAMPERED-CoT-RESPONSES-ARC.csv",
    "responses/tampered/phi responses/PHI-TAMPERED-CoT-RESPONSES-TRUTHFUL.csv",
    "responses/tampered/phi responses/PHI-TAMPERED-CoT-RESPONSES-WINO.csv"
]

file_path = r"responses\benchmarks\llama 3.1 responses\LLAMA-3.1-NON-CoT-RESPONSES-ARC.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

llama_arc = 0 

def process_accuracy(df):
    accuracy = 0
    for index, row in df.iterrows():
        llm_answ = row[2].replace(".", "").replace("\n", "").replace("<output>", "")
        ground_truth = eval(row[3])

        if alphabet.index(llm_answ[0].capitalize()) == ground_truth.index(1):
            accuracy = accuracy + 1
    return accuracy

def process_accuracy_for_tampered(df):
    accuracy = 0
    for index, row in df.iterrows():
        llm_answ = row[0].replace(".", "").replace(" ", "").replace("\n", "").replace("<output>", "")
        ground_truth = eval(row[6])

        if alphabet.index(llm_answ[0].capitalize()) == ground_truth.index(1):
            accuracy = accuracy + 1
    return accuracy

def asr(df):
    asr = 0
    for index, row in df.iterrows():
        llm_answ = row[0].replace(".", "").replace(" ", "").replace("\n", "").replace("</output>", "")
        #tampered_
        if row[1] in llm_answ:
            asr = asr + 1
    return asr


all_files = benchmark_llama + benchmark_phi + tampered_llama + tampered_phi

accuracies = {}


print("ACCURACIES: ")

for file in all_files:

    df = pd.read_csv(file)
    
    if "tampered" in file:

        accuracy = process_accuracy_for_tampered(df)
    else:

        accuracy = process_accuracy(df)

    accuracies[file] = accuracy

    print(f"Accuracy for {file}: {accuracy}" + "%")

asrs = {}

print("ASRs: ")

for file in tampered_llama + tampered_phi:

    df = pd.read_csv(file)
    
    asr0 = asr(df)

    asrs[file] = asr0

    print(f"Attack Success Rate (ASR) for {file}: {asr0}" + "%")
 

 

