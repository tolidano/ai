limit and lwm plists
oh-my-zsh / p10k
lm studio
- download mlx models
postgresapp
- add bin to zshrc
brew app list
- rust, unlink py3.14
- pyenv, install pypy 3.11
- pip install pipx
- pipx install open-webui
- open-webui serve (8080)
- remove openai, add lmstudio
- datasets==3.6.0
- set up audio
skald https://blog.yakkomajuri.com/blog/local-rag
qdrant https://qdrant.tech/documentation/guides/installation/#docker
koboldcpp

podman:
tried, but colima good enough

colima:
colima start --network-address --network-mode bridged --cpu 4 --memory 6 --disk 15

headscale:
https://headscale.net/stable/setup/install/container/
could not get it running, kept failing on a socket chmod
tried with pure local binary, but stopped in favor of...

openvpn:
took the free 2-connection setup (can replace with the community kylemanna version)
had to fiddle with colima, but now works

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
- https://www.reddit.com/r/comfyui/comments/17iwi7p/comfyui\_manager\_on\_mac/
https://github.com/AUTOMATIC1111/stable-diffusion-webui
https://medium.com/@tchpnk/z-image-turbo-comfyui-on-apple-silicon-2026-0aa78d05132d
https://www.bentoml.com/blog/a-guide-to-open-source-image-generation-models

doc parsing:
https://docling-project.github.io/docling/getting\_started/installation/#ocr-engines

browser use:
https://docs.browser-use.com/supported-models#ollama

instagram:
https://instaloader.github.io/basic-usage.html

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
