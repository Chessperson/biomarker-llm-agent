# Biomarker LLM Agent

Ollama agent analyzes synthetic omics → trauma predictions (coagulopathy/neuro risk).

## Run Demo
```bash
ollama create biomarker-agent -f Modelfile
python test agent.py
```
Output: `{"risks": ["coagulopathy"], "recommendations": ["plasma"]}`

[Multi-Omics Synth](https://github.com/chessperson/multiomics-synth)
