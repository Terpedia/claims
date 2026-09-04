# Terpene effect claims: an evidence-bounded receptor hypothesis map

**Working manuscript — 4 September 2026**

**Proposed article type:** Perspective article (evidence-based pharmacological perspective)

**Keywords:** terpenes; receptor pharmacology; evidence grading; structure–function
hypotheses; translational pharmacology; reproducibility; claim auditing

## Abstract

Promotional terpene tables often present biological effects as if they were
properties of a compound. We reinterpreted one Terpedia promotional matrix as
109 marked effect hypotheses spanning 16 compounds, drawn from 17 explicitly
named terpene columns,
then linked those hypotheses to a receptor-oriented literature map. The
analysis preserves stereochemical labels, separates direct receptor
pharmacology from animal mechanism studies and computational predictions, and
does not treat missing database joins as evidence of inactivity. Fifty-nine
hypothesis rows involved compounds with direct receptor-pharmacology evidence
at the compound level, while 14 rows had only indirect mechanistic or
computational support. Only seven hypothesis rows had an existing local Terpedia receptor-evidence
link, all involving linalool and a GABA-A receptor complex. No promotional
effect was classified as fully supported because the current evidence map does
not yet provide effect-specific, identity-resolved validation for those rows.
The resulting matrix is therefore a prioritization tool for structure–function
research, not an efficacy catalogue.

## 1. Introduction

Terpenes are commonly associated with broad labels such as “anti-inflammatory,”
“sedative,” “analgesic,” or “neuroprotective.” Such labels can be useful as
search terms, but they collapse several distinct propositions: that a defined
chemical identity is present; that it reaches a relevant biological system;
that it interacts with a named protein; that the interaction changes receptor
or channel function; and that the resulting mechanism explains a measured
phenotype at a relevant exposure.

This study treats promotional claims as hypotheses and asks a narrower
question: which protein or receptor mechanisms are plausible starting points
for testing them? The distinction matters because target evidence is not
equivalent to efficacy evidence, and a null join in a database is not a
biological negative.

## 2. Materials and methods

### 2.1 Promotional hypothesis source

We used the Terpedia Google Sheet snapshot dated 26 June 2026. Its matrix
contains effect labels in rows, terpene labels in columns, source counts, and
“x” marks indicating an association. We converted each marked cell into a
unique hypothesis identified by a stable local ID. The resulting register has
109 marked compound–effect rows across 16 compounds. The source header contains
17 named compounds, but l-limonene has no marked cells and therefore contributes
no hypothesis row.

### 2.2 Identity and evidence policy

α-pinene, β-pinene, d-limonene, and l-limonene were retained as separate
labels. A receptor association was accepted only as a literature lead when the
source named the compound or a clearly defined stereoisomer. Receptor evidence
was classified as: (i) direct binding and functional receptor pharmacology;
(ii) functional receptor pharmacology in recombinant or heterologous systems
without in-vivo validation; (iii) animal or tissue mechanism studies without
direct binding; (iv) computational or network-based nomination; (v)
phenotype-only evidence; (vi) sensory-only evidence; or (vii) unresolved.
These tiers describe compound–target evidence, not support for the effect label.

The evidence boundary for every row is: “receptor association does not
establish efficacy, causality, dose–response, or human relevance.” Missing
structure joins and missing target records were recorded as unresolved rather
than inactive.

### 2.3 Terpedia crosswalk

The local Terpedia evidence layer was checked against the receptor interactome
and available protein/structure projections. A local receptor-evidence link
means that a compound–protein association exists in the current Terpedia
evidence set; it does not mean that the promotional effect is validated. The
literature pass was targeted and hypothesis-generating, not a registered
systematic review, so absence from this map is not evidence of absence from
PubMed or biology.

### 2.4 Support definitions

We reserve “supported effect” for an identity-resolved study that measures the
specific effect, identifies an appropriate biological context, and provides an
evidence chain adequate to the scope of the claim. A receptor mechanism alone
is “mechanistically relevant,” not “effect supported.” The unit of the 59/109
and 14/109 summaries is a hypothesis row, so the same compound-level paper can
appear in multiple effect rows and must not be interpreted as independent
replication.

We used the following non-exclusive evidence ladder when interpreting the
matrix; the permitted conclusions are summarized in Table 1:

**Table 1. Evidence ladder for compound–target interpretation.**

| Level | Meaning | Permitted conclusion |
| --- | --- | --- |
| E0 | No compound-specific evidence in the current map | Target/effect remains unresolved |
| E1 | Sensory, phenotype-only, docking, or network nomination | Prioritizes testing; does not establish a target |
| E2 | Animal, tissue, or antagonist-supported mechanism | Supports a bounded mechanism in the tested model |
| E3 | Recombinant or heterologous functional receptor pharmacology | Supports compound–target function under the assay conditions |
| E4 | Direct binding plus functional target evidence, with effect-specific validation | Supports only the measured effect and scope |

*Abbreviations:* E0–E4, evidence ladder levels 0 through 4.

The current manuscript reports E3/E4 compound-level evidence separately from
effect-level support. No row meets the E4 definition for the promotional effect
itself.

## 3. Results

### 3.1 Overall support profile

Of the 109 hypothesis rows, 59 were attached to compounds with direct receptor
pharmacology somewhere in the literature map, and 14 rows had indirect
mechanistic or computational support. Seven rows had an existing local
Terpedia receptor link.
All 109 retained an `effect_support_status` of `unresolved`, because the map
does not yet connect each effect label to an identity-resolved, appropriately
scoped assay or clinical outcome.

### 3.2 Stronger receptor-mechanism leads

β-caryophyllene is the clearest immune and nociceptive lead. It has reported
binding and functional agonism at CB2 [1], and CB2-dependent analgesic effects
have been reported in mouse models [2]. These results support a testable CB2-mediated
mechanism; they do not validate every anti-inflammatory, analgesic, or
neuroprotective label in the promotional matrix.

α-pinene, linalool, and borneol provide convergent GABA-A hypotheses, but with
different identities, receptor contexts, and exposure questions. α-pinene was
reported to potentiate GABA-A-mediated synaptic responses in brain slices and
to show flumazenil-sensitive effects in a mouse sleep model; the proposed
benzodiazepine-site interaction was supported by molecular modeling rather
than a direct biophysical binding assay [3]. Linalool enhanced GABA-A currents
in recombinant systems [4], while borneol modulated human recombinant
α1β2γ2L GABA-A receptors [5]. These findings make sedation, anxiety, and
nociception useful
follow-up domains, not established human effects.

α-bisabolol supports two distinct lines of inquiry: direct inhibition of the
α7 nicotinic acetylcholine receptor [6] and antagonist-sensitive behavioral
evidence implicating GABA-A signaling. These should not be merged into a
single mechanism without experiments that discriminate them.

Myrcene and nerolidol are plausible TRPV1 leads from heterologous human-TRPV1
expression experiments, not native human pain studies [7]. The related nanoparticle
literature is formulation-specific and cannot be read as proof of free-terpene
pharmacology. Terpineol is a weaker CB1/CB2/D2 hypothesis because its current
support comes from mouse antagonist experiments and docking rather than direct
receptor binding [8]. Separate mouse studies of borneol reported bounded
hyperalgesia and anxiety-related phenotypes [9,10], and linalool altered
respiratory-neuron activity in a rat brainstem preparation [11].

### 3.3 Unresolved and misleading target categories

Several compounds remain without compound-specific human receptor evidence in
this first pass, including d-limonene, l-limonene, fenchol, and terpinolene.
Humulene has plausible immune and nociceptive target families but no resolved
target in the present map. Caryophyllene oxide has a reported mouse sedative
phenotype [12], while one study did not support a GABA-A potentiation mechanism;
the target therefore remains unresolved.
The formulation-specific nanoparticle evidence does not establish free-terpene
pharmacology [13].

Insect odorant-receptor findings for ocimene and caryophyllene oxide are valid
sensory biology but are not evidence for human therapeutic receptor targets.
Similarly, a docking score or a network-pharmacology edge is a prioritization
signal, not a demonstrated interaction.

## 4. Discussion

The matrix shows why “how many claims are supported?” has more than one answer.
At the receptor-mechanism level, 59 hypothesis rows inherit direct
compound-level pharmacology and 14 inherit weaker mechanistic leads. At the
strict promotional-effect level, none is yet fully supported in this dataset.
The difference is
not a failure of receptor biology; it is a consequence of preserving the
logical steps between molecular interaction and phenotype.

The present study is not a quantitative structure–activity relationship
analysis: it does not calculate descriptors, cluster scaffolds, or estimate
structure-dependent potency. Its contribution is an identity-safe evidence
architecture. Follow-up structure–function analysis should proceed as a staged graph:
identity → structure → protein target → receptor function → tissue or animal
phenotype → exposure-relevant effect. Each edge needs its own source, assay
context, species, concentration, stereochemical scope, and uncertainty label.
This structure also makes negative results interpretable: “no join found” may
reflect representation, release coverage, or identity mismatch rather than
absence of activity.

### A pharmacology-first interpretation framework

The central unit of analysis is not the terpene name alone, but the
compound–target–endpoint tuple. For example, “linalool is sedative” is too
coarse to evaluate. A pharmacologically interpretable proposition would specify
the linalool identity and stereochemical scope, the GABA-A receptor composition,
the experimental preparation, the concentration range, the measured current or
behavioral endpoint, and whether the exposure is achievable in the relevant
organism. The same compound may have different actions at different
concentrations, receptor subtypes, metabolites, or preparations.

This tuple-based approach prevents two common errors. First, evidence for a
target is not copied across unrelated endpoints. A linalool experiment that
potentiates GABA-A current supports a receptor-function statement; it does not
by itself support anxiolysis, anticonvulsant efficacy, analgesia, or clinical
sedation. Second, evidence for one stereoisomer is not silently generalized to
another. This is particularly important for pinene and limonene labels, for
which the promotional source uses distinct names but does not consistently
provide a complete stereochemical specification.

### Evidence extraction and reproducibility

Each literature record should be extracted into a row-level evidence object
with at least the following fields: compound label as published; normalized
identity; stereochemistry; target gene or stable protein identifier; species;
cell or tissue preparation; assay type; concentration and units; exposure
route; direction of effect; comparator; antagonist or genetic control; source
identifier; and the authors’ stated limitation. A missing field is not silently
filled from a different paper. Instead, it receives an unresolved status.

The present map applies this principle at a first-pass level. It preserves
PubMed identifiers and source URLs for the receptor leads, while the linked
CSV matrix preserves the relationship between every promotional row and its
compound-level evidence tier. The data products are intentionally more granular
than the prose: readers can inspect the 109 rows, identify which rows inherit
the same compound-level paper, and distinguish a direct receptor result from an
animal antagonist experiment or an in-silico nomination.

For a subsequent systematic update, two reviewers should independently screen
title/abstract records and resolve disagreements before full-text extraction.
Searches should be rerun by compound and effect using PubMed, Europe PMC, and
the primary target or assay database where appropriate. The search date,
complete query strings, deduplication procedure, exclusion reasons, and final
included-record list should be versioned with the matrix. This would allow the
map to move from a targeted perspective to a reproducible systematic evidence
review without changing its conservative claim policy.

### Translational pharmacology and exposure

Receptor potency is necessary but not sufficient for translational plausibility.
The relevant comparison is between the free concentration at the target site
and the concentration producing the measured receptor effect, with attention to
absorption, metabolism, protein binding, tissue distribution, and volatility.
Plant or beverage composition data describe an administered matrix, not the
unbound plasma or brain concentration of an isolated terpene. Likewise, a dose
that produces a mouse behavioral effect cannot be compared directly with an
in-vitro EC50 without considering route, bioavailability, species metabolism,
and active metabolites.

The experimental plan therefore prioritizes concentration–response curves,
orthogonal receptor assays, antagonist or knockout controls, and basic
pharmacokinetic measurements. For behavioral studies, locomotor and motor
coordination controls are required so that apparent anxiolysis, sedation, or
analgesia is not explained by nonspecific impairment. For inflammatory or
antimicrobial claims, receptor assays should be supplemented by cell-based or
microbial endpoints rather than assumed to be the causal route.

### What would change a claim grade?

A claim should move from unresolved to mechanistically relevant when a
compound-specific effect is reproduced in an appropriate preparation and a
selective pharmacological or genetic intervention changes the endpoint. It
should move to direct target evidence when binding or validated functional
receptor data establish the interaction under defined conditions. It should
move to effect-supported only when the named promotional endpoint is measured
with adequate controls, identity, dose–response, and context. Replication in a
second preparation or laboratory should increase confidence, but should not
erase limitations in exposure or clinical generalizability.

This grading scheme also permits negative and mixed findings to be useful. A
failed binding assay may demote a target while leaving a non-receptor mechanism
open. Antagonist blockade may support a pathway without proving direct binding.
A positive result in a recombinant system may establish receptor capability
without showing that the compound reaches that receptor in vivo. These are not
inconsistencies; they are different edges in the evidence graph.

### 4.1 Relevance to pharmacology practice

This framework is intended for researchers, curators, and reviewers who must
decide whether a broad natural-product statement is ready to become a testable
pharmacological proposition. It makes the evidentiary bottleneck visible: the
largest gap is often not finding a possible target, but connecting a chemically
defined ligand to a reproducible endpoint under a plausible exposure. The
resulting queue can guide assay selection, replication priorities, and the
design of data systems that retain negative and unresolved results. In this
respect, the contribution is methodological and translational rather than a
claim that any one terpene is a therapeutic agent. It is aligned with a
pharmacology perspective format because it uses existing observations to
define new, falsifiable target and mechanism hypotheses while identifying the
experiments required for validation.

## 5. Limitations and next experiments

The promotional source is a secondary matrix with uneven source counts and no
assay-level definitions. The literature pass is not a systematic review, and
the current receptor map is not exhaustive. Several rows use broad compound
names whose stereochemistry, purity, or metabolite identity may differ from
the tested material. Beverage or plant-matrix concentrations cannot substitute
for unbound plasma or brain exposure.

The next release should: (1) attach every hypothesis to primary citations;
(2) resolve exact structures and stereoisomers; (3) map receptor records to
stable protein identifiers; (4) distinguish binding, functional, docking, and
phenotype evidence; and (5) test the highest-priority compound–receptor pairs
in identity-resolved assays with concentration–response measurements. The
prioritized plan below operationalizes those requirements.

### 5.1 Prioritized test plan

The machine-readable test plan is in
[`data/hypotheses-to-test.csv`](../data/hypotheses-to-test.csv). It converts
the literature leads into 14 falsifiable experiments with critical controls,
primary endpoints, and interpretation rules. Six high-priority rows test
β-caryophyllene–CB2, α-pinene–GABA-A, linalool–GABA-A, borneol–GABA-A,
α-bisabolol–α7 nAChR, and β-myrcene–TRPV1. Medium-priority rows address
α-bisabolol–GABA-A, nerolidol–TRPV1, terpineol–CB1/CB2/D2, limonene
enantiomers, and non-receptor antimicrobial/antioxidant effects. Lower-priority
rows address phytol receptor nominations and caryophyllene oxide target
discovery. The final row defines the evidence package required before any
promotional claim is promoted.

The plan uses orthogonal controls wherever possible: receptor antagonists or
knockout systems for mechanism, vehicle and positive controls for assay
validity, stereoisomer comparisons for identity, locomotor controls for animal
behavior, and concentration–response plus pharmacokinetic checks for exposure.
A positive receptor result supports only the measured molecular or phenotypic
endpoint; a null result narrows the hypothesis but does not prove biological
absence.

## 6. Conclusion

Terpedia can support a useful receptor hypothesis map for promotional terpene
claims, but it cannot yet support the promotional effects as established
biological facts. The current matrix is strongest as an auditable research
queue: it identifies where direct receptor evidence exists, where literature
adds a plausible mechanism, and where the correct conclusion remains
unresolved.

## 7. Data and code

The versioned public repository for the data products and build scripts is
https://github.com/Terpedia/claims.

Supporting Information Tables S1–S4 provide the machine-readable claims–terpene
matrix, receptor hypothesis map, prioritized hypotheses-to-test table, and
derived hypothesis register, respectively. These files are supplied with the
submission and preserve row-level provenance; they are not independent claims
of efficacy.

- [Claims–terpene matrix](../data/claims-terpene-matrix.csv)
- [Receptor hypothesis map](../data/receptor-hypothesis-map.csv)
- [Hypothesis-register builder](../scripts/build_hypothesis_register.py)
- [Matrix builder](../scripts/build_claims_terpene_matrix.py)
- [Prioritized hypotheses-to-test table](../data/hypotheses-to-test.csv)

## 8. Declarations

This perspective uses a Terpedia-curated promotional snapshot and a targeted
literature map; it is not a systematic review or a clinical guideline. No
clinical recommendation is made. Source provenance, identity decisions, and
evidence boundaries are retained in the linked machine-readable artifacts.

## 9. References

1. Gertsch J et al. Beta-caryophyllene is a dietary cannabinoid. *Proc Natl Acad Sci U S A*. 2008;105(26):9099–9104. [PMID 18574142](https://pubmed.ncbi.nlm.nih.gov/18574142/); doi:10.1073/pnas.0803601105.
2. Klauke AL et al. The CB2-selective phytocannabinoid β-caryophyllene exerts analgesic effects in mouse models. *Eur Neuropsychopharmacol*. 2014;24(4):608–620. [PMID 24210682](https://pubmed.ncbi.nlm.nih.gov/24210682/); doi:10.1016/j.euroneuro.2013.10.008.
3. Yang H et al. α-Pinene enhances non-rapid eye movement sleep in mice through GABA-A-benzodiazepine receptors. *Mol Pharmacol*. 2016;90(5):530–539. [PMID 27573669](https://pubmed.ncbi.nlm.nih.gov/27573669/); doi:10.1124/mol.116.105080.
4. Milanos S et al. Metabolic products of linalool and modulation of GABA-A receptors. *Front Chem*. 2017;5:46. [PMID 28680877](https://pubmed.ncbi.nlm.nih.gov/28680877/); doi:10.3389/fchem.2017.00046.
5. Granger RE et al. (+)- and (−)-borneol: efficacious positive modulators of GABA action at human recombinant α1β2γ2L GABA-A receptors. *Biochem Pharmacol*. 2005;69(7):1101–1111. [PMID 15763546](https://pubmed.ncbi.nlm.nih.gov/15763546/); doi:10.1016/j.bcp.2005.01.002.
6. Nurulain S et al. Inhibitory actions of bisabolol on α7-nicotinic acetylcholine receptors. *Neuroscience*. 2015;306:91–99. [PMID 26283025](https://pubmed.ncbi.nlm.nih.gov/26283025/); doi:10.1016/j.neuroscience.2015.08.019.
7. Jansen C et al. Myrcene and terpene regulation of TRPV1. *Channels (Austin)*. 2019;13(1):344–366. [PMID 31446830](https://pubmed.ncbi.nlm.nih.gov/31446830/); doi:10.1080/19336950.2019.1654347.
8. Vieira G et al. Antidepressant-like effect of terpineol in an inflammatory model of depression. *Biomolecules*. 2020;10(5):792. [PMID 32443870](https://pubmed.ncbi.nlm.nih.gov/32443870/); doi:10.3390/biom10050792.
9. Jiang J et al. (+)-Borneol alleviates mechanical hyperalgesia in mice. *Eur J Pharmacol*. 2015;757:53–58. [PMID 25835611](https://pubmed.ncbi.nlm.nih.gov/25835611/); doi:10.1016/j.ejphar.2015.03.056.
10. Cao B et al. (+)-Borneol suppresses conditioned fear recall and anxiety-like behaviors in mice. *Biochem Biophys Res Commun*. 2018;495(2):1588–1593. [PMID 29223397](https://pubmed.ncbi.nlm.nih.gov/29223397/); doi:10.1016/j.bbrc.2017.12.025.
11. Shibuya Y et al. Effects of linalool on respiratory neuron activity in a newborn-rat brainstem preparation. *Biomed Res*. 2024;45(4):151–161. [PMID 39010191](https://pubmed.ncbi.nlm.nih.gov/39010191/); doi:10.2220/biomedres.45.151.
12. Dougnon G, Ito M. Caryophyllene oxide induces sedative activity in mice. *Pharmaceuticals (Basel)*. 2021;14(7):651. [PMID 34358077](https://pubmed.ncbi.nlm.nih.gov/34358077/); doi:10.3390/ph14070651.
13. El-Hammadi MM et al. Nanoparticles enhance effects of cannabis-based terpenes on calcium influx in TRPV1-expressing cells. *Int J Pharm*. 2022;616:121524. [PMID 35104595](https://pubmed.ncbi.nlm.nih.gov/35104595/); doi:10.1016/j.ijpharm.2022.121524.
