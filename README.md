# CoT-Redirection: Can Chains of Thought be manipulated in Large Language Models?

This repository is the official implementation of **CoT-Redirection**.

| ![An example of CoT-Redirection applied.](https://github.com/sahal-mulki/cot-redirection/blob/1f3a54d1b6e0c84d479ed87cbdb1d145175cf2b5/Picture2.png) | 
|:--:|
| *An example of CoT-Redirection applied.* |

# Table of Contents.
- [Table of Contents](#table-of-contents)
- [Abstract](#abstract)
- [Requirements](#requirements)
- [Acknowledgements](#acknowledgements)

## Updates:

I'm glad to announce that my paper won Best Research Paper in the HW-TWS Action Research Cohort of '25! [More information here.](https://www.linkedin.com/posts/sahalmulki_ai-llm-machinelearning-activity-7338238288173932545-LEq3). 

### Update 2❗

I'm honored to be presenting this paper at [ISDIA '2026](https://isdia.org/) in Dubai at the 7th of February. I'll be updating this page with the Springer publication DOI, link and citation once available. 

# Abstract

Large Language Models (LLMs) are widely used AI systems that process, understand and generate high-quality natural language text. While Chain of Thought (CoT) prompting has emerged as an effective strategy to enhance LLM reasoning capabilities, it may also serve as a valuable yet under ex-plored attack vector for novel adversarial attacks on LLMs. This study investigates whether adversarial manipulation of a LLM’s CoT reasoning steps can lead to attacker-controlled responses that override the model’s intended outputs. To test our hypothesis, we introduced a novel CoT-based redirection method designed to influence model responses in a simulated scenario where attackers could inject text into the models’ CoT steps and we conducted a systematic review of related literature. Our results showed that our attack method (“CoT-Redirection”) demonstrated very high attack success rates of 97-100% on two leading open-source LLMs (Llama 3.1 8B and Phi 3 Medium), with task accuracy dropping to near-zero levels under attack conditions; a reduction of approximately 60-70 percentage points from baseline CoT performance. While our results confirm that CoT reasoning can serve as a potent attack vector for adversaries wishing to steer model responses; our findings are constrained by a limited sample size (300 questions), two tested models, and computational resources. However, our work provides initial empirical evidence of a new dimension of adversarial vulnerability in rea-soning-driven architectures and aims to stimulate further research at the in-tersection of CoT prompting and adversarial attacks in LLMs.

# Requirements

You may also easily use the Google Colab version of the dataset generation notebooks.

### To install dependencies:

`pip install -r requirements.txt`

# Acknowledgements

I'd like to specially thank Dr. Maheen Hasib from Heriot-Watt University Dubai for her invaluable feedback and mentorship on this paper. Further, I'd like to thank my school, The Westminster School, Dubai, on presenting me with this opportunity.


# Cite this:

```
@inproceedings{mulki2026cotredirection,
  title = {CoT-Redirection: Can Chains of Thought be manipulated in Large Language Models?},
  author = {Muhammad Sahal Mulki and Maheen Hasib},
  year = {2026},
  language={English}
}
```
