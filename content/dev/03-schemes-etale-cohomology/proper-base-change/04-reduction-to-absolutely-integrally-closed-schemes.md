---
title: Reduction to absolutely integrally closed schemes
decls:
  - UpperTheory.Et.E2.n17
  - UpperTheory.Et.E2.n13
  - UpperTheory.Et.E2.n10
  - UpperTheory.Et.E2.n9
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reduction to absolutely integrally closed schemes

Let $A$ be a local ring, $q$ a unit in $A$, and $p : P \to \operatorname{Spec} A$ a quasi-compact and quasi-separated map. To prove the closed fibre condition $\mathrm{PB}_{q,i}(p)$, we first replace $P$ by schemes $Z$ that are integral over $P$ and AIC. This section proves the main step of this reduction: if the condition holds for all such $Z$, then it holds for one integral surjective $Y \to P$. A second step, descent along integral surjective maps, then gives the condition for $P$ itself. The reduction needs one general fact about étale cohomology: it commutes with cofiltered limits of schemes.

We use the notation of the previous sections. All schemes in this section are quasi-compact and quasi-separated (qcqs) where we say so.

### Cohomology of a limit

**Theorem 3.4.1 (Cohomology commutes with limits).** Let $(X_j)_{j \in J}$ be a cofiltered system of qcqs schemes with affine transition maps, and let $X = \lim_j X_j$ with projections $\pi_j : X \to X_j$. Let $q$ be a unit on each $X_j$, and assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Then for all $n$ and $i$ the maps $\pi_j^*$ induce an isomorphism
$$\operatorname*{colim}_j H^n(X_j, \mathbb{Z}/q(i)) \xrightarrow{\ \sim\ } H^n(X, \mathbb{Z}/q(i)).$$

Lean: `UpperTheory.Et.E2.n17`.

This is the étale form of a theorem of SGA 4, Exposé VII, §5. Here we prove it from the axioms.

*Proof.* Fix one index $j_0$. We prove the statement for all systems whose stage $j_0$ is a given qcqs scheme $X_0$, by induction on $X_0$. The induction principle says: a property of schemes that holds for affine schemes, and that holds for $X$ whenever $X = U \cup V$ with $U, V$ quasi-compact open and the property holds for $U$, $V$ and $U \cap V$, holds for every qcqs scheme.

If $X_0$ is affine, then each $X_j$ with $j \to j_0$ is affine, and $X$ is the spectrum of the filtered colimit of their rings. This case is axiom B1 for the filtered colimit of these rings.

If $X_0 = U \cup V$, we pull the cover back to each $X_j$ and to $X$. The Mayer-Vietoris sequences of these covers form a compatible system of exact sequences, and a filtered colimit of exact sequences is exact. The five lemma then gives the statement for $X_0$ from the statement for $U$, $V$ and $U \cap V$. $\square$

### Absolutely flat covers

**Definition 3.4.2 (Product type ring).** A ring $W$ is of *product type* if it is absolutely integrally closed (each monic polynomial of positive degree over $W$ has a root) and each $a \in W$ is a product $a = eu$ with $e$ idempotent and $u$ a unit.

For example, a product of algebraically closed fields is of product type: in each factor, $a = 0$ or $a$ is a unit. If $W$ is of product type and $\mathfrak{q}$ is a prime of $W$, then the local ring $W_{\mathfrak{q}}$ is a field, because the image of an idempotent in a local ring is $0$ or $1$. It is algebraically closed because $W$ is absolutely integrally closed.

**Definition 3.4.3 (Clopen system).** Let $Y$ be a scheme and $y \in Y$. A *clopen system at $y$* is a cofiltered system $(D_j)$ of schemes with maps $\iota_j : D_j \to Y$ such that each $\iota_j$ is an open and closed immersion with $y$ in its image, the transition maps are affine and compatible with the $\iota_j$, and the system has a limit $D_\infty$.

So the $D_j$ are clopen neighbourhoods of $y$, and $D_\infty$ is their intersection.

For a map $w : \operatorname{Spec} W \to P$, we write $P^W$ for the *normalization* of $P$ in $\operatorname{Spec} W$. It is the relative spectrum of the integral closure of $\mathcal{O}_P$ in $w_* \mathcal{O}_{\operatorname{Spec} W}$. The map $P^W \to P$ is integral, and $w$ factors through it.

**Lemma 3.4.4 (Components of the normalization).** Let $P$ be a qcqs scheme, $W$ a ring of product type and $w : \operatorname{Spec} W \to P$ a map. Then each point $y$ of $P^W$ has a clopen system whose limit is an AIC scheme.

Lean: `UpperTheory.Et.E2.n13`.

*Proof.* Since each $a \in W$ is $eu$ with $e$ idempotent and $u$ a unit, the clopen subsets $\operatorname{Spec} We$ of $\operatorname{Spec} W$ that contain a prime $\mathfrak{q}$ have the local ring $W_{\mathfrak{q}}$ as the colimit of their rings $We$. Normalization commutes with this limit. So for a suitable prime $\mathfrak{q}$ of $W$, the preimages in $P^W$ of these clopen sets form a clopen system at $y$ whose limit is the normalization of $P$ in $\operatorname{Spec} W_{\mathfrak{q}}$, for the composite $\operatorname{Spec} W_{\mathfrak{q}} \to \operatorname{Spec} W \to P$. By the remark after the definition, $\Omega = W_{\mathfrak{q}}$ is an algebraically closed field. The normalization of $P$ in $\operatorname{Spec} \Omega$ is integral, with an affine open cover by spectra of rings $R'$, where $R'$ is the integral closure in $\Omega$ of a subring $R$. Such an $R'$ is an integrally closed domain, and its fraction field is the algebraic closure of the fraction field of $R$ in $\Omega$, which is algebraically closed. By the first section, $R'$ is absolutely integrally closed. So the limit is an AIC scheme. $\square$

**Lemma 3.4.5 (An integral cover with AIC components).** Let $P$ be a qcqs scheme. There is an integral surjective map $k : Y \to P$ such that each point $y \in Y$ has a clopen system with these properties: its limit $D_\infty$ is an AIC scheme, and for each $j$ the composite $D_\infty \to D_j \to Y \to P$ is integral.

Lean: `UpperTheory.Et.E2.n10`.

*Proof.* We take a ring $W$ of product type with a surjective map $w : \operatorname{Spec} W \to P$. For example, cover $P$ by finitely many affine opens $\operatorname{Spec} R_m$ and let $W$ be the product over $m$ and over $x \in \operatorname{Spec} R_m$ of an algebraic closure of the residue field $\kappa(x)$. A product of algebraically closed fields is of product type, and the maps $R_m \to \overline{\kappa(x)}$ give $w$. Let $Y = P^W$ and let $k : Y \to P$ be the normalization map. It is integral. It is surjective, because $w$ is surjective and factors through $k$. By [Lemma 3.4.4](/entry/n13/), each point of $Y$ has a clopen system whose limit is an AIC scheme. For every clopen system the map $D_j \to Y$ is a closed immersion, and $D_\infty \to D_j$ is the limit of the closed immersions $D_{j'} \to D_j$, so it is a closed immersion. Closed immersions are integral, so the composites with $k$ are integral. $\square$

### The reduction

The last ingredient is a lemma on clopen systems.

**Lemma 3.4.6 (Clopen systems).** Assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Let $A$ be a local ring with $q$ a unit, and let $g : Y \to \operatorname{Spec} A$ with $Y$ qcqs. Assume that each $y \in Y$ has a clopen system $(D_j)$ such that the closed fibre condition holds for the composite $D_\infty \to Y \to \operatorname{Spec} A$. Then the closed fibre condition holds for $g$.

*Proof.* Write $Y_0$, $D_{j,0}$ and $D_{\infty,0}$ for the closed fibres. The cohomology of a finite disjoint union of clopen subsets is the product of their cohomology groups. Since $Y$ is quasi-compact, each cover of $Y$ by clopen subsets has a finite subcover, which we refine to a finite cover by disjoint clopen subsets. By [Theorem 3.4.1](/entry/n17/), applied to a system $(D_j)$ and to its closed fibres $(D_{j,0})$, the cohomology of $D_\infty$ is the colimit of the cohomology of the $D_j$, and the same holds for $D_{\infty,0}$.

*Injectivity.* Let $x \in H^n(Y)$ die on $Y_0$. Fix $y$ and its system. The image of $x$ on $D_\infty$ dies on $D_{\infty,0}$, so it is $0$ by the closed fibre condition for $D_\infty$. So $x$ dies on some clopen neighbourhood $D_j$ of $y$. These neighbourhoods cover $Y$. We refine them to a finite disjoint clopen cover, on each part of which $x$ is $0$. So $x = 0$.

*Surjectivity.* Let $z \in H^n(Y_0)$. Fix $y$ and its system. By the closed fibre condition, the image of $z$ on $D_{\infty,0}$ is the restriction of a class on $D_\infty$, which comes from a class $x$ on some $D_k$. The classes $x|_{D_{k,0}}$ and $z|_{D_{k,0}}$ agree on $D_{\infty,0}$, so they agree on some $D_{k',0}$. So $y$ has a clopen neighbourhood $D$ with a class on $D$ that restricts to $z|_{D_0}$. We refine these neighbourhoods to a finite disjoint clopen cover and take the product of the classes. Its restriction to $Y_0$ is $z$. $\square$

**Theorem 3.4.7 (Reduction to AIC schemes).** Assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Let $A$ be a local ring, $q$ a unit in $A$, $P$ a qcqs scheme and $p : P \to \operatorname{Spec} A$ a map. Assume that $\mathrm{PB}_{q,i}(h \circ p)$ holds for every AIC scheme $Z$ and every integral map $h : Z \to P$. Then there is an integral surjective map $k : Y \to P$ such that $\mathrm{PB}_{q,i}(p \circ k)$ holds.

Lean: `UpperTheory.Et.E2.n9`.

*Proof.* Let $k : Y \to P$ be as in [Lemma 3.4.5](/entry/n10/). Then $Y$ is qcqs, because $k$ is integral and $P$ is qcqs. Let $y \in Y$ and take its clopen system $(D_j)$ from the lemma. The limit $D_\infty$ is an AIC scheme, and the map $D_\infty \to P$ is integral. By hypothesis, the closed fibre condition holds for $D_\infty \to P \to \operatorname{Spec} A$. This is the hypothesis of the lemma on clopen systems for $g = p \circ k$. So $\mathrm{PB}_{q,i}(p \circ k)$ holds. $\square$

**Remark 3.4.8 (Formalization).** The limit theorem is stated as two parts, surjectivity and injectivity of the map from the colimit. The axioms come as one record of hypotheses. The two lemmas on normalizations are statements about schemes only. The surjective map from a ring of product type, the limits of clopen systems, the normalization in an algebraically closed field and the integrality of $D_\infty \to Y$ are separate lemmas, which we checked from their statements. The lemma on clopen systems has the name `etale_pro_equivalence_of_continuity_mayer_vietoris_lifting_stage_glue` ([CoverCut.lean](lean:Development/EtaleCohomology/EtaleSheaves/CoverCut.lean#L18)).
