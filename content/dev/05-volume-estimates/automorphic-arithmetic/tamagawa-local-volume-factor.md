---
id: tamagawa-local-volume-factor
title: The sup norm of a cusp form is bounded by its Petersson norm
kind: theorem
decl: UpperTheory.Lit.Tam.tamagawa_local_volume_factor
module: Development.AutomorphicArithmetic.ThetaCorrespondence.FockModels.TamagawaPeterssonLambdaSqNonneg
covers: 511
status: drafted
drafted_by: writer@claude
---
This theorem bounds the square of the sup norm of a holomorphic cusp form by an explicit constant times the square of its Petersson norm. It feeds the volume branch below [the covolume bound](/entry/top-covol-g-alt-alt/), through three theorems of the same file: a bound on the dimension of a space of cusp forms (`finrank_cuspW_le_supConst2`), `petersson_norm_tamagawa_formula`, and `holSub_supE_sq_le_supConst2_mul_petE_sq`. Despite its name, the theorem does not compute a local factor of a Tamagawa volume.

## Statement

Let $D$ be a datum `D7` with CM field $E$, integer $d$ and rank $r$, $j$ an index, and $(H, \mathrm{Dw}, l, X_o, c)$ a moduli space with coefficient field $F = c.F$ and level $M = l.M$. For each $\sigma \colon F \to \mathbb{C}$ let $U_\sigma$ be a uniformization: finitely many components $X_k$, each a set of frames with a group $\Gamma_k$, and a dictionary from the adelic group $G(\mathbb{A})$ of the hermitian space $W_j$ to the frames of the components. Assume the laws `Laws` of this dictionary and `GoodEmb` at $\sigma$.

Let $\lambda = (\lambda_k)$ be a weight, $w > 0$ a bound for its spread on each component, and suppose that the character $\chi_{\lambda_k}$ is trivial on $\Gamma_k$. For a family $P = (P_k)$ in the span of the holomorphic cusp sections of weight $\lambda$ (`holSub`), let

- $\|P\|_\infty = \sup_{k,\, x} \|P_k\|_{\lambda}(x)$, the sup of the pointwise norm over the frames of all components (`supE`);
- $\|P\|_{\mathrm{Pet}}$ be the $L^2$ norm of the pointwise norm over $G(\mathbb{Q})\backslash G(\mathbb{A})$, for the normalized measure `muQ1`, read through the dictionary (`petE`).

**Theorem.** Assume `True` and `TorusBound`. Then

$$\|P\|_\infty^2 \le C\, \|P\|_{\mathrm{Pet}}^2, \qquad C = \mathrm{locConst}(E, r, w, \varepsilon) \cdot \mathrm{massLev2}(E, r, M),$$

where $\varepsilon = $ `epsLev` depends on $E$, $d$, $M$, $w$. This is `supConst2`.

## Proof

1. `abelian₂.holSub_SS` puts each $P_k$ in the space of cusp sections. `exists_selfDual_data_transvection_principal_level` gives, for each $k$, a lattice $L'$ stable under $\Gamma_k$ and elements of $\Gamma_k$ given by the flow `flowMat` along each isotropic vector of $L'$ (the lemma name calls them transvections). `finMu_unconditional` gives a base frame $x_0$ and a fundamental set $F_k$ with measure $\mu_{F,k}$.
2. **Local bound.** `SupModel.comp_bound`: at each frame $y$ of $X_k$, $\|P_k\|_\lambda(y)^2 \le \mathrm{locConst} \cdot \int_{F_k} \|P_k\|_\lambda^2\, d\mu_{F,k}$.
3. **Unfolding.** `adelicProbability_eq_normalised_fundamentalSets`: for a measurable function $\Phi$ on frames that is invariant under $\Gamma_k$ on the left and under the Borel group on the right, $\int_{G(\mathbb{Q})\backslash G(\mathbb{A})} \Phi \cdot \sum_k \mu_{F,k}(F_k) = \sum_k \int_{F_k} \Phi\, d\mu_{F,k}$. Apply it to $\Phi = \|P\|_\lambda^2$.
4. **Total mass.** [`Plug.comp`](/entry/plug-comp/): $\sum_k \mu_{F,k}(F_k) \le \mathrm{massLev2}(E, r, M)$.

Steps 2 to 4 give $\|P_k\|_\lambda(y)^2 \le C\,\|P\|_{\mathrm{Pet}}^2$ at each frame. Take the sup. The rest is bookkeeping.

## In the Lean code

The theorem is in [TamagawaPeterssonLambdaSqNonneg.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/TamagawaPeterssonLambdaSqNonneg.lean#L43). The lemmas:

- `GlobalTheory.SupModel.comp_bound`, in [WeightedFrameSumPositive.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/WeightedFrameSumPositive.lean#L56). It calls `cuspForm_sup_norm_le_petersson_integral_component`, which we have not unfolded.
- `adelicProbability_eq_normalised_fundamentalSets` and `exists_selfDual_data_transvection_principal_level`; we have read their statements only.
- `MainStatements.Tam.Plug.comp`, in [Imports.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/ConstantSupremum/Imports.lean#L17), whose type `CompSt` is the mass bound of step 4.

Both hypotheses before $D$ are unused. The first is `True`. The second, `TorusBound` (a bound on a number of tori by the class number of $E$ times a power of $M$), is introduced as `hTB` and never used. The caller `holSub_supE_sq_le_supConst2_mul_petE_sq` passes `trivial` and `normOneTorusClassNumberBound_proof` for them. The name says "Tamagawa local volume factor", but the statement is a sup-norm bound. In `muQ1`, a quotient of mass $0$ or $\infty$ gets a Dirac measure as a default value.
