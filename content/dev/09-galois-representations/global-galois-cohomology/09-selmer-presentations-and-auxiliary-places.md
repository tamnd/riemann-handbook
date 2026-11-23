---
title: Selmer presentations and auxiliary places
decls:
  - GlobalTheory.SelFun.oneMatrix_of_galoisCohomology
  - GlobalTheory.NewPrime.step
  - GlobalTheory.StepTwo.Dyadic.bound_mod_two_of_hypothesis
  - GlobalTheory.T.boundModTwoUniformizerAtTwo_of_chebotarev
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Selmer presentations and auxiliary places

This section studies the Selmer groups of a Galois module twisted by a family of characters. First it proves that these Selmer groups have a square presentation over the group ring of the characters, with no unit entry. Then it proves the inductive step that adds one auxiliary place, chosen by Chebotarev, to control the determinant of the presentation. The two results give an order bound: when the cyclotomic invariant $\nu$ is positive, the determinant has a coefficient of bounded degree and of valuation at most $v(\ell^\nu)$. The next section uses this bound to build good twists, and through it the result reaches [the local export condition from rational rows](/entry/export-at-of-bundles-alt/). Background is in [Selmer and Tate-Shafarevich groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups), [the splitting of primes](/learn/number-fields/#the-splitting-of-primes) and [decomposition groups, inertia and Frobenius](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius).

### Setting

Let $F$ be a [[number field|MWBDFS2KJ5]] with [[absolute Galois group|PGKWBJDTKX]] $G = \operatorname{Gal}(\bar F/F)$. A twist system attaches to each twist index $i$ a prime $\ell = \ell_i$, a complete discrete valuation ring $O$ with maximal ideal $\mathfrak{m}$ and residue field $k$, and for each sign $s$ a free $O$-module $T_s$ of rank $r$ with a continuous action of $G$. A Bloch-Kato phase datum fixes the local conditions. Let $\varepsilon$ be the $\ell$-adic [[cyclotomic character|XSGB5K2KEG]] and $n = tr$ for a fixed integer $t$. Put
$$\nu = \min_{g \in G} v_\ell\bigl(\varepsilon(g)^n - 1\bigr),$$
with $\nu = 0$ if all $\varepsilon(g)^n$ equal $1$, and let $I = \ell^\nu \mathfrak{m}$.

Fix $M \geq 1$ and a finite family of auxiliary [[places|BT5V3TSNY6]] $P_q$, $q \in \iota$, each with a character $d_q : G \to \mathbb{Z}/\ell^M$. Let
$$\Lambda = O\bigl[(\mathbb{Z}/\ell^M)^\iota\bigr]$$
be the group ring and let $\kappa : G \to \Lambda^\times$ send $g$ to the group element $(d_q(g))_q$. For a discrete $\Lambda$-module $B$ killed by powers of $\ell$, the group $G$ acts on $T_s \otimes B$ through $T_s$ and $\kappa^{-1}$. Let $Q$ be the set of places of $F$ below the $P_q$, and let $\operatorname{Sel}_Q(B) \subseteq H^1(G, T_s \otimes B)$ be the [[Selmer group|36YNSTESMQ]] with the local conditions of the phase datum and relaxed conditions at $Q$.

The ring map $O[x_q : q \in \iota] \to \Lambda$ with $x_q \mapsto e_q - 1$, where $e_q$ is the $q$-th basis element of the group, is surjective. A polynomial $F$ *represents* an element of $\Lambda$ if it maps to it.

**Definition 2.9.1 (presentation).** A square matrix $\Phi$ of size $a$ over $\Lambda$ *computes the Selmer data* if, for every discrete $\ell$-power torsion $\Lambda$-module $B$, there is an isomorphism $\ker(\Phi : B^a \to B^a) \cong \operatorname{Sel}_Q(B)$, natural in $B$.

### The Selmer presentation

The results of this section assume eleven statements of Galois cohomology, given as hypotheses: a Chebotarev statement (for an open normal subgroup $U$ of $G$, an element $g$ and a finite set $A$ of places, there is an unramified place $v \notin A$ of degree one with a Frobenius in $gU$); Poitou-Tate duality for totally complex fields; cohomological dimension two; tame local statements; local finiteness; local Tate duality; the local Euler characteristic formula; global finiteness; the global Euler characteristic formula; unramified orthogonality; and a six-part statement on Poitou-Tate cokernels, the Tate-Shafarevich group, $H^2$ duality and local cohomology.

**Theorem 2.9.2 (Selmer presentation).** Assume the eleven statements. Let $i$ be a twist index and $s$ a sign that satisfies the Galois hypotheses. Let $M \geq 1$ and let $(P_q)$ be auxiliary places that pass the slope test, with $Q$ the places below them. Then there is a square matrix $\Phi$ over $\Lambda$ that computes the Selmer data, and no entry of $\Phi$ is a unit.

Lean: `GlobalTheory.SelFun.oneMatrix_of_galoisCohomology`.

*Proof.* Consider the functor $B \mapsto \operatorname{Sel}_Q(B)$ on discrete $\ell$-power torsion $\Lambda$-modules.

Step 1: left exactness. The residual module $T_s \otimes k$ has no invariants under $G$, and the local conditions are saturated. So a short exact sequence $0 \to B' \to B \to B''$ gives an exact sequence $0 \to \operatorname{Sel}_Q(B') \to \operatorname{Sel}_Q(B) \to \operatorname{Sel}_Q(B'')$.

Step 2: limits. The Selmer group of a direct limit is the direct limit of the Selmer groups.

Step 3: the obstruction. Let $a = \dim_k \operatorname{Sel}_Q(k)$. The obstruction to right exactness lives in a group built from $H^2$ and the local cohomology at $Q$. By Poitou-Tate duality, cohomological dimension two, local and global finiteness, the Euler characteristic formulas and a count of the local conditions, its dimension is at most $a$. The count uses the Galois hypotheses on $s$, which make the local terms balance.

Step 4: the matrix. A left exact functor on torsion modules that commutes with direct limits, with $a$-dimensional value on $k$ and an obstruction of dimension at most $a$, is the kernel of an $a \times a$ matrix $\Phi$ over $\Lambda$. Then $\ker(\Phi \otimes k)$ has dimension $a$, so $\Phi \otimes k = 0$. Hence every entry of $\Phi$ lies in the maximal ideal of $\Lambda$ and is not a unit. $\square$

### The inductive step

Split the auxiliary places into first-half places $P_{(1)}, \dots, P_{(R)}$ and second-half places $P'_{(1)}, \dots, P'_{(n)}$ with $n \leq R$. Let $e = v(\ell^\nu)$ be the valuation of $\ell^\nu$ in $O$.

**Definition 2.9.3 (determinant conditions).** The family $P$ satisfies $\mathrm{NF}(c)$ if, for every $\Phi$ that computes the Selmer data and every polynomial $F$ that represents $\det \Phi$, some coefficient of $F$ of degree less than $c$ is not in $I$. It satisfies $\mathrm{NFit}(c)$ if, for every such $\Phi$ of size $a$, either $a = 0$, or some entry of the adjugate of $\Phi$ is represented by polynomials that have a unit coefficient of degree less than $c$ in which the first-half variables with index at least $n$ do not occur.

**Definition 2.9.4 (Step).** For a twist index $i$ and a sign $s$, the property $\mathrm{Step}(i, s)$ says: if $\nu > 0$, $n < R$ and $2(e+1)w + 2 + 2r \leq \ell^{M - \nu - 1}$ with $\nu + 2 \leq M$, and $P$ is a family of places with the localization conditions for a small subgroup $L$ and a tame inertia element $z$, and $P$ satisfies $\mathrm{NFit}(w+1)$, then there is one more second-half place $P'_{(n+1)}$ such that the extended family keeps the localization conditions and satisfies $\mathrm{NF}(2(e+1)w + 2 + 2r)$.

**Theorem 2.9.5 (new auxiliary place).** Assume the eleven statements and that the Selmer presentation exists for all data. Then $\mathrm{Step}(i, s)$ holds for each twist index $i$ and each sign $s$ that satisfies the Galois hypotheses.

Lean: `GlobalTheory.NewPrime.step`.

*Proof.* Put $c = 2(e+1)w + 2$.

Case 1: $P$ satisfies $\mathrm{NF}(c)$. Chebotarev gives a new place, not in the given finite set, whose Frobenius is conjugate to a prescribed element modulo $L$. The growth lemma says that adding one place raises the degree bound by at most $2r$. This gives $\mathrm{NF}(c + 2r)$.

Case 2: some $\Phi$ of size $a$ computes the Selmer data, and $\det \Phi$ is represented by a polynomial $F_0$ whose coefficients of degree less than $c$ all lie in $I$. If $a = 0$, then $\det \Phi = 1$, and $1 \notin I$, a contradiction. So by $\mathrm{NFit}(w+1)$ an adjugate entry $\Phi^{\mathrm{adj}}_{b b'}$ is represented by a polynomial $F_1$ with a unit coefficient of low degree.

From $F_0$ and $F_1$ one builds a finite local $O$-algebra $A$ killed by $I$, an element $t \in A$ with $t^{\ell^{M-\nu-1}} = 0$, and a ring map $\varphi : \Lambda \to A$ with $e_q \mapsto 1 + a_q t$, such that $\varphi(\det \Phi) = 0$ and $\varphi(\Phi^{\mathrm{adj}}_{b b'})$ divides $t^{(e+1)w}$, while a suitable product of $\ell^\nu$ and a power of $t$ stays nonzero in $A$. Since $\Phi \cdot \Phi^{\mathrm{adj}} = \det \Phi \cdot 1$, the column $(\varphi(\Phi^{\mathrm{adj}}_{u b'}))_u$ lies in $\ker(\varphi(\Phi))$ on $A^a$. Through the presentation it gives a Selmer class $x$ with coefficients in $A$.

The order formula for the dual Selmer group, from Poitou-Tate duality and the Euler characteristic formulas, gives a class $y$ in the dual Selmer group that the global pairing does not kill against $x$. The local invariants of these classes vanish at the first-half places. Let $U \leq L$ be an open normal subgroup on which the cocycles of $x$ and $y$ become simple. Chebotarev gives a new place $P'_{(n+1)}$ whose Frobenius lies in a coset of $U$ where the local pairing of $x$ and $y$ is nonzero. At this place the class $x$ fails the new local condition, and the determinant of a presentation for the extended family gains a coefficient outside $I$ of degree less than $c + 2r$. $\square$

### The order bound

**Theorem 2.9.6 (order bound when $\nu > 0$).** Assume the eleven statements. Let $i$ be a twist index with $\nu > 0$ and let $T$ be a set of signs that satisfy the Galois hypotheses. Then there are integers $R$, $D$ and $M_0$ such that for all $M \geq M_0$, every admissible family, every tame inertia element $z$, every open normal subgroup $H'$ of $G$ and every finite set $A$ of places, there are $2R$ auxiliary places $P$ that pass the slope test and avoid $A$ with the following property. For each $s \in T$, each $\Phi$ that computes the Selmer data at $P$ and each polynomial $F$ that represents $\det \Phi$, some coefficient of $F$ of degree at most $D$ has valuation at most $v(\ell^\nu)$.

Lean: `GlobalTheory.StepTwo.Dyadic.bound_mod_two_of_hypothesis`.

*Proof.* A coefficient is outside $I = \ell^\nu \mathfrak{m}$ if and only if its valuation is at most $v(\ell^\nu)$. So it is enough to reach $\mathrm{NF}(c)$ for a bounded $c$. The proof is an induction on the number $n$ of second-half places. It has five inputs.

1. Prescribed Frobenius: for elements $h_1, \dots, h_R$ that fix the $2\ell^M$-th roots of unity, Chebotarev gives first-half places avoiding $A$ whose Frobenius elements are conjugate to the $h_a$ modulo a given open subgroup.
2. Choice of the $h_a$: global finiteness and a spanning argument for the cocycle forms give elements $h_a$ such that each matching choice of Frobenius elements cuts the residual Selmer group down to corank $1$ (corank $0$ when $\nu = 0$). This uses that a residual Selmer group and its dual have the same dimension.
3. Start: with corank $1$, an adjugate entry has a unit coefficient of degree at most $4rn + 1$. This uses the residual order bound and a reciprocity law for the auxiliary places.
4. Growth: one more place keeps $\mathrm{NF}$ and $\mathrm{NFit}$, with the degree bound raised by $2r$. This uses the tame local statements and the Selmer presentation.
5. The new place: the previous theorem.

Each stage adds one second-half place. After $R$ stages the family has $2R$ places, and $\mathrm{NF}(c)$ holds for a bound $c$ that depends only on $R$, $r$ and $e$. $\square$

**Theorem 2.9.7 (order bound when $\nu > 0$, second form).** The order bound when $\nu > 0$ holds under the same eleven statements.

Lean: `GlobalTheory.T.boundModTwoUniformizerAtTwo_of_chebotarev`.

*Proof.* The statement is the same as that of the previous theorem. $\square$

**Remark 2.9.8 (Formalization).** The presentation theorem is in [SelmerPresentationMatrixOfGaloisCohomology.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SelmerPresentationMatrixOfGaloisCohomology.lean#L20). It does not use the hypotheses `Cheb`, `TameLocal` and `UnramifiedOrthogonality`. A second name, `GlobalTheory.T.selmerPresentationMatrix_of_galois_cohomology`, has the same statement and is proved by a `first | exact ...` tactic ([SelmerPresentationMatrixOfGaloisCohomologyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SelmerPresentationMatrixOfGaloisCohomologyStatement.lean#L9)). The inductive step `GlobalTheory.NewPrime.step` is in [AntiOfKer.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AntiOfKer.lean#L153); it does not use `CohDimTwo` and `UnramifiedOrthogonality`. The properties `Start`, `Grow`, `Step`, `NF` and `NFit` are in [Small2.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/Small2.lean#L40), and the induction `thmC_of_parts` is in [AddValLeOfNotMem.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AddValLeOfNotMem.lean#L87). The order bound is in [BoundModTwoUniformizerAtTwoOfChebotarev.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BoundModTwoUniformizerAtTwoOfChebotarev.lean#L25), and its second name is proved by a `first | exact ...` tactic ([BoundModTwoUniformizerAtTwoOfChebotarevStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BoundModTwoUniformizerAtTwoOfChebotarevStatement.lean#L9)). The names "mod two", "at two" and the namespace `Dyadic` suggest $\ell = 2$, but the statement is `ThmC`, which covers every $\ell_i$ with $\nu_i > 0$. The Galois hypothesis `GalHyp` ([IsTameInertiaElementAtTwistPrime.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsTameInertiaElementAtTwistPrime.lean#L119)) has a conjunct `True` and asks $r \geq 100$. The last hypothesis, `Gen.ArchimedeanSignatureMatching`, contains nothing archimedean; it is the six-part statement above. The ring $\Lambda$ is `abelian₂`, the map from polynomials is `toLam`, and the presentation property is `Computes`.
