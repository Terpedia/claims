# Receptor hypothesis research — 2026-09-04

## Finding

The promotional matrix should be treated as a set of effect hypotheses. A
receptor target is useful only as a mechanistic bridge and cannot, by itself,
support the effect label. The first literature pass produced a candidate map
for all 17 compounds in the matrix, but only a subset has compound-specific
receptor evidence.

The strongest leads are:

- β-caryophyllene → CB2/CNR2: direct binding and functional agonism were
  reported, and a separate mouse pain study found CB2-dependent analgesia.
- α-pinene → GABAA benzodiazepine-site receptor: receptor modulation was
  reported in recombinant/brain-slice experiments and linked to mouse sleep.
- linalool → GABAA receptor: positive allosteric modulation was reported in
  recombinant receptor systems, with additional rat brainstem evidence.
- borneol → GABAA receptor: both enantiomers modulated human recombinant
  α1β2γ2L GABAA receptors; animal analgesia/anxiety studies used GABAA
  antagonism as a mechanistic test.
- α-bisabolol → α7 nicotinic acetylcholine receptor: direct inhibition was
  reported; separate behavioral work implicates GABAA signaling.

Terpineol is a useful but weaker lead: antagonist experiments and docking in a
mouse inflammatory-depression model nominate CB1, CB2, and D2, without direct
ligand-receptor binding. Phytol is weaker still because the current result is
primarily computational plus preclinical.

## Important boundaries

The table contains no receptor field, and most effect labels have no
compound-specific receptor support. “Unresolved” means the current evidence
set did not establish a target; it is not evidence that the compound is
inactive. Odorant-receptor findings in insects and docking predictions are
retained as context, not promoted to human receptor evidence.

The machine-readable map is
[`data/receptor-hypothesis-map.csv`](../data/receptor-hypothesis-map.csv).
It should be joined to the generated hypothesis register by compound, then
reviewed claim-by-claim. The next pass should retrieve full text and assay
conditions, resolve stereochemistry, and compare assay concentrations with
plausible unbound exposure.
