from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

device = "cpu"

tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")

model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base").to(device)

@app.route('/paraphrase', methods=['POST'])

def paraphrase():
    num_beams=5
    num_beam_groups=5
    num_return_sequences=5
    repetition_penalty=10.0
    diversity_penalty=3.0
    no_repeat_ngram_size=2
    temperature=0.7
    max_length=500

    content = request.json
    prompt = content['prompt']

    input_ids = tokenizer(
        f'paraphrase: {prompt}',
        return_tensors="pt", padding="longest",
        max_length=max_length,
        truncation=True,
    ).input_ids
    
    outputs = model.generate(
        input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
        num_beams=num_beams, num_beam_groups=num_beam_groups,
        max_length=max_length, diversity_penalty=diversity_penalty
    )

    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    print(res[0])
    #output = model.generate(input_ids)
    #decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify(
        { 'result': 
            [
                res[0],
                res[1],
                res[2],
                res[3]
            ]
        }
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)



    '''

    '''