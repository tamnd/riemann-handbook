---
title: The de Rham structure and the Poincaré bundle
decls:
  - PositivityTheory.DualRT.abelianDeRham
  - GlobalTheory.T.cohomologous_neg_torsor_cocycle_of_orthogonal
  - GlobalTheory.PtExt.cohom_fv_neg_tanCoc_of_orthogonal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The de Rham structure and the Poincaré bundle

This section proves the *de Rham structure* of an [[abelian scheme|JDDXZ89N33]], which the section on lifting along nilpotent divided powers used as its fact 1 (Theorem (De Rham structure)). It adds to the Hodge and de Rham structure of the last section three things: the Hodge filtration as a direct summand of the right rank, the rigidity of de Rham homology under nilpotent divided power thickenings, and the duality given by the Chern class of a line bundle. The section then proves a lemma on a line bundle $P$ on a product $A \times B$ (Lemma (Tangent vectors and the Chern class)). It computes the first order deformation of $P$ along a tangent vector of $B$ as a class on $A$, in terms of the pairing that the Chern class of $P$ induces. For a Poincaré bundle this is the classical identification of the tangent space of the dual with $H^1(A, \mathcal{O})$. Both results are used on the way to [EveryCharacter](/step/every-character/).

Throughout, $R$ is a ring and $A$ an abelian scheme over $R$, [[smooth|EXKGG9X6J0]] of relative dimension $g$. We use the notation of the section on square zero lifts. $H^1_{\mathrm{dR}}(A)$ is the first de Rham cohomology, computed here as the cohomology of the structure sheaf on the infinitesimal site with the zero ideal; $H^{\mathrm{pr}}_{\mathrm{dR}}(A) \subset H^1_{\mathrm{dR}}(A)$ is its primitive part; $D_{\mathrm{dR}}(A)$ is the $R$-dual of $H^{\mathrm{pr}}_{\mathrm{dR}}(A)$. Let $F^1(A) \subset H^{\mathrm{pr}}_{\mathrm{dR}}(A)$ be the primitive classes of 1-forms and $\mathrm{Fil}(A) \subset D_{\mathrm{dR}}(A)$ its annihilator.

A *tangent vector* of $A$ is a morphism $v : \mathrm{Spec}\, R[\varepsilon] \to A$ over $R$ that reduces to the unit section modulo $\varepsilon$. For a global 1-form $f$ and a tangent vector $v$, the pullback $v^* f$ is a form on $\mathrm{Spec}\, R[\varepsilon]$, and we write $f(v) \in R$ for its $\varepsilon$ part. We say that $h \in D_{\mathrm{dR}}(A)$ is the *Lie image* of $v$ if $v$ is a tangent vector and $h(\mathrm{cl}(f)) = f(v)$ for every global 1-form $f$ whose class is primitive. We say that *Lie images are exact* for $A$ if every $h \in D_{\mathrm{dR}}(A)$ is the Lie image of exactly one $v$, and every tangent vector $v$ has some Lie image. Then $h \mapsto v$ maps $D_{\mathrm{dR}}(A)$ onto the tangent space at the unit, and its kernel is $\mathrm{Fil}(A)$, since $h$ is the Lie image of the unit point exactly when $h \in \mathrm{Fil}(A)$. This is the dual of the Hodge sequence $0 \to \Omega \to H^1_{\mathrm{dR}} \to H^1(\mathcal{O}) \to 0$ in de Rham homology.

**Definition 1.16.1 (Form of a line bundle).** Let $L$ be a line bundle on $A$ and $\psi$ a bilinear form on $D_{\mathrm{dR}}(A)$. We say that $\psi$ is a *form of $L$* if there are primitive classes $a_1, \dots, a_n, b_1, \dots, b_n$ such that $\sum_k a_k \cup b_k$ is the Chern class of $L$ in $H^2_{\mathrm{dR}}(A)$ and
$$\psi(x, y) = \sum_{k=1}^n \bigl( x(a_k)\, y(b_k) - x(b_k)\, y(a_k) \bigr).$$
For abelian schemes $A$ and $B$ and a line bundle $P$ on $A \times B$, a bilinear map $\varphi : D_{\mathrm{dR}}(A) \times D_{\mathrm{dR}}(B) \to R$ is a *form of $P$* if there are primitive $a_k$ on $A$ and $b_k$ on $B$ with $\sum_k \mathrm{pr}_1^* a_k \cup \mathrm{pr}_2^* b_k$ the Chern class of $P$ and $\varphi(x, y) = \sum_k x(a_k)\, y(b_k)$.

Over $\mathbb{C}$ the form of an ample $L$ is, up to a constant, the Riemann form of $L$ (see the section on periods over the complex numbers). The form of a Poincaré bundle is the pairing of Poincaré duality in de Rham homology, from the section on lifting along nilpotent divided powers.

**Theorem 1.16.2 (De Rham structure).** Let $R$ be a ring and $A$ an abelian scheme over $R$, smooth of relative dimension $g$.

1. (Free.) Every class in $H^1_{\mathrm{dR}}(A)$ is primitive, $H^1_{\mathrm{dR}}(A)$ is finite projective of rank $2g$ at each prime, and cup product gives an isomorphism $\bigwedge^2 H^1_{\mathrm{dR}}(A) \cong H^2_{\mathrm{dR}}(A)$.
2. (Hodge.) Lie images are exact for $A$, and $F^1(A)$ is a direct summand of $H^{\mathrm{pr}}_{\mathrm{dR}}(A)$, finite projective of rank $g$ at each prime.
3. (Base change.) For every $R$-algebra $R'$ and every abelian scheme $A'$ over $R'$ that is the base change of $A$ as a group, the pullback $D_{\mathrm{dR}}$ map is a base change isomorphism, and $F^1(A')$ is the $R'$-span of the pullback of $F^1(A)$.
4. (Rigidity.) Let $I \subset R$ be an ideal with nilpotent divided powers $\kappa$, $\pi : R \to R_0$ surjective with kernel $I$, and $A_0$ the base change of $A$ to $R_0$ as a group. Then pullback along $A_0 \to A$, from $H^{\mathrm{pr}}_{\mathrm{dR}}(A)$ to the primitive part of the crystalline $H^1$ of $A_0$ relative to $(R, I, \kappa)$, is bijective.
5. (Duality.) Let $L$ be a line bundle on $A$ and $\psi$ a form of $L$. Then $\psi$ vanishes on $\mathrm{Fil}(A) \times \mathrm{Fil}(A)$. If $K(L)$ is trivial, then $\psi$ is a perfect pairing.

Lean: `PositivityTheory.DualRT.abelianDeRham`.

Here $K(L)$ is the kernel of $L$ from the section on additive line bundles. *Trivial* means that a point $x \in A(T)$ for which $\tau_x^* L \otimes \mathrm{pr}^* L^{-1}$ is locally trivial on $T \times A$ is the unit.

We use the following facts.

1. (Page.) The Hodge and de Rham structure implies parts 1, 2 and 3 for every abelian scheme.
2. (Crystalline and de Rham.) For each ring $R$ with an ideal $I$ and nilpotent divided powers $\kappa$, each scheme $X_0$ over $R_0 = R/I$ and each smooth lift $X$ of $X_0$ to $R$ that is separated and quasicompact, pullback along $X_0 \to X$ from the de Rham $H^1$ and $H^2$ of $X$ to the crystalline $H^1$ and $H^2$ of $X_0$ relative to $(R, I, \kappa)$ is bijective. With part 1, this gives part 4.
3. (Surjectivity.) The crystalline comparison and the Hodge and de Rham structure of the section on square zero lifts imply a surjectivity statement for every abelian scheme. With parts 1 to 3, it gives part 5.

*Proof.* The Hodge and de Rham structure holds by [Theorem 1.15.1](/entry/ab-coh-abelian-hodge-de-rham/) (Hodge and de Rham structure). Fact 1 gives parts 1 to 3. Fact 2, applied with part 1, gives part 4. The crystalline comparison is proved, so fact 3 applies, and together with parts 1 to 3 it gives part 5. $\square$

We turn to the lemma. It is stated with cochains on points, which we now define. Let $X$ be a scheme over $R$ and $W = (W_i)$ a family of open sets of $X$. A point $x \in X(D)$ for an $R$-algebra $D$ is *small* for $W$ if $x$ factors through some $W_i$.

**Definition 1.16.3 (Point cochains).** A *point 0-cochain* $k$ on $X$ assigns to each $R$-algebra $D$ and each $x \in X(D)$ an element $k(x) \in D$. A *point 1-cochain* $f$ assigns to each map $\phi : D \to D'$ of $R$-algebras and each $x \in X(D)$ an element $f(\phi, x) \in D'$. It is a *cocycle relative to $W$* if
$$f(\psi \circ \phi, x) = \psi(f(\phi, x)) + f(\psi, \phi_* x)$$
for all $\phi : D \to D'$, $\psi : D' \to D''$ and small $x$. It is the *coboundary* of $k$ relative to $W$ if $f(\phi, x) = k(\phi_* x) - \phi(k(x))$ for small $x$. Two point 1-cochains are *cohomologous relative to $W$* if their difference is a coboundary relative to $W$.

A 1-cocycle $f$ of the structure sheaf on the infinitesimal site gives a point 1-cochain $f^\flat$: a point $x \in X(D)$ is a trivial thickening of $X$, a map $\phi$ is a map of trivial thickenings, and $f^\flat(\phi, x)$ is the value of $f$ on it. A line bundle gives another point 1-cochain. Let $P$ be a line bundle on $A \times B$, given by charts $(U_j)$ and transition functions $g_{jj'}$. Its *charts on $A$* are the open sets $\iota^{-1}(U_j)$, where $\iota = (\mathrm{id}, 1) : A \to A \times B$. A *choice of charts* assigns to each small $x \in A(D)$ an index $j(x)$ with $x$ in the chart $\iota^{-1}(U_{j(x)})$. For a tangent vector $v$ of $B$, the *tangent cocycle* of $P$ along $v$ is
$$t_{P, v}(\phi, x) = \frac{b}{a}, \qquad a + b\varepsilon = g_{j(\phi_* x),\, j(x)}\bigl(\phi_* x, v\bigr) \in D'[\varepsilon],$$
the logarithmic derivative of the transition function at the $D'[\varepsilon]$-point $(\phi_* x, v)$ of $A \times B$. It describes the restriction of $P$ to $A \times \mathrm{Spec}\, R[\varepsilon]$ along $v$, a first order deformation of $P|_{A \times \{1\}}$.

**Lemma 1.16.4 (Tangent vectors and the Chern class).** Assume the Hodge and de Rham structure. Let $A$ and $B$ be abelian schemes over $R$, smooth of relative dimension $g$, $P$ a line bundle on $A \times B$, and $\varphi$ a form of $P$ with $\varphi(x, y) = 0$ for $x \in \mathrm{Fil}(A)$ and $y \in \mathrm{Fil}(B)$. Let $h' \in D_{\mathrm{dR}}(B)$ be the Lie image of a tangent vector $v$ of $B$. Let $c \in H^{\mathrm{pr}}_{\mathrm{dR}}(A)$ satisfy $\varphi(h, h') = h(c)$ for all $h \in \mathrm{Fil}(A)$, and let $f$ be a 1-cocycle on the infinitesimal site that represents $c$. Let $j$ be a choice of charts of $P$ on $A$. Then $f^\flat$ and $-t_{P, v}$ are cohomologous relative to the charts of $P$ on $A$.

Lean: `GlobalTheory.PtExt.cohom_fv_neg_tanCoc_of_orthogonal` (also `GlobalTheory.T.cohomologous_neg_torsor_cocycle_of_orthogonal`, a second name).

In words: the deformation of $P$ along $v$ is minus the class $c$ that $\varphi(\cdot, h')$ defines on $\mathrm{Fil}(A)$. When $\varphi$ is perfect, as for a Poincaré bundle, this identifies the tangent space of $B$ with a quotient of $H^{\mathrm{pr}}_{\mathrm{dR}}(A)$ by the forms, that is, with $H^1(A, \mathcal{O})$.

We use four facts, all under the hypotheses of the lemma. A *contraction* of a point 2-cochain $w$ on $A \times B$ with $v$ is a point 1-cochain on $A$ obtained by inserting $v$ in the second factor.

1. (A Chern representative.) There is a 2-cocycle $w$ on the infinitesimal site of $A \times B$ that represents the Chern class of $P$, that vanishes on triples of trivial thickenings, and such that every contraction of $w$ with $v$ is cohomologous to $-f^\flat$ on all of $A$.
2. (Contractions exist.) For a tangent vector $v$, each such $w$ has a contraction with $v$.
3. (Contraction and transition functions.) Let $w$ represent the Chern class of $P$ and vanish on triples of trivial thickenings. Each contraction of $w$ with $v$ is cohomologous, relative to the charts of $P$ on $A$, to $t_{P,v} + u_v$, where $u$ is a point 1-cocycle on $A \times B$ relative to the charts of $P$, and $u_v(\phi, x)$ is the $\varepsilon$ part of $u$ at the point $(x, v)$ over $D'[\varepsilon]$.
4. (The $\varepsilon$ part.) Under the Hodge and de Rham structure, $u_v$ is cohomologous to $0$ relative to the charts of $P$ on $A$, for each such $u$.

*Proof.* Take $w$ as in fact 1 and a contraction $\kappa$ of $w$ with $v$ by fact 2. By fact 1, $\kappa + f^\flat = \delta k_1$ for a point 0-cochain $k_1$. By fact 3, $\kappa - t_{P,v} - u_v = \delta k_2$ relative to the charts. By fact 4, $u_v = \delta k_3$ relative to the charts. So
$$f^\flat + t_{P,v} = \delta(k_1 - k_2 - k_3)$$
on small points, which is the claim. $\square$

**Remark 1.16.5 (Formalization).** The theorem is `GlobalTheory.Published.AbelianDeRham`, the conjunction of `Free`, `Hodge`, `BaseChange`, `Rigid` and `Duality` in [CrysToDRBijective.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/CrysToDRBijective.lean#L24). Lie images are `IsLieImage` and their exactness is `LieExact`, forms are `IsPolForm` and `GlobalTheory.AbDual.IsCorrForm`, and trivial $K(L)$ is `KTriv`. Facts 1 to 3 for the theorem are `AbelianDeRhamStructureFromPages.Adrs.abelianDeRhamStructure_of_page` applied to `MainStatements.Hodge.Free.abelianDeRhamPage`, `AbelianDeRham.rigid_of_free_of_crystallineDeRham` with `FubiniStudyChowHeightFormula₂.Adr.crystallineDeRham`, and `CrystallinePoints.Pd.duality_of_surjAll` with `PositivityTheory.DualRT.surjAll`. The statement `CrystallinePoints.Pd.SurjAll` asks a map `toP` to be surjective; `toP` and the page were not unfolded. The page is built from the Hodge and de Rham structure by `page_of_hodge` and then taken apart again, and [AbelianDeRhamDuality.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/DualAbelianScheme/AbelianDeRhamDuality/AbelianDeRhamDuality.lean#L17) builds the same structure twice, at lines 17 and 21. The theorem uses the second proof of the Hodge and de Rham structure. The namespaces `PositivityTheory` and `FubiniStudyChowHeightFormula₂` do not describe the content, and a different theorem, `CrystallinePoints.Pd.abelianDeRham`, has the same last name. For the lemma, point cochains are `Fn0` and `Fn1`, $f^\flat$ is `fv`, the tangent cocycle is `tanCoc` with the logarithmic derivative `dl` ([ExistsDatNeZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsDatNeZero.lean#L276)), and the four facts are `GlobalTheory.T.exists_chernRepresentative_contraction_of_orthogonal`, `GlobalTheory.PtExt.ContrMor.exists_contr`, `GlobalTheory.T.chernClass_contraction_tangent_eq_torsorCocycle` and `GlobalTheory.T.eps_part_cocycle_coboundary_of_hodgeDeRham`, cited by their statements. The value of a function at a point outside its open set is taken to be $0$ in `evU`, so $t_{P,v}$ has a junk value at points that are not small; the lemma only looks at small points. The lemma asks $A$ and $B$ to have the same relative dimension $g$.
