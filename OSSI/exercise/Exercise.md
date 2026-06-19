# A simple Copilot research exercise:
GW offers a few generative AI tools to students. Let’s look at [**Copilot**](https://it.gwu.edu/microsoft-copilot) and talk about why we would use this tool. It’s safe - university vetted. Can get it to do something useful? We’ll treat it like an unpaid research intern, have it collect lots of data, check it’s sources, and structure it’s output in a usable, presentable way. Can we get it to do a research task in minutes that would take you hours, and provide trustworthy results?

When I start projects I often do research to get the lay of the land, get ideas for my build, assess tools I might need. It takes time, and I'm not very methodical! Google is great, but often sites that compare things don't do so by the criteria I'm interested in, and picking through twenty or thirty sites kills a lot of daylight.

Think about a research question that compares *some things,* for example:
- What are top ten strangest Lego bricks?
- What are top five easiest CAD tools for beginners?
- What are the best LLMs for writing python and working with unstructured data?

And, you want 5 credible online sources for each of *the things.*  

Now think about what criteria will help you select from those results
- (Ex: lego) how complicated is the morphology of the brick?
- (Ex: CAD) what are the hardware requirements for each app and which formats can it export?
- (Ex: AI) can I run the model locally with my hardware specifications?
- You want Copilot to check for consistency across the sources
- You want the results returned in a table format (it will be in markdown)
- Copy the result into a new file.

Here’s an example of what a structured prompt might look like:
> Compare 10 fruits. For each fruit, provide nutritional information. For each fruit, gather info from the 5 most reliable sources on the web. Where the sources have conflicting information, explain. Present the results in a table with four columns: name of fruit, nutritional information, links to sources, and discussion of conflicting source information.

Extra credit:
- Commit to a GIT repo. Notice that the markdown formatting from Copilot is honored in GitHub.

---

Some things to do:
- Consider, how long would it take you to collect this information manually, before assessing whether is it accurate? 
- Check all of the links; do they work? Are they pointing to the right place? Is the information on the linked pages relevant? Overall, is this more or less accurate than if you had collected this information manually?

---

### General recipes I keep handy.
I keep lots of snippets that can be added to prompts to improve results. I find them all over the place - message boards, Instagram, Substack... sometime I even think of my own. Mix, match, use when needed: 

**Personas** prime the response with context and perspective:  
```
You are a subject matter expert in (your domain).
```

**Citing the model you use** is a good practice for transparency into what is human- vs. LLM-generated. I require all of my students (art students!) to do something like:  
```
Prepend the model used, the prompt, and the date it was generated to the beginning of the document in the following YAML structure:
—
Model: (model name)
Prompt: (insert prompt)
Date: (insert yy/mm/dd)
—
```

**Tables** are obviously a good, human-readable structure as mentioned above. The pattern I use is:
```
Save the results to a markdown table with these specific columns (list the column names separated by commas)
```
.JSON is another structured format the LLMs can create reasonable well. Specifying a data structure for the LLM responses makes it easier to get predictable and verifiable output. 

**Links** provide pointers to real sources that you can verify:
```
Create a list of sources and their links. Double check that the links are valid; if the links are 404, do not include them.
```
