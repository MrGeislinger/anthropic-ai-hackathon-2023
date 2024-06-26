# Anthropic AI Hackathon 2023

> Project for 2023 Anthropic AI Hackathon from lablab: https://lablab.ai/event/anthropic-ai-hackathon

# Demo

Demo is live! [https://whatd-i-miss.streamlit.app/](https://whatd-i-miss.streamlit.app/)
> Note that the Streamlit instance probably has to be woken up

Though the supplied Antrhopic API Key can only handle one request at a time. Consider [supplying your own](https://www.anthropic.com/earlyaccess)


# Setup

Current version should be able to be run out of the box (get's precomputed parts via GitHub's releases). Should be simple enough to follow these directions:

1. Clone Repo: `git clone git@github.com:MrGeislinger/anthropic-ai-hackathon-2023.git`
2. (Optional) Create an environment (like conda: `conda create --name wim python=3.11)
  - Note I used `python 3.11` other recent versions might work but can't guarantee...
3. Install requirements: `pip install -r requirements.txt`
4. Run app: `streamlit run app.py`
5. Enjoy! (`localhost:8501`)

## Loading Config Example

For a simple example data config file, see `config.json` from [v0.1.1](https://github.com/MrGeislinger/anthropic-ai-hackathon-2023/releases/tag/v0.1.1). Simply download file to workspace to use in deployed Streamlit app.


## Creating Your Own transcripts from Audio

Associated repo to create transcripts for this tool from a set of videos on YouTube playlist: https://github.com/MrGeislinger/whisper-extract
Repo will be updated periodically indpendent from this project.

I suggest using the `small` model first since larger models can take a significant amount of time.

