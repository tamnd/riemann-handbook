---
title: The local clauses for the normalized family
decls:
  - Formalism.MainNotions.N.K.StB.hRho_full
  - Formalism.MainNotions.N.K.StB.hRho_rN
  - Formalism.MainNotions.N.K.Closed.tbTarget_row
  - Formalism.MainNotions.N.K.Closed.open_inputs_at_normalized
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local clauses for the normalized family

The display bound of the last section has local hypotheses on the blocks of the ring datum. Five of them are not given by the ring datum itself: one clause on block $0$, one on the row places, two on the character blocks, and one that ties the rows together. This section proves the five clauses for the normalized family $r^{\mathrm{N}}$ from the conditions of [the Selmer bound at a point](/entry/selmer-bound-at-point-main/). The result, the theorem on the open clauses at the end, is used in the proof of [Theorem 2.5.7](/entry/theorem-n5-from-inputs/).

We keep the notation of the last section. We refer to the conditions of the Selmer bound at a point by their numbers there. In particular, the *unramified condition* is the part of condition 3 that says each $r_x$ is unramified outside $\ell$, $S$ and $Q$; the *inertia condition* is the part of condition 4 on the action of inertia at the places of $S \cup Q$; the *tame generator conditions* are the rest of condition 4; and the *gain conditions* are the crystalline and gain conditions on the twists of $r_x$ in condition 7. Fix a ring datum for a family $r$ that is normal at $\pi$, with an idempotent pair $(e_B, e_1)$ and a corner perturbation $s$ for $g_0$. Assume that $r$ is continuous, that the ring datum has the properties (T), and that $e_1$ has rank one on block $0$ at $\pi'$. For $g \in G_E$ put $u(g) = \chi(g)^{-1} r(g) \in R'$, where $\chi(g) = \chi_1(g)$ as a unit of $\mathbb{T}'$. For $0 \leq c \leq t$ let $M_c$ be block $c$ at $\pi'$, an $\mathcal{O}$-module with the action of $G_E$ through $u$. So $M_0 \cong \mathcal{O}^r$ with $\rho_\pi \otimes \chi_1^{-1}$, and $M_c \cong \mathcal{O}$ with $\varepsilon^{1-c}$ for $c \geq 1$.

The places of $E$ above $\ell$ are split into row places and column places. For each place $w$ above $\ell$ let $D_w$ be a decomposition group. The datum gives, for each block $c$ and place $w$, a submodule $F(c, w) \subseteq H^1(D_w, M_c)$, the local condition at $w$. We write $H^1_{\mathrm{lc}}$ for the classes of locally constant cocycles. For $a \in \mathcal{O}$ and a submodule $F$, let $a^{-1}F$ be the classes $z$ with $az \in F$.

**Definition 2.4.1 (The five clauses).** The *open clauses* for the ring datum are:

1. the *$\rho$-clause*: block $0$ is a quotient $V/\Lambda$ of an $L$-module $V$ by a lattice $\Lambda$ that carries an $R'$-linear tensor map, compatible with $e_1$; the classes at the column places that are combinations of fixed cocycles $\kappa$ lie in $F(0, w)$; the local condition on $\Lambda$ at each column place is saturated and is spanned, up to torsion, by independent classes $\kappa_z$; $r$ and $\chi$ are trivial on a fixed family of inertia groups $I_o$; and the length of the classes in $H^1_{\mathrm{lc}}(G_E, M_0)$ that are unramified at each $I_o$ and lie in $F(0, w)$ at each row and column place is at most $s$, the length of the Selmer group $\mathrm{Sel}_\pi$;
2. the *row clause*: for each block $c \geq 1$ and each row place $w$, let $Y \subseteq R'$ be the left ideal spanned by the elements $y(g) = (u(g) - 1)\mathcal{E}$; if $\psi : Y \to M_c$ is $\mathcal{O}$-linear and $D_w$-equivariant, and $z$ is the cocycle $g \mapsto \psi(y(g))$ on $D_w$, then $\ell^{c_B} [z] \in F(c, w)$; and
$$\ell\Big( \big(H^1_{\mathrm{lc}}(D_w, M_c) \cap \ell^{-c_B} F(c, w)\big) \big/ F(c, w) \Big) \leq e_{\mathcal{O}} \, c_B \, (d_w + 1) ;$$
3. the *character clause* for each block $c \geq 2$, with the Tate-Shafarevich term $\text{Ш}_{c-1}$;
4. the *first local clause* for block $1$;
5. the *row tie*, six conditions on the row places.

Lean: `Formalism.MainNotions.N.K.Final.RhoOpenA` (also `Formalism.MainNotions.N.K.Final.TBOpen`, `Formalism.MainNotions.N.K.Final.ChiOpen`, `Formalism.MainNotions.N.K.Final.FirstLocalConditionOpen`, `Formalism.MainNotions.N.K.StD.RowTieIn`).

The $\rho$-clause is where the Selmer group of $\rho_\pi \otimes \chi_1^{-1}$ enters the bound. Classes on block $0$ that satisfy all local conditions form a Selmer group of $M_0 = \rho_\pi \otimes \chi_1^{-1}$, and the clause bounds their length by $s = \ell(\mathrm{Sel}_\pi)$. The row clause says that at a row place the local condition is reached from the cocycles of the ring after multiplication by $\ell^{c_B}$, with a loss bounded in terms of the local degree $d_w = [E_w : \mathbb{Q}_\ell]$.

**Theorem 2.4.2 ($\rho$-clause).** Let $r$ be normal at $\pi$ and let the ring datum be as above. Assume the unramified condition for $r$, the decomposition $r_\pi \otimes L \cong \rho_\pi \otimes L \oplus \chi_1 \oplus \cdots \oplus \chi_t$, and the finiteness of local $H^1$ at the places above $\ell$. Then the $\rho$-clause holds, with the classes $\kappa$, $\kappa_z$ and the lattice that the datum fixes.

Lean: `Formalism.MainNotions.N.K.StB.hRho_full`.

*Proof.* A general lemma gives the $\rho$-clause from the unramified condition, the decomposition, and three facts on the local conditions at the column places: each one has finite length; its rank is the number $j_w$ of fixed classes; and the Selmer group of block $0$ has length $s$. The first fact follows from the finiteness of local $H^1$. The second and third follow from the normal form at $\pi$, since block $0$ at $\pi'$ is then $\rho_\pi \otimes \chi_1^{-1}$ itself. $\square$

**Theorem 2.4.3 ($\rho$-clause for the normalized family).** Assume the unramified condition for $r$, the decomposition of $r_\pi$, and the finiteness of local $H^1$. Then the $\rho$-clause holds for each ring datum of $r^{\mathrm{N}}$ as above.

Lean: `Formalism.MainNotions.N.K.StB.hRho_rN`.

*Proof.* The family $r^{\mathrm{N}}$ is normal at $\pi$, and its decomposition at $\pi$ is an equality. The unramified condition passes from $r$ to $r^{\mathrm{N}}$: at $x \neq \pi$ the two families agree, and at $\pi$ the decomposition shows that $\rho_\pi$ and the $\chi_c$ are unramified wherever $r_\pi$ is. Now apply the last theorem to $r^{\mathrm{N}}$. $\square$

**Theorem 2.4.4 (Row target).** Let $r$ be normal at $\pi$, continuous, with a ring datum as above, and let $c_B \in \mathbb{N}$. Assume the local torsion bound of condition 9 with constant $c_B$ at the row places, the good-coefficient condition at each place above $\ell$, the compatibility of local coefficient fields, Fontaine's conditions at the places above $\ell$, the gain conditions, and the decomposition of $r_\pi$. Then a target statement for the rows holds, from which the row clause follows.

Lean: `Formalism.MainNotions.N.K.Closed.tbTarget_row`.

*Proof.* The torsion bound and the good-coefficient condition give a trivial bound at each row place. At a row place $w$, the decomposition gives a line in $r_\pi \otimes L$; with the ring datum, it embeds into the local representation at $w$; Fontaine's conditions and the gain conditions then give the local target for each block. The continuity of $r$ gives the continuity of the local action. A general lemma joins the trivial bound, the compatibility of coefficient fields and the local targets into the target statement. $\square$

**Theorem 2.4.5 (Open clauses for the normalized family).** Assume the gain conditions, the unramified condition and the inertia condition for $r$, the tame generator conditions, the decomposition of $r_\pi$, Fontaine's conditions, the finiteness of local $H^1$, the compatibility of local coefficient fields, and the good-coefficient condition. Assume that for each $v \in Q$ and each $g$ in the inertia group at $v$ there is $n$ with $\chi_1(g) = \chi_1(\gamma_v)^n$. Let $c_B \in \mathbb{N}$, and assume the local torsion bound with constant $c_B$ for $r^{\mathrm{N}}$. Then for each ring datum of $r^{\mathrm{N}}$ as above, the five open clauses hold.

Lean: `Formalism.MainNotions.N.K.Closed.open_inputs_at_normalized`.

*Proof.* The family $r^{\mathrm{N}}$ is normal at $\pi$, and its decomposition at $\pi$ holds with no hypothesis. The gain conditions, the unramified condition and the inertia condition pass from $r$ to $r^{\mathrm{N}}$ through the decomposition of $r_\pi$. Then:

1. the $\rho$-clause is the theorem on the $\rho$-clause for the normalized family;
2. the row clause follows from the row target, applied to $r^{\mathrm{N}}$;
3. the character clauses and the first local clause follow, by two general lemmas, from the normal form, the unramified and inertia conditions for $r^{\mathrm{N}}$, the decomposition, the tame generator conditions, and the condition on $\chi_1$ at the places of $Q$;
4. the row tie follows, by a general lemma, from two facts on the rows of the ring datum of $r^{\mathrm{N}}$, which hold with no further hypothesis. $\square$

**Remark 2.4.6 (Formalization).** The local conditions $F(c, w)$ are `FS`, the fixed classes are `KFin.κ` and `KFin.κz`, and the number $s$ is `sN`, the length of `selPi` ([HigherColumnInvariantsBound.lean](lean:Formalism/AdmissibleDesigns/HigherColumnInvariantsBound.lean#L121)). The $\rho$-clause is `InRhoFixReal2`. We did not unfold `InChiFixReal`, `InChiLoc`, the six conditions of `RowTieIn`, the target `TB.TBTarget`, or the good-coefficient condition `SelfGood`; the text names them by role only. The general lemma of the first proof is `hRho_of`, with the three facts `KTate.finFf_rec`, `KTate.rankFf_normAt` and `selFS_of_normAt`; the transfer lemmas are `Norm.admG2_rN`, `Norm.admG4_rN`, `Norm.admG5_rN` and `Norm.decomposes_normalized`. We read their statements, not their proofs. In `open_inputs_at_normalized` ([StatementOneBFromUnramified.lean](lean:Formalism/AdmissibleDesigns/StatementOneBFromUnramified.lean#L74)) the $\rho$-clause is proved by `hRho_rN` with the hypotheses for $r$, while the transferred hypothesis for $r^{\mathrm{N}}$ is computed in the same proof and used only by the other clauses. The unramified, inertia and gain conditions are `admG4`, `admG5` and `admG2`; the tame generator conditions are `TameGeneratorConditions`. The general lemmas of the last proof are `StC.chi_of`, `StC.first_local_clause_of` and `KRowA.rowTieIn_of` with `RowB.rowMat_SN` and `RowB.orbC_S`; we read only their statements. The row tie uses no hypothesis beyond the ring datum. The good-coefficient condition, the compatibility of coefficient fields, Fontaine's conditions and the torsion bound are used only for the row clause. `hRho_full`, `hRho_rN`, `tbTarget_row` and `open_inputs_at_normalized` all run under `maxHeartbeats 4000000`.
