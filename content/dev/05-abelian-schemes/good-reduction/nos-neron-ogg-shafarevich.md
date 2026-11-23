---
id: nos-neron-ogg-shafarevich
title: Proof of the criterion of Néron, Ogg and Shafarevich
kind: theorem
decl: UpperTheory.Lit.Nos.Nos.neronOggShafarevich
module: Development.AutomorphicArithmetic.ThetaCorrespondence.GoodReduction.NeronOggShafarevich
covers: 353
status: drafted
drafted_by: writer@claude
---
This theorem proves the criterion of Néron, Ogg and Shafarevich for an [[abelian variety|R7W03TXRS9]] over the fraction field of a discrete valuation ring. Its second name, [`UpperTheory.Lit.neronOggShafarevich`](/entry/lit-neron-ogg-shafarevich/), passes it to [the theorems of Serre and Tate on good reduction](/entry/serre-tate-good-reduction/). The proof assembles five implications; the hard one is [good reduction from infinitely many unramified torsion levels](/entry/has-good-reduction-of-infinite-torsion-unramified/).

## Statement

Let $R$ be a discrete valuation ring with perfect residue field $k$ and fraction field $K$. Let $\Omega$ be a separable closure of $K$ and $I$ the inertia group of a valuation ring $V$ of $\Omega$ above $R$. Let $A$ be an abelian variety over $K$. Then these are equivalent:

1. $A$ has good reduction over $R$;
2. $I$ fixes $A[m](\Omega)$ for each $m$ with $m \neq 0$ in $k$;
3. $I$ fixes $A[m](\Omega)$ for infinitely many $m$ with $m \neq 0$ in $k$;
4. $I$ acts trivially on the [[Tate module|4CSMQFTGD8]] $T_\ell(A)$ for some prime $\ell$ with $\ell \neq 0$ in $k$.

The terms are defined in [the entry for the Serre-Tate theorems](/entry/serre-tate-good-reduction/). This is Theorem 1 of Serre and Tate (Good reduction of abelian varieties, Ann. of Math. 88, 1968).

## Proof

Each of five arrows is one lemma, and `tfae_finish` closes the cycle.

- $1 \Rightarrow 2$ is `torsionUnramified_of_hasGoodReduction_alt`.
- $2 \Rightarrow 4$ and $2 \Rightarrow 3$ are the two halves of `torsionUnramified_imp_tateModule_and_infinite`. From 2, pick a prime $\ell \neq 0$ in $k$; each level $A[\ell^n]$ is fixed, so $T_\ell(A)$ is fixed. The set of $m$ with $m \neq 0$ in $k$ is infinite, which gives 3.
- $4 \Rightarrow 3$ is `infinite_torsionUnramified_of_tateModuleUnramified`. If $I$ fixes $T_\ell(A)$, it fixes each $A[\ell^n]$, and the $\ell^n$ form an infinite set.
- $3 \Rightarrow 1$ is [`hasGoodReduction_of_infinite_torsionUnramified`](/entry/has-good-reduction-of-infinite-torsion-unramified/). This is the step with real content.

## In the Lean code

The theorem is at [line 22 of NeronOggShafarevich.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/NeronOggShafarevich.lean#L22). The first three lemmas are in the namespace `GlobalTheory.T`, in files named `TorsionUnramifiedOfHasGoodReductionStatement.lean`, `TorsionUnramifiedImpTateModuleAndInfiniteStatement.lean` and `InfiniteTorsionUnramifiedOfTateModuleUnramifiedStatement.lean` in `Development/AbelianVarietyTheory/Proofs/DivisorProofs/`. We read their statements, not their proofs; the sketches above for $2 \Rightarrow 4$, $2 \Rightarrow 3$ and $4 \Rightarrow 3$ are the standard arguments, not a reading of the Lean proofs.

Two of the lemmas have weaker hypotheses than the theorem. `torsionUnramified_of_hasGoodReduction_alt` does not assume that $A$ is an abelian variety, since good reduction already gives an abelian scheme. `torsionUnramified_imp_tateModule_and_infinite` assumes neither that $A$ is an abelian variety nor that $V$ lies above $R$. The hypothesis that $k$ is perfect appears only in the lemmas for $4 \Rightarrow 3$ and $3 \Rightarrow 1$.
