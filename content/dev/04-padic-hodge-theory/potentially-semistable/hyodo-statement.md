---
id: hyodo-statement
title: De Rham cocycles of a semistable representation are semistable (named form)
kind: theorem
decl: GlobalTheory.T.hyodo_statement
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.HyodoStatementStatement
covers: 301
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for `GlobalTheory.PMon.hyodo`, which has no entry of its own, so we give its proof here. It says that for a semistable representation $V$ of $G_K$ over $\mathbb{Q}_\ell$, a cocycle that splits over $B_{\mathrm{dR}}$ splits over $B_{\mathrm{st}}$. Its one use is in [the matrix form](/entry/hyodo-mat/), which applies it to a restriction of scalars.

## Statement

The statement is `Hyodo`. Let $\ell$, $P$, $A$ and the tie be as in [the matrix form](/entry/hyodo-mat/). Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $V$ a finite-dimensional $\mathbb{Q}_\ell$-vector space with its module topology, and $\rho$ a representation of $G_K$ on $V$ with continuous orbit maps. Assume that $\rho$ is semistable (`IsSst`): $\dim_{\mathbb{Q}_\ell} (V \otimes B_{\mathrm{st}})^{G_K} = [K_0 : \mathbb{Q}_\ell] \dim V$. Let $c \colon G_K \to V$ be a continuous cocycle, and assume that some $b \in V \otimes B_{\mathrm{dR}}$ has $c(g) \otimes 1 = g b - b$ for all $g$. Then some $b' \in V \otimes B_{\mathrm{st}}$ has $c(g) \otimes 1 = g b' - b'$ for all $g$.

In the notation of Bloch and Kato (*The Grothendieck Festschrift* I, Progr. Math. 86, 1990), the hypothesis says that the class of $c$ is in $H^1_g(K, V)$. The conclusion says that it is in the kernel of $H^1(K, V) \to H^1(K, V \otimes B_{\mathrm{st}})$.

## Proof

The proof of `PMon.hyodo` counts dimensions of spaces of cocycles. Write $Z_g$, $Z_f$, $Z_e$ for the continuous cocycles that split over $B_{\mathrm{dR}}$, over $B_{\mathrm{cris}}$, and over $B_{\mathrm{cris}}^{\varphi = 1}$. These are `geometricCocycles`, `finiteCocycles` and `crystallineCocycles`.

1. `exists_tateTwistDual_perfectPairing` gives $V'$ with a perfect pairing $V \times V' \to \mathbb{Q}_\ell$ on which $G_K$ acts by the cyclotomic character (`IsDual1`).
2. $V$ is de Rham by `isDeRham_of_isSemistable`, and $V'$ is de Rham by `de_rham_filtration_duality`. The continuous cocycles of $V$ form a finite-dimensional space (`finiteDimensional_continuousCocycles_galoisRep`).
3. `semistable_cocycles_between_blochKato_and_continuous` gives a space $S$ of continuous cocycles that split over both $B_{\mathrm{st}}$ and $B_{\mathrm{dR}}$, with $\dim S \ge \dim Z_f(V) + \dim D_{\mathrm{cris}}(V')^{\varphi = 1}$. So $S \subseteq Z_g(V)$.
4. `finrank_blochKato_g_add_e_le_f_add_f` gives $\dim Z_g(V) + \dim Z_e(V') \le \dim Z_f(V) + \dim Z_f(V')$.
5. `finrank_finite_le_exponential_cocycles` gives $\dim Z_f(V') \le \dim Z_e(V') + \dim D_{\mathrm{cris}}(V')^{\varphi = 1}$.

From 3 to 5, $\dim Z_g(V) \le \dim S$, so $S = Z_g(V)$. The cocycle $c$ is in $Z_g(V)$, so it is in $S$, and it splits over $B_{\mathrm{st}}$.

## In the Lean code

The theorem is in [HyodoStatementStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HyodoStatementStatement.lean#L7). Its proof is `first | exact @GlobalTheory.PMon.hyodo | ...`, and the first branch closes the goal. `Hyodo` is in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L41). `PMon.hyodo` is in [HyodoStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HyodoStatement.lean#L20). We read the statements of its lemmas, not their proofs.

The Lean name `crystallineCocycles` is for the cocycles that split over $B_{\mathrm{cris}}^{\varphi = 1}$, which is $H^1_e$ in the notation of Bloch and Kato. The lemma name `finrank_finite_le_exponential_cocycles` calls the same space "exponential". The property $Z_f(V) \subseteq S$ from step 3 is not used. The name refers to Hyodo; we have not checked a source for the attribution.
