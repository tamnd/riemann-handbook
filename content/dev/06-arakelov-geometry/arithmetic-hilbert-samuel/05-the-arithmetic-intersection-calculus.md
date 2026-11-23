---
title: The arithmetic intersection calculus from principalisation
decls:
  - GlobalTheory.MixHtCalc.arFormExists_arMix_heightProjection
  - GlobalTheory.T.arithIntersection_forms_of_archimedean_statements
  - GlobalTheory.MixHt.arCalc_cycleHeights_of_analytic
  - GlobalTheory.T.arithIntersectionCalculus_cycleHeights_of_analytic
  - GlobalTheory.MixHt.arCalc_of_principalisation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The arithmetic intersection calculus from principalisation

This section proves the seven rules of arithmetic intersection theory on arithmetic varieties from principalisation of ideals alone. The rules are the arithmetic intersection calculus of [the chapter on heights](/entry/ar-calc-direct/), which proves them by a second route. Here they come from [the mixed heights](/entry/exists-is-mix-of-arch/) of the previous section. The calculus is used by every later section of this chapter, and so by [the arithmetic Hilbert-Samuel formula](/entry/arith-hilbert-samuel-of-principalisation/).

### Heights and the calculus

Let $X$ be an arithmetic variety of relative dimension $D$ over $k$, and let $\bar L$ be a hermitian line bundle on $X$. We recall the definitions of [the chapter on heights](/entry/ar-calc-direct/) and of the [heights](/learn/arakelov/#heights) of Volume 1.

**Definition 6.5.1 (Height function).** A height function for $\bar L$ is a function $h$ on the points of $X$ with three properties. If $Z \subseteq X$ is integral, closed, of dimension $d$ and an algebra over a finite field $\kappa$, then $h(\eta_Z) = (L|_Z)^d \log \#\kappa$. If $Z$ is integral of dimension $1$ with $\Gamma(Z, \mathcal{O}_Z)$ of characteristic zero, then $h(\eta_Z)$ is the arithmetic degree of $\bar L|_Z$:
$$h(\eta_Z) = \sum_z \operatorname{mult}_z(\operatorname{div} r) \log \#\kappa(z) - \sum_\sigma \sum_{y \in Z_\sigma(\mathbb{C})} \log \|r\|_\sigma(y)$$
for every rational section $r$. If $Z$ has dimension $e + 1 \ge 2$ in characteristic zero, then for every $n$ and every rational section $r$ of $\bar L|_Z^{\,n}$ the archimedean integral exists and
$$n \, h(\eta_Z) = \sum_z \operatorname{mult}_z(\operatorname{div} r) \, h(z) - \sum_\sigma \int_{Z_\sigma(\mathbb{C})} \log \|r\|_\sigma \, c_1(\bar L)^e.$$
A real number $a$ is a self intersection of $\bar L$ if some height function $h$ has $h(\eta_X) = a$.

The self intersection is the arithmetic intersection number $\widehat{\deg}(\hat c_1(\bar L)^{D+1})$ of Gillet and Soulé. For a family $(\bar L_j)_{j \in \iota}$ and $n \in \mathbb{Z}^\iota$ we write $\bar L^n = \bigotimes_j \bar L_j^{n_j}$ and $\ell_n = \sum_j n_j x_j$. An arithmetic intersection form is a linear map $\Phi$ on the real polynomials in the variables $x_j$ that vanishes on homogeneous polynomials of degree other than $D + 1$, such that $\Phi(\ell_n^{D+1})$ is a self intersection of $\bar L^n$ for every $n$. So $\Phi$ is the polarisation of the self intersection.

**Definition 6.5.2 (Arithmetic intersection calculus).** The arithmetic intersection calculus is the conjunction of seven rules on all arithmetic varieties: existence of height functions and of arithmetic and geometric intersection forms; the change of metric formula for a trivial bundle $\mathcal{O}(u)$; the shift formula, which says that if $a$ is a self intersection of $\bar L$, then $a + (D+1) t \deg L_{\mathbb{C}}$ is a self intersection of $\bar L$ with its norm multiplied by $e^{-t}$; the mixed formula through a rational section; the projection formula for a morphism that maps the generic point to the generic point with residue degree $\delta \ne 0$; invariance under isometries and integral changes of the family; and the formula for a raised metric. Here $\deg L_{\mathbb{C}} = \int c_1(\bar L)^D$, summed over the embeddings. The precise statements are in [the chapter on heights](/entry/ar-calc-direct/).

We also need a projection formula for heights of cycles.

**Definition 6.5.3 (Height projection).** Height projection holds if the following is true. Let $X$ and $Y$ be arithmetic varieties over $k$ of relative dimensions $D$ and $e$, let $\pi : Y \to X$ be a morphism over $k$ such that the closure of $\pi(\eta_Y)$ has dimension $e + 1$, with residue degree $\delta = [\kappa(\eta_Y) : \kappa(\pi(\eta_Y))] \ne 0$. Let $h$ be a height function for $\bar L$ on $X$. Then $\delta \, h(\pi(\eta_Y))$ is a self intersection of $\pi^*\bar L$.

### The proofs

**Theorem 6.5.4 (Forms, mixed formula and projection).** Assume archimedean integrability and archimedean reciprocity. Then every finite family of hermitian line bundles on an arithmetic variety has an arithmetic intersection form, the mixed formula holds, and height projection holds.

Lean: `GlobalTheory.MixHtCalc.arFormExists_arMix_heightProjection` (also `GlobalTheory.T.arithIntersection_forms_of_archimedean_statements`, a second name).

*Proof.* By [the existence of mixed heights](/entry/exists-is-mix-of-arch/), every ambient scheme has a system $T$ of mixed heights up to every dimension. From these systems and archimedean integrability, the development proves that every finite family has an arithmetic intersection form and that the mixed formula holds; the mixed formula is the recursion of the mixed heights read in the first bundle. We cite these two results.

For height projection, let $\pi : Y \to X$ be as in the definition, and let $T$ be a system of mixed heights on $Y$ up to dimension $e + 1$. The diagonal of $T$ gives a height function $h'$ for $\pi^* \bar L$. The projection formula for heights at every point gives $h'(\eta_Y) = \delta \, h(\pi(\eta_Y))$. So $\delta \, h(\pi(\eta_Y))$ is a self intersection of $\pi^* \bar L$. $\square$

**Theorem 6.5.5 (Calculus from the archimedean statements).** Assume archimedean integrability and archimedean reciprocity. Then the arithmetic intersection calculus holds, and so do the rules on heights of cycles: existence, the mixed formula and height projection.

Lean: `GlobalTheory.MixHt.arCalc_cycleHeights_of_analytic` (also `GlobalTheory.T.arithIntersectionCalculus_cycleHeights_of_analytic`, a second name).

*Proof.* The calculus follows from the existence of intersection forms, the mixed formula and height projection by a result of the development, which derives the remaining rules from these three. Apply it to [the previous theorem](/entry/ar-form-exists-ar-mix-height-projection/). The rules on heights of cycles follow from the calculus, again by a result of the development. $\square$

**Theorem 6.5.6 (Arithmetic intersection calculus from principalisation).** Assume principalisation of ideals. Then the arithmetic intersection calculus holds.

Lean: `GlobalTheory.MixHt.arCalc_of_principalisation`.

*Proof.* Principalisation implies archimedean integrability, by a result of the development on the integrability of $\log \|r\|$ against Chern forms. It implies archimedean reciprocity by [the archimedean reciprocity law](/entry/arch-recip-of-principalisation/). Apply [the calculus from the archimedean statements](/entry/ar-calc-cycle-heights-of-analytic/) and keep the first part. $\square$

**Remark 6.5.7 (Formalization).** The last theorem proves the rules on heights of cycles as well and then discards them ([ArCalcOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArCalcOfPrincipalisation.lean#L12)). The calculus is defined in the namespace of published results, but here it is proved, not assumed. The construction of the forms from the mixed heights, the derivation of the other rules and the projection formula for heights at every point are cited results; we did not open their proofs.
