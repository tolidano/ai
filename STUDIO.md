limit and lwm plists
stop machine from sleeping
oh-my-zsh / p10k
lm studio
- download mlx models
postgresapp
- add bin to zshrc
brew app list
- rust, unlink py3.14
- pyenv, install pypy 3.11 and python 3.11 and python 3.13
- pip install pipx
- pipx install open-webui
- open-webui serve (8080)
- remove openai, add lmstudio
- datasets==3.6.0
- set up audio, see settings (model downloaded, not optimal, lots of fiddling)
- set up image (ComfyUI first, then connect, copy settings from z-image turbo workflow)
koboldcpp


podman:
tried, but colima good enough

colima:
colima start --network-address --network-mode bridged --cpu 4 --memory 6 --disk 15
need network-address and bridged to allow access on the same 192.168.1.0/24 space

headscale:
https://headscale.net/stable/setup/install/container/
could not get it running, kept failing on a socket chmod
tried with pure local binary, but stopped in favor of...

openvpn:
took the free 2-connection setup (can replace with the community kylemanna version)
had to fiddle with colima (see above), but now works (not openvpn specific problem)
running on phone and laptop

unsorted:
https://github.com/rishikanthc/Scriberr
https://github.com/ufal/SimulStreaming
https://github.com/simular-ai/Agent-S?tab=readme-ov-file
https://github.com/filipstrand/mflux
https://github.com/ILikeAI/AlwaysReddy
https://github.com/Mintplex-Labs/anything-llm?tab=readme-ov-file

models:
https://huggingface.co/mlx-community/models?sort=likes
https://huggingface.co/collections/mlx-community/qwen3-vl
- downloaded the 30b
https://huggingface.co/collections/mlx-community/qwen3-coder-moe
https://huggingface.co/collections/mlx-community/qwen3-next
- downloaded the 80b
https://huggingface.co/collections/mlx-community/gpt-oss
- downloaded 20b and 120b

agents:
https://github.com/mudler/LocalAGI

RAG/memory:
https://github.com/mudler/LocalRecall
skald https://blog.yakkomajuri.com/blog/local-rag
qdrant https://qdrant.tech/documentation/guides/installation/#docker
https://docling-project.github.io/docling/examples/rag\_milvus/#a-recipe

ui:
https://github.com/open-webui/open-webui
https://github.com/mudler/LocalAI

encoders:
https://huggingface.co/cross-encoder
https://huggingface.co/BAAI/bge-m3
https://huggingface.co/sentence-transformers

image gen:
https://github.com/comfyanonymous/ComfyUI
- pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
- validate with import torch;print(torch.backends.mps.is\_available())
- https://www.reddit.com/r/comfyui/comments/17iwi7p/comfyui\_manager\_on\_mac/
https://medium.com/@tchpnk/z-image-turbo-comfyui-on-apple-silicon-2026-0aa78d05132d
https://www.bentoml.com/blog/a-guide-to-open-source-image-generation-models
z-image turbo on comfyUI, dev mode, exported API workflow to open webui uploader, copied node numbers, set steps 20

doc parsing:
https://docling-project.github.io/docling/getting\_started/installation/#ocr-engines
pip install docling and docling[tesserocr] (needs tesseract)
docling-tools models download
pip install "docling-serve[ui]"
https://github.com/docling-project/docling-serve
docling-serve run --enable-ui
TODO: run with image description services: https://github.com/docling-project/docling-serve/blob/main/docs/usage.md

browser use:
https://docs.browser-use.com/supported-models#ollama

instagram:
https://instaloader.github.io/basic-usage.html
pip install instaloader

voice ai:
https://github.com/eustlb/speech-to-speech
https://github.com/KoljaB/LocalAIVoiceChat
https://github.com/KoljaB/RealtimeTTS
https://github.com/OHF-Voice/piper1-gpl
https://modal.com/blog/open-source-stt
https://medium.com/@princekrampah/real-time-llm-voice-chat-in-python-kokoro-moonshine-open-source-models-6c6270cbe967
https://github.com/speaches-ai/speaches
https://github.com/EpicenterHQ/epicenter/tree/main/apps/whispering#install-whispering
https://github.com/ml-explore/mlx-examples/tree/main/whisper
https://github.com/mustafaaljadery/lightning-whisper-mlx
https://huggingface.co/collections/mlx-community/vibevoice
https://huggingface.co/collections/mlx-community/chatterbox-tts
https://huggingface.co/collections/mlx-community/voxcpm
