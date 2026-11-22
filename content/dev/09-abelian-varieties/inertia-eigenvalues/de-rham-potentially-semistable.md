---
id: de-rham-potentially-semistable
title: De Rham representations are potentially semistable
kind: theorem
decl: GlobalTheory.deRham_potentiallySemistable
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.DeRhamPotentiallySemistable
covers: 1386
status: drafted
drafted_by: writer@claude
---
This theorem says that a de Rham representation of the Galois group of a finite extension of $\mathbb{Q}_\ell$ is potentially semistable. It is the $p$-adic monodromy theorem, conjectured by Fontaine and proved by Berger (L. Berger, "Représentations $p$-adiques et équations différentielles", *Invent. Math.* 148 (2002), 219-284). It sits below the trunk step [EveryCharacter](/step/every-character/). The proof here is short: it reduces the statement to a matrix form, [`pAdicMonodromyTheorem_matrixForm`](/entry/p-adic-monodromy-theorem-matrix-form/), and the real work is in [`matThm_holds`](/entry/mat-thm-holds/).

## Statement

The statement is the proposition `DeRhamPotSemistable`. Let $\ell$ be a prime. Let $P$ be a datum of type `LocPrime l`: abstract period rings $B$ and $B_{\mathrm{dR}}$ with a Galois action, a Frobenius on $B$, a map $B \to B_{\mathrm{dR}}$, an element $t$ and the cyclotomic character. Let $A$ be a datum of type `LocAinf l P`. Assume that a tie `LocTied l P A` exists. It identifies $B$ with $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ with the de Rham period ring, compatibly with all the structure (see [[Fontaine's period rings|K6HW8YWCQJ]]). Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $V$ a finite-dimensional $\mathbb{Q}_\ell$-vector space with its module topology, and $\rho$ a representation of $G_K$ on $V$ with continuous orbit maps. Then

$$\dim_K D_{\mathrm{dR}}(V) = [K : \mathbb{Q}_\ell]\,\dim V \ \Longrightarrow\ \operatorname{rank}_{\mathbb{Q}_\ell^{\mathrm{ur}}} D_{\mathrm{pst}}(V) = \dim V.$$

The left side is `IsDR`. The right side is `IsPst`. Here $D_{\mathrm{pst}}(V)$ is the union over finite extensions $K' \supseteq K$ of $(V \otimes B_{\mathrm{st}})^{G_{K'}}$, with $B_{\mathrm{st}} = B[X]$ and $g(X) = X + c(g)\,t$ for a Kummer cocycle $c$.

## Proof

The proof is one line. It applies `deRham_potSemistable_of_matrix_monodromy` to the matrix form `pAdicMonodromyTheorem_matrixForm`. The first lemma is a wrapper of `FromMat.deRhamPotSemistable_of_matThm`, which works as follows.

1. Choose a basis of $V$. Write $\rho$ as a matrix representation in $\mathrm{GL}_n(\mathbb{Q}_\ell) \subset \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$.
2. This matrix representation satisfies `IsRat 1`: its entries are fixed by Frobenius and are continuous.
3. `exists_invertible_deRhamPeriodMatrix_of_isDR` gives a period matrix $Q \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $\rho(g)\,g(Q) = Q$. This is `AdmDR`.
4. The matrix form gives a finite extension $K' \supseteq K$ and $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ with $\rho(g)\,g(Q) = Q$ for $g \in G_{K'}$.
5. `isSemistable_of_invertible_periodMatrix_semistableRing` makes $\rho|_{G_{K'}}$ semistable. Then `isPotentiallySemistable_of_semistable_restrict` gives `IsPst`.

## In the Lean code

The theorem is in [DeRhamPotentiallySemistable.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamPotentiallySemistable.lean#L11). The statement is in [DeRhamPotSemistable.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/DeRhamPotSemistable.lean#L13), and the reduction is in [DeRhamPotSemistableOfMatrixMonodromy.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamPotSemistableOfMatrixMonodromy.lean#L40).

- [`pAdicMonodromyTheorem_matrixForm`](/entry/p-adic-monodromy-theorem-matrix-form/), the matrix form.
- `deRham_potSemistable_of_matrix_monodromy`, the reduction.

The statement lives in the folder `PublishedTheorems`, but here it is proved, not assumed. The rings are abstract. The statement has content only through the hypothesis `Nonempty (LocTied l P AI)`, which ties them to Fontaine's rings. The reduction uses the matrix form only with $r = 1$, that is, with coefficients in $\mathbb{Q}_\ell$. Five declarations use this theorem, among them the literature bundle in `EveryCharacterOfLiteratureOfVWin.lean` and `Inp.pst` in `Crys.lean`.
