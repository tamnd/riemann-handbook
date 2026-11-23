---
id: exists-pel-ok-factor
title: Degeneration data are a factor of a unitary tensor power
kind: theorem
decl: GlobalTheory.Mum.exists_pelOK_factor
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryPELTypeFactorDegData
covers: 558
status: drafted
drafted_by: writer@claude
---
This theorem embeds degeneration data $D$ as a factor of data $D'$ of unitary PEL type for the field $\mathbb{Q}(\zeta_{21})$. The data $D'$ are a tensor power $D^r$, twisted by a unimodular hermitian form. The result is restated as [`exists_unitaryPELType_factor_degData`](/entry/exists-unitary-peltype-factor-deg-data/), which is step 2 of [`has_of_base`](/entry/has-of-base/).

## Statement

Let $R$ satisfy `Base R` and let $D$ be degeneration data over $R$ for $\mathfrak{m}$ with lattice $X \neq 0$. The objects of the conclusion:

- A *host* for a CM field $E$ (`Host`): a prime $d \equiv 7 \pmod{16}$, an element $\sqrt{-d} \in \mathcal{O}_E$, an element $w_0$ with $2 w_0 = 1 + \sqrt{-d}$, complex conjugation $a \mapsto \bar a$ on $\mathcal{O}_E$, and the condition that $E$ is unramified over its maximal real subfield.
- A *unitary datum* $\mathrm{Dm}$ (`Datum H`): a finite projective $\mathcal{O}_E$-module $\Lambda$ with an alternating unimodular $\mathbb{Z}$-form $\langle\,,\rangle$ with $\langle a x, y\rangle = \langle x, \bar a y\rangle$, integers $p, q$ with $p + q = \operatorname{rank} \Lambda$, and a positive complex structure on $\Lambda \otimes \mathbb{R}$ of signature $(p, q)$.
- `PelOK Dm D' o`: $p = q \geq 1$; a trivialisation `TraceFormTwistIso` attached to $w_0$; at each geometric generic point $\operatorname{Spec} F$ and each $\tau \colon \mathcal{O}_E \to F$, the $\tau$-eigenspace of $\mathcal{O}_E$ on the Lie algebra of $B'_F$ has a dimension $n$ with $n + \operatorname{rank}_{\mathcal{O}_E} X' = p$; and for each compatible system of roots of unity a map from $\Lambda$ to the torsion points of $D'$ (`TateIsoQ`). We have not unfolded `TraceFormTwistIso`, `LieMult` or `TateIsoQ` beyond their first lines.
- A *factor* $D \to D'$ (`Factor`): a ring $O$ with involution acting on $D'$, an idempotent $e$ and an element $f$ of $O$, maps $\mathrm{inc} \colon B \to B'$ and $\mathrm{pr} \colon B' \to B$ of the abelian parts with $\mathrm{pr} \circ \mathrm{inc} = 1$ and $\mathrm{inc} \circ \mathrm{pr} = e$, the same for the lattices, and compatibility with $c$, with the line bundles through $f$, and with $\tau$. `Factor.Alg` asks that $e^* e = b \, e^* f e$ for some $b > 0$, that $e^* f e = e^* f^* e$, and that $e$ is a left multiple of $e^* f e$.

**Theorem.** There are $E$, $H$, $\mathrm{Dm}$, $D'$ and an action $o$ of $\mathcal{O}_E$ on $D'$ with `PelOK Dm D' o`, and a factor $F \colon D \to D'$ with `F.Alg`.

## Proof

1. `exists_host`: take $E = \mathbb{Q}(\zeta_{21})$ with $d = 7$ and $w_0 = (1 + \sqrt{-7})/2$.
2. `unimodLattice`: there are $r \geq 1$, an integer matrix $W$ and a ring map $\rho \colon \mathcal{O}_E \to M_r(\mathbb{Z})$ such that $S = W + W^T$ is positive definite with $\det S = \pm 1$, $\rho(a)^T S = S \rho(\bar a)$, and $W = S \rho(w_0)$. It comes from the trace form of $E$ (`exists_cmField_traceForm_gram_matrix_posDef`) made unimodular (`exists_unimodular_posDef_form_adjoint_rep_of_posDef`).
3. `exists_tensorDegenerationData_of_unimodular_posDef`: there are data $D'$ with a tensor structure $T$ (`Tens`): abelian part $B^r$, lattice $X^r$, and line bundle $\bigotimes_{i,j} (\mathrm{pr}_i, \mathrm{pr}_j)^* \Lambda(L)^{W_{ij}}$, where $\Lambda(L) = m^*L \otimes p_1^*L^{-1} \otimes p_2^*L^{-1} \otimes 0^*L$ on $B \times B$.
4. `exists_ringOfIntegers_module_on_tensor_data`: $\rho$ gives an action $o$ of $\mathcal{O}_E$ on $D'$ with `TraceFormTwistIso`.
5. `tensorDegData_unitary_type`: there is $\mathrm{Dm}$ with `PelOK Dm D' o`. This step uses $X \neq 0$ and characteristic zero.
6. `exists_algebraic_factor_of_unimodular_tensor`: $D$ is a factor of $D'$ with `Factor.Alg`.

## In the Lean code

The theorem is in [ExistsUnitaryPELTypeFactorDegData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryPELTypeFactorDegData.lean#L20). We read the statements of the lemmas of steps 2 to 6, not their proofs. `exists_host` uses the host `HostModel.host` of [OneAddZeta21PowSevenAddPowFourteenEqZero.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/OneAddZeta21PowSevenAddPowFourteenEqZero.lean#L297).

The field $E$ does not depend on $D$. The datum $\mathrm{Dm}$ is linked to $D'$ only through `PelOK`.
