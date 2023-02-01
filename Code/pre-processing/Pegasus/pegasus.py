import torch
import pandas as pd
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from tqdm import tqdm
from scipy.special import softmax
from scipy.stats import entropy
from nltk.tokenize import word_tokenize
import sys,math

def main():

    model_name = 'tuner007/pegasus_paraphrase'
    torch_device = 'cpu' #'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(
            model_name).to(torch_device)

    def get_response(input_text, num_return_sequences=None, num_beams=None, temperature=None):
        
        input_ids = tokenizer([input_text], 
                            truncation=True, padding='longest',
                            max_length=100, return_tensors="pt")
       
        generated_outputs = model.generate(**input_ids, max_length=100,  do_sample=False,
                num_beams=1,  return_dict_in_generate=True, output_scores=True)
        
       
        gen_tokens_seq = [tokenizer.decode(g, skip_special_tokens = True) for g in generated_outputs.sequences]
        num_generated_tokens = len(generated_outputs['scores'])
        gen_ids = []
        probs = []
        
        for i1 in range(0, num_generated_tokens, 1):
            temptensor = generated_outputs['scores'][i1][0]
            gen_id = torch.argmax(temptensor).item()
            log_prob = generated_outputs['scores'][i1][0][gen_id].item()
            probs.append(log_prob)
            gen_ids.append(gen_id)
        
        gen_probs = torch.tensor(probs)
        gen_probs = gen_probs.view(1,-1)
        
        unique_prob_per_sequence = torch.softmax(gen_probs, dim=-1)#oftmax(gen_probs)#.sum(-1)/num_generated_tokens #diving over the length to normalize
        entropy_prediction = entropy(unique_prob_per_sequence[0].tolist(), 2)
        
        gen_ids = torch.tensor(gen_ids)
        gen_ids = gen_ids.view(1, -1)
        gen_ids_seq = [tokenizer.decode(g, skip_special_tokens = True) for g in gen_ids]
        print("\nPerturbed: {}\nNormalized Prob: {}\nEntropy: {} \n\n".format(' '.join(gen_ids_seq),unique_prob_per_sequence, entropy_prediction)) 

        return (' '.join(gen_ids_seq), entropy_prediction)
        
    df = pd.read_csv('analyze-full-context.csv',index_col='Unnamed: 0')

    perturbedSentences = []
    confidenceValues = []
    originalSentences = list(df['javaDocFirstSentence'])
    
    to_remove = []
    for (idx, row) in tqdm(df.iterrows()):
        sentence = row['javaDocFirstSentence'] 
        perturbed,confidence = get_response(sentence)
        perturbedSentences.append(perturbed)
        confidenceValues.append(confidence)

    df['pegasusPerturbed'] = perturbedSentences
    df['pegagusPerturbedEntropy'] = confidenceValues
    df.to_csv('pegasus-result.csv')


if __name__ == '__main__':
    main()
