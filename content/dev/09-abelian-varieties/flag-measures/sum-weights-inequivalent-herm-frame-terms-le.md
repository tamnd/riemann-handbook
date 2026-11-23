---
id: sum-weights-inequivalent-herm-frame-terms-le
title: The weights of inequivalent terms for one normal form, statement form
kind: theorem
decl: GlobalTheory.T.sum_weights_inequivalent_hermFrameTerms_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.SumWeightsInequivalentHermFrameTermsLeStatement
covers: 385
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`FixedForm.main`](/entry/fixed-form-main/). Its only user is [`one_class`](/entry/one-class/), in step 4 of its proof. The content is in [`FixedForm.main`](/entry/fixed-form-main/).

## Statement

The notation is that of [`one_class`](/entry/one-class/).

**Theorem.** Let $K$ satisfy `IsCMUnram`, $N$ a normal form of length $r$, $g \ge 1$, and $\Lambda_0$ a lattice that is a term for $N$. Let $(\Lambda_i)_{i \in s}$ be a finite family of lattices. Suppose that each $\Lambda_i$ is a term for $N$ and has the same three invariants as $\Lambda_0$: the lattice $L(N.F, N.F', \cdot)$, the definite part lattice for $(N.F', N.F)$, and the graph lattice at $g$. Suppose that no two distinct $\Lambda_i$ are in one orbit of $R_N$. Then
$$\sum_{i \in s} \omega_N(\Lambda_i) \le N_T^2 \Bigl(\frac{\Delta}{\mathrm{gI}(N, \Lambda_0)}\Bigr)^{\dim W_t(N)/2} \Delta^{c_f + 2} (D_b \Delta N_T)^{10000(r+1)^3}.$$

Here $\Delta, D_b, N_T$ are the invariants of $N$, and $W_t(N)$ is the orthogonal of the common space of the two flags and of the vectors `ist` of $N$.

## Proof

The proof is the term `GlobalTheory.DegAsm.FixedForm.main`. There is nothing else.

## In the Lean code

The theorem is at [SumWeightsInequivalentHermFrameTermsLeStatement.lean line 11](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SumWeightsInequivalentHermFrameTermsLeStatement.lean#L11). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative already fits. The first step of `FixedForm.main` bounds the number of the lattices $L(N.F', N.F, \Lambda_i)$ by $N_T^2$ with `card_innerLattices_with_definite_trace_le_norm`; we have not read the rest.
