---
title: "Insert Chapter Title>"
author: "Your Name Here"  # Prefer a single string; add multiple authors separated by commas if needed
date: "2025-11-01" # Use YYYY-MM-DD
description: "Short, 1 or 2 sentence summary of the chapter's purpose and scope."
keywords: ["DraCor", "digital humanities", "programmable corpora"] # Adapt keywords to fit your chapter; make it specific
license: "CC BY 4.0"
# Jupyter Book notes:
# - The book structure (chapters) is defined in _toc.yml; keep this file as a single chapter page.
# - Keep British English across the textbook.
---

# {{ Insert your Title Here }}

<!--
This is a contributor-facing template for DraCor Textbook chapters.
Audience: beginner first; no prior programming knowledge assumed.
Keep prose clear and concise; avoid unexplained jargon.
-->

```{note}
**How to use this template:** Replace placeholders, keep the section order, and keep examples concise. Screenshots and short code snippets are welcome.
```

## 1. Overview

State what this chapter covers and why it matters within the DraCor ecosystem. Mention links to neighbouring chapters for continuity.

> **Example:** This chapter introduces the DraCor front end and shows how to explore corpora and individual plays through its interactive interface. Readers will learn to navigate textual data, access character and speech information, use built-in visualization tools such as network graphs and speech distribution, and discover how to download data files from the Downloads section of each play.

## 2. Pre-requisites (Optional)

List conceptual/technical assumptions explicitly. Keep them minimal.

- Basic familiarity with literary studies or DH concepts.
- No programming experience required.
- Web browser and internet access.

## 3. Learning Outcomes

After completing this chapter, learners will be able to:

1. <Outcome 1>
2. <Outcome 2>
3. <Outcome 3>
4. <Outcome 4>

## 4. Theoretical Background

The DraCor front end represents the most accessible entry point to the idea of a **programmable corpus**—a corpus that is not only readable by humans but also structured for computational use through open standards and interfaces. As part of the DraCor research infrastructure, the front end connects textual, metadata, and analytical layers within a reproducible workflow.


```{admonition} Tip for authors
When expanding this section, connect the front end to DraCor’s underlying architecture (TEI data, API, GitHub repositories) and to discussions about open data and research infrastructures.
```

## 5. Practical Examples

Provide 1–3 focused walkthroughs. Prefer small, reproducible steps.

### Example A — Front-End Walkthrough (no code)

1. Open <corpus URL> and navigate to a play.
2. Explore tabs:  *Network*, *Speech Distribution*, *Full text*
3. Identify one insight and link it to the underlying data concept.


### Example B — API Teaser (optional code)

```python
# Minimal example for Jupyter Book users (optional)
# Requires: pydracor installed in the environment
# !pip install pydracor
import pydracor
dracor = pydracor.DraCor()
corpus = dracor.get_corpus("caldracor")
len(corpus["plays"])
```

## 6. Exercises

Design 2–3 exercises that can be completed in 10–20 minutes each.
Provide expected outputs or self-check questions.

**Exercise 1.** Compare *Speech Distribution* and *Network* tabs for a play.*Self-check:* Which characters are most central?

**Exercise 2.** Retrieve the character list for a play via the API. *Self-check:* How would you cite this dataset?

## 7. Teaching Notes (Optional?)

Guidance for instructors (time planning, scaffolding, assessment).

- 60–90 minutes session; pairs or small groups.
- Ask for short reflective notes on interpretive limits of each visualization.

## 8. Further Reading and Resources (Optional)

- DraCor API Documentation: https://dracor.org/doc/api
- forTEXT unit: Netzwerkanalyse mit Gephi
- Walsh, Melanie. *Introduction to Cultural Analytics*

> Add links to HU DraCor Notebooks, CLS Infra, GitHub issues relevant to the chapter.

## 9. Glossary

| Term | Definition |
| --- | --- |
| **Corpus** | Structured collection of texts prepared for analysis. |
| **API** | Interface for programmatic data access. |
| **Front End** | User-facing web interface of DraCor. |
| **Character Network** | Graph of co-presence/interaction among characters. |

## 10. Next Steps

Point to the immediate next chapter(s) and an advanced alternative.

- Continue with: *API Usage* (data access and reproducibility).
- Advanced: *Local Infrastructure* (running services, data pipelines).

## 11. References

Use in-text citations and include a short list here. 

- <Author, Year>. <Title>. <Venue>. <DOI/URL>.

---

<!-- Contributor Checklist (keep this block) -->
- [ ] YAML metadata filled (title, author, date, description, keywords).
- [ ] Learning outcomes are observable (verbs like *describe, navigate, interpret, link*).
- [ ] At least 2 exercises with self-checks.
- [ ] Figures and/or short code snippets where helpful.
- [ ] References added.
