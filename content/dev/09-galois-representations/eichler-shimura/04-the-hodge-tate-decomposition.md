---
title: The Hodge-Tate decomposition
decls:
  - UpperTheory.Gal.Seam.HT.hodgeTate_comparison_smooth_projective
  - UpperTheory.Gal.KunnethLefschetz.G.sqCore
  - UpperTheory.Gal.KunnethLefschetz.G.sqEx3
  - UpperTheory.Gal.Seam.HT.htBij
  - UpperTheory.Gal.Seam.HT.htSpecGood
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hodge-Tate decomposition

To read off the Hodge-Tate jumps of a Galois piece we need the Hodge-Tate decomposition of the cohomology of a smooth projective variety over a $p$-adic field. This section states it in the form that the next section uses: a matrix $\Phi$ that carries a basis of étale cohomology to a basis adapted to Hodge cohomology, with the expected Galois law. The proof goes in three steps: an injective Hodge-Tate map, a dimension count, and the matrix.

Throughout, $\ell$ is a prime, $K$ is a finite extension of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, $\mathbb{C}_\ell$ is the completion of $\overline{\mathbb{Q}}_\ell$, and $\chi : G_K \to \mathbb{Z}_\ell^\times$ is the [cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules). A *model* is a scheme $X$ with a map $X \to \operatorname{Spec} \mathcal{O}_K$. It is *smooth* in the sense of this chapter if it is projective, strictly semistable for some uniformizer, and smooth. For such a model write $V_n = H^n(X_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$ and $\mathrm{Hdg}^{a,n}$ for the Hodge cohomology of the generic fibre $X_K$ in total degree $n$ and form degree $a$. It vanishes for $a > n$.

**Theorem 3.4.1 (Hodge-Tate decomposition; Faltings).** Let $X$ be a smooth projective variety over $K$. Then there is a canonical $G_K$-equivariant isomorphism
$$\mathbb{C}_\ell \otimes_{\mathbb{Q}_\ell} H^n(X_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell) \cong \bigoplus_{a=0}^{n} \mathbb{C}_\ell(-a) \otimes_K H^{n-a}(X, \Omega^a_{X/K}),$$
functorial in $X$ (G. Faltings, $p$-adic Hodge theory, J. Amer. Math. Soc. 1 (1988); see also O. Brinon and B. Conrad, *CMI Summer School Notes on p-adic Hodge Theory*, 2009).

We prove the form of this theorem that we need in three stages.

**Proposition 3.4.2 (injective Hodge-Tate map).** For each $K$ there is a family of pairings
$$h_{a,n} : V_n \times (\mathrm{Hdg}^{a,n})^\vee \to \mathbb{C}_\ell,$$
$\mathbb{Q}_\ell$-linear in the first and $K$-linear in the second variable, natural in the model, with $\chi(\sigma)^a\, h_{a,n}(\sigma v, \varphi) = \sigma(h_{a,n}(v, \varphi))$ for $\sigma \in G_K$, such that for every smooth model the induced map
$$\mathbb{C}_\ell \otimes_{\mathbb{Q}_\ell} V_n \to \bigoplus_{a} \operatorname{Hom}_K\bigl((\mathrm{Hdg}^{a,n})^\vee, \mathbb{C}_\ell\bigr)$$
is injective, and for a connected model of relative dimension $d$ the top-degree map on $V_{2d}$ is injective.

Lean: `UpperTheory.Gal.Seam.HT.hodgeTate_comparison_smooth_projective`.

*Proof.* This is [Theorem 2.3.6 of Volume 4](/entry/hodge-tate-of-etale-side/) applied to the étale side of the comparison for smooth models, which is proved in another chapter. $\square$

The Proposition gives only an injective map, not an isomorphism. To prove surjectivity we use the blow-up of the square of the model along its diagonal.

**Lemma 3.4.3 (blow-up of the diagonal).** Let $M$ be a smooth model of relative dimension $d + 1$. Let $P = M \times_{\mathcal{O}_K} M$ with projections $p_1, p_2$ and diagonal $\Delta : M \to P$, and let $\pi : Y \to P$ be the blow-up of $P$ along $\Delta$. Then $P$ and $Y$ are smooth models, the square with the diagonal is a pullback, the blow-up has the expected form after base change to $K$, and the line bundle of the exceptional divisor on $Y$ is trivialized on an étale cover.

Lean: `UpperTheory.Gal.KunnethLefschetz.G.sqCore` (also `UpperTheory.Gal.KunnethLefschetz.G.sqEx3`, the same statement under the extra hypothesis $d \geq 1$).

*Proof.* The product of two projective smooth models is projective and smooth of relative dimension $2d + 2$. The blow-up of a smooth scheme along a smooth closed subscheme is smooth and projective over the base, and its exceptional divisor is a Cartier divisor. A smooth scheme over $\mathcal{O}_K$ is strictly semistable for any uniformizer. Blow-up commutes with the flat base change $\mathcal{O}_K \to K$. $\square$

**Theorem 3.4.4 (bijective Hodge-Tate map).** The pairings of the Proposition can be chosen so that, in addition, for every smooth model of relative dimension $d$ and every $n$, the map
$$\bigoplus_{a \leq n} \mathbb{C}_\ell \otimes_K \mathrm{Hdg}^{a,n} \to \operatorname{Hom}_{\mathbb{Q}_\ell}(V_n, \mathbb{C}_\ell)$$
dual to the Hodge-Tate map is injective, and
$$\dim_{\mathbb{Q}_\ell} V_n = \sum_{a=0}^{n} \dim_K \mathrm{Hdg}^{a,n}.$$

Lean: `UpperTheory.Gal.Seam.HT.htBij`.

*Proof.* Take the pairings of the Proposition. The dual injectivity is a diagonal argument on the blow-up of the Lemma. On $Y$ the étale first Chern class of the exceptional line bundle, cup products, and pullbacks along $p_1$, $p_2$ and $\pi$ express the class of the diagonal in $V_{2+2d}$ of $P$ through Künneth components $a_s \otimes b_s$ from $M$. Pairing this decomposition with the Hodge side and using the injectivity in top degree from the Proposition gives the dual injectivity. The étale cohomology of a smooth model is finite-dimensional, so injectivity in both directions gives the dimension formula. $\square$

**Theorem 3.4.5 (Hodge-Tate frames).** Let $K$ be a finite extension of $\mathbb{Q}_\ell$ and $n \geq 0$. For every smooth model $M$ of some relative dimension, there is a frame: a $\mathbb{Q}_\ell$-basis $b$ of $V_n$ of size $d_n$, and $K$-bases of $\mathrm{Hdg}^{a,n}$ of sizes $e_a$ with $\sum_a e_a = d_n$. For every frame there is a matrix $\Phi$ over $\mathbb{C}_\ell$, with rows indexed by $b$ and columns by the pairs $(a, i)$, such that

1. $\Phi$ is invertible;
2. for all $\sigma \in G_K$, with $\rho(\sigma)$ the matrix of $\sigma$ on $V_n$ in the basis $b$,
$$\rho(\sigma)\, \sigma(\Phi) = \Phi\, \operatorname{diag}\bigl(\chi(\sigma)^{-a}\bigr)_{(a,i)};$$
3. for a map $u : M' \to M$ of smooth models, $\Phi$ is natural: the matrix of $u^*$ on étale cohomology times $\Phi_M$ equals $\Phi_{M'}$ times the matrix of $u^*$ on Hodge cohomology.

Lean: `UpperTheory.Gal.Seam.HT.htSpecGood`.

*Proof.* By the Theorem on the bijective map, the Hodge-Tate map $\mathbb{C}_\ell \otimes V_n \to \bigoplus_a \mathbb{C}_\ell(-a) \otimes \mathrm{Hdg}^{a,n}$ is injective between spaces of the same dimension, so it is an isomorphism, and frames exist. Let $\Phi$ be its inverse matrix in the chosen bases. It is invertible. The Galois law of the pairing gives the second property, and the naturality of the pairing together with the [natural isomorphism of Hodge cohomology](/entry/hodge-iso-natural-cech/) with its Čech form gives the third. $\square$

**Remark 3.4.6.** The proof of the last theorem uses only the injectivity and the dimension formula of Theorem 3.4.4. The second injectivity of that theorem is not used.

**Remark 3.4.7 (Formalization).** `UpperTheory.Gal.Seam.HT.hodgeTate_comparison_smooth_projective` is called a comparison but gives only the injective map of Proposition 3.4.2; a second theorem with the same short name in `CrystallineSemistableComparison.HT` has other hypotheses and is not used. The statement `CrystallineSemistableComparison.Onto.SqEx3` asks for $1 \leq d$, but `UpperTheory.Gal.KunnethLefschetz.G.sqEx3` drops this hypothesis and calls `UpperTheory.Gal.KunnethLefschetz.G.sqCore`, which does not need it. In Lemma 3.4.3 the exceptional line bundle is given as descent data, a smooth surjective map $f$ with a unit cocycle, and the lemma says that $f$ is étale. The group $\mathrm{Hdg}^{a,n}$ (`CrystallineSemistableComparison.HT.Hdg`) is the degree $n$ Čech cohomology of the $a$-th graded piece of a filtered complex, read here as $H^{n-a}(X_K, \Omega^a)$. A smooth model is `Model.Sm`. The Künneth argument in the proof of Theorem 3.4.4 is only sketched here.
