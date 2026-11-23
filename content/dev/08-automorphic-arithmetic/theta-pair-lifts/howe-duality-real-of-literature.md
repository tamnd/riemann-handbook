---
id: howe-duality-real-of-literature
title: Howe duality at the real places for the trivial representation, from the literature
kind: theorem
decl: UpperTheory.LiteratureTheorems.howe_duality_real_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 434
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It takes the argument $O$ of type [OpenLiteratureStatements](/step/open-literature-statements-def/), ignores it, and returns the theorem [`howeDualityReal_holds`](/entry/howe-duality-real-holds/), which has the real content (433 of the 434 declarations below this one). Its result fills the field `howeDualityReal` of the bundle [ThetaLocalInputs](/step/published-results-first/).

## Statement

Let $E/F$ be a CM extension. Let $X$ be an $n$-dimensional space over $E$ with a nondegenerate Hermitian matrix, and $W$ a $d$-dimensional space with a nondegenerate skew-Hermitian matrix. Let $\omega$ be a [[Weil representation|CD20HVR9V8]] of $U(X) \times U(W)$ for a standard character $\psi$ and splitting characters $\chi_X$, $\chi_W$. Fix an embedding at each infinite place, and Cartan involutions for $X$ and for $iW$, with maximal compact subgroups $K_X$ and $K_W$.

Let $\mathrm{Pol}$ be the space of Schwartz functions at the infinite places that the Gaussians span under the Heisenberg derivatives. Call a subspace $N$ admissible when:

1. $N \subseteq \mathrm{Pol}$;
2. $N$ contains $Y f$ and $(k - 1) f$ for each $f \in \mathrm{Pol}$, each derivative $Y$ along a one-parameter subgroup of $U(X)_\infty$, and each $k \in K_X$;
3. $N$ is stable under the derivatives of $U(W)_\infty$ and under $K_W$.

So $\mathrm{Pol}/N$ is a quotient of the $U(X)$-coinvariants of $\mathrm{Pol}$, with an action of $U(W)$. The conclusion has two parts:

1. strictly increasing chains of admissible subspaces have bounded length;
2. the sum of two proper admissible subspaces is proper.

So the coinvariants have finite length and a unique irreducible quotient. This has the form of the [[theta correspondence|ZBGT50BW0Z]] for the trivial representation of $U(X)$ at the real places, as in Howe (J. Amer. Math. Soc. 2, 1989).

## Proof

The proof is `GlobalTheory.howeDualityReal_holds`, with no change.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L437). The statement `HoweDualityReal` is at [HoweDualityReal.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/HoweDualityReal.lean#L21), and the condition `ThetaSubInf` is at [line 9](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/HoweDualityReal.lean#L9).

- The argument $O$ is not used.
- The proof at [HoweDualityRealHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HoweDualityRealHolds.lean#L18) does not use the four hypotheses `ResEtaPow` and `IsHecke` on $\chi_X$ and $\chi_W$.
- That proof moves $\mathrm{Pol}$ to a tensor product of Fock spaces and calls `GlobalTheory.T.howe_duality_characters_fock_tensor_product`. I have not unfolded that lemma.
