---
id: cut-closed-main
title: Cutting a vertical divisor by an effective divisor
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CutClosed.main
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.CutEffectiveDivisor
covers: 458
status: drafted
drafted_by: writer@claude
---
This theorem proves `CutByEffectiveDivisor.Statement`, an identity of intersection numbers on a model over a discrete valuation ring. Its statement form is [`cut_effective_divisor`](/entry/cut-effective-divisor/). The proof reduces to an effective vertical divisor, then argues by induction on the common vertical components, with a blow-up in the induction step.

## Statement

Let $O$ be a discrete valuation ring with a uniformizer $\varpi$. Let $A = O[x_{k,i}]$ be a polynomial ring with one block of variables for each $k$ in a finite set $K$, graded by multidegree in $\mathbb{N}^K$. All primes below are multihomogeneous and relevant: no block of variables lies in them.

- A *model* of dimension $e$ is a prime $P$ with $P \cap O = 0$ and $\dim A/P = e + 1 + |K|$ (`IsModelOver`).
- For $h \notin P$, $\operatorname{div}_P(h)$ is the cycle that gives each minimal prime $W$ of $P + (h)$ the length of $(A/(P + (h)))_W$. For $f, g \notin P$, $\operatorname{div}_P(f/g) = \operatorname{div}_P(f) - \operatorname{div}_P(g)$.
- For a prime $W$ and degrees $a_1, \dots, a_n \in \mathbb{Z}^K$, $v(W; a_1, \dots, a_n)$ is the eventual value of the mixed differences, in the directions $a_i$, of the Hilbert function of the special fibre of $W$ (`vNum`).
- $f/g$ is a *vertical divisor of degree $b$* on $P$ if $f, g \notin P$ are multihomogeneous with degree difference $b$, every component of $\operatorname{div}_P(f/g)$ contains $\varpi$, and $f/g$ is a unit in $A/P$ at every prime that does not contain $\varpi$.

**Theorem.** Let $P$ be a model of dimension $d + 1$, $f/g$ a vertical divisor of degree $b$ on $P$, and $s \notin P$ multihomogeneous of degree $c$. Assume that $f/g$ is a vertical divisor on each component $H$ of $\operatorname{div}_P(s)$ with $\varpi \notin H$. Then for each $L = (a_1, \dots, a_d)$,

$$\sum_G \operatorname{ord}_G(f/g)\, v(G; c, L) = \sum_{W \ni \varpi} \operatorname{ord}_W(s)\, v(W; b, L) + \sum_{W \not\ni \varpi} \operatorname{ord}_W(s) \sum_G \operatorname{ord}^W_G(f/g)\, v(G; L).$$

Here $\operatorname{ord}^W_G(f/g)$ is the multiplicity of $G$ in $\operatorname{div}_W(f/g)$. The identity has the shape of the commutativity of intersection with divisors (Fulton, *Intersection Theory*, Theorem 2.4). We have not checked the match in detail.

## Proof

1. `EffectiveShift`: for some $n$, $\varpi^n f / g$ is *effective*, that is, regular at every relevant prime above $P$.
2. The identity for $\varpi^n f/g$ (`EffectiveCase`) is proved by strong induction on the common excess, the largest product $\operatorname{ord}_G(s) \operatorname{ord}_G(f/g)$ over primes $G \ni \varpi$. If no vertical component is common to both divisors, `NoCommonComponentCase` applies. It is `NumbersDVR_C3NoCommon`. Otherwise `CommonFactorInduction.of_open` blows up the model, gets a new model with smaller excess, and moves the identity back. Its inputs are seven blow-up lemmas: the Rees algebra, the strict transform, the drop of the excess, two push forwards, and two lemmas on horizontal components.
3. `UniformiserCase` is the identity for the divisor $\varpi/1$.
4. `ShiftByUniformiser` gets the identity for $f/g$ from those for $\varpi^n f/g$ and $\varpi/1$.

## In the Lean code

The theorem is in [CutEffectiveDivisor.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/CutEffectiveDivisor.lean#L25). The definitions are in [Objects.lean](lean:GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/Objects.lean#L106) and the statement in [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/Statements.lean#L27). The induction of step 2 is `EffectiveCase.proof` in [ImportsAlt.lean](lean:GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/ImportsAlt.lean#L12). The local lemma `verticalPush` (line 19) builds the push forward of vertical cycles from the blow-up model, a fibre degree lemma, `blow_up_fibre_semilocal` and `projection_formula_degree`. We have not opened the proofs of the lemmas named in steps 1, 3 and 4. In step 2 the induction hypothesis covers models with any block set and any dimension, not only $P$ and $d$.
