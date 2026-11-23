---
title: Hermitian forms and conjugacy classes
decls:
  - PositivityTheory.BCUSide.L.hermitian_form_local_global
  - GlobalTheory.T.hermitian_form_local_global
  - GlobalTheory.UnitaryClasses.ExistForm.main
  - GlobalTheory.T.hermitian_local_data_almost_all
  - GlobalTheory.UnitaryClasses.existForm
  - GlobalTheory.UnitaryClasses.part3
  - GlobalTheory.UnitaryClasses.main
  - GlobalTheory.T.unitary_conjugacy_sign_product
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hermitian forms and conjugacy classes

This section describes the rational conjugacy classes of a definite unitary group with a given regular elliptic characteristic polynomial. There are three statements. Two rational elements that are conjugate at every finite place are conjugate. The local signs of a rational element have product $1$. A family of local elements whose signs have product $1$ comes from a rational element. The proof goes through [[Hermitian forms|8NJ7XY6F1S]] that are invariant under one fixed element, and a local-global principle for these forms. The result is used in [the next section](/entry/fixed-p/) to turn the class sum of [the Hecke trace](/entry/tr-on-forms-hop-eq-geom/) into a sum of products of local $\kappa$-orbital integrals. For the background, see [Hermitian and skew-Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms) and [the local classification](/learn/hermitian-lattices/#local-classification).

### Setting

We keep the notation of [the Hecke traces](/entry/tr-on-forms-hop-eq-kern-sum/): $E$ is a CM field with maximal totally real subfield $E^+$ and conjugation $c$, every finite place of $E$ is unramified over $E^+$, $\mathrm{U}(E)$ is the definite [[unitary group|0R9R0Y1HDK]] of the standard form, and $S$ is a section. For a matrix $g$ put $g^* = {}^t c(g)$. A finite place $w$ of $E$ is *split* if it splits over $E^+$, and *nonsplit* otherwise. At a nonsplit $w$ the conjugation extends to a continuous involution $c_w$ of $E_w$, and $g^*$ is defined with $c_w$. For $w \in S$ let $\mathrm{U}_w$ and $K_w$ be as in that section: $\mathrm{U}_w = \mathrm{GL}_n(E_w)$ if $w$ is split, and $\mathrm{U}_w = \{g : g^* g = 1\}$ if $w$ is nonsplit.

**Definition 2.10.1 (Elliptic polynomials).** Let $\mathrm{Ell}(E, n)$ be the set of monic separable $P \in E[X]$ of degree $n$ such that, for every embedding $\tau : E \to \mathbb{C}$, every root of $\tau(P)$ has absolute value $1$.

The characteristic polynomial of an element of $\mathrm{U}(E)$ has roots of absolute value $1$, since the element is unitary at every infinite place. So the regular classes of $\mathrm{U}(E)$ are the classes with characteristic polynomial in $\mathrm{Ell}(E, n)$.

**Definition 2.10.2 (Local sign).** Let $w$ be a nonsplit place, $H$ an invertible Hermitian matrix over $E_w$, $A$ an $n \times n$ matrix over $E_w$ and $Q \in E_w[X]$. Let $v_1, \dots, v_d$ be a basis of $\ker Q(A)$. Put
$$\epsilon_w(H, Q, A) = (-1)^{\mathrm{ord}_w \det(v_i^* H v_j)_{i, j}}.$$
For a split place put $\epsilon_w(H, Q, A) = 1$. For $\gamma \in \mathrm{U}_w$ write $\epsilon_w(Q, \gamma) = \epsilon_w(1, Q, \gamma)$.

A change of basis multiplies the determinant by an element $x\, c_w(x)$, which has even order since $w$ is unramified over $E^+$. So the sign does not depend on the basis. For the standard form it is the sign $\epsilon_{Q_1}$ of [the inert places](/entry/kap-orb-congruence-eq-kap-sum/). For $P_1 \in E[X]$ we write $\epsilon_w(H, P_1, A)$ for the sign of the image of $P_1$ in $E_w[X]$.

### The local-global principle for invariant forms

Fix $\gamma_0 \in \mathrm{GL}_n(E)$ with characteristic polynomial $P \in \mathrm{Ell}(E, n)$. A Hermitian matrix $H$ over $E$ is *$\gamma_0$-invariant* if $\gamma_0^* H \gamma_0 = H$, and *totally positive* if for every embedding $\tau$ of $E$ there is an invertible complex $Q$ with $\tau(H) = Q^* Q$. The same words apply to a Hermitian matrix over $E_w$ for a nonsplit $w$. Two $\gamma_0$-invariant forms $H$, $H'$ over $E_w$ are *equivalent* if $H' = c^* H c$ for some invertible $c$ that commutes with $\gamma_0$.

**Theorem 2.10.3 (Local-global principle for invariant forms).** Let $E$ be a CM field in which every finite place is unramified over $E^+$, $S$ a section, and $\gamma_0 \in \mathrm{GL}_n(E)$ with characteristic polynomial $P \in \mathrm{Ell}(E, n)$. Let $H_0$ be an invertible, $\gamma_0$-invariant, totally positive Hermitian matrix over $E$ with
$$\prod_{w \in S} \epsilon_w(H_0, P_1, \gamma_0) = 1 \quad \text{for every monic divisor } P_1 \text{ of } P.$$
For each nonsplit $w$ let $H_w$ be an invertible, $\gamma_0$-invariant Hermitian matrix over $E_w$. Suppose that $H_w$ is equivalent to $H_0$ for almost all $w$, and that
$$\prod_{w \in S} \epsilon_w(H_w, P_1, \gamma_0) = 1 \quad \text{for every monic divisor } P_1 \text{ of } P.$$
Then there is a $\gamma_0$-invariant, totally positive Hermitian matrix $H'$ over $E$ that is equivalent to $H_w$ at every nonsplit $w$.

Lean: `PositivityTheory.BCUSide.L.hermitian_form_local_global` (also `GlobalTheory.T.hermitian_form_local_global`, a second name).

*Proof.* Let $A = E[X]/(P)$, a product of fields $F_Q = E[X]/(Q)$ over the irreducible factors $Q$ of $P$. Since the roots of $P$ have absolute value $1$, each factor $Q$ is sent to itself by $x \mapsto c(x)^{-1}$ on roots, so $c$ extends to an involution of each $F_Q$ with $X \mapsto X^{-1}$. Let $F_Q^+$ be its fixed field.

*Step 1: ratios.* At a nonsplit $w$, both $H_w$ and $H_0$ are $\gamma_0$-invariant, so $H_0^{-1} H_w$ commutes with $\gamma_0$. As $P$ is separable, it is a polynomial in $\gamma_0$: $H_w = H_0\, m_w(\gamma_0)$ with $m_w \in E_w[X]$. Hermitian symmetry puts the image of $m_w$ in each factor into the fixed part $F_Q^+ \otimes E^+_v$, where $v$ is the place of $E^+$ below $w$.

*Step 2: one factor.* Fix $Q$. Two forms $H_0\, m(\gamma_0)$ and $H_0\, m'(\gamma_0)$ are equivalent in the $Q$-component if and only if $m'/m$ is a norm from $F_Q \otimes E^+_v$ there. At the places where $H_w$ is equivalent to $H_0$, the local ratio is a norm. The sign condition for the divisors $P_1$ of $P$ says that the product over all places of the quadratic symbols of the local ratios is $1$. The idelic form of the norm theorem for the quadratic extension $F_Q / F_Q^+$ then gives a global $t_Q \in (F_Q^+)^\times$ that is, at each place, the local ratio times a norm, and that is positive at each real place, since $H_0$ is totally positive. The sign condition on $H_0$ is used to compare the product formula for $H_0$ with the one for the family $(H_w)$.

*Step 3: gluing.* By the Chinese remainder theorem there is $m \in E[X]$ whose image in $F_Q$ is $t_Q$ for each $Q$. Put $H' = H_0\, m(\gamma_0)$. It is Hermitian because each $t_Q$ is fixed by the involution, it is $\gamma_0$-invariant since $m(\gamma_0)$ commutes with $\gamma_0$, it is totally positive since each $t_Q$ is totally positive, and it is equivalent to $H_w$ at every nonsplit $w$ by the choice of $t_Q$. $\square$

**Theorem 2.10.4 (Existence of a global invariant form).** Let $E$, $S$ and $\gamma_0$ be as in the previous Theorem. For each nonsplit $w$ let $H_w$ be an invertible, $\gamma_0$-invariant Hermitian matrix over $E_w$. Suppose that for almost all $w$ there are $k, m \in \mathrm{GL}_n(E_w)$ with $k^{-1} \gamma_0 k \in \mathrm{GL}_n(\mathcal{O}_w)$, $m \in \mathrm{GL}_n(\mathcal{O}_w)$ and $m = k^* H_w k$, and that
$$\prod_{w \in S} \epsilon_w(H_w, P_1, \gamma_0) = 1 \quad \text{for every monic divisor } P_1 \text{ of } P.$$
Then there is a $\gamma_0$-invariant, totally positive Hermitian matrix $H'$ over $E$ that is equivalent to $H_w$ at every nonsplit $w$.

Lean: `GlobalTheory.UnitaryClasses.ExistForm.main` (also `GlobalTheory.T.hermitian_local_data_almost_all`, a second name; `GlobalTheory.UnitaryClasses.existForm`, a third name).

*Proof.* There is an invertible, $\gamma_0$-invariant, totally positive Hermitian $H_0$ over $E$: a trace form on $A = E[X]/(P)$ with a totally positive coefficient, carried to $E^n$ by a basis in which $X$ acts as $\gamma_0$. Its local signs have product $1$: the Gram determinant on $\ker P_1(\gamma_0)$ is a totally positive element $d$ of $E^+$, and $\prod_{w \in S} (-1)^{\mathrm{ord}_w d}$ is the product of the values of the quadratic character of $E/E^+$ at $d$ over the finite places, which is $1$ by the product formula, since $d$ is positive at the real places. For almost all $w$, the place is good for $\gamma_0$ and $H_0$, and a unimodular $\gamma_0$-invariant form there is equivalent to $H_0$. So $H_w$ is equivalent to $H_0$ for almost all $w$. Now apply the previous Theorem. $\square$

### Classes in the definite unitary group

For $\gamma \in \mathrm{U}(E)$ and $w \in S$ let $\gamma_w$ be its image in $\mathrm{U}_w$.

**Theorem 2.10.5 (Conjugacy classes and signs).** Let $E$ be a CM field in which every finite place is unramified over $E^+$, $n \ge 1$, $S$ a section and $P \in \mathrm{Ell}(E, n)$.

1. If $\gamma, \gamma' \in \mathrm{U}(E)$ have characteristic polynomial $P$ and $\gamma'_w$ is conjugate to $\gamma_w$ in $\mathrm{U}_w$ for every $w \in S$, then $\gamma'$ is conjugate to $\gamma$ in $\mathrm{U}(E)$.
2. If $\gamma \in \mathrm{U}(E)$ has characteristic polynomial $P$ and $P_1$ is a monic divisor of $P$, then $\prod_{w \in S} \epsilon_w(P_1, \gamma_w) = 1$.
3. Let $y_w \in \mathrm{U}_w$, $w \in S$, have characteristic polynomial $P$, with $y_w \in K_w$ for almost all $w$, and with $\prod_{w \in S} \epsilon_w(P_1, y_w) = 1$ for every monic divisor $P_1$ of $P$. Then there is $\gamma \in \mathrm{U}(E)$ with characteristic polynomial $P$ such that $\gamma_w$ is conjugate to $y_w$ in $\mathrm{U}_w$ for every $w \in S$.

Lean: `GlobalTheory.UnitaryClasses.main` (also `GlobalTheory.T.unitary_conjugacy_sign_product`, a second name). Item 3 is also `GlobalTheory.UnitaryClasses.part3`.

*Proof.* *Item 1.* Since $P$ is separable, $\gamma' = h^{-1} \gamma h$ for some $h \in \mathrm{GL}_n(E)$. An element $g$ of $\mathrm{U}(E)$ with $g^{-1} \gamma g = \gamma'$ exists if and only if there is $c$ commuting with $\gamma$ with $c^* c = (h h^*)^{-1}$: put $g = c h$ in one direction and $c = g h^{-1}$ in the other. The same holds over $E_w$ at each nonsplit $w$. So the hypothesis gives local solutions $c_w$ at every nonsplit place. The element $(h h^*)^{-1}$ commutes with $\gamma$ and lies in the fixed part of the algebra $E[\gamma] \cong \prod_Q F_Q$, and it is totally positive. By the norm theorem for the quadratic extensions $F_Q / F_Q^+$, local norms at every place give a global norm, so a global $c$ exists. At split places there is no condition, and at the real places it holds by positivity.

*Item 2.* Let $V = \ker P_1(\gamma) \subseteq E^n$ and $d$ the Gram determinant of the standard form on a basis of $V$. It is a nonzero element of $E^+$, positive at every real place, since the standard form is positive definite. The kernel of $P_1(\gamma_w)$ is $V \otimes E_w$, so $\epsilon_w(P_1, \gamma_w) = (-1)^{\mathrm{ord}_w d}$ at each nonsplit $w$. Since $E/E^+$ is unramified at all finite places, $(-1)^{\mathrm{ord}_w d}$ is the value at $d$ of the local quadratic character, and it is $1$ at split places. The product formula for the quadratic character gives the claim.

*Item 3.* Let $\gamma_0 \in \mathrm{GL}_n(E)$ have characteristic polynomial $P$, for example the companion matrix. Since $P$ is separable, $y_w = k_w^{-1} \gamma_0 k_w$ for some $k_w \in \mathrm{GL}_n(E_w)$. At a nonsplit $w$ put $H_w = (k_w^{-1})^* k_w^{-1}$. Since $y_w$ is unitary, $H_w$ is $\gamma_0$-invariant. For almost all $w$ we have $y_w \in K_w$, which is the integrality condition of the Theorem on existence with $m = 1$. Conjugation by $k_w$ carries the standard form on $\ker P_1(y_w)$ to $H_w$ on $\ker P_1(\gamma_0)$, so $\epsilon_w(H_w, P_1, \gamma_0) = \epsilon_w(P_1, y_w)$, and the sign condition holds. That Theorem gives a global $H'$, totally positive, $\gamma_0$-invariant, with $H' = c_w^* H_w c_w$ at each nonsplit $w$. Then $H' = (k_w^{-1} c_w)^* (k_w^{-1} c_w)$ is locally the standard form at every nonsplit place. By Landherr's theorem, a Hermitian form over $E$ that is positive definite at every infinite place and locally standard at every nonsplit place is globally standard: $H' = h^* h$ with $h \in \mathrm{GL}_n(E)$. Put $\gamma = h \gamma_0 h^{-1}$. Then $\gamma^* \gamma = 1$ since $\gamma_0^* H' \gamma_0 = H'$, and $\gamma$ has characteristic polynomial $P$. At a nonsplit $w$, the element $g_w = k_w^{-1} c_w h^{-1}$ is unitary and $\gamma_w = g_w^{-1} y_w g_w$. At a split $w$ the elements $\gamma_w$ and $y_w$ are conjugate in $\mathrm{GL}_n(E_w)$, since they have the same separable characteristic polynomial. $\square$

Item 1 says that a stable class of $\mathrm{U}(E)$ is determined by its local classes, and items 2 and 3 say which families of local classes occur: the obstruction is a product of signs, one for each divisor $P_1$, and the signs are the values of the endoscopic character $\kappa$. This is the global form of the statement that the stable class of $\gamma$ splits into the classes of the kernel of a map to a group of signs. It is the input for the stabilization of the class sum in [the next section](/entry/geom-urat-eq-geom-u/).

**Remark 2.10.6 (Formalization).** The hypothesis $n \ge 1$ of the Theorem on classes is not used ([UnitaryConjugacySignProduct.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryConjugacySignProduct.lean#L145)). Item 2 is proved for every polynomial $P_1$ and every $\gamma \in \mathrm{U}(E)$, without the conditions on the characteristic polynomial ([UnitaryConjugacySignProduct.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryConjugacySignProduct.lean#L59)). The Theorem on existence has the name `hermitian_local_data_almost_all` as its second name, but it states the existence of a global form, not a property of local data ([HermitianLocalDataAlmostAll.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/HermitianLocalDataAlmostAll.lean#L13)). Its proof combines four named results: the existence of $H_0$, the sign product for $H_0$, the equivalence with $H_0$ at almost all places, and the local-global principle. We did not unfold the first three. The proof of the local-global principle is formal ([HermitianFormLocalGlobal.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLemmas/HermitianFormLocalGlobal.lean#L227)); the global element of Step 2 comes from a lemma for each factor ([HermitianFormLocalGlobal.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLemmas/HermitianFormLocalGlobal.lean#L59)), which uses an existence result for elements whose quadratic symbols have product $1$. In item 1 the Hasse step is a named result, and in item 3 Landherr's theorem is a named result for CM fields; both are used as given. The sign of the Definition is computed with a basis chosen by `Module.finBasis`, and the function $c_w$ is defined by choice, with the identity as a fallback that is not reached at nonsplit places ([SimpleTwistedTraceFormulaStable.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SimpleTwistedTraceFormulaStable.lean#L91)). The second names are restatements by `first | exact …`.
