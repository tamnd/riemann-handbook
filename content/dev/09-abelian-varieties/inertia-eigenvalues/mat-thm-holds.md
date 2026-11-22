---
id: mat-thm-holds
title: The p-adic monodromy theorem in matrix form
kind: theorem
decl: GlobalTheory.PMon.matThm_holds
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.PAdicMonodromyTheoremMatrixForm
covers: 1361
status: drafted
drafted_by: writer@claude
---
This theorem says that a matrix representation of $G_K$ with de Rham period matrices has a semistable period matrix over a finite extension of $K$. It is the matrix form of the $p$-adic monodromy theorem (Berger, *Invent. Math.* 148 (2002), 219-284). [`pAdicMonodromyTheorem_matrixForm`](/entry/p-adic-monodromy-theorem-matrix-form/) renames it, and [`deRham_potentiallySemistable`](/entry/de-rham-potentially-semistable/) uses it.

## Statement

The statement is `MatThm`. Let $\ell$ be a prime, and let $P$, $A$ be period data with a tie `LocTied l P A` to Fontaine's rings (see [[Fontaine's period rings|K6HW8YWCQJ]]). Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r > 0$, and $\rho \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$. Write $\mathrm{Fr}$ for the Frobenius of $\mathbb{Q}_\ell^{\mathrm{ur}}$, acting on matrix entries, and $\chi$ for the cyclotomic character.

- `IsRat r ρ`: the entries of $\rho$ are continuous and fixed by $\mathrm{Fr}^r$, and the elements fixed by $\mathrm{Fr}^r$ lie in $K$.
- `AdmDR P ρ`: for each $m \ge 0$ some $Q \in \mathrm{GL}_n(B_{\mathrm{dR}})$ has $\mathrm{Fr}^m(\rho(g))\,g(Q) = Q$ for all $g \in G_K$.
- `AdmSt P ρ`: some finite $K' \supseteq K$ and $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ have $\rho(g)\,g(Q) = Q$ for all $g \in G_{K'}$.

Then `IsRat r ρ` and `AdmDR P ρ` imply `AdmSt P ρ`.

## Proof

The proof applies `padicMonodromyMatrixForm_of_induction_cases`, a wrapper of `matThm_of_steps`, to five steps. Two more notions occur.

- `Framed P ρ w`, for $w \colon \{0, \dots, r-1\} \times \{1, \dots, n\} \to \mathbb{Z}$: for each $m < r$ some $U$ with $U, U^{-1}$ in $\mathrm{Fil}^0$ has $\mathrm{Fr}^m(\rho(g))\,g(U) = U \operatorname{diag}(\chi(g)^{w(m,j)})_j$.
- `Splits r ρ`: after a change of basis fixed by $\mathrm{Fr}^r$, $\rho$ is block upper triangular with two nonempty blocks.

The five steps, with $\varepsilon_{x,y}$ equal to $-1$ at $x$, $+1$ at $y$ and $0$ elsewhere:

1. `FrameEx`: under `IsRat`, `AdmDR` holds if and only if $\rho$ is framed for some weight.
2. `TwistStep`: a framed $\rho$ reduces to a framed $\rho'$ of total weight $0$, over some $K'$ and $r'$.
3. `SenStep`: a $\rho$ framed with weight $0$ satisfies `AdmSt`.
4. `RedStep`: a de Rham $\rho$ that splits satisfies `AdmSt` if `MatThm` holds in smaller sizes.
5. `ModStep`: a framed $\rho$ that does not split reduces to a framed $\rho'$ of weight $w + \varepsilon_{x,y}$, for each $x \ne y$.

Here "reduces to" means that `AdmSt` for $\rho'$ implies `AdmSt` for $\rho$.

The outer induction is on $n$. Steps 1 and 2 give a weight $w$ of total $0$. The inner induction is on $\sum w^2$. If $w = 0$, use step 3. If $\rho$ splits, use step 4 and the outer hypothesis. Else the lemma `arith` gives $x$, $y$ with $w(x) > 0 > w(y)$, so $w + \varepsilon_{x,y}$ has total $0$ and a smaller sum of squares. Use step 5 and the inner hypothesis.

Step 3 rests on `SenFinite`: if a continuous $\rho \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell)$ has $M \in \mathrm{GL}_n(\mathbb{C}_\ell)$ with $\rho(g)\,g(M) = M$, then $\rho(I_K)$ is finite. This is Sen's theorem (S. Sen, *Invent. Math.* 62 (1980), 89-116), proved here as `senFinite`. Step 3 also uses `UnrStep`: finite image of inertia implies `AdmSt`.

## In the Lean code

The theorem is in [PAdicMonodromyTheoremMatrixForm.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PAdicMonodromyTheoremMatrixForm.lean#L14), and the induction in [PadicMonodromyMatrixFormOfInductionCases.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PadicMonodromyMatrixFormOfInductionCases.lean#L44). The steps are defined in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L11), the other notions in [AdmSt.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmSt.lean#L33). The step proofs are wrappers of `FrameEquiv.frameEx`, `twistStep`, `senStep`, `Red.redStep` and `modStep_holds`.

Under `IsRat r ρ` only $m$ modulo $r$ matters in `AdmDR`. `ModStep` is stated for every pair $x \ne y$, but the induction needs it only when $w(x) > 0 > w(y)$. We have not unfolded the lemmas inside `modStep_holds` that build $\rho'$.
