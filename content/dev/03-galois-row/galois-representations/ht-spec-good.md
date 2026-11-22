---
id: ht-spec-good
title: Hodge-Tate period matrices for smooth projective models
kind: theorem
decl: UpperTheory.Gal.Seam.HT.htSpecGood
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.CrystallineTowers.ClosedHT
covers: 2373
status: drafted
drafted_by: writer@claude
---
This theorem gives, for a smooth projective variety with good reduction over a finite extension of $\mathbb{Q}_\ell$, an invertible period matrix that turns the Galois action on étale cohomology into the Hodge-Tate twists. It goes to [jumpStep_holds](/entry/jump-step-holds/), the local step which says where the Hodge-Tate jumps of a representation from a tower occur. That step is part of the [Galois row](/step/geo-one-holds/).

## Statement

Let $\ell$ be a prime, $K$ a finite extension of $\mathbb{Q}_\ell$ inside $\overline{\mathbb{Q}}_\ell$ with ring of integers $\mathcal{O}_K$, and $n \geq 0$. A *model* $M$ is a scheme $X$ with a map $p \colon X \to \operatorname{Spec} \mathcal{O}_K$. It is *good* (`Model.Sm`) if $p$ is projective, strictly semistable for some uniformizer, and smooth. Write $X_K$ for the generic fibre. Let $V^n = H^n_{\mathrm{et}}(X_{\overline{K}}, \mathbb{Q}_\ell)$ with its action $\rho$ of $G_K$, and $H^{a, n-a} = H^{n-a}(X_K, \Omega^a)$.

A *frame* of $M$ in degree $n$ is a $\mathbb{Q}_\ell$-basis $b_1, \dots, b_d$ of $V^n$ and, for each $0 \leq a \leq n$, a $K$-basis of $H^{a,n-a}$ with $e_a$ elements.

**Theorem.** Let $M$ be good, with $p$ smooth of some relative dimension. Then:

1. $M$ has a frame in degree $n$ with $\sum_a e_a = d$;
2. for each frame $F$ there is a $d \times \sum_a e_a$ matrix $\Phi_F$ over $\mathbb{C}_\ell$ that is invertible and satisfies, for all $\sigma \in G_K$,
$$\rho(\sigma)\, \sigma(\Phi_F) = \Phi_F \cdot \operatorname{diag}\bigl(\chi(\sigma)^{-a}\bigr),$$
where $\chi$ is the cyclotomic character and the column of a basis vector of $H^{a,n-a}$ carries $\chi(\sigma)^{-a}$;
3. the choice is natural: for a map $u \colon X' \to X$ over $\mathcal{O}_K$ between good models, $E(u)\, \Phi_F = \Phi_{F'}\, H(u)$, where $E(u)$ and $H(u)$ are the matrices of $u^*$ on étale and on Hodge cohomology.

So $\Phi_F$ is the matrix of a $G_K$-equivariant isomorphism $\bigoplus_a H^{a,n-a} \otimes_K \mathbb{C}_\ell(-a) \cong V^n \otimes \mathbb{C}_\ell$. This is the Hodge-Tate decomposition of Faltings (J. Amer. Math. Soc. 1, 1988), here in the case of good reduction and with a naturality clause.

## Proof

The proof is `Spec.htSpecGood_of` applied to [htBij](/entry/ht-bij/), to `hodge_iso_natural_cech` and to `Top.etFin_holds`.

1. [htBij](/entry/ht-bij/) gives a Hodge-Tate pairing $P$: for each $v \in V^n$, a $\mathbb{C}_\ell$-valued function on the dual of each Hodge piece. It is injective on $V^n \otimes \mathbb{C}_\ell$, and $\dim V^n = \sum_a \dim_K \mathrm{Hdg}(a, n)$.
2. `hodge_iso_natural_cech` identifies the Hodge pieces $\mathrm{Hdg}(a, a+j)$ of $P$ with $H^j(X_K, \Omega^a)$, naturally in $X$.
3. `etFin_holds` says that $V^n$ has finite dimension. With the rank formula this gives a frame with $\sum_a e_a = d$ (`frame_ex`).
4. Let $H_F$ be the matrix of $P$ in the frame. It is square by the rank formula and has trivial kernel by injectivity, so it is invertible. Put $\Phi_F = H_F^{-1}$ (`phi_spec`).
5. The equivariance axiom of $P$ gives the twist identity for $H_F$ (`equi_entry`), and inversion moves it to $\Phi_F$ (`isHT`).
6. The naturality axiom of $P$ and the naturality of step 2 give $H(u)\, H_F = H_{F'}\, E(u)$ (`nat_entry`). Inversion gives clause 3.

## In the Lean code

The theorem is in [ClosedHT.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/ClosedHT.lean#L21). The statement `HTSpecGood` is in [HTSpecGood.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/HodgeTateSpectral/HTSpecGood.lean#L15). The proof `htSpecGood_of` is in [SpecOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/SpecOf.lean#L324). Frames, `IsHT`, `etMat` and `hodgeMat` are in [HTSpecAllHodge.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/HTSpecAllHodge.lean#L35).

We have not unfolded `HQ`, the étale cohomology in $V^n$, or `Hdg`. The reading of $\mathrm{Hdg}(a, a+j)$ as $H^j(X_K, \Omega^a)$ comes from the isomorphism `HdgIso`. From [htBij](/entry/ht-bij/) the proof uses only injectivity and the rank formula. The surjectivity and the top-degree clause are not used.
