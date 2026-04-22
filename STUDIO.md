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
- set up audio, see settings (model downloaded, not optimal, lots of fiddling)
- set up image (ComfyUI first, then connect, copy settings from z-image turbo workflow)
- upgrade to 0.7.2 (start there, maybe datasets not needed)
- docling serve for parsing PDFs
- brew tap antoniorodr/memo && brew install antoniorodr/memo/memo
- nvm, lts/krypton, npm install -g openclaw
koboldcpp
kiwix / hotspot
- gutenberg, wikipedia, etc
searxng container (run.sh in dev/searxng), modify the settings.yml for json / rss and GET
crawl4ai container (run.sh in dev/crawl4ai)

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

models:
https://huggingface.co/mlx-community/models?sort=likes
qwen3.6-35b
qwen3.5-122b
medqwen
saullm
drsam

agents:
openclaw

RAG/memory:
openclaw

ui:
openclaw

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
todo: ernie

doc parsing:
https://docling-project.github.io/docling/getting\_started/installation/#ocr-engines
pip install docling and docling[tesserocr] (needs tesseract)
docling-tools models download
pip install "docling-serve[ui]"
https://github.com/docling-project/docling-serve
docling-serve run --enable-ui
TODO: run with image description services: https://github.com/docling-project/docling-serve/blob/main/docs/usage.md

slack:
openclaw
- followed directions for token, but see openclaw.json for customizations required for channel/user

browser use:
openclaw

instagram:
https://instaloader.github.io/installation.html
https://instaloader.github.io/basic-usage.html
pip install instaloader

skills:
https://github.com/openclaw/openclaw/blob/main/skills/apple-notes/SKILL.md

unsorted:
https://github.com/rishikanthc/Scriberr
https://github.com/ufal/SimulStreaming
https://github.com/simular-ai/Agent-S?tab=readme-ov-file
https://github.com/filipstrand/mflux
https://github.com/ILikeAI/AlwaysReddy
https://github.com/Mintplex-Labs/anything-llm?tab=readme-ov-file

voice ai:
https://github.com/ml-explore/mlx-examples/tree/main/whisper
https://huggingface.co/collections/mlx-community/vibevoice
https://huggingface.co/collections/mlx-community/chatterbox-tts
https://huggingface.co/collections/mlx-community/voxcpm
https://modal.com/blog/open-source-stt
https://medium.com/@princekrampah/real-time-llm-voice-chat-in-python-kokoro-moonshine-open-source-models-6c6270cbe967
https://github.com/speaches-ai/speaches
https://github.com/SYSTRAN/faster-whisper
https://github.com/EpicenterHQ/epicenter/tree/main/apps/whispering#install-whispering
