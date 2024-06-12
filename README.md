# ai

playing around with AI

## hardware

macbook pro m2 max 64gb 1tb early 2023 used, ebay, $2400 in early 2024
Run: sudo sysctl iogpu.wired\_limit\_mb=57344

## notes/links

https://medium.com/@tubelwj/introduction-to-ai-model-quantization-formats-dc643bfc335c
https://heidloff.net/article/running-llm-flan-t5-locally/
http://www.answer.ai
https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm
https://venturebeat.com/ai/apple-releases-openelm-small-open-source-ai-models-designed-to-run-on-device/
https://huggingface.co/openbmb/MiniCPM-V-2
https://www.bentoml.com/blog/a-guide-to-open-source-image-generation-models
https://stable-diffusion-art.com/install-mac/

All of Wikipedia
https://dumps.wikimedia.org/commonswiki/20240420/
https://library.kiwix.org/#lang=eng&q=wikipedia

make an Ai Pin clone with no laser:
https://www.amazon.com/dp/B0CGWP616W?tag=woodartsupp00-20&linkCode=ogi&th=1 $64 20g
https://shop.allnetchina.cn/products/copy-of-radxa-zero-3w?variant=48051150750012 $32 20g
https://github.com/PiSugar/PiSugar $40 50g

Screen record like Rewind: https://github.com/yuka-friends/Windrecorder https://github.com/jasonjmcghee/rem
Index Wikipedia https://foojay.io/today/indexing-all-of-wikipedia-on-a-laptop/
Lite LLM https://github.com/BerriAI/litellm
Vision OSS https://huggingface.co/openbmb/MiniCPM-V-2 
Apple CoreNet https://github.com/apple/corenet
vLLM fork seems pretty interesting, may get updates faster than upstream: https://github.com/PygmalionAI/aphrodite-engine
Voice cloning https://github.com/myshell-ai/OpenVoice
RAG https://github.com/truefoundry/cognita
Memary on ReAct https://github.com/kingjulio8238/memary running on https://github.com/ysymyth/ReAct
Interesting https://brainsteam.co.uk/2024/05/01/llms-cant-do-probability/
Interesting https://github.com/abi/secret-llama
There's also Gemini Nano, an on-device model!
also this thing is cool:
    pipx install llm # or brew install llm
    llm install llm-gemini --upgrade
    llm keys set gemini
    # paste API key here
    llm -m gemini-1.5-flash-latest 'a short poem about otters'
Plugins for llm https://llm.datasette.io/en/stable/plugins/directory.html#plugin-directory
Check? https://nian.llmonpy.ai/
Telemetry / Observability for LLMs https://github.com/traceloop/openllmetry
Paligemma Multimodal https://blog.roboflow.com/paligemma-multimodal-vision/
Falcon is back https://ollama.com/library/falcon2
Math for ML https://mathacademy.com/courses/mathematics-for-machine-learning
Llama https://github.com/ggerganov/llama.cpp
Llama2 https://github.com/karpathy/llama2.c?tab=readme-ov-file
Metaskills Exports - https://github.com/metaskills/experts
Unremarkable Experts - https://www.unremarkable.ai/experts/
new Meta model - Chameleon https://arxiv.org/pdf/2405.09818
Llama3 from Scratch - https://github.com/naklecha/llama3-from-scratch
open source testgen https://www.codium.ai/blog/we-created-the-first-open-source-implementation-of-metas-testgen-llm/ 
Verta AI https://www.verta.ai/
Phi 3 Cookbook - https://github.com/microsoft/Phi-3CookBook
Prometheus Evals - https://www.marktechpost.com/2024/05/22/prometheus-eval-and-prometheus-2-setting-new-standards-in-llm-evaluation-and-open-source-innovation-with-state-of-the-art-evaluator-language-model/?amp
Golden Gate Claude https://www.anthropic.com/news/golden-gate-claude
prompt tuning thread on HN https://news.ycombinator.com/item?id=40474716
WizardILM - Apparently the 8b is pretty good, there might be a 13b version too? Also OpenChat 3.6 is out, and apparently beats Llama3-8b, which is pretty impressive.
LLMs in Terminal https://github.com/darrenburns/elia?tab=readme-ov-file
Drawing gadget. https://drawing.pics
Who is the Human https://www.reddit.com/r/Damnthatsinteresting/comments/1d29rxj/ai_npcs_try_to_figure_out_who_among_them_is_the/
Yann LeCun https://medium.com/@stevecohen_29296/yann-lecun-limits-of-llms-agi-the-future-of-ai-8e103a8398ab

### todo/investigate

InvokeAI, Automatic1111, Draw Things, Diffusers, DiffusionBee
Starling, Wizard, StarCoder

## repos

### mixed

https://github.com/open-webui/open-webui
https://github.com/Stability-AI/StableCascade
https://github.com/apple/corenet
https://github.com/PygmalionAI/aphrodite-engine
https://github.com/myshell-ai/OpenVoice
https://github.com/truefoundry/cognita

#### https://github.com/ggerganov/whisper.cpp

* The README has the info for this one. 
* I downloaded the "large-v3" model with the script.
* So now I do ./main -f samples/jfk.wav -m models/ggml-large-v3.bin 
* Or I can do the microphone input thing
* You can do STT with all the major cloud providers, AWS, Azure, GCP as well

### serving

https://github.com/microsoft/semantic-kernel
https://github.com/vllm-project/vllm
https://github.com/BerriAI/litellm
https://github.com/prantlf/ovai

### automation

https://github.com/Skyvern-AI/skyvern
https://github.com/lavague-ai/LaVague

## things to install

https://ollama.com
https://lmstudio.ai
https://pinokio.computer

## running

Ollama

Updating all models:
```bash
for n in `ollama list | rg -v minut | rg -v NAME | cut -f1`; do echo "$n - Starting"; ollama pull $n; echo "$n - Done"; done;
```

## models

### chat

https://ollama.com/library/phi3
https://ollama.com/library/llama3
https://ollama.com/library/openchat
https://ollama.com/library/gemma
https://ollama.com/library/nexusraven
https://ollama.com/library/tinyllama
https://ollama.com/library/starling-lm

### code

https://ollama.com/library/codegemma
https://ollama.com/library/codellama
https://ollama.com/library/phind-codellama

### moe

https://ollama.com/library/wizardlm2
https://ollama.com/library/mixtral

### image

https://ollama.com/library/llava
https://ollama.com/library/bakllava
