# Prompt exploration
This is my sketchpad for testing out research prompts.

## First Iteration
```
What is the state of research into generating 3D meshes from single 2D images? find as many published papers as you can from the last 6 months (at least 10.) Create a table that compares them: the first column should include the paper title; the second column should be a link to the paper; the third column should be the paper's abstract.
```
This is garbage... I'm boring myself!

## Second Iteration
```
You are an AI researcher focused on systems for generating 3D meshes from single images.

What are the most authoritative sources for information on AI models that can generate a 3D mesh from a single image? Create a table that lists the sources (minimum 3, maximum 30). The first column provides the name of the source; the second column provides a link to the source; the third column provides a summary of the source; the fourth column provides links to 3 other referring sources that claim this source is or is not authoritative; the fifth column provides a short analysis of whether and how there referrers differ; the last column provides a confidence rating of high | medium | low.

Do not leave any cells blank. If you are unsure, at any point, ask me for guidance.
For the source links: check that they are live; if 404 then do not include.
For the referrer links: check that they are live; if 404 then do not include.
If no referrer links can be found, do not include the source.

Your goal is to find the most performant system that will run on a consumer laptop.

Save the result as "RAG-research.md" to /Users/james/GIT/Hermes/OSSI/corpus

Prepend the model used, the prompt, and the date it was generated to the beginning of the document in the following YAML structure:
—
Model: (model name)
Prompt: (insert prompt)
Date: (insert yy/mm/dd)
—
```
Still not very interesting. I'm not technical enough to understand most of what's in these papers.

## Third iteration
```
I am an artist looking for for tools that generate 3D meshes from single images.

Compare tools on [Hugging Face](https://huggingface.co/) that generate 3D meshes from single images.

For each of the results create a table with the folllowing columns:
- name of project
- link
- how active is the model?
- when was it last updated
- can it run on a consumer laptop?

Do not leave any cells blank. If you are unsure, at any point, ask me for guidance.
For the source links: check that they are live; if 404 then do not include.
For the referrer links: check that they are live; if 404 then do not include.
If no referrer links can be found, do not include the source.

Your goal is to find the most performant system that will run on a consumer laptop.

Save the result as "RAG-research.md" to /Users/james/GIT/Hermes/OSSI/corpus

Prepend the model used, the prompt, and the date it was generated to the beginning of the document in the following YAML structure:
—
Model: (model name)
Prompt: (insert prompt)
Date: (insert yy/mm/dd)
—
```
