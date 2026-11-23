---
title: Quotients of absolutely integrally closed domains without E1
decls:
  - UpperTheory.Et.QuasiAffineEquivalence.a27
  - UpperTheory.Et.QuasiAffineEquivalence.a31
  - UpperTheory.Et.QuasiAffineEquivalence.a33
  - UpperTheory.Et.QuasiAffineEquivalence.intersectionNumber_baseChange
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Quotients of absolutely integrally closed domains without E1

The last four sections of this chapter prove the axioms E1 and E3, which the earlier sections assume. In this section we prove two statements about a quotient $S$ of an absolutely integrally closed domain. First, $\mathrm{sp}(S)$ is acyclic for $q$. Second, if an ideal $J \subseteq S$ lies in the Jacobson radical and idempotents lift from $S/J$ to $S$, then $\mathrm{sp}(S/J) \to \mathrm{sp}(S)$ is an equivalence for $\mathbb{Z}/q(i)$. The next section uses the second statement to prove E1. [Theorem 3.2.3](/entry/n78/) of the section on quotients also gives the acyclicity of $\mathrm{sp}(S)$, but its proof uses E1. Here we do not use E1, and we use only the axioms A1, A9, B1 and B2.

### Rings and pairs

Throughout, $q \geq 1$ is an integer and $\mathbb{Z}/q(i)$ is the Tate twist of section 1. For a ring $S$ and $f \in S$ we write $S_f = S[1/f]$ and $D(f) \subseteq \operatorname{Spec} S$ for the basic open set. If $f, g \in S$, we have restriction maps $S_f \to S_{fg}$ and $S_g \to S_{fg}$. For a class or a locally constant function $a$ on $\operatorname{Spec} S_f$ we write $a|_{fg}$ for its restriction to $\operatorname{Spec} S_{fg}$.

**Definition 3.11.1 (QA ring).** A ring $S$ is a *QA ring* if there is an absolutely integrally closed domain $T$ and a surjective ring map $T \to S$.

**Definition 3.11.2 (Good pair).** Let $C$ be a ring and $J \subseteq C$ an ideal. The pair $(C, J)$ is *good* if $J$ is contained in the Jacobson radical of $C$ and every idempotent of $C/J$ is the image of an idempotent of $C$.

A henselian pair is good. The next section shows that for a henselian pair $(A, I)$ and an integral map $A \to B$, the pair $(B, IB)$ is good.

**Definition 3.11.3 (Primitive root).** Let $B$ be a ring in which $q$ is a unit. A *primitive $q$-th root of unity* in $B$ is a root $\zeta \in B$ of the $q$-th cyclotomic polynomial. A ring map $f : B \to C$ sends it to a primitive root $f(\zeta)$ in $C$.

### Facts that we take as given

We take as given the following facts. Facts 1, 6, 7 and 8 are commutative algebra. Facts 2 to 5 are about cohomology, and each of them states the axioms that it uses.

1. *(Closure.)* A QA ring $S$ is absolutely integrally closed. For $f \in S$ the ring $S_f$ is a QA ring, and for an ideal $J \subseteq S$ the ring $S/J$ is a QA ring. If $T \to S$ is surjective with $T$ an absolutely integrally closed domain, then a monic polynomial over $S$ lifts to a monic polynomial over $T$, $T_{f'}$ is again such a domain for a lift $f'$ of $f$, and $T_{f'} \to S_f$ is surjective.
2. *(Degree zero.)* Assume A9 and $q \geq 1$. For each ring $B$ with a primitive $q$-th root of unity $\zeta$ there is an isomorphism $e_{B, \zeta}$ from the group of locally constant functions $\operatorname{Spec} B \to \mathbb{Z}/q$ to $H^0(\mathrm{sp}(B), \mathbb{Z}/q(i))$. It is natural: for $f : B \to C$ we have $f^* e_{B, \zeta}(\varphi) = e_{C, f(\zeta)}(\varphi \circ \operatorname{Spec} f)$.
3. *(Zariski vanishing.)* Assume B1 and B2. Let $S$ be absolutely integrally closed with $q$ a unit, and let $n > 0$. For each class $x \in H^n(\mathrm{sp}(S), \mathbb{Z}/q(i))$ and each prime $\mathfrak{p}$ of $S$ there is $f \notin \mathfrak{p}$ with $x|_{D(f)} = 0$. The local ring $S_{\mathfrak{p}}$ is strictly henselian, so B2 kills $x$ on $S_{\mathfrak{p}}$, and $S_{\mathfrak{p}}$ is the filtered colimit of the rings $S_f$ with $f \notin \mathfrak{p}$, so B1 kills $x$ on one $S_f$.
4. *(Mayer-Vietoris.)* Assume A1. Let $f, g \in S$ with $(f, g) = S$, and let $F$ be a sheaf. Suppose every class of $H^n(\mathrm{sp}(S_{fg}), F)$ has the form $a|_{fg} - b|_{fg}$ with $a$ a class on $S_f$ and $b$ a class on $S_g$. Then a class of $H^{n+1}(\mathrm{sp}(S), F)$ that vanishes on $S_f$ and on $S_g$ is $0$.
5. *(Empty spectrum.)* Assume A1. If $S$ is the zero ring, then $H^{n+1}(\mathrm{sp}(S), \mathbb{Z}/q(i)) = 0$ for all $n$ and $i$.
6. *(Lifting of locally constant functions.)* If $(C, J)$ is a good pair, then restriction is a bijection from locally constant functions $\operatorname{Spec} C \to Y$ to locally constant functions $\operatorname{Spec}(C/J) \to Y$, for every set $Y$. Such functions correspond to finite families of orthogonal idempotents with sum $1$; these families lift because $(C, J)$ is good, and the lift is unique because $J$ is in the Jacobson radical.
7. *(Sections of finite étale algebras.)* Let $S$ be a QA ring and $C$ a finite étale $S$-algebra with $\operatorname{Spec} C \to \operatorname{Spec} S$ surjective. Then there is an $S$-algebra map $C \to S$. The proof lifts $C$ to an étale algebra over the domain $T$ and splits $C$ along idempotents into pieces whose spectra map by open immersions onto open and closed subsets of $\operatorname{Spec} S$. Since these images cover $\operatorname{Spec} S$, the inverse maps glue along idempotents of $S$ to a section.
8. *(The torsor ring.)* This is the ring in the proof of the lemma below. It is finite étale over $S$ with surjective spectrum, and a section of it gives the splitting.

Facts 2 and 8 hold for every ring, but we apply them only to QA rings.

### Splitting locally constant functions

The first result is the degree $0$ case of the hypothesis in the Mayer-Vietoris fact.

**Lemma 3.11.4 (Splitting of locally constant functions).** Let $q \geq 1$, let $S$ be a QA ring, and let $f, g \in S$ with $(f, g) = S$. Then every locally constant function $\varphi : \operatorname{Spec} S_{fg} \to \mathbb{Z}/q$ has the form $\varphi = a|_{fg} - b|_{fg}$, with $a$ locally constant on $\operatorname{Spec} S_f$ and $b$ locally constant on $\operatorname{Spec} S_g$.

Lean: `UpperTheory.Et.QuasiAffineEquivalence.a27`.

*Proof.* The sets $\varphi^{-1}(c)$ for $c \in \mathbb{Z}/q$ are open and closed and cover $\operatorname{Spec} S_{fg}$. So there are orthogonal idempotents $\varepsilon_c \in S_{fg}$ with $\sum_c \varepsilon_c = 1$ and $\varepsilon_c \notin \mathfrak{p}$ exactly when $\varphi(\mathfrak{p}) = c$. Let $R$ be the set of pairs $(x, y)$ of functions $x : \mathbb{Z}/q \to S_f$ and $y : \mathbb{Z}/q \to S_g$ with
$$
x(k)|_{fg} = \sum_{c \in \mathbb{Z}/q} \varepsilon_c \, y(k + c)|_{fg} \quad \text{for all } k \in \mathbb{Z}/q.
$$
With the operations of the product ring, $R$ is a subring, since the right side is a ring map in $y$: the idempotents are orthogonal with sum $1$. The constant pairs $x(k) = s$, $y(k) = s$ for $s \in S$ lie in $R$, so $R$ is an $S$-algebra. Over $D(f)$ the second component is determined by the first, and $R_f \cong S_f^{\,q}$; over $D(g)$ the first is determined by the second, and $R_g \cong S_g^{\,q}$. Thus $R$ is the $\mathbb{Z}/q$-torsor over $\operatorname{Spec} S$ obtained by gluing two trivial torsors along the translation by $\varphi$. Fact 8 says that $R$ is finite étale over $S$ with surjective spectrum. By fact 7 there is an $S$-algebra map $\sigma : R \to S$.

The map $\sigma$ induces ring maps $(\mathbb{Z}/q \to S_f) \to S_f$ and $(\mathbb{Z}/q \to S_g) \to S_g$ on the two factors, compatible on $S_{fg}$ through the relation above. A ring map from a finite product of copies of $S_f$ to $S_f$ is given by a family of orthogonal idempotents of $S_f$ with sum $1$, that is, by a locally constant function $\alpha : \operatorname{Spec} S_f \to \mathbb{Z}/q$: the map sends $x$ to $x(\alpha(\mathfrak{p}))$ near $\mathfrak{p}$. In the same way the second factor gives $\beta : \operatorname{Spec} S_g \to \mathbb{Z}/q$. On the open set $\varphi = c$ of $\operatorname{Spec} S_{fg}$ the relation reads $x(k) = y(k + c)$, so $\alpha(\mathfrak{p}) = k$ if and only if $\beta(\mathfrak{p}) = k + c$. Hence $\beta|_{fg} = \alpha|_{fg} + \varphi$. We put $a = -\alpha$ and $b = -\beta$. Then $a|_{fg} - b|_{fg} = \beta|_{fg} - \alpha|_{fg} = \varphi$. $\square$

### Acyclicity

**Theorem 3.11.5 (QA rings are acyclic).** Assume A1, A9, B1 and B2. Let $q \geq 1$, and let $S$ be a QA ring in which $q$ is a unit. Then $\mathrm{sp}(S)$ is acyclic for $q$: $H^n(\mathrm{sp}(S), \mathbb{Z}/q(i)) = 0$ for all $n > 0$ and all $i$.

Lean: `UpperTheory.Et.QuasiAffineEquivalence.a31`.

For $n \geq 0$ and $i \in \mathbb{Z}$ we let $\mathrm{MV}(n, i)$ be the statement: for every QA ring $S$ with $q$ a unit and all $f, g \in S$ with $(f, g) = S$, every class of $H^n(\mathrm{sp}(S_{fg}), \mathbb{Z}/q(i))$ has the form $a|_{fg} - b|_{fg}$ with $a$ a class on $S_f$ and $b$ a class on $S_g$.

*Proof of the theorem.* We use one claim.

*Claim.* Assume A1, and let $n \geq 0$ and $i$ be such that $\mathrm{MV}(n, i)$ holds. Let $S$ be a QA ring with $q$ a unit, and let $x \in H^{n+1}(\mathrm{sp}(S), \mathbb{Z}/q(i))$. Suppose that each prime $\mathfrak{p}$ of $S$ has an $f \notin \mathfrak{p}$ with $x|_{D(f)} = 0$. Then $x = 0$.

*Proof of the claim.* Let $I$ be the set of $g \in S$ with $x|_{D(g)} = 0$. If $g \in I$ and $a \in S$, then $S_g \to S_{ag}$ exists, since $g$ is a unit in $S_{ag}$; so $x|_{D(ag)}$ is a restriction of $x|_{D(g)} = 0$, and $ag \in I$. Let $f, g \in I$ and $h = f + g$. In $S' = S_h$ the elements $f$ and $g$ generate the unit ideal. The ring $S'$ is a QA ring by fact 1, $\mathrm{MV}(n, i)$ applies to $(S', f, g)$, and $x|_{D(h)}$ vanishes on $S'_f$ and on $S'_g$, which are localizations of $S_f$ and $S_g$. By fact 4, $x|_{D(h)} = 0$, so $h \in I$. Thus $I \cup \{0\}$ is an ideal. By hypothesis it is contained in no maximal ideal, so $1 \in I$ or $1 = 0$. In the first case $x = x|_{D(1)} = 0$. In the second case $S$ is the zero ring and $x = 0$ by fact 5. This proves the claim.

We now prove the theorem. First, $\mathrm{MV}(0, i)$ holds for every $i$. Let $S$ be a QA ring with $q$ a unit and $(f, g) = S$. By fact 1 the ring $S$ is absolutely integrally closed, so the $q$-th cyclotomic polynomial, which is monic, has a root $\zeta \in S$. Its images give primitive roots in $S_f$, $S_g$ and $S_{fg}$. By fact 2 a class $c$ in degree $0$ on $S_{fg}$ is $e(\varphi)$ for a locally constant function $\varphi$. The lemma on splitting gives $\varphi = a|_{fg} - b|_{fg}$, and by naturality $c = e(a)|_{fg} - e(b)|_{fg}$.

Next, let $k \geq 0$ and suppose that $\mathrm{MV}(k, i)$ holds for all $i$. Let $S$ be a QA ring with $q$ a unit and $x \in H^{k+1}(\mathrm{sp}(S), \mathbb{Z}/q(i))$. By fact 1 the ring $S$ is absolutely integrally closed, so fact 3 gives the hypothesis of the claim, and $x = 0$. Thus $H^{k+1}$ vanishes for all QA rings with $q$ a unit. Since $S_{fg}$ is again such a ring, every class of degree $k + 1$ on it is $0 = 0|_{fg} - 0|_{fg}$, and $\mathrm{MV}(k + 1, i)$ holds.

By induction $\mathrm{MV}(k, i)$ holds for all $k \geq 0$ and $i$, and the step shows $H^{k+1}(\mathrm{sp}(S), \mathbb{Z}/q(i)) = 0$ for all $k \geq 0$. $\square$

### The equivalence for good pairs

**Theorem 3.11.6 (Equivalence for QA rings).** Assume A1, A9, B1 and B2. Let $q \geq 1$, let $S$ be a QA ring in which $q$ is a unit, and let $J \subseteq S$ be an ideal such that $(S, J)$ is a good pair. Then for every $i$ the map $\mathrm{sp}(S/J) \to \mathrm{sp}(S)$ is an equivalence for $\mathbb{Z}/q(i)$.

Lean: `UpperTheory.Et.QuasiAffineEquivalence.a33` (also `UpperTheory.Et.QuasiAffineEquivalence.intersectionNumber_baseChange`).

*Proof.* Let $\pi : S \to S/J$ be the quotient map. We show that $\pi^* : H^n(\mathrm{sp}(S)) \to H^n(\mathrm{sp}(S/J))$ is bijective for each $n$, with coefficients $\mathbb{Z}/q(i)$.

If $n < 0$, both groups are $0$ by A9.

If $n = 0$, let $\zeta \in S$ be a root of the $q$-th cyclotomic polynomial, which exists because $S$ is absolutely integrally closed (fact 1). By the naturality in fact 2, $\pi^* e_{S, \zeta}(\varphi) = e_{S/J, \pi(\zeta)}(\varphi|_{\operatorname{Spec}(S/J)})$. The maps $e$ are bijective, and restriction of locally constant functions is bijective by fact 6, since $(S, J)$ is good. Hence $\pi^*$ is bijective.

If $n > 0$, the ring $S/J$ is a QA ring by fact 1, and $q$ is a unit in it. By the theorem on acyclicity both groups are $0$. $\square$

**Remark 3.11.7 (Formalization).** The namespace `QuasiAffineEquivalence` refers to QA rings, not to quasi-affine schemes. The names `a0` to `a33` number the steps of one chain: each step applies a proof of a fact to the earlier steps, and `a27`, `a31` and `a33` are the lemma and the two theorems of this section ([EquivalenceQuasiAffine.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleAxioms/EquivalenceQuasiAffine.lean#L66)). The name `intersectionNumber_baseChange` is a second name for `a33` and has no relation to intersection numbers; five other files of the same folder use this name for the last step of their chains. The statements carry their axioms as hypotheses, so `a33` says "A1, A9, B1 and B2 imply the equivalence". Fact 8 is two statements, one for the étale property and one for the section; the proof of the second also reads off the idempotents that give $\alpha$ and $\beta$ ([LCSplitPf.lean](lean:Development/EtaleCohomology/EtaleSheaves/LCSplitPf.lean#L111)). The induction in the proof of acyclicity is on the statement $\mathrm{MV}(k, i)$ for all $i$ at once ([AcycQAPf.lean](lean:Development/EtaleCohomology/EtaleSheaves/AcycQAPf.lean#L26)).
