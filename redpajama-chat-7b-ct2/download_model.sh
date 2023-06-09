mkdir togethercomputer
git lfs install --skip-smudge
git clone https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Chat togethercomputer/redpajama-chat-7b
cd togethercomputer/redpajama-chat-7b
git lfs pull
git lfs install --force
pwd
ls -l
