---
title: Cutting out a representation of dimension a
decls:
  - UpperTheory.Gal.Int.Div.divOne_holds
  - UpperTheory.Gal.Int.Div.divAll_holds
  - UpperTheory.Gal.Int.Div.seedFinOdd_of_geoOne
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cutting out a representation of dimension a

The Galois row in weight one (Definition 3.7.1) gives, for a space $U$ of automorphic forms on $\mathrm{U}(a)$, representations $\rho$ of some large dimension. At good places they satisfy only a divisibility: the Satake polynomial of $U$ kills $\rho$ of a Frobenius element. This section cuts out of such a $\rho$ a representation $r$ of dimension $a$ whose Frobenius characteristic polynomials are the Satake polynomials, and it shows that $r$ does not depend on $\rho$. Then the local information that the different $\rho$ carry at different places all moves to one $r$. The results are [Theorem 3.25.3](/entry/div-one-holds/), [Theorem 3.25.5](/entry/div-all-holds/) and [the seed theorem](/entry/seed-fin-odd-of-geo-one/), which is the first input of [the main line](/entry/core-all-of/).

We keep the notation of Section 07. $E$ is a CM field, $\Omega$ an algebraic closure, $G_E = \mathrm{Gal}(\Omega/E)$, $\ell$ a prime and $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. We fix $d > 0$ with $-d$ a square in $E$; a split place $w$ is *usable* if $-d$ is a square in $\mathbb{Q}_q$ for the prime $q$ below $w$. $U$ is an automorphic space on $\mathrm{U}(a)$. For a Satake parameter $B$ of $U$ at a split place $w$, $\mathrm{sat}_a(B) = \{N(w)^{(a-1)/2}\beta : \beta \in B\}$ and $P_B(X) = \prod_{b \in \mathrm{sat}_a(B)} (X - b)$. A finite multiset $s$ is *generic* if no other multiset of the same size, with all elements in $s$, has the same product.

### Subrepresentations and the base condition

**Definition 3.25.1 (Inside and covers).** Let $\Gamma$ be a group, $k$ a field, $r : \Gamma \to \mathrm{GL}_a(k)$ and $\rho : \Gamma \to \mathrm{GL}_d(k)$. Then $r$ is *inside* $\rho$ if there is a $d \times a$ matrix $A$ of rank $a$ with $\rho(g) A = A\, r(g)$ for all $g$. And $r$ *covers* $\rho$ if for some $m$ there is a matrix $B$ of rank $d$ with $(r(g) \otimes 1_m) B = B \rho(g)$ for all $g$.

Lean: `UpperTheory.Gal.Int.Div.Inside` (also `UpperTheory.Gal.Int.Div.Covers`).

So $r$ is inside $\rho$ when it is a subrepresentation, and $r$ covers $\rho$ when $\rho$ is a quotient of a sum of copies of $r$. If $r$ is inside $\rho$, then $a \leq d$, the kernel of $\rho$ is in the kernel of $r$, and a polynomial that kills $\rho(g)$ kills $r(g)$.

**Definition 3.25.2 (Geometric base, determinant character, divided representation).** A continuous $\rho : G_E \to \mathrm{GL}_{n}(\overline{\mathbb{Q}}_\ell)$ is a *geometric base* for $U$ if $\rho$ is semisimple, there is a finite set $X$ such that at each usable $w \notin X$ with $w \nmid \ell$ and each Satake parameter $B$ of $U$ at $w$, $\rho$ is trivial on inertia and $\iota^{-1} P_B$ kills $\rho(\sigma^{-1})$ for every Frobenius $\sigma$ at $w$, and at some $w \mid \ell$ and some $\tau$ the Hodge-Tate jumps of $\rho$ contain a lacunary set of $a$ integers. A continuous character $\psi$ of $G_E$ is a *determinant character* for $U$ if at each split $w$ with Satake parameter $B$ it satisfies, as a representation of dimension one, the local clauses of an attached representation for the single parameter $\prod \mathrm{sat}_a(B)$. A continuous semisimple $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ is *divided from* $U$ if there are an open dense $V \subset G_E$ and a finite set $X$ such that at each usable $w \notin X$ with $w \nmid \ell$ and each Satake parameter $B$, $r$ is trivial on inertia and $\iota$ of the characteristic polynomial of $r(s^{-1})$ is $P_B$ for each Frobenius $s \in V$ at $w$.

Lean: `UpperTheory.Gal.Int.Div.VBase` (also `UpperTheory.Gal.Int.Div.IsDetChar`, `UpperTheory.Gal.Int.Div.IsDivRep`).

The representations $\rho$ of Definition 3.7.1 are geometric bases. The lacunary jumps are the hypothesis that lets one cut out a piece of dimension $a$.

### One small representation

The construction uses five facts. We state them as they are used.

1. *Cutting.* Let $\rho$ be continuous and semisimple with a lacunary set of $a$ Hodge-Tate jumps, and $\psi$ a continuous character. Suppose that for a dense set of $g$ there is a monic $Q$ of degree $a$ with $Q(\rho(g)) = 0$ and $\psi(g) = (-1)^a Q(0)$. Then there is a continuous semisimple $r$ of dimension $a$, inside $\rho$ and covering $\rho$, such that the set of $g$ where $r(g)$ has a separable characteristic polynomial is open and dense.
2. *Density.* For each finite $X$, the Frobenius elements at usable places $w \notin X$ prime to $\ell$ where $U$ has Satake parameters are dense in $G_E$.
3. *Determinant.* If $\psi$ is a determinant character for $U$, then at each split $w \nmid \ell$ with Satake parameter $B$, $\psi$ is trivial on inertia and $\iota\,\psi(\sigma^{-1}) = \prod \mathrm{sat}_a(B)$ for each Frobenius $\sigma$.
4. *Subrepresentations.* The facts after the definition of inside.
5. *Separable pinning.* If a monic $Q$ of degree $a$ kills an $a \times a$ matrix $M$ whose characteristic polynomial is separable, then $Q$ is that characteristic polynomial.

Fact 5 is elementary. The characteristic polynomial $\chi_M$ is separable, so it equals the minimal polynomial of $M$, which divides $Q$. Both are monic of degree $a$.

Fact 1 is a theorem of Sen type with a group theoretic step. The lacunary jumps give an element of the Lie algebra of the Zariski closure of the image of $\rho$ with $a$ lacunary eigenvalues, and this element, with the polynomials $Q$, picks out $r$.

**Theorem 3.25.3 (One small representation).** Let $\psi$ be a determinant character for $U$ and let $\rho$ be a geometric base for $U$. Then there is $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ divided from $U$ that is inside $\rho$ and covers $\rho$.

Lean: `UpperTheory.Gal.Int.Div.divOne_holds` (also `UpperTheory.Gal.Int.Div.divOne_of`, `UpperTheory.Gal.Int.Div.DivOne`).

*Proof.* Let $X$ be the finite set of the geometric base. By fact 2 the Frobenius elements at the good places outside $X$ are dense, so their inverses are dense too. Let $g = \sigma^{-1}$ be one of them, at $w$ with parameter $B$, and put $Q = \iota^{-1} P_B$. Then $\mathrm{sat}_a(B)$ has $a$ elements, so $Q$ is monic of degree $a$, and $Q(\rho(g)) = 0$ by the base condition. By fact 3, $\psi(g) = \iota^{-1} \prod \mathrm{sat}_a(B) = (-1)^a Q(0)$. Fact 1 gives $r$, inside $\rho$ and covering it, with an open dense set $W$ of separable elements. Put $V = W^{-1}$.

Let $w \notin X$ be good with parameter $B$. Since $r$ is inside $\rho$ and $\rho$ is trivial on inertia at $w$, so is $r$. For a Frobenius $s$ at $w$ with $s \in V$, $Q$ kills $\rho(s^{-1})$, hence kills $r(s^{-1})$, and $r(s^{-1})$ has a separable characteristic polynomial. By fact 5 this polynomial is $Q$. So $r$ is divided from $U$. $\square$

**Lemma 3.25.4 (Uniqueness).** Two representations divided from $U$ are isomorphic.

Lean: `UpperTheory.Gal.Int.Div.DivUniq`.

*Proof.* Let $r, r'$ have sets $V, X$ and $V', X'$. By fact 2 the inverses of the Frobenius elements at good places outside $X \cup X'$ are dense, and $V \cap V'$ is open and dense, so their intersection is dense. On this set the characteristic polynomials of $r$ and $r'$ are equal. Two continuous semisimple representations whose characteristic polynomials agree on a dense set are isomorphic. $\square$

### All geometric bases at once

**Theorem 3.25.5 (One representation for all bases).** Let $a \geq 1$ and suppose that $U$ has a geometric base. Then there is $r$ divided from $U$ such that for every geometric base $\rho$ of $U$ and every place $w$:

1. if $w$ is split and prime to $\ell$, $B$ is a generic Satake parameter of $U$ at $w$, and $\iota^{-1}P_B$ kills $\rho$ of every inverse Frobenius at $w$, with $\rho$ trivial on inertia, then $r$ is trivial on inertia at $w$ and $\iota$ of the characteristic polynomial of $r(\sigma^{-1})$ is $P_B$ for every Frobenius $\sigma$;
2. if $\rho$ is crystalline at $w$ and its jumps contain the jumps of the weights of $U$, then $r$ is crystalline and de Rham at $w$ with exactly these jumps;
3. if $w$ is split, $B$ is generic and $\rho$ is crystalline at $w$ with, for some $g$ of degree $-1$, the characteristic polynomial of $g$ on $\mathrm{WD}_w(\rho)$ dividing a power of $P_B$, then $r$ is crystalline at $w$ and $\mathrm{WD}_w(r)$ has the characteristic polynomials of the unramified representation with parameters $\mathrm{sat}_a(B)$.

Lean: `UpperTheory.Gal.Int.Div.divAll_holds` (also `UpperTheory.Gal.Int.Div.divAll_of`, `UpperTheory.Gal.Int.Div.DivAll`).

*Proof.* A determinant character $\psi$ for $U$ exists; it comes from an algebraic Hecke character whose value at each split $w$ is the product of the Satake parameters. Fix a geometric base $\rho_0$ and let $r$ be the representation of [Theorem 3.25.3](/entry/div-one-holds/) for $\rho_0$. Then $\det r = \psi$, since both are continuous and agree on the dense set of facts 2 and 3. Let $\rho$ be any geometric base. The theorem gives $r'$ divided from $U$, inside $\rho$ and covering $\rho$. By the lemma, $r' \cong r$, so $r$ is inside $\rho$ and covers $\rho$.

Clause 1. $r$ is trivial on inertia since $\rho$ is. For a Frobenius $\sigma$, $\iota^{-1}P_B$ kills $r(\sigma^{-1})$, and by fact 3, $\iota \det r(\sigma^{-1}) = \prod \mathrm{sat}_a(B)$. The multiset $\mathrm{sat}_a(B)$ is generic since $B$ is. A matrix killed by $\iota^{-1}P_B$ has eigenvalues in $\iota^{-1}\mathrm{sat}_a(B)$, and the product fixes the multiset by genericity. So the characteristic polynomial is $P_B$.

Clause 2. Since $r$ is inside $\rho$, it is crystalline at $w$, and its jumps are in those of $\rho$. Since $r$ covers $\rho$, $\rho$ is inside a sum of copies of $r$, so the jumps of $\rho$ are in a multiple of those of $r$. The jumps of the weights of $U$ at $\tau$ are $a$ distinct integers, and $r$ has exactly $a$ jumps at $\tau$, so they are equal.

Clause 3. The characteristic polynomial of $g$ on $\mathrm{WD}_w(r)$ divides that on $\mathrm{WD}_w(\rho)$, so it divides a power of $P_B$. Its roots have product $\prod \mathrm{sat}_a(B)$ by the determinant, and genericity gives that it is $P_B$. A crystalline Weil-Deligne representation is unramified with zero monodromy, so this one value fixes the characteristic polynomials on the whole Weil group. $\square$

### The seed statement

**Definition 3.25.6 (Seed statement).** The *seed statement* says the following. Let $a$ be odd, let $d$ satisfy the field conditions of Definition 3.7.1, let $T$ be a finite set of non-split places, and let $w_0, v'$ be split places above $\ell$ that are apart. Let $U, S, Y$ be given. Then there is a finite set $Z_0$ of usable places prime to $\ell$ and apart from $w_0$ and from $S$ such that for each $U'$ on $\mathrm{U}(a)$ that is automorphic off $T$, has the type of Definition 3.7.1 at $w_0$, has the lacunary weight relative to $U$, has Satake parameters off $w_0$ and $S$ and at $v'$, and is generic at $Z_0$, there is a continuous semisimple $r$ of dimension $a$ such that:

1. $r$ is divided from $U'$, at the places apart from $S$;
2. at each usable $w \in Y$ prime to $\ell$ and apart from $S$, with a generic parameter $B$, $r$ satisfies the Frobenius clause of the theorem above;
3. at each $w \in Y$ above $\ell$ and apart from $w_0$, $v'$ and $S$, $r$ is crystalline and de Rham with the jumps of the weights of $U'$, and with a generic parameter $B$ the Frobenius power sums of $\mathrm{WD}_w(r)$ are those of $\mathrm{sat}_a(B)$.

Lean: `GlobalTheory.CongL.SeedFinOdd` (also `GlobalTheory.CongL.SeedWU4`).

**Theorem 3.25.7 (Seed).** If the Galois row in weight one holds, then the seed statement holds.

Lean: `UpperTheory.Gal.Int.Div.seedFinOdd_of_geoOne` (also `UpperTheory.Gal.Int.Div.seedFinOdd_of`).

*Proof.* Take $Z_0 = \emptyset$. Fix $U'$ with the conditions. Its lacunary weight gives a lacunary weight at $v'$.

The Galois row in weight one needs two places $u_0, u'$ over the same place of $\mathbb{Q}(x)$, with $x^2 = -d$, and at the places $w$ above $\ell$ it gives information only for $w$ over the same place of $\mathbb{Q}(x)$ as $u'$. For a split place $u$, its conjugate $\bar u$ lies over the same place of $E^+$. For $u$ and $w$ above $\ell$, either $u$ or $\bar u$ lies over the same place of $\mathbb{Q}(x)$ as $w$. The type at $w_0$, the Satake parameters and the lacunary weight at $v'$ pass to the conjugate places. So for each $w \mid \ell$ we can choose $u_0 \in \{w_0, \bar w_0\}$ and $u' \in \{v', \bar v'\}$ over the place of $\mathbb{Q}(x)$ under $w$, with the same apartness as $w_0$ and $v'$, and apply the Galois row in weight one to $(u_0, u')$.

At $w = v'$ this gives a geometric base, and [Theorem 3.25.5](/entry/div-all-holds/) gives $r$ divided from $U'$. This is clause 1. For each further place, the Galois row in weight one at the pair chosen for it gives a geometric base $\rho$ with the local property at $w$, and the corresponding clause of the theorem moves this property to the same $r$. Genericity in the sense of the type gives generic parameters. The places above $\ell$ are split, since the non-split places are prime to $\ell$. Clause 3 in power sums follows from equal characteristic polynomials. $\square$

**Remark 3.25.8 (Formalization).** The three theorems are in [DivisionOneGeometricRepresentation.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/DivisionOneGeometricRepresentation.lean#L53), lines 53 and 54, and [MainFin.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/MainFin.lean#L13). We read `divOne_of` in [PDivOne.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PDivOne.lean#L35), `divAll_of` in [PhiOfDivOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PhiOfDivOf.lean#L166), `divUniq_of`, `frobSeed_of`, `jumpSeed_of`, `divSet_of` and `seedFinOdd_of` in full, and only the outline of `phiSeed_of`. Facts 1 to 5 are `DivSet`, `DenseUs`, `DetFrob`, `InFacts` and `SepPin`. We did not open `denseUs_of`, `detFrob_of`, `inFacts_of`, `sepPin_of`, `detEx_of`, `centU_of`, `divDet_of`, `subLoc_of`, `genPin_of`, `rootPin_of`, `algGen_of`, `coverIn_of`, `jumpCard_of`, `GlobalTheory.SplitAttUniq.repIso_of_dense`, the facts on conjugate places, or the inputs of `divSet_of`: `LateralTheory.DivDb.goal_holds` (the group theoretic step `DivWCoreLac`), `senWLac_of` and `lacBridge_of`. Some odd points. `divSet_of` takes `InFacts` as an argument and does not use it ([PDivSet.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PDivSet.lean#L18)). `PhiOfDiv` ([InsideRefl.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/InsideRefl.lean#L118)) and `phiOfDiv_of` (PhiOfDivOf.lean, line 161) are not used. `seedFinOdd_of` ([SeedFinOddOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/SeedFinOddOf.lean#L47)) takes $Z_0 = \emptyset$ and does not use the hypotheses $w \in Y$ and apartness from $S$, so the seed statement holds in a stronger form. The group theoretic step has the generic name `goal_holds`.
