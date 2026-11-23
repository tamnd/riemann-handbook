---
id: fundamental-lemma-lattice-frob-fixed-forall-degree
title: A Frobenius-fixed lattice change in each degree, a second name
kind: theorem
decl: GlobalTheory.T.fundamentalLemmaLatticeFrobFixed_forall_degree
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.FundamentalLemmaLatticeFrobFixedForallDegreeStatement
covers: 624
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`flAt_all`](/entry/fl-at-all/). It states `FLAt r` for every $r$. Its only user is [`modStep_holds`](/entry/mod-step-holds/), step 5 of the $p$-adic monodromy induction, which uses it to change a frame by one elementary weight step. The real content is in [`flAt_all`](/entry/fl-at-all/).

## Statement

Use the notation of [`modStep_holds`](/entry/mod-step-holds/): $B_{\mathrm{dR}}$ with $\mathrm{Fil}^a$ and $t$, the ring $B$ with Frobenius $\varphi$ and $\iota \colon B \to B_{\mathrm{dR}}$, the Frobenius $\mathrm{Fr}$ of $\mathbb{Q}_\ell^{\mathrm{ur}}$, and $\varepsilon_{x,y}$, equal to $-1$ at $x$, $+1$ at $y$ and $0$ elsewhere.

**Theorem** (`FLAt r`, for all $r \ge 0$). Let $\ell$ be a prime, $P$ period data with a tie to Fontaine's rings (`LocTied`), and $n$ a finite index set. Let $U_0, \dots, U_{r-1} \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $U_m, U_m^{-1}$ in $\mathrm{Fil}^0$. Let $x = (m_0, j_0) \ne y$ in $\{0, \dots, r-1\} \times n$. Assume that the column $j_0$ of $U_{m_0}$ is independent modulo $\mathrm{Fil}^1$ over the field fixed by $\mathrm{Fr}^r$: if $c \in (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ has $\mathrm{Fr}^r(c_i) = c_i$ and $\sum_i c_i (U_{m_0})_{i j_0} \in \mathrm{Fil}^1$, then $c = 0$. Then there is $A \in \mathrm{GL}_n(B)$ with $\varphi^r(A) = A$ such that for each $m < r$ some $W_m$ with $W_m, W_m^{-1}$ in $\mathrm{Fil}^0$ satisfies

$$\iota(\varphi^m(A)) = U_m \operatorname{diag}\bigl(t^{\varepsilon_{x,y}(m,j)}\bigr)_{j}\, W_m.$$

In words: write $y = (m_1, j_1)$. Up to a change of basis that is invertible over $\mathrm{Fil}^0$, $\iota(\varphi^m(A))$ is $U_m$ with column $j_0$ times $t^{-1}$ when $m = m_0$, and column $j_1$ times $t$ when $m = m_1$. And $A$ has entries fixed by $\varphi^r$.

## Proof

The tactic `first | exact @X | …` closes the goal with $X$ = `PMon.flAt_all`. Nothing else happens.

## In the Lean code

The theorem is in [FundamentalLemmaLatticeFrobFixedForallDegreeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FundamentalLemmaLatticeFrobFixedForallDegreeStatement.lean#L7). `FLAt` is in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L79). The condition "$U_m, U_m^{-1}$ in $\mathrm{Fil}^0$" is `UnitM`. For $r = 0$ the statement is empty, since there is no $x$.
