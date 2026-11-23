---
id: geo-bound-of-quoted-prime
title: The geometric Hilbert-Samuel bound from the quoted theorems
kind: theorem
decl: GlobalTheory.HSShort.geoBound_of_quoted'
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArithmeticHilbertSamuelBound
covers: 686
status: drafted
drafted_by: writer@claude
---
This theorem derives the bound `GeoBound` from the quoted theorems `Quoted`. Its proof is one application of an abstract lemma to four inputs. It has a second name, [arithmeticHilbertSamuelBound](/entry/arithmetic-hilbert-samuel-bound/). Below this theorem are 686 declarations.

## Statement

The hermitian data $X$ (`Data F`) over a number field $F$ has a smooth projective variety $Y$ of dimension $D$, a line bundle $L$ with sections, $n$ generators, hermitian frames, a constant $\Lambda$ (`abelian₂`), the top self-intersection $\delta$ of $L$ (`del`), a level $T \ge D + 1$, lattices $M_j$ of sections with hermitian norms, and constants $\beta$, $\Lambda_D$, $\Lambda_T$. Let $d$ be the rank of $M_T$. The hypothesis `GeoHyp X Λ₀` asks that $F$ is totally complex, that $X$ is birational (`Birational`), that two bundles are nef and big, the conditions `MulStable` and `NormsLe`, a multiplication bound with $\beta$, $1 \le \Lambda$, $1 \le \Lambda_0$, and short bases of $M_0$, $M_D$, $M_T$ with norms at most $\Lambda_0$, $\Lambda_D$, $\Lambda_T$. A number $h$ is a height of $X$ (`IsHeight`) if there are $e > 0$ and a Chow form $f$ of degree $e$ of the image with $(D+1)\,e\,h$ = `formHeight` of $f$.

Put $C = 26$, $z = 1 - \binom{T-1}{D}\delta/d$, $G = (D+1)(\log n + 1)/2 + 1$ and
$$\log\rho = \log\Lambda + C\log\bigl(nD\delta(2 + \lvert h\rvert + \log\Lambda)\bigr).$$

**Theorem.** Assume `Quoted`. If `GeoHyp X Λ₀` holds and $h$ is a height of $X$, then $0 \le z \le 1$ and
$$\begin{aligned}&{(1 - z)\bigl(Th - 3(D+1)\lvert h\rvert - \log\Lambda_0 - CD^2\log(e^{\log\rho}T) - (T+D+1)\log\beta - (T+D^2)(G+2)\bigr)}\\ &{\quad - z\bigl(T\log(2e^{\log\rho}\sqrt\beta) + \log\Lambda_D + \log\Lambda_T\bigr) \le \frac{\deg M_T}{d}.}\end{aligned}$$

This is `HSClaimS` with $j_0 = 1$ and $J = \log\Lambda_0$.

## Proof

The proof is `T.explicit_arithmetic_hilbertSamuel_bound`, which has the type `Quoted → BertiniNF → HeightTie → SlopeBound → GeoBound`, applied to:

1. `Quoted` itself;
2. `T.bertiniNumberField_of_hilbertSamuel₂`, which derives `BertiniNF` from `Quoted`: a Chow form of the image has degree `del`, and off a nonzero polynomial the linear sections are simple;
3. `HeightTieProof.heightTie` applied to `HSShort.htMul`, which give `HeightTie`: a formula for the height of $c f^e$ in terms of $h$ and a harmonic number;
4. `T.slopeLowerBound_topLattice_offHypersurface`, which gives `SlopeBound`: the claim for an abstract lattice system.

`explicit_arithmetic_hilbertSamuel_bound` is proved by `HSShortTop.geoBound_of_abstract` in `ExplicitArithmeticHilbertSamuelBound.lean`. That proof builds the lattice system of $X$, applies `SlopeBound` to it, and uses `HeightTie` to pass from the Chow form to $h$.

## In the Lean code

The theorem is at [ArithmeticHilbertSamuelBound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithmeticHilbertSamuelBound.lean#L19). `GeoBound` and `GeoHyp` are in [HermSysHypOneLeLambdaZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HermSysHypOneLeLambdaZero.lean#L269), and `HSClaimS` is in [HSClaim.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/RealCubicMeans/LogMeanShares/LogMeanStatements/HSClaim.lean#L16).

- The proof here is a pure assembly. The real content is in `geoBound_of_abstract` and in `slopeLowerBound_topLattice_offHypersurface`, which have no entry in the handbook outline.
- We have not unfolded the fields of `Quoted`, `BertiniNF`, `HeightTie` or `SlopeBound` beyond their statements.
