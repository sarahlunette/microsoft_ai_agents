**INTRODUCTION**

First get the zephyr model and biomistral if you want to try out. You will use the uncleaned notebook LLM_app.py that will be cleaned later. Just skip the part that says it is to skip and you don't need to go further than the snapshot_downloads to run the cells.

In order to create the colab api, you'll have to run the with_cloudflared.iynb on colab and get the cloudflare external address to input in the llm_app_generate_on_colab.py in the COLAB_URL.

Then, in local, launch uvicorn llm_app_generated_on_colab:app --port 9000 (attention port changes so that there is no problem with the local launch on colab, which may or may not be the case).

Then, in local again, launch streamlit demo as streamlit run demo.py

In the complete_app folder, you should run buildozer init and then buildozer android debug

With OpenMTP put the application on your phone, in the download folder (this is on Google Phone) and install it (the API version) calling onto colab (so you will have to modify the link to cloudfare everytime and repackage and reinstall the application).
