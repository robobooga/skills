---
name: explain-simply
description: Explain any document, concept, or piece of text in plain everyday language with analogies. Use this skill whenever the user wants something simplified, dumbed down, made accessible, or explained like they're five. Trigger on phrases like "explain this simply", "explain like I'm 5", "ELI5", "dumb this down", "what does this actually mean", "explain in plain English", "I don't understand this", "make this simple", "break this down", "what is this saying", "translate this", "explain to a non-expert", "explain to someone who knows nothing about", or any time the user shares a document/text/concept and wants it made more understandable. Even if the user doesn't say "explain-simply" explicitly — any request to make something more accessible, cut through jargon, or understand a confusing text should use this skill.
---

# Explain Simply

Your job is to make something that's confusing or jargon-heavy crystal clear to someone with no background knowledge. The standard to aim for: could a curious 14-year-old understand this? Not a smart adult who just hasn't heard the term, but someone encountering the concept cold.

## The core challenge

Jargon is sneaky. You can strip out one technical term and accidentally replace it with another one. Read what you wrote as if you've never heard any of the terms involved. If a sentence requires any prior knowledge to understand, rewrite it.

Analogies are your most powerful tool. A good analogy doesn't just decorate the explanation — it *is* the explanation. Find the thing in everyday life that works the same way. Good analogy fodder: cooking, sports, driving, school, money/banking, plumbing, electricity, a city, a factory, a recipe.

## How to structure the explanation

**1. The one-line gist**
Lead with a single sentence that captures the whole thing — even if it's imprecise. Give people a peg to hang the rest on.

**2. The big-picture analogy** (if the topic is complex)
Before diving in, orient the reader with an analogy that captures the overall shape of the thing. "This whole system works like a restaurant kitchen, where..." sets up the rest much better than jumping straight into pieces.

**3. Walk through the key ideas**
Go through the main concepts one at a time. For each one:
- State it in plain English first
- Then give a concrete analogy if it's abstract
- Keep paragraphs short — one idea per paragraph

Don't cover everything in the source material, just the load-bearing ideas. If there are 10 bullet points and 3 of them carry 90% of the meaning, explain those 3 well.

**4. The bottom line**
End with 2–3 plain-language takeaways: what does this actually mean, what should the reader do or believe after reading this? If the user shared a contract/policy/warning, explicitly flag what matters for them.

## Output format

```
**The short version:** [one sentence — what this thing is or does, in plain English]

---

[Explanation in plain prose, organized by concept. Use analogies freely. Bold the names of concepts when you first introduce them so they're easy to scan.]

---

**Bottom line:**
- [plain English takeaway 1]
- [plain English takeaway 2]
- [plain English takeaway 3 if needed]
```

## Calibration

- **Keep it warm, not dumbed down.** You're not patronizing the reader — you're being a good explainer. The tone should be like a knowledgeable friend, not a teacher talking to a slow student.
- **Shorter is almost always better.** A tight 200-word explanation that lands beats a thorough 800-word one that loses people halfway through.
- **Match depth to what was asked.** A one-paragraph concept gets a one-paragraph explanation. A 10-page whitepaper gets something more thorough — but still structured and skimmable, not a wall of text.
- **When in doubt about scope**, explain the thing the user is most likely confused about, not every detail in the source.
- **Never use the word "utilize".** If you catch yourself writing like a textbook, stop and rewrite.

## Example

**User shares:** *"Neural networks use gradient descent to minimize a loss function via backpropagation through the computational graph."*

**Good output:**

**The short version:** A neural network learns by making guesses, measuring how wrong it was, and then adjusting its internal dials to do better next time.

---

Think of it like tuning a radio. You turn the dial, hear static, and nudge it a bit. Too far left — more static. Back right a bit — clearer. You keep adjusting until the signal is sharp. That's basically what a neural network does, except it has millions of dials and adjusts them all at once using math.

The **"loss function"** is just the measurement of how wrong the network's guess was — like counting how much static you heard. Lower is better.

**"Gradient descent"** is the strategy for which direction to turn the dial. It's like being blindfolded on a hilly landscape and trying to find the lowest valley by always stepping in whichever direction feels downhill.

**"Backpropagation"** is just the process of figuring out which dials were most responsible for the mistake, so you know which ones to adjust most. Like figuring out which ingredient made the soup too salty before you decide what to fix.

---

**Bottom line:**
- Neural networks get better by repeatedly making guesses and adjusting based on how wrong they were
- All those intimidating terms describe parts of that same feedback loop
- You don't need to understand the math to grasp what's happening: guess → measure mistake → adjust → repeat
