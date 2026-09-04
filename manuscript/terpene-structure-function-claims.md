# Terpene effect claims: an evidence-bounded receptor hypothesis map

**Working manuscript — 4 September 2026**

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

## Introduction

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

## Materials and methods

### Promotional hypothesis source

We used the Terpedia Google Sheet snapshot dated 26 June 2026. Its matrix
contains effect labels in rows, terpene labels in columns, source counts, and
“x” marks indicating an association. We converted each marked cell into a
unique hypothesis identified by a stable local ID. The resulting register has
109 marked compound–effect rows across 16 compounds. The source header contains
17 named compounds, but l-limonene has no marked cells and therefore contributes
no hypothesis row.

### Identity and evidence policy

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

### Terpedia crosswalk

The local Terpedia evidence layer was checked against the receptor interactome
and available protein/structure projections. A local receptor-evidence link
means that a compound–protein association exists in the current Terpedia
evidence set; it does not mean that the promotional effect is validated. The
literature pass was targeted and hypothesis-generating, not a registered
systematic review, so absence from this map is not evidence of absence from
PubMed or biology.

### Support definitions

We reserve “supported effect” for an identity-resolved study that measures the
specific effect, identifies an appropriate biological context, and provides an
evidence chain adequate to the scope of the claim. A receptor mechanism alone
is “mechanistically relevant,” not “effect supported.” The unit of the 59/109
and 14/109 summaries is a hypothesis row, so the same compound-level paper can
appear in multiple effect rows and must not be interpreted as independent
replication.

## Results

### Overall support profile

Of the 109 hypothesis rows, 59 were attached to compounds with direct receptor
pharmacology somewhere in the literature map, and 14 rows had indirect
mechanistic or computational support. Seven rows had an existing local
Terpedia receptor link.
All 109 retained an `effect_support_status` of `unresolved`, because the map
does not yet connect each effect label to an identity-resolved, appropriately
scoped assay or clinical outcome.

### Stronger receptor-mechanism leads

β-caryophyllene is the clearest immune and nociceptive lead. It has reported
binding and functional agonism at CB2, and CB2-dependent analgesic effects have
been reported in mouse models. These results support a testable CB2-mediated
mechanism; they do not validate every anti-inflammatory, analgesic, or
neuroprotective label in the promotional matrix.

α-pinene, linalool, and borneol provide convergent GABA-A hypotheses, but with
different identities, receptor contexts, and exposure questions. α-pinene was
reported to potentiate GABA-A-mediated synaptic responses in brain slices and
to show flumazenil-sensitive effects in a mouse sleep model; the proposed
benzodiazepine-site interaction was supported by molecular modeling rather
than a direct biophysical binding assay. Linalool enhanced GABA-A currents in
recombinant systems, and borneol modulated human recombinant α1β2γ2L GABA-A
receptors. These findings make sedation, anxiety, and nociception useful
follow-up domains, not established human effects.

α-bisabolol supports two distinct lines of inquiry: direct inhibition of the
α7 nicotinic acetylcholine receptor and antagonist-sensitive behavioral
evidence implicating GABA-A signaling. These should not be merged into a
single mechanism without experiments that discriminate them.

Myrcene and nerolidol are plausible TRPV1 leads from heterologous human-TRPV1
expression experiments, not native human pain studies. The related nanoparticle
literature is formulation-specific and cannot be read as proof of free-terpene
pharmacology. Terpineol
is a weaker CB1/CB2/D2 hypothesis because its current support comes from mouse
antagonist experiments and docking rather than direct receptor binding.

### Unresolved and misleading target categories

Several compounds remain without compound-specific human receptor evidence in
this first pass, including d-limonene, l-limonene, fenchol, and terpinolene.
Humulene has plausible immune and nociceptive target families but no resolved
target in the present map. Caryophyllene oxide has a reported mouse sedative
phenotype, while one study did not support a GABA-A potentiation mechanism;
the target therefore remains unresolved.

Insect odorant-receptor findings for ocimene and caryophyllene oxide are valid
sensory biology but are not evidence for human therapeutic receptor targets.
Similarly, a docking score or a network-pharmacology edge is a prioritization
signal, not a demonstrated interaction.

## Discussion

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

## Limitations and next experiments

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
in identity-resolved assays with concentration–response measurements.

### Prioritized test plan

The machine-readable test plan is in
[`data/hypotheses-to-test.csv`](../data/hypotheses-to-test.csv). It converts
the literature leads into falsifiable experiments with critical controls and
interpretation rules. The highest-priority tests are β-caryophyllene–CB2,
α-pinene–GABA-A, linalool–GABA-A, borneol–GABA-A, α-bisabolol–α7 nAChR, and
β-myrcene–TRPV1. The table also includes non-receptor antimicrobial and
antioxidant tests, because not every promotional effect should be forced into
a receptor mechanism.

## Conclusion

Terpedia can support a useful receptor hypothesis map for promotional terpene
claims, but it cannot yet support the promotional effects as established
biological facts. The current matrix is strongest as an auditable research
queue: it identifies where direct receptor evidence exists, where literature
adds a plausible mechanism, and where the correct conclusion remains
unresolved.

## Data and code

- [Claims–terpene matrix](../data/claims-terpene-matrix.csv)
- [Receptor hypothesis map](../data/receptor-hypothesis-map.csv)
- [Hypothesis-register builder](../scripts/build_hypothesis_register.py)
- [Matrix builder](../scripts/build_claims_terpene_matrix.py)
- [Prioritized hypotheses-to-test table](../data/hypotheses-to-test.csv)

## Selected references

1. β-caryophyllene as a CB2 ligand and functional agonist: [PMID 18574142](https://pubmed.ncbi.nlm.nih.gov/18574142/).
2. CB2-dependent β-caryophyllene analgesia in mice: [PMID 24210682](https://pubmed.ncbi.nlm.nih.gov/24210682/).
3. α-pinene and GABA-A benzodiazepine-site modulation: [PMID 27573669](https://pubmed.ncbi.nlm.nih.gov/27573669/).
4. Linalool and GABA-A receptor modulation: [PMID 28680877](https://pubmed.ncbi.nlm.nih.gov/28680877/).
5. Borneol modulation of human recombinant GABA-A receptors: [PMID 15763546](https://pubmed.ncbi.nlm.nih.gov/15763546/).
6. α-bisabolol inhibition of α7 nicotinic receptors: [PMID 26283025](https://pubmed.ncbi.nlm.nih.gov/26283025/).
7. Myrcene and nerolidol regulation of TRPV1: [PMID 31446830](https://pubmed.ncbi.nlm.nih.gov/31446830/).
8. Terpineol cannabinoid/dopamine mechanism study: [PMID 32443870](https://pubmed.ncbi.nlm.nih.gov/32443870/).
