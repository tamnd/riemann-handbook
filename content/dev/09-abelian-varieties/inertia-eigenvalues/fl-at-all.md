---
id: fl-at-all
title: A Frobenius-fixed lattice change in each degree, by restriction of scalars
kind: theorem
decl: GlobalTheory.PMon.flAt_all
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.FundamentalLemmaLatticeFrobFixedForallDegree
covers: 622
status: drafted
drafted_by: writer@claude
---
This theorem proves `FLAt r` for every $r$. It is the proof of [`fundamentalLemmaLatticeFrobFixed_forall_degree`](/entry/fundamental-lemma-lattice-frob-fixed-forall-degree/), which states it, and the result goes to [`modStep_holds`](/entry/mod-step-holds/). The proof reduces degree $r$ to degree $1$. It replaces $n$ frames of size $n$ by one frame of size $nr$, applies the degree-one case [`fundamentalLemmaLattice_degreeOne`](/entry/fundamental-lemma-lattice-degree-one/), and descends the answer back.

## Statement

`FLAt r` for all $r \ge 0$, as in [the statement entry](/entry/fundamental-lemma-lattice-frob-fixed-forall-degree/). The notation is the same: frames $U_0, \dots, U_{r-1}$, indices $x = (m_0, j_0) \ne y = (m_1, j_1)$, the ring $B$ with $\varphi$ and $\iota$, and $\varepsilon_{x,y}$.

## Proof

If $r = 0$, there is no $x$, and there is nothing to prove. Let $r > 0$.

1. **An unramified basis.** `unramifiedExt_fixedField_frobeniusPow_degree` gives the unramified extension $E$ of $\mathbb{Q}_\ell$ of degree $r$, as the elements of $\mathbb{Q}_\ell^{\mathrm{ur}}$ fixed by $\mathrm{Fr}^r$, and a $\mathbb{Q}_\ell$-basis $\omega_0, \dots, \omega_{r-1}$ of $E$ with $\det \Omega \ne 0$, where $\Omega = (\mathrm{Fr}^m(\omega_k))_{m,k}$.
2. **One large frame.** Index rows and columns by $n \times \{0, \dots, r-1\}$. Let $R = 1_n \otimes \Omega$ and $U' = R^{-1} \operatorname{diag}(U_0, \dots, U_{r-1})$, with the $U_m$ as diagonal blocks. By `isBdRPlusUnitMatrix_restrictionLatticeMatrix`, $U'$ and $U'^{-1}$ have entries in $\mathrm{Fil}^0$. By `linearIndependent_restrictionLattice_column`, the column $(j_0, m_0)$ of $U'$ is independent modulo $\mathrm{Fil}^1$ over the elements fixed by $\mathrm{Fr}$. This is the hypothesis of `FLAt 1`.
3. **Degree one.** `fundamentalLemmaLattice_degreeOne` gives $A_0 \in \mathrm{GL}_{nr}(B)$ with $\varphi(A_0) = A_0$ and $\iota(A_0) = U' \operatorname{diag}(t^{\varepsilon})\, W_0$, where $\varepsilon$ is $-1$ at $(j_0, m_0)$ and $+1$ at $(j_1, m_1)$, and $W_0, W_0^{-1}$ have entries in $\mathrm{Fil}^0$.
4. **Back to size $n$.** For each column $c$ of $A_0$ let $v_c \in B^n$ have entries $\sum_k \omega_k (A_0)_{(i,k),c}$. By `restrictionLattice_columns_condition_linearIndependent`, the $nr$ vectors $v_c$ are linearly independent over $\mathbb{Q}_\ell$, and each satisfies the lattice condition `LatC`: its entries are fixed by $\varphi^r$, and for each $m$, $\iota(\varphi^m(v_c)) = U_m \operatorname{diag}(t^{\varepsilon_{x,y}(m,j)})_j\, w$ for some $w$ with entries in $\mathrm{Fil}^0$.
5. **An $E$-basis.** Let $V$ be the $\mathbb{Q}_\ell$-span of the $v_c$. By `frobFixedLatticeCondition_smul_of_frobenius_fixed`, `LatC` is stable under multiplication by $E$, and by `mem_span_restrictionLattice_columns` each vector with `LatC` lies in $V$. So $V$ is an $E$-space. `exists_frobeniusFixed_unramified_tower_basis` gives $a_1, \dots, a_n \in V$ such that the $\omega_k a_j$ form a $\mathbb{Q}_\ell$-basis of $V$.
6. **The matrix.** `exists_frobeniusFixed_matrix_units_of_lattice_basis` turns $a_1, \dots, a_n$ into $A \in \mathrm{GL}_n(B)$ with the properties of `FLAt r`.

The rest is bookkeeping: an identity of $\varepsilon$ under the swap $(m, j) \leftrightarrow (j, m)$ of index order, proved by `grind`.

## In the Lean code

The theorem is in [FundamentalLemmaLatticeFrobFixedForallDegree.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FundamentalLemmaLatticeFrobFixedForallDegree.lean#L21). The large frame $U'$ is `U0`, the vectors $v_c$ are `colv` and the condition is `LatC`, all in [IsUnitDetResMat.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsUnitDetResMat.lean#L41). The callees are second names of lemmas whose proofs we have not opened. In particular we have not checked how step 6 builds $A$ from the $a_j$.

Of the facts that the lemma in step 1 returns about $E$ (its degree, $E \subseteq \mathbb{Q}_\ell^{\mathrm{ur}}$, and $E$ as the fixed field of $\mathrm{Fr}^r$), the proof uses none. It uses only $\omega$.
