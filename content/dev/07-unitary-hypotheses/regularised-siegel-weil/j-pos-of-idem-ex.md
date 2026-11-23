---
id: j-pos-of-idem-ex
title: A cut operator at a good place that acts on spherical sections by a scalar
kind: theorem
decl: GlobalTheory.CompanionTheory.Jp.jPos_of_idemEx
module: Development.WeilBound.RepresentationTheoryGL.RegularisedSiegelWeil.ThetaIdempotents.ThetaCoefficients.JPosOfIdemEx
covers: 378
status: drafted
drafted_by: writer@claude
---
This theorem proves `JPos`, the input of [`resCore`](/entry/res-core/) that gives a place $v$, a cut operator $C$ at $v$ and an entire function $c$ with $c(t/2) \ne 0$. In `resCore`, the $K_v$-average of $C$ multiplies the Laurent coefficients by $c(t/2)$, and this kills the coefficients of order $k \ge 2$. The theorem has the hypothesis `IdemEx`, but the proof does not use it. So it proves `JPos` outright.

## Statement

Let $G = U(n,n)(\mathbb{A}_F)$ with Siegel parabolic $P$, as in [`resCore`](/entry/res-core/), and let $n(x)$ be the unipotent element $\begin{pmatrix} 1 & x \\ 0 & 1 \end{pmatrix}$ for an adelic Hermitian matrix $x$ (`IsNMap`). A *cut* $C$ at a finite place $v$ is a finite set of Hermitian matrices $x$ supported at $v$, with complex coefficients $c_x$. It acts on functions by $(CF)(g) = \sum_x c_x F(g\, n(x))$. Say that $C$ *kills rank below $r$* if $\sum_x c_x \psi(\operatorname{tr} x\beta) = 0$ for each rational Hermitian $\beta$ of rank less than $r$ for which $\psi(\operatorname{tr} x\beta) = 1$ at all $v$-integral $x$. Let $K_v$ be the maximal compact subgroup at $v$, with Haar probability measure $\nu_v$.

**Theorem.** Let $n = r + t$ with $r \ge 1$, $\psi$ a nontrivial character of $\mathbb{A}_F / F$, $\chi$ a Hecke character with $\chi|_{\mathbb{A}_F^\times} = \eta^r$, and $S$ a finite set of places. Then there are $v \notin S$, a cut $C$ at $v$ that kills rank below $r$, and an entire $c$ with $c(t/2) \ne 0$, such that for each $z \in \mathbb{C}$ and each right $K_v$-invariant $f$ with $f(qg) = \chi(\det a_q)\,|\det a_q|^{z + n/2} f(g)$ for $q \in P$,

$$\int_{K_v} (Cf)(gk)\, d\nu_v(k) = c(z)\, f(g) \quad \text{for all } g.$$

## Proof

1. `jacquet_piatetski_bound_holds` gives a place $v \notin S$ where $\psi$ has conductor exactly the integers (`GoodPsi`), and an embedding $\tau \colon E \to F_v$, so $v$ splits in $E$. At $v$, $\chi$ is trivial on the ideles whose two components have the same absolute value (`GoodChi`).
2. `split_place_rank_cut_of_alternative`, applied to five proved statements whose names say Iwasawa decomposition, height bound, uniform boundedness, compactness and positivity, gives `SplitPlaceRankCutEigenvalue`. At $v$ it gives $C$ and $c$: $C$ kills rank below $r$, and $c(z)$ is the $K_v$-average of $C$ applied to the local spherical section of parameter $z$.
3. `section_eigenfunction_maximal_compact` moves this identity from the local spherical section to each global $f$ as above.

## In the Lean code

The theorem is in [JPosOfIdemEx.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/ThetaCoefficients/JPosOfIdemEx.lean#L19). `JPos`, `IdemEx` and `Cut` are in [WeakApproximationFinitePlace.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/SingularNullSets/WeakApproximationFinitePlace.lean#L319). `GoodPsi`, `GoodChi` and `SplitPlaceRankCutEigenvalue` are in [SectionEigenfunctionMaximalCompact.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SectionEigenfunctionMaximalCompact.lean#L20). We have not read the proofs of the three lemmas or of the five local statements.

- The first step is `intro _`: the hypothesis `IdemEx` (existence of idempotents for each finite set of places) is not used. The name says "of IdemEx", but the theorem holds without it.
- `JPos` assumes that $f$ is continuous. The proof does not use this.
- The name `jacquet_piatetski_bound_holds` suggests a bound of Jacquet and Piatetski-Shapiro, but its statement `GoodPlacesOutsideFiniteSet` only gives a good place.
