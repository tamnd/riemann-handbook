---
title: Strong approximation for quaternions
decls:
  - GlobalTheory.T.mem_closure_normOne_of_strongApproximation
  - GlobalTheory.QSA.DivAssembly.strongApproximation_normOne_divisionQuaternion
  - GlobalTheory.T.strongApproximation_quaternion_normOne_split
  - GlobalTheory.QSA.strongApprox_nrm_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Strong approximation for quaternions

[Strong approximation](/learn/groups/#strong-approximation) for a group $G$ over a number field $F$ and a finite set $S$ of places says that $G(F) \, G(F_S)$ is dense in $G(\mathbb{A}_F)$. This section proves it for the group of norm-one elements of a quaternion algebra over $F$, under the condition that the algebra splits at every place of $S$. The division case is the main step; its proof truncates an adelic element to finitely many places and uses Fujisaki's compactness lemma. The next section transfers the result to the special unitary group of a Hermitian plane, and the section after it to the special unitary group of any nondegenerate Hermitian form of rank at least two.

### Quaternions over the adeles

Let $F$ be a number field, $\mathbb{A}_F$ its [adele ring](/learn/number-fields/#adeles-and-ideles), and $a, b \in F^\times$. For a commutative ring $R$ and $a, b \in R$ let $(a, b)_R$ be the quaternion algebra with basis $1, i, j, k$ over $R$ and $i^2 = a$, $j^2 = b$, $ij = -ji = k$. We write $x = x_0 + x_1 i + x_2 j + x_3 k$.

**Definition 1.11.1 (Reduced norm).** The *reduced norm* of $x \in (a, b)_R$ is
$$\mathrm{nrm}(x) = x_0^2 - a x_1^2 - b x_2^2 + a b x_3^2.$$

Lean: `GlobalTheory.QSA.nrm`.

The reduced norm is multiplicative, and $x \bar x = \mathrm{nrm}(x)$ for the conjugate $\bar x = x_0 - x_1 i - x_2 j - x_3 k$. So the elements of norm one form a group, and the inverse of such an element is its conjugate.

**Definition 1.11.2 (Adelic quaternion algebra).** The *adelic quaternion algebra* is $D_{\mathbb{A}} = (a, b)_{\mathbb{A}_F}$, with $a$ and $b$ viewed in $\mathbb{A}_F$. Its topology is the topology of $\mathbb{A}_F^4$ through the four coordinates $x_0, x_1, x_2, x_3$. The map $x \mapsto \hat x$ from $D = (a, b)_F$ to $D_{\mathbb{A}}$ applies the diagonal embedding $F \to \mathbb{A}_F$ to each coordinate.

Lean: `GlobalTheory.QSA.DA` (also `GlobalTheory.QSA.rat`).

The algebra $D$ is a *division algebra* if $\mathrm{nrm}(x) = 0$ implies $x = 0$ for $x \in D$. Otherwise there is a nonzero $x \in D$ with $\mathrm{nrm}(x) = 0$, and $D$ is *split*: it is isomorphic to $M_2(F)$.

To speak of the places of a set $S$ we use idempotents of $\mathbb{A}_F$. Let $S_1$ be a finite set of infinite places of $F$ and $S_2$ a finite set of finite places, and $S = S_1 \cup S_2$.

**Definition 1.11.3 (Place idempotent).** An element $\varepsilon \in \mathbb{A}_F$ is a *place idempotent* for $(S_1, S_2)$ if its component at $v$ is $1$ for $v \in S$ and $0$ for $v \notin S$.

Lean: `GlobalTheory.Published.IsPlacesIdem`.

Then $\varepsilon^2 = \varepsilon$, and for $x$ in $\mathbb{A}_F$ or $D_{\mathbb{A}}$ the equation $\varepsilon x = x$ says that $x$ is $0$ outside $S$. So $\varepsilon (h - 1) = h - 1$ says that $h$ is $1$ at each place outside $S$: it is an element of $D_{F_S} = \prod_{v \in S} D_v$, viewed in $D_{\mathbb{A}}$.

**Definition 1.11.4 (Rational times local).** For $\varepsilon \in \mathbb{A}_F$ let
$$H_0(\varepsilon) = \{ \hat\gamma \, h : \gamma \in D, \ \mathrm{nrm}(\gamma) = 1, \ h \in D_{\mathbb{A}}, \ \mathrm{nrm}(h) = 1, \ \varepsilon (h - 1) = h - 1 \}.$$

Lean: `GlobalTheory.QSA.H0`.

For a place idempotent $\varepsilon$ of $S$, the set $H_0(\varepsilon)$ is $D^1(F) \, D^1(F_S)$, where $D^1$ is the group of norm-one elements. Strong approximation for $D^1$ and $S$ is the statement that every norm-one element of $D_{\mathbb{A}}$ lies in the closure of $H_0(\varepsilon)$.

### The division case

**Theorem 1.11.5 (Division quaternion algebras).** Let $a, b \in F^\times$ with $(a, b)_F$ a division algebra. Let $\varepsilon$ be a place idempotent for $(S_1, S_2)$ with $S_1 \cup S_2$ nonempty. Assume that for every $t \in \mathbb{A}_F$ there is $h \in D_{\mathbb{A}}$ with $\mathrm{nrm}(h) = 1$ and $\varepsilon h_0 = \varepsilon t$. Then every $g \in D_{\mathbb{A}}$ with $\mathrm{nrm}(g) = 1$ lies in the closure of $H_0(\varepsilon)$.

Lean: `GlobalTheory.T.mem_closure_normOne_of_strongApproximation` (also `GlobalTheory.QSA.DivAssembly.strongApproximation_normOne_divisionQuaternion`).

The last hypothesis says that the reduced trace $2h_0$ of a norm-one element takes every value at the places of $S$. At a place $v$ where $D_v$ is a division algebra this fails, since the norm-one group of $D_v$ is compact. So the hypothesis implies that $D$ splits at every place of $S$.

*Proof.* We use these facts, proved in another part of the development. We have opened their statements.

1. *Products.* If $\varepsilon^2 = \varepsilon$, the closure of $H_0(\varepsilon)$ is closed under multiplication.
2. *Fujisaki.* There is a compact set $C \subseteq D_{\mathbb{A}}$ such that every $y \in D_{\mathbb{A}}$ with $\mathrm{nrm}(y)$ a unit of $\mathbb{A}_F$ is $y = l \, \hat\delta \, c$ with $\delta \in D$, $\mathrm{nrm}(\delta) \neq 0$, $l \in \mathbb{A}_F^\times$, and $c \in C$ with $c^{-1} \in C$.
3. *Local relation.* Under the hypotheses of the theorem, let $g$ have norm one with $\varepsilon (g - 1) = 0$, and let $W$ be a neighborhood of $g$. Then there are $w \in W$, $y \in D_{\mathbb{A}}$ with $\mathrm{nrm}(y)$ a unit, $\gamma \in D$ of norm one, and $h$ of norm one with $\varepsilon (h - 1) = h - 1$, such that $y w = \hat\gamma \, y \, h$.
4. *Compact conjugation.* Let $X$ be a Hausdorff topological monoid, $H \subseteq X$ and $C \subseteq X$ compact. If each neighborhood $W$ of $g$ contains a $w$ with $c w c' \in H$ for some $c, c' \in C$ with $c c' = c' c = 1$, then $c g c'$ lies in the closure of $H$ for some such $c, c'$.
5. *Removing the conjugation.* Let $\eta$ be a place idempotent and $\varepsilon^2 = \varepsilon$. If $g$ has norm one, $\eta (g - 1) = g - 1$, and $c g c^{-1}$ lies in the closure of $H_0(\varepsilon)$ for a unit $c$, then $g$ lies in the closure of $H_0(\varepsilon)$.
6. *Approximation of $1$.* Every neighborhood of $1$ in $\mathbb{A}_F$ contains a place idempotent.

For an idempotent $e$ of $\mathbb{A}_F$ and $g \in D_{\mathbb{A}}$ put $g^{(e)} = e (g - 1) + 1$, the element that agrees with $g$ where $e = 1$ and with $1$ where $e = 0$. A direct computation gives $\mathrm{nrm}(g^{(e)}) = e \, \mathrm{nrm}(g) + (1 - e)$, and
$$g^{(1 - e)} \, g^{(e)} = g,$$
since $(1 - e) e = 0$.

*Step 1: $g$ is $1$ outside a finite set $T$.* Let $\eta$ be a place idempotent with $\eta (g - 1) = g - 1$ and $\mathrm{nrm}(g) = 1$. Put $g_S = g^{(\varepsilon)}$ and $g_N = g^{(1 - \varepsilon)}$. Then $g = g_N g_S$, both have norm one, and $\varepsilon (g_S - 1) = g_S - 1$, so $g_S = \hat 1 \, g_S$ lies in $H_0(\varepsilon)$. Also $\varepsilon (g_N - 1) = 0$ and $\eta (g_N - 1) = g_N - 1$.

Let $W$ be a neighborhood of $g_N$. Fact 3 gives $w \in W$, $y$, $\gamma$ and $h$ with $y w = \hat\gamma \, y \, h$. Fact 2 gives $y = l \, \hat\delta \, c$. Let $c' = c^{-1}$. Since $l$ is a unit and central, $\hat\delta c w = \hat\gamma \hat\delta c h$. Let $\delta' = \mathrm{nrm}(\delta)^{-1} \bar\delta$, so $\delta' \delta = 1$. Then
$$c w c' = \widehat{\delta' \gamma \delta} \; (c h c').$$
Here $\mathrm{nrm}(\delta' \gamma \delta) = 1$, $\mathrm{nrm}(c h c') = 1$, and $c h c' - 1 = c (h - 1) c'$ is $0$ outside $S$. So $c w c' \in H_0(\varepsilon)$. By fact 4, applied to $X = D_{\mathbb{A}}$, $H = H_0(\varepsilon)$ and the compact set $C$, there are $c, c' \in C$ with $c c' = c' c = 1$ and $c g_N c'$ in the closure of $H_0(\varepsilon)$. Fact 5 gives $g_N$ in the closure of $H_0(\varepsilon)$. By fact 1, $g = g_N g_S$ lies in the closure.

*Step 2: general $g$.* Let $\mathrm{nrm}(g) = 1$ and let $V$ be a neighborhood of $g$. The map $\eta \mapsto \eta (g - 1) + 1$ from $\mathbb{A}_F$ to $D_{\mathbb{A}}$ is continuous and sends $1$ to $g$, so the preimage of $V$ is a neighborhood of $1$. By fact 6 it contains a place idempotent $\eta$. The element $g^{(\eta)}$ lies in $V$, has norm $\eta + (1 - \eta) = 1$, and satisfies $\eta (g^{(\eta)} - 1) = g^{(\eta)} - 1$. By step 1 it lies in the closure of $H_0(\varepsilon)$. So $g$ lies in the closure of the closure, which is the closure. $\square$

### The split condition

**Theorem 1.11.6 (Quaternions split at $S$).** Let $a, b \in F^\times$ and let $\varepsilon$ be a place idempotent for $(S_1, S_2)$ with $S_1 \cup S_2$ nonempty. Assume that there are $p, q \in \mathbb{A}_F$ with $\varepsilon \bigl(b - (p^2 - a q^2)\bigr) = 0$. Then every $g \in D_{\mathbb{A}}$ with $\mathrm{nrm}(g) = 1$ lies in the closure of $H_0(\varepsilon)$.

Lean: `GlobalTheory.T.strongApproximation_quaternion_normOne_split` (also `GlobalTheory.QSA.strongApprox_nrm_one`).

The hypothesis says that at each place $v$ of $S$ the element $b$ is a norm from the algebra $F_v[\sqrt a]$, that is, $D_v$ is split for every $v \in S$.

*Proof.* We use two more facts from another part of the development, whose statements we have opened.

1. *Split algebras.* If $(a, b)_F$ is split, the conclusion holds for every place idempotent $\varepsilon$ of a nonempty $S$.
2. *Prescribed trace.* Let $R$ be a commutative ring in which $a$, $b$ and $2$ are units, and let $\varepsilon, p, q \in R$ with $\varepsilon^2 = \varepsilon$ and $\varepsilon \bigl(b - (p^2 - a q^2)\bigr) = 0$. Then for every $t \in R$ there is $h \in (a, b)_R$ with $\mathrm{nrm}(h) = 1$ and $\varepsilon h_0 = \varepsilon t$.

If there is a nonzero $x \in D$ with $\mathrm{nrm}(x) = 0$, fact 1 applies. Otherwise $D$ is a division algebra. Apply fact 2 with $R = \mathbb{A}_F$: here $a$, $b$ and $2$ are units since they are nonzero elements of $F$, and $\varepsilon^2 = \varepsilon$. This gives the hypothesis on traces of the theorem on division quaternion algebras, and that theorem gives the conclusion. $\square$

In the split case the hypothesis on $p$ and $q$ is not used.

**Remark 1.11.7 (Classical form).** Strong approximation for an algebraic group $G$ over $F$ that is simply connected and absolutely almost simple holds for each finite set $S$ of places with $\prod_{v \in S} G(F_v)$ not compact (M. Kneser; V. Platonov; see V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*, Chapter 7). For $G = D^1$ the condition is that $D_v$ is split at some $v \in S$. J. Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288, treats strong approximation for $D^1$ and Fujisaki's lemma, which is the compactness statement used in the division case. The theorems here ask more: that $D$ split at every place of $S$. In the division case the splitting enters through the hypothesis on traces at $S$, and in the theorem on quaternions split at $S$ through the elements $p$ and $q$.

**Remark 1.11.8 (Formalization).** The quaternion algebra is Mathlib's `ℍ[R, a, b]`, and its topology in [OneMemH0WeightZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/OneMemH0WeightZero.lean#L18) is the topology induced by the four coordinates. The place idempotents are defined in [NotIsCompactUnivFv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/NotIsCompactUnivFv.lean#L16). The fact $\varepsilon^2 = \varepsilon$ for a place idempotent is proved twice in this section: as `GlobalTheory.QSA.DivAssembly.isPlacesIdem_idem` and as `GlobalTheory.QSA.isPlacesIdem_mul_self` at [StrongApproximationQuaternionNormOneSplit.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/StrongApproximationQuaternionNormOneSplit.lean#L14). The facts of the division case are `GlobalTheory.T.closure_normOneProducts_h0_properties`, `GlobalTheory.T.fujisaki_divisionQuaternionAlgebra_mod_centre`, `GlobalTheory.T.normOneQuaternion_near_conj_rational_times_supported`, `GlobalTheory.T.exists_conj_mem_closure_of_isCompact`, `GlobalTheory.T.mem_closure_rationalNormOne_of_idempotent_conj` and `GlobalTheory.T.exists_placesIdempotent_near_one_adeles`; those of the split condition are `GlobalTheory.T.strongApproximation_normOne_splitQuaternionAlgebra` and `GlobalTheory.T.quaternion_norm_one_prescribed_re_at_idempotent`. The truncation formula for the norm and the product $g^{(1-e)} g^{(e)} = g$ are `nrm_trunc` and `prod_decomp` in the file of the division case. The wrappers `GlobalTheory.T.mem_closure_normOne_of_strongApproximation` and `GlobalTheory.T.strongApproximation_quaternion_normOne_split` restate their companions without change.
