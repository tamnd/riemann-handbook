---
id: has-type-all-of-closure
title: Limits of discrete series coefficients are coefficient series
kind: theorem
decl: GlobalTheory.ClosureSeries.hasTypeAll_of_closure
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.HasAllKTypesOfClosureDiscreteSeriesCoefficients
covers: 560
status: drafted
drafted_by: writer@claude
---
This theorem says that a function on $U(p,q)$ that is a locally uniform limit of [[matrix coefficients|J85Q7QGGHS]] of a discrete series $\sigma$ is an absolutely convergent series of such coefficients. It reduces the claim to the $K$-projections of the function and proves it for each projection. The result reaches [`closure_model`](/entry/closure-model/) through the second name [`hasAllKTypes_of_closure_discreteSeriesCoefficients`](/entry/has-all-ktypes-of-closure-discrete-series-coefficients/).

## Statement

Let $J = \operatorname{diag}(\pm 1)$ with signs $\varepsilon \in \{\text{true}, \text{false}\}^n$, $G = \{g : g^* J g = J\} = U(p,q)$, $\mathfrak{g} = \{X : X^* J + J X = 0\}$, and $K = G \cap U(n)$ with Haar probability measure $dk$. Let $\sigma$ act unitarily on $\mathcal{H}$, with $d\sigma(X) w = \frac{d}{dt}\sigma(e^{tX}) w \big|_{t=0}$. For a finite list $S$ of words in $\mathfrak{g}$ put $\lVert w \rVert_S = \sum_{(X_1, \dots, X_m) \in S} \lVert d\sigma(X_1) \cdots d\sigma(X_m) w \rVert$.

- $w$ is *smooth* if $(t_i) \mapsto \sigma(e^{t_1 X_1} \cdots e^{t_k X_k}) w$ is $C^\infty$ for all $X_i \in \mathfrak{g}$.
- $\ell$ is *Sobolev* if $\lvert \ell(w) \rvert \leq C \lVert w \rVert_S$ on smooth $w$ for some $C$ and $S$.
- $f$ is `UMG` if there are $N$ and functions $F_l$, one for each word $l$, with $F_\emptyset = f$ on $G$, $F_{X l}(g) = \frac{d}{dt} F_l(g e^{tX}) \big|_{t=0}$, and $\lvert F_l(g) \rvert \leq C_l (1 + \sum_{a,b} \lvert g_{ab} \rvert^2)^N$.
- `HasTypeAll` $(\sigma, f)$: there are $S$, a continuous $B$ with $\lVert \sigma(g) w \rVert_S \leq B(g) \lVert w \rVert_S$, smooth $v_i$, linear $\ell_i$ and $C_i \geq 0$ with $\lvert \ell_i(w) \rvert \leq C_i \lVert w \rVert_S$, $\sum_i C_i \lVert v_i \rVert_{S'} < \infty$ for every $S'$, and $f(g) = \sum_i \ell_i(\sigma(g) v_i)$ on $G$.

**Theorem.** Assume `HarishChandraModules` and `CasselmanWallach`. Let $\sigma$ be a [[discrete series|9AB7HYGPEK]] with Harish-Chandra parameter $\lambda$ (`IsDS`), and $f$ continuous on $G$ and `UMG`. Suppose that for each compact $C$ and $\delta > 0$ there are Sobolev $\ell_j$ and smooth $v_j$, finitely many, with $\lvert f(y) - \sum_j \ell_j(\sigma(y) v_j) \rvert < \delta$ on $C \cap G$. Then `HasTypeAll` $(\sigma, f)$.

`CasselmanWallach` is the globalization theorem: a $(\mathfrak{g}, K)$-map from the $K$-finite vectors into a smooth Fréchet representation of moderate growth extends uniquely to the smooth vectors (W. Casselman, Canad. J. Math. 41, 1989; N. Wallach, *Real Reductive Groups II*, Chapter 11).

## Proof

1. `std_of_isDS` turns `IsDS` into `Std`: $\sigma$ is unitary and irreducible, its $K$-finite vectors are smooth, it has a formal degree and a nonzero $K$-finite vector.
2. By [`discreteSeriesCoeffSeries_of_kTypeProjections`](/entry/discrete-series-coeff-series-of-k-type-projections/) it is enough to show this: for each continuous $K$-finite $e$ on $K$, the projection $f_e(y) = \int_K e(k) f(yk)\, dk$ equals a finite sum $\sum_a L_a(\sigma(y) w_a)$ on $G$, with $L_a$ Sobolev and $w_a$ $K$-finite.
3. `compactAverage_continuousOn_uniformModerateGrowth`: $f_e$ is continuous and `UMG`.
4. `kProjection_limit_discreteSeriesCoeffs`: there are fixed $K$-finite $w_1, \dots, w_d$ such that $f_e$ is a locally uniform limit of sums $\sum_a L_a(\sigma(y) w_a)$. Only the $L_a$ change with $C$ and $\delta$.
5. `eq_matrixCoeff_of_locallyUniform_limit_kFinite`, which uses both literature statements: such a limit is itself of that form.

## In the Lean code

The theorem is in [HasAllKTypesOfClosureDiscreteSeriesCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/HasAllKTypesOfClosureDiscreteSeriesCoefficients.lean#L23). `HasTypeAll` is in [HasTypeAllAddOfEquiv.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HasTypeAllAddOfEquiv.lean#L28). `UMG`, `Std` and `std_of_isDS` are in [NormDwLeSobNorm.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/NormDwLeSobNorm.lean#L48). We have not opened the proofs of the lemmas of steps 3 to 5.

The conclusion uses `lieOf (Jm ε)` and `UH (Jm ε)`. These are $\mathfrak{g}$ and $G$ by definition, so step 2 needs no rewriting. The hypothesis `IsHCParam lam` is introduced as `_` and never used.
