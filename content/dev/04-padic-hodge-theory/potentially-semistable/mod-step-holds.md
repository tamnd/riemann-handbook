---
id: mod-step-holds
title: One elementary change of the Hodge-Tate frame
kind: theorem
decl: GlobalTheory.PMon.modStep_holds
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.MonodromyIrreducibleElementaryWeightModification
covers: 654
status: drafted
drafted_by: writer@claude
---
This theorem proves `ModStep`, step 5 of the induction in [the $p$-adic monodromy theorem in matrix form](/entry/mat-thm-holds/). Its second name is [`monodromy_irreducible_elementary_weightModification`](/entry/monodromy-irreducible-elementary-weight-modification/), and that entry gives the statement. In words: if $\rho$ is framed with weight $w$ and does not split, then for each $x \ne y$ we can move one unit of weight from $x$ to $y$ and replace $\rho$ by a $\rho'$ such that $\rho$ is potentially semistable if $\rho'$ is. The work is in the lattice lemma [`fundamentalLemmaLatticeFrobFixed_forall_degree`](/entry/fundamental-lemma-lattice-frob-fixed-forall-degree/).

## Statement

`ModStep`, as in [the second name](/entry/monodromy-irreducible-elementary-weight-modification/). Write $B_{\mathrm{dR}}$ for the de Rham ring of the period data $P$, with filtration $\mathrm{Fil}^a$ and the element $t$. Write $B$ for the ring of $P$ with Frobenius $\varphi$ and the map $\iota \colon B \to B_{\mathrm{dR}}$ (in Lean `P.R.B`, `P.φB`, `P.ιB`). A frame for $\rho$ in degree $m < r$ is $U_m \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $U_m, U_m^{-1}$ in $\mathrm{Fil}^0$ and $\mathrm{Fr}^m(\rho(g))\, g(U_m) = U_m \operatorname{diag}(\chi(g)^{w(m,j)})_j$.

## Proof

Let $U_0, \dots, U_{r-1}$ be the frames, and write $x = (m_0, j_0)$.

1. **Facts on $B_{\mathrm{dR}}$.** `deRhamPeriodRing_field_tPow_filtration_units` says that $B_{\mathrm{dR}}$ is a field, that each $z \ne 0$ has an exact filtration degree, and that $\mathrm{Fil}^a \cdot \mathrm{Fil}^b \subseteq \mathrm{Fil}^{a+b}$. From these, $1 \notin \mathrm{Fil}^1$.
2. **A good column.** Let $u$ be column $j_0$ of $U_{m_0}$. Its entries lie in $\mathrm{Fil}^0$. Some entry is not in $\mathrm{Fil}^1$: else row $j_0$ of $U_{m_0}^{-1}$ times $u$ gives $1 \in \mathrm{Fil}^1$.
3. **An eigenvector.** The frame equation, read in column $j_0$, says $\mathrm{Fr}^{m_0}(\rho(g))\, g(u) = \chi(g)^{w(x)} u$ for all $g \in G_K$.
4. **Independence.** `residue_indep_of_not_reducibleOverUnramified` uses that $\rho$ does not split: if $c \in (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ is fixed by $\mathrm{Fr}^r$ and $\sum_i c_i u_i \in \mathrm{Fil}^1$, then $c = 0$.
5. **The lattice.** Step 4 is the hypothesis of `FLAt r`. [`fundamentalLemmaLatticeFrobFixed_forall_degree`](/entry/fundamental-lemma-lattice-frob-fixed-forall-degree/) gives $A \in \mathrm{GL}_n(B)$ with $\varphi^r(A) = A$ and, for each $m$, a $W_m$ with $W_m, W_m^{-1}$ in $\mathrm{Fil}^0$ and $\iota(\varphi^m(A)) = U_m \operatorname{diag}(t^{\varepsilon_{x,y}(m,j)})_j\, W_m$.
6. **The new representation.** `exists_rep_of_frobeniusFixed_frame_change` takes the frames and $A$ and returns $\rho'$ with `IsRat r ρ'`, framed with weight $w + \varepsilon_{x,y}$, and with `AdmSt P ρ'` implying `AdmSt P ρ`.

## In the Lean code

The theorem is in [MonodromyIrreducibleElementaryWeightModification.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MonodromyIrreducibleElementaryWeightModification.lean#L15). It calls four lemmas, each a second name: `deRhamPeriodRing_field_tPow_filtration_units` (for `PMon.bdR_tied`), `residue_indep_of_not_reducibleOverUnramified` (for `residue_indep_of_not_splits`), `fundamentalLemmaLatticeFrobFixed_forall_degree` (for `flAt_all`) and `exists_rep_of_frobeniusFixed_frame_change` (for `exists_rep_of_fixed_frame_change`). We have not opened the proofs of the first, second and fourth, so we do not say how $\rho'$ is built from $A$.

The proof uses only the weight $w(x)$ and the frame $U_{m_0}$ in steps 2 to 4. The other frames enter only in steps 5 and 6. The hypothesis $x \ne y$ is used only in step 5.
