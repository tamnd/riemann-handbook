---
id: ker-ent-hyp-true
title: The four kernel entry conditions for true column choices
kind: theorem
decl: GlobalTheory.Mem.Col2.TC.kerEntHyp_true
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.KernelEntryHypOfTrueColumnChoices
covers: 402
status: drafted
drafted_by: writer@claude
---
This theorem proves `KerEntHyp`, the four conditions that the explicit kernel entry datum `kerEntC` needs. Its copy [`kernelEntryHyp_of_trueColumnChoices`](/entry/kernel-entry-hyp-of-true-column-choices/) is called by [`kerEntC_true`](/entry/ker-ent-c-true/). The proof only collects four lemmas, one for each condition.

## Statement

Let $I$ be true column choices with `I.Ok` and the pins, and let $D$ be the datum `I.rec7 l Z`, with coefficient field $L$ and $m$ levels. Let $Y$ be a divisor datum, $O$ a family of lift objects, `Pl` a choice of embeddings $\iota_w \colon L \to \mathbb{C}_p$ for each place $w$, and `Bs` a family of matrices $B$ over $\mathbb{C}_p$.

**Theorem.** Assume that the primes of $Y$ are those of $I$, that $O$ is standard and unfolded below level $m$, that the jets of $I$ lie in the right space, that each $B$ is a basis matrix of the matching lattice of $O$ (`BasOk`), and that at level free places each entry of $B$ is some $\iota_w(x)$ with $x \in L$. Then `KerEntHyp` holds: at each level free place $w$ and level $i < m$,

1. `val`: each target projection has the norm of some $\iota_w(b)$;
2. `latS`: a function on the classes at level $i$ comes from the local lattice at $w$ if and only if it is in the forms space and each class has a representative with all source projections of norm at most 1;
3. `latT`: the same at level $i+1$, with target projections;
4. `kform`: on a pair related by the kernel map, each target projection is the factor `unC` times a source projection taken at a polynomial built from `thAtW`.

A source projection evaluates a lifted polynomial at $B$ with a determinant twist and reads it in a dual basis. A target projection does the same at level $i+1$, then evaluates on minors. A place is level free when its residue characteristic avoids the prime of the word, two fixed primes and the primes of $Y$.

## Proof

Each field comes from one lemma, applied to all eight hypotheses: `targetPairing_sizes_in_coefficientField_valueGroup`, `trueChains_kernelDatum_sourceSideLattice`, `kernelDatum_lattice_target_side_trueChains` and `kernelEntries_form_true_chains`. These are copies of `KerVal.prTC_val`, `KerLatS.kerEntHyp_latS`, `TC.kerEnt_latT` and `TC.kerEnt_kform_true`.

## In the Lean code

The theorem is in [KernelEntryHypOfTrueColumnChoices.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/KernelEntryHypOfTrueColumnChoices.lean#L19). `KerEntHyp` is in [KerEntHyp.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData/KerEntHyp.lean#L149), `BasR` in [GL3Columns.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GL3Columns.lean#L521), `LevFree` in [DataKerI.lean](lean:Formalism/LocalRingCardinality/DataKerI.lean#L65). We have not opened the four lemmas, or unfolded `rhoOf` and `thAtW`.

The factor `unC` ([line 127](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData/KerEntHyp.lean#L127)) is a product `unF` of values and determinant powers, but it is set to 1 when `unF` is 0. So it is never 0 by definition.
