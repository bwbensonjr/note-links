---
id: 153
url: https://partnerhelp.netflixstudios.com/hc/en-us/articles/43393929218323-Using-Generative-AI-in-Content-Production
title: Using Generative AI in Content Production &ndash; Netflix | Partner Help Center
domain: partnerhelp.netflixstudios.com
source_date: '2025-11-11'
tags:
- ai
- llm
- security
summary: Netflix provides guidance for production partners on responsibly using generative
  AI tools in content creation, emphasizing transparency and adherence to key principles.
  The guidance establishes that low-risk GenAI uses—such as temporary creative aids
  that don't replicate copyrighted material, replace talent, or compromise data security—may
  not require formal approval, but any use involving final deliverables, talent likenesses,
  personal data, or third-party intellectual property requires written approval. Netflix
  expects all partners to report their intended GenAI use and follow strict protocols
  around data protection, ethical representation, and respecting performer consent
  and union requirements.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Using Generative AI in Content Production &ndash; Netflix | Partner Help Center

Using Generative AI in Content Production
=========================================

[*Skip to Translations*](#h_01K39BXBFJKBC2HEXRP00QCG8J)

**Introduction**
----------------

Generative AI tools (GenAI)  that allow users to rapidly generate new and creatively unique media (video, sound, text, and image) are increasingly being used across creative workflows in Content Production. At Netflix, we see these tools as valuable creative aids when used transparently and responsibly.

This guidance helps filmmakers, production partners, and vendors understand when and how to use GenAI tools in production. It also offers [a practical tool](#h_01K1BTNMC4RTXXMXPKW2TJJ2ZJ) for assessing and enabling confident GenAI use when producing content for Netflix. 

To support global productions and stay aligned with best practices, we expect all production partners to share any intended use of GenAI with their Netflix contact, especially as new tools continue to emerge with different capabilities and risks. 

Most low-risk use cases that follow the guiding principles below are unlikely to require legal review. However, if the output includes final deliverables, talent likeness, personal data, or third-party IP, written approval will be required before you proceed.

---

**TABLE OF CONTENTS**
---------------------

[Guiding Principles](#h_01K1BTNMBC8DKAF1607XQ3S9AK)

[What use cases always require written approval?](#h_01K1BTNMBHW1JSCHK4914BAXDE)

[1. Data Use](#h_01K1BTNMBHB5GW4FJW8X64KHNN)

[2. Creative Output](#h_01K1BTNMBKMP99CP2PCXZ8W3H5)

[3. Talent & Performance](#h_01K1BTNMBP76KFGEWAFWAH22TA)

[4. Ethics & Representation](#h_01K1BTNMBRSBGNTCCTY9DBXMV2)

[How can I ensure confidentiality and data protection?](#h_01K1BTNMBS130Y200ZWV3H6ZAT)

[Are the considerations different for final output vs temporary media?](#h_01K1BTNMBVFQYQNJCCMKR254VK)

[What should we consider before using GenAI for talent enhancement?](#h_01K1BTNMBWWPTJJA79EFPY8NRJ)

[What if I’m using a custom workflow or working with a vendor who is?](#h_01K1BTNMC21630W4ZWFFS0EYP2)

[Appendix](#h_01K1BTNMC3K7ECQKP84CDSQVZG)

[Proposed Use Case Matrix](#h_01K1BTNMC4RTXXMXPKW2TJJ2ZJ)

---

**Guiding Principles**
----------------------

Given the sensitivities surrounding the use of these tools and the evolving legal landscape, it is essential to act responsibly when employing generative workflows. Netflix asks partners to consider the following guiding principles before leveraging GenAI in any creative workflow: 

1. The outputs do not replicate or substantially recreate identifiable characteristics of unowned or copyrighted material, or infringe any copyright-protected works
2. The generative tools used do not store, reuse, or train on production data inputs or outputs.
3. Where possible, generative tools are used in an [enterprise-secured environment](#h_01K1BTNMBS130Y200ZWV3H6ZAT) to safeguard inputs.
4. Generated material is temporary and not part of the [final deliverables](#h_01K1BTNMBVFQYQNJCCMKR254VK).
5. GenAI is not used to replace or generate new [talent performances](#h_01K1BTNMBWWPTJJA79EFPY8NRJ) or union-covered work without consent.

If you can confidently say "yes" to all the above, socializing the intended use with your Netflix contact may be sufficient. If you answer “no” or “unsure” to any of these principles, escalate to your Netflix contact for more guidance before proceeding, as written approval may be required. 

If your partner vendor is using a custom GenAI workflow — meaning a pipeline built from multiple tools or models — the same principles apply. More details can be found [here](#h_01K1BTNMC21630W4ZWFFS0EYP2). 

---

**What use cases always require written approval?**
---------------------------------------------------

Below are a few examples of situations that, in addition to reporting intended use, always require escalation and written approval before proceeding. 

#### **1. Data Use**

Protecting personal data and creative rights is essential when working with GenAI. These tools often require input data to generate outputs, and how that data is handled matters. Before using any GenAI tool, especially third-party or off-the-shelf options, consider whether you are using material that requires special handling, clearance, or consent.

* Use of Proprietary or Personal Information: Do not input Netflix-owned materials (e.g., unreleased assets, scripts, production images) or personal data (e.g., cast or crew details) into tools unless explicitly approved.
* Third-Party or Unowned Talent Assets: Do not train or fine-tune models using material from artists, performers, or other rights holders unless you have the proper legal clearance.

Example: Training an image model in the style of another artist using a library of their past work, where Netflix or the talent has not cleared rights.

#### **2. Creative Output**

AI-generated content must be used with care, especially when it forms a visible or story-critical part of the production. Whether you're designing a world, a character, or artwork that appears in a scene, the same creative and legal standards apply as with traditionally produced assets.

* Generation of Key Creative Elements: GenAI should not be used to generate main characters, key visual elements, or fictional settings that are central to the story without written approval.
  + Examples: GenAI is used to generate a second killer doll to play the red light/green light game with Young-hee in Squid Game.
* Copyrighted or Estate-Controlled: Avoid using inputs (e.g., prompts, images) that reference copyrighted materials or likenesses of public figures or deceased individuals without appropriate permissions.
  + Example: “Create an image inspired by [McCurry’s Afghan Girl](https://www.stevemccurry.com/posters/p/afghan-girl)” or referencing distinctive features of a known performer (e.g., “Create a character with Meryl Streep’s nose”).

#### **3. Talent & Performance**

Respect for performers and their work is foundational to the responsible use of GenAI. Whether enhancing a recorded performance or generating a digital likeness, the threshold for consent and care is exceptionally high when the intent or character of a performance may be altered.

* Synthetic or Digital Replicas - Do not create digital performers, voices, or likenesses of real talent without explicit and documented consent and complying with guild requirements (where applicable).
* Significant Digital Alterations to Performances - Be cautious when making changes that affect a performance's emotional tone, delivery, or intent, as even subtle edits may have legal or reputational implications.

Examples include visual ADR (altering lip-sync or facial performance to match new, unscripted dialogue).

#### **4. Ethics & Representation**

Audiences should be able to trust what they see and hear on screen. GenAI (if used without care) can blur the line between fiction and reality or unintentionally mislead viewers. That’s why we ask you to consider both the intent and the impact of your AI-generated content.

* Misleading or Misrepresentative Content: Avoid creating content that could be mistaken for real events, people, or statements if they never actually occurred (e.g., fabricated footage, dialogue, or scenes presented as authentic).
  + Example: using GenAI to create a fake news segment featuring a real journalist delivering a fabricated statement, even if intended as background.
* Impact on Union Roles: Ensure that your use of GenAI does not replace or materially impact work typically done by union-represented individuals, including actors, writers, or crew members, without proper approvals or agreements.

---

**How can I ensure confidentiality and data protection?**
---------------------------------------------------------

The use of tools covered by Netflix Enterprise Agreements provides an additional level of security to protect input data. Speak with your Netflix primary contact about available tools and the onboarding process. These tools:

* Prevent capture, training, or resale of your inputs
* Protect sensitive inputs like scripts, production images, or talent visuals

Even with secure tools, any use of sensitive information (e.g., talent likeness, unreleased footage, contracts) requires escalation to your Netflix contact.

When not using enterprise tools, ensure that any AI tools, plugins, or workflows you use do not train on inputs or outputs, as using the wrong license tier or missing pre-negotiated data terms could compromise confidentiality. You are responsible for reviewing the terms and conditions (T&Cs). Please check with your Netflix contact if you have any further questions.

**Are the considerations different for final output vs temporary media?**
-------------------------------------------------------------------------

If created with GenAI, content that appears in the final cut—even in the background—can raise legal, copyright, or trust issues with the audience. That’s why we ask you to flag any GenAI-generated elements early, especially if they will be seen or heard on screen.

If your proposed use case includes visual, audio, or text elements generated by AI (e.g., posters, documents, signage, or news clippings), contact your Netflix representative as early as possible for legal guidance. These items may require rights clearance before they can be included in final deliverables.

Some GenAI-generated props or set pieces may be considered incidental, for example, a historical document shown briefly in the background and not referenced in the scene. However, if the element is prominent (e.g., a character reads it aloud or it contributes to the story), it must be treated with greater care.

In these cases, you can use GenAI to explore ideas or mockups. Still, the final version should involve meaningful human input and follow the legal review process through your Netflix contact.

---

**What should we consider before using GenAI for talent enhancement?**
----------------------------------------------------------------------

There is a long tradition of digitally altering performances in post-production and VFX. However, the use of AI to modify or replicate a performer's likeness or voice introduces new legal, ethical, and reputational challenges. Therefore, obtaining consent when appropriate and exercising caution are crucial. Many talent enhancement use cases require legal review, so please plan accordingly. Here are some guidelines to consider: 

* If creating a Digital Replica (i.e., a generated output recognizable as the voice and/or likeness of an identifiable performer for the purpose of portraying them in photography or soundtrack, they did not perform), consent is required. No further consent is needed to use the Digital Replica if the performance output: (1)  remains substantially as scripted, performed, or recorded (e.g. reshoots); (2) depicts activities incapable of being performed by a human for safety reasons; or (3) results in the performer being unrecognizable (e.g. wearing a mask).

* Digital Alterations: Consent is generally required for digital alterations, except for those customarily done in the entertainment and film industry, such as:
  + Alterations where the photography or soundtrack remains substantially as scripted, performed, or recorded.
  + Post-production changes for cosmetics, wardrobe, noise reduction, timing, continuity, pitch, clarity, and similar purposes.
  + Circumstances where dubbing or using a double is permitted under existing agreements.

* Model Usage:
  + Any models trained to perform talent enhancement manipulation should be used solely for the production in question and within the scope of work agreed upon with the talent.
  + Models must not be used to create an actor's performance in another production, pitch, or concept without the express consent of all parties involved.
* Quality Assurance:
  + Perform early tests to ensure that the quality of the outputs is acceptable both creatively and technically, so as not to adversely affect the talent’s original performance.
  + Where applicable and practical, plan dedicated data capture sessions with the talent to ensure the best possible outcomes.
  + Avoid enhancements that could harm the actor’s reputation, dignity, or personal image.

By following these guidelines, you can navigate the complexities of using AI in creative workflows while respecting the rights and integrity of performers.

---

**What if I’m using a custom workflow or working with a vendor who is?**
------------------------------------------------------------------------

For vendors: If you're delivering work to Netflix using a custom GenAI workflow built from multiple tools, each step in the pipeline must meet our standards for data protection, consent, and content integrity as outlined in this document. 

For production partners: If you're hiring a vendor or AI studio, use this guidance as a framework to help assess how they manage data, creative control, and final outputs. If you are unsure whether the pipeline meets the expectations outlined in this guidance, seek guidance from your Netflix contact. 

---

**Appendix**
------------

### **Proposed Use Case Matrix**

We have provided a  Proposed Use Case Matrix at the end of this guidance as a tool to triage your proposed use case quickly. 

|  |  |  |
| --- | --- | --- |
| **Proposed Use Case** | **Action** | **Rationale** |
| Using GenAI for ideation only (moodboards, reference images) | ✅ | Low risk, non-final, likely not needing escalation if guiding principles are followed. |
| Using GenAI to generate background elements (e.g., signage, posters) that appear on camera | :warning: | Use judgment: Incidental elements may be low risk, but if story-relevant, please escalate. |
| Using GenAI to create final character designs or key visuals | :octagonal_sign: | Requires escalation as it could impact legal rights, audience perception, or union roles. |
| Using GenAI for talent replication (re-ageing, or synthetic voices) | :octagonal_sign: | Requires escalation for consent and legal review. |
| Using unowned  training data (e.g., celebrity faces, copyrighted art) | :octagonal_sign: | Needs escalation due to copyright and other rights risk. |
| Using Netflix's proprietary material | :warning: | Needs escalation for review if outside secure enterprise tools. |

### **Translations**

[Español (Latinoamérica)](https://drive.google.com/file/d/1OhOJXv6cwcc8Ob61K_zuxOxxzJst5V-V/view?usp=drive_link)

[Français](https://drive.google.com/file/d/1PcVBUivo-CYSIj_fXMjPwS9lh6WC9WlT/view?usp=sharing)

[Português](https://drive.google.com/file/d/16v2PFCYKk08s0o37kHJ4LZmr6n5cdxia/view?usp=drive_link)

[ไทย](https://drive.google.com/file/d/122a0P_EASxSQ2CklK2Tnm6N4CjrbC92h/view?usp=drive_link)

[Türkçe](https://drive.google.com/file/d/1Gr8ml-b9QSoWLkZkN18p03uNVQs5Aj2X/view?usp=drive_link)

[繁體中文](https://drive.google.com/file/d/1wU1Q6zTd7zt7G7umgtk2VRepkGAwruA8/view?usp=drive_link)

Was this article helpful?
142 out of 151 found this helpful
