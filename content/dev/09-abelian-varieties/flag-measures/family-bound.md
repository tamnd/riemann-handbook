---
id: family-bound
title: The mean square over one family of second-type terms
kind: theorem
decl: GlobalTheory.HL.FamilyBound.family_bound
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermitianDoubleCosetSecondTypeFamilyAmpSqLe
covers: 413
status: drafted
drafted_by: writer@claude
---
This theorem bounds the weighted mean square of the oscillating sums over one family $\mathcal{F}(\beta, J, \beta_J)$ of second-type terms. It combines a cancellation bound for each sum with two mass bounds, and the defect index $\beta$ cancels in the product. Its statement form is [`hermitianDoubleCoset_secondType_family_ampSq_le`](/entry/hermitian-double-coset-second-type-family-amp-sq-le/), which [`ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/) uses. The cancellation bound is [`amplitude_le_mass_secondType_family`](/entry/amplitude-le-mass-second-type-family/).

## Statement

The notation is in [the entry for `ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/), and the family $\mathcal{F}(\beta, J, \beta_J)$ is defined in [the statement form](/entry/hermitian-double-coset-second-type-family-amp-sq-le/). Let $A_0 = H^{9(r+1)^2 + 12(r+1)}$, $A_1 = 4 H^{4(r+1)}$ and $e = q^{1 - (k - 2r - 3)}$.

**Theorem.** If $4r + 7 \leq k$, then for all $\beta, J, \beta_J$:
$$\mathrm{ampSq}\bigl(\mathcal{F}(\beta, J, \beta_J)\bigr) \leq 98 \, A_0 A_1 e^2 \, \mathrm{nn}.$$

## Proof

If the family has no term, the left side is $0$. Otherwise fix a term $(d_0, \Lambda_0)$ in it.

1. **The defect is a power of $q$.** By `exponents_and_defect`, $\beta = q^i$ for some $i$, and defect index $1$ means defect zero. Second-type terms have a nonzero defect, so $q \neq 1$ and $q \geq 2$.
2. **Mass for each datum.** Let $d$ be any datum. For a term $\Lambda$ in the family, `small_image` gives $|I(d, \Lambda)| = q^m$ with $q^m \leq \beta = q^i$, so $m \leq i$. Here $I(d, \Lambda)$ is a lattice quotient that we have not unfolded (`cardI`). `hermitianDoubleCoset_mass_le_and_finite` bounds the mass of the terms with $|I| = q^m$ by $A_0 (q^m)^{k-1}$. Summing the geometric series (`geom_le`, with ratio $q^{k-1} \geq 2$):
$$m\bigl(d, \mathcal{F}\bigr) \leq \sum_{m=0}^{i} A_0 (q^{k-1})^m \leq 2 A_0 \beta^{k-1}.$$
3. **Cancellation.** [`amplitude_le_mass_secondType_family`](/entry/amplitude-le-mass-second-type-family/) gives $|a(d, \mathcal{F})| \leq 7 e \cdot m(d, \mathcal{F})$ for each $d$.
4. **Basic inequality.** `basic_inequality` turns steps 2 and 3 into
$$\mathrm{ampSq}(\mathcal{F}) \leq (7e)^2 \cdot 2 A_0 \beta^{k-1} \cdot \sum_d \nu(d) \, m(d, \mathcal{F}).$$
This is $|a|^2 \leq (7e)^2 \, m \cdot m$ with one factor $m$ bounded by step 2.
5. **Mass of defect $\beta$.** The family lies inside the terms of defect index $\beta$, so `sumData_mass_be_eq_le` gives $\sum_d \nu(d) \, m(d, \mathcal{F}) \leq A_1 \beta^{-(k-1)} \, \mathrm{nn}$.

The product is $49 e^2 \cdot 2 A_0 \beta^{k-1} \cdot A_1 \beta^{-(k-1)} = 98 A_0 A_1 e^2$.

## In the Lean code

The theorem is in [HermitianDoubleCosetSecondTypeFamilyAmpSqLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianDoubleCosetSecondTypeFamilyAmpSqLe.lean#L59). It calls:

- `GlobalTheory.HL.Defect.exponents_and_defect` and `GlobalTheory.HL.SmallImage.small_image`, `resQ_pos`;
- `GlobalTheory.T.hermitianDoubleCoset_mass_le_and_finite`;
- `GlobalTheory.T.amplitude_le_mass_secondType_family`;
- `GlobalTheory.HL.BasicIneq.basic_inequality` and `GlobalTheory.T.sumData_mass_be_eq_le`;
- `geom_le`, `mass_mono`, `mass_le_sum` and `sumData_mono` in the same file.

The proof gets $q \geq 2$ from a term of the family, although `UnramOrder.order_facts` gives $q \geq 2$ for every frame datum. The mass bound of step 2 needs only $k \geq 1$. The factor $\beta^{k-1}$ from step 2 and the factor $\beta^{-(k-1)}$ from step 5 cancel exactly, so the bound does not depend on $\beta$, $J$ or $\beta_J$.
