---
id: sum-hv-formal-kernel
title: A sum of harmonic values over the formal kernel of a similitude
kind: theorem
decl: GlobalTheory.PlaceInt.FormSum.sum_hv_formal_kernel
module: Development.AbelianVarietyTheory.Proofs.RingsOfIntegers.SumHarmonicValuesFormalKernelSimilitude
covers: 482
status: drafted
drafted_by: writer@claude
---
This theorem is a trace formula on the formal group of an integral chart. A sum of harmonic values over the formal points of $\ker(pq)$ is $\#(\ker q) \cdot \prod_\tau \tau(\det p)^{m_\tau}$ times one chart value of level $1$, which `ChBound` then bounds. The [statement form](/entry/sum-harmonic-values-formal-kernel-similitude/) restates it, and [`sum_hv_primary_kernel`](/entry/sum-hv-primary-kernel/) applies it on each coset.

## Statement

Take the setting, notation and first three hypotheses of [`sum_hv_primary_kernel`](/entry/sum-hv-primary-kernel/), without $g$. The other hypotheses are:

- $a \colon J \to A_x^n$ is injective, with image the $u$ that $pq$ kills whose coordinates are formal points of $C$ (`FormPt`).
- Each section $F_b$ of $L^{N^2}$ is regular on the integral model (`Regular`, not unfolded here).
- $G_{i,b}$ is the translate of $F_b$ by $a_{i,b}$ (`Moves`).
- If $q a_i = 0$, there are $r_b \in T$ with $\prod_b r_b = 1$ and $G_{i,b} = r_b F_b$.
- $P \in$ `HH c w n`, and $\iota(s \cdot P')$ is integral, where $P'$ is $P$ after the change of variables by $pq$.

**Theorem.** There is $z \in \operatorname{Frac} T$ with $v(z)/e \geq -\rho$ and
$$\iota(s) \sum_{i \in J} \mathrm{hv}(G_i, P) = \#\{i : q a_i = 0\} \cdot \iota\Bigl(\prod_{\tau} \tau(\det p)^{m_\tau}\Bigr) \cdot z.$$

## Proof

Let $B$ be the integral formal biextension of $C$, from `integralChart_formalBiextension_gauge_bound`. That lemma also gives the bound: under `ChBound`, each value `nabValN` of an integral series under an integral polynomial has $v/e \geq -\rho$.

1. **Germs.** Each $F_b$ has an integral germ $f_b$ (`regular_section_integral_germ_unique_scale`). Let $f = \prod_b f_b$ on $n$ copies of the formal group. Each $a_i$ has formal coordinates $\alpha_i$. By `kills_formalPoints_iff_mem_coordinateKernel` and `formal_group_points_of_integral_chart_spec`, $\alpha$ is a bijection from $J$ onto the coordinate kernel `kerM B (pq)`.
2. **Translates.** `exists_translateUnit_symmetric_formalGroup_point` gives series $u_{i,b}$ such that the germ of $G_{i,b}$ is $u_{i,b}$ times the shift of $f_b$ by $\alpha_{i,b}$. Let $U_i = \prod_b u_{i,b}$.
3. **The factor $\kappa$.** `exists_integral_exponential_similitude_gauge` gives an integral series $\kappa$ with constant term $1$. By `prod_symmetricTranslationUnits_eq_kappa_ratio`, $U_i \cdot \mathrm{shift}_{\alpha_i} \kappa = \kappa$.
4. **The trace.** `jacobian_nonzero_splitting_of_product` says: if $f$ is invariant under shifts by `kerM B q`, then the sum of its shifts over `kerM B (pq)` is $\#\ker q \cdot \mathrm{jac}(p) \cdot \mathrm{pull}_{pq}(g)$ for some integral $g$. It needs finite height, a split kernel (from $\ell$ and `AllRat`), and $\mathrm{jac}(pq) \neq 0$. For $q a_i = 0$, the hypothesis $G_i = rF$ gives $U_i \cdot \mathrm{shift}_{\alpha_i} f = f$. With this, the local lemma `sum_twisted` adds the twist by $U_i$ and $\kappa$:
$$\sum_i U_i \cdot \mathrm{shift}_{\alpha_i} f = \#\ker q \cdot \mathrm{jac}(p) \cdot \kappa \cdot \mathrm{pull}_{pq}(g).$$
5. **Jacobian.** `jacM_eq_prod` gives $\mathrm{jac}(x) = \prod_\tau \tau(\det x)^{m_\tau}$. For $x = pq$ this is nonzero, since $\det((pq)^*) \det(pq) = N^{2n} \neq 0$.
6. **Values.** `harmonicValue_integralPoint_eq_value_on_biextensionCopies` writes $\mathrm{hv}(G_i, P)$ as `nabValN` of level $N^2$ of $U_i \cdot \mathrm{shift}_{\alpha_i} f$. The value is linear in the series. `connectionValueLevel_kappa_mul_pullback` turns level $N^2$ on $\kappa \cdot \mathrm{pull}_{pq}(g)$ with $P$ into level $1$ on $g$ with $P'$.

Then $z$ is the level $1$ value of $g$ under $s P'$, and the bound from $B$ gives $v(z)/e \geq -\rho$.

## In the Lean code

The theorem is in [SumHarmonicValuesFormalKernelSimilitude.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHarmonicValuesFormalKernelSimilitude.lean#L203). The local lemmas `sum_twisted`, `sim_two_sided` and others are in the same file.

The hypothesis `ChBound` enters only through the bound of `integralChart_formalBiextension_gauge_bound`. `ChBound` is an infimum over the same values, so that bound is close to its definition. `Good3` goes into the finite height and split kernel lemmas.
