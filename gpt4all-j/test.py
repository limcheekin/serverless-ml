from gpt4allj import Model

model = Model('./models/ggml-gpt4all-j', instructions='avx')
print(model.generate('AI is going to'))
