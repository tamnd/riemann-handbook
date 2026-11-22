---
id: join-out-of-literature
title: JoinOut from five results on complex multiplication and zeta values
kind: theorem
decl: UpperTheory.LiteratureTheorems.join_out_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 1604
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `JoinOut` by one call to [`joinOut_of_five`](/entry/join-out-of-five/), with five leaf results as inputs. It is the field `join` of the [non-endoscopic bundle](/entry/literature-nonexistence/). The real content is in [`joinOut_of_five`](/entry/join-out-of-five/), which holds 1,598 of the 1,604 declarations below this theorem.

## Statement

Let $O$ be a proof of [OpenLiteratureStatements](/step/open-literature-statements-def/). Then `JoinOut` holds. `JoinOut` is the conjunction of five statements. By their definitions, which we read but did not unfold to the end:

1. `ToricDenominator`: for an abelian CM field $E$, there are rational values $z$ on the class group of $E$, with the property `IsClassZetaVals` at $2s$ (not unfolded), that bound from below the $\ell$-adic valuations of certain toric sums attached to Hecke characters of $E$, for each prime $\ell$.
2. `Transport`: for an imaginary quadratic field $K$ of discriminant $-d$ with $d > 4$, each $\sigma \in \operatorname{Aut}(\mathbb{C})$ that fixes $K$ moves $j(\Lambda_K)$ to $j(\Lambda_\sigma)$ for a lattice $\Lambda_\sigma$ of an ideal given by an idele; ratios of toric sums over CM fields $E \supset K$ are algebraic, and $\sigma$ acts on them by an explicit factor.
3. `TwistedTransport`: there is a period $\Omega_0 \neq 0$ such that twisted toric sums, divided by a power of $\Omega_0$, are algebraic.
4. `ZetaDenominators`: for a CM field $E$ and $s \geq 1$, the partial zeta values of the maximal real subfield at $2s$ have bounded denominators.
5. `Refl`: a reflection identity $\Lambda(s)\Lambda_0(1-s) = u\,\Lambda(1-s)\Lambda_0(s)$ for two Hecke L-functions at integers $s \leq 0$ in a range, with $u$ a unit away from a given modulus.

## Proof

The proof is

```
joinOut_of_five (ellipticMainTheoremCM' O) (hilbertClassFieldJ' O)
  (siegel_klingen_deligne_ribet_of_literature O)
  (partial_zeta_functional_equation_of_literature O) (heckeTateFunctionalEquation' O)
```

The five inputs are, by their statements: the main theorem of [[complex multiplication|D3HEJTVY7G]] for elliptic curves (Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, 1971, Theorem 5.4); the fact that $K(j(\mathcal{O}_K))$ is the [[Hilbert class field|WWCJ7CR2R3]] of $K$ (Cox, *Primes of the form $x^2 + ny^2$*, Theorem 11.1), with more facts on $j$-invariants; the rationality of partial zeta values of a totally real field at $1 - k$ (Siegel, Nachr. Akad. Wiss. Göttingen 1970) with the congruences of Deligne and Ribet (Invent. Math. 59, 1980); the functional equation of partial zeta functions of a totally real field; and the Hecke-Tate functional equation. Each input is one line that cites a theorem of another file. None reads $O$.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L233). `JoinOut` is at [HypothesisBundleConversions.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HypothesisBundleConversions.lean#L7). `joinOut_of_five` is at [JoinOutOfFive.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/JoinOutOfFive.lean#L15).

- The argument $O$ is not used.
- The name "join out" says nothing about the content. The five conjuncts are results on CM periods and zeta denominators.
