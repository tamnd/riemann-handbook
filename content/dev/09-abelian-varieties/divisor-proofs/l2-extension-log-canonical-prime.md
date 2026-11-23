---
id: l2-extension-log-canonical-prime
title: L2 extension from the common zeros of n sections
kind: theorem
decl: GlobalTheory.l2ExtensionLogCanonical'
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.L2ExtensionLogCanonical
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{L2ExtensionLogCanonical}$, an $L^2$ extension theorem for sections of $K_Y + E$ from a finite set of points on a compact complex manifold $Y$. Its only caller is [the literature form of the statement](/entry/l2-extension-log-canonical-of-literature/), which fills the field `q8` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/). The proof joins two lemmas.

## Statement

The setting is the structure `WeightedAtlas n Y ι La`. Here $Y$ is a compact Hausdorff space with a holomorphic atlas of charts to $\mathbb{C}^n$. $La$ is an additive group of line bundles, each given by a holomorphic cocycle $g$ and smooth local weights $\phi$ with $\phi_j = \phi_i - \log \lvert g_{ij} \rvert^2$, so that $\lvert s \rvert^2 = \lvert s_i \rvert^2 e^{-\phi_i}$. A special element $\kappa$ has the Jacobian determinant of the chart changes as its cocycle, so its sections are $n$-forms, and $\mu$ is a measure with density $e^{\phi_\kappa}$ in each chart.

**Theorem.** Let $n \ge 1$, and suppose that some $H \in La$ has a weight with positive definite Levi form in each chart. Let $E, L \in La$ and let $s = (s_1, \dots, s_n)$ be holomorphic sections of $L$ such that:

1. the common zero set $S$ of the $s_k$ is finite;
2. at each $P \in S$, the Jacobian $J(P)$ of $(s_1, \dots, s_n)$ in the chart at $P$ is nonzero;
3. $\lvert s \rvert^2 = \sum_k \lvert s_k \rvert^2 \le 1$ on $Y$.

Put $\psi = n \log \lvert s \rvert^2$, so $\psi \le 0$. Let $\delta > 0$, and suppose that $\phi_E + \alpha \psi$ has nonnegative Levi form off $S$ for each $\alpha \in [1, 1 + \delta]$. Then for each function $f$ on $Y$ there is a holomorphic section $F$ of $\kappa + E$ with $F(P) = f(P)$ at each $P \in S$, in the chart at $P$, and

$$\int_Y \frac{2^n}{1 + \delta^2 \psi^2}\, \lvert F \rvert^2 e^{-\psi}\, d\mu \le \frac{34}{\delta}\, c_n \sum_{P \in S} \frac{\lvert f(P) \rvert^2}{\lvert J(P) \rvert^2}\, e^{-\phi_E(P) + n \phi_L(P)}, \qquad c_n = \frac{2^{n+1} \pi^n}{(n-1)!}.$$

This has the form of an $L^2$ extension theorem of the type of Ohsawa and Takegoshi (Math. Z. 195, 1987), from the finite set $S$ where $s$ vanishes, with the weight $1/(1 + \delta^2\psi^2)$. We have not matched the statement, or the constant $34/\delta$, to a numbered theorem in a source.

## Proof

1. `T.exists_etale_frame_off_finite_zeroSet` uses the positive bundle $H$ and the finite zero set. It gives a line bundle $\Lambda$ with a semipositive weight and a section $\tau$, such that the set $U$ where $\tau \neq 0$ is dense and $\lvert \tau \rvert^2 \le C \lvert s \rvert^2$ for some $C > 0$. It also gives a map $z \colon Y \to \mathbb{C}^n$ that is holomorphic with nonzero Jacobian on $U$ (`Etale`), and a frame $\beta$ of $\kappa + E$ on $U$.
2. `T.l2_extension_etale_coordinates_finite_zeros` takes these data and all the other hypotheses, and gives $F$ with the bound.

## In the Lean code

The theorem is in [L2ExtensionLogCanonical.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/L2ExtensionLogCanonical.lean#L13). The statement is in [L2ExtensionLogCanonical.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/L2ExtensionLogCanonical.lean#L32), and `WeightedAtlas` is in [FamilyLeCoords.lean](lean:ReciprocityTheory/L2DbarEstimates/PlurisubharmonicCharts/FamilyLeCoords.lean#L14). The lemmas:

- `exists_etale_frame_of_finite_zeroSet` in [ExistsEtaleFrameOffFiniteZeroSet.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsEtaleFrameOffFiniteZeroSet.lean#L20);
- `l2_extension_of_etale_coordinates` in [L2ExtensionEtaleCoordinatesFiniteZeros.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/L2ExtensionEtaleCoordinatesFiniteZeros.lean#L68).

The `T.` names are `first | exact ...` restatements of these. We have not opened their proofs. `Etale` and `nz` are in [EtaleEmpty.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EtaleEmpty.lean#L20). The positivity of $H$ is used only in step 1. On $S$ the Lean value of $\psi$ is $0$ (since `Real.log 0 = 0`); as $S$ is finite, the integral does not change.
