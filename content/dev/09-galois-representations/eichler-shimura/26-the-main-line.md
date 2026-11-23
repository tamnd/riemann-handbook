---
title: The main line
decls:
  - UpperTheory.Gal.Int.Core.joinUp_holds
  - UpperTheory.Gal.Int.Core.rowCsd_of
  - UpperTheory.Gal.Int.Core.core_of_limU
  - UpperTheory.Gal.Int.Core.core_of_limOdd
  - UpperTheory.Gal.Int.Core.toCore
  - UpperTheory.Gal.Int.Core.toCoreK
  - UpperTheory.Gal.Int.coreAll_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The main line

This section proves the spherical Galois row (Definition 3.18.2) from the seed statement, the congruence statement and the theta lift statement [TLiftK](/step/tlift-k-def/). [The limit corollary](/entry/lim-fin-odd-of/) gives Galois representations for spaces on $\mathrm{U}(a)$ with $a$ odd. Five steps carry them to all regular algebraic polarized cuspidal $\pi$: the Frobenius above $\ell$, the removal of auxiliary places, all ranks by the theta lift, descent to $\mathrm{GL}_a$, and base change to reach every place. The result is [the main line theorem](/entry/core-all-of/), the input of Theorem 3.18.4.

We keep the notation of Sections 18, 24 and 25: $E$ is a CM field, $G_E = \mathrm{Gal}(\Omega/E)$, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, and $x_B$ is the unramified Weil-Deligne representation of a Satake parameter $B$. Let $\eta_E$ be the quadratic character of $E^+$ attached to $E$. The field $E$ satisfies the *strong field conditions* if $-d$ is a square in $E$ for some $d > 0$, $[E^+ : \mathbb{Q}]$ is even, $E/E^+$ is unramified at every finite place, every place above $\ell$ is split, and three places above $\ell$ are pairwise apart. It satisfies the *inertia condition* if at each non-split place, the place of $E^+$ below is prime to $2$, has norm greater than $3$ and does not contain the different of $E^+$.

### Rows and scopes

**Definition 3.27.1 (Spherical clauses and rows).** Let $\pi$ be a cuspidal representation of $\mathrm{GL}_a(\mathbb{A}_E)$, $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$, and $w$ a place where $\pi$ has a Satake parameter $B$. The four *spherical clauses* at $w$ are those of item 2 of Definition 3.18.2: if $w \nmid \ell$, the Frobenius eigenvalues of $r$ at $w$ are $\mathrm{sat}_a(B)$; $r$ is de Rham at $w$ with the jumps of the infinity type of $\pi$; $r$ is crystalline at $w$; and each $g \in W_A$ has the same characteristic polynomial on $\mathrm{WD}_w(r)$ and on $x_B$. For a condition $p$ on places, $\pi$ has a *row on $p$* if a continuous semisimple $r$ satisfies the four clauses at each $w$ with $p(w)$ where $\pi$ has a Satake parameter.

Lean: `GlobalTheory.RoadU.SphAt` (also `UpperTheory.Gal.Int.Core.RowP`).

**Definition 3.27.2 (Scopes and the core statement).** A pair $(\pi, \chi)$ is in scope *all* if $\pi$ is regular algebraic and polarized by $\chi$. It is in scope *good* if also $-d$ is a square in $E$ for some $d > 0$, $[E^+ : \mathbb{Q}]$ is even, and each non-split place is prime to $\ell$, unramified over $E^+$, with a Satake parameter for $\pi$. It is in scope *csd* if it is good and $\chi = \eta_E^a$. The *core statement* is Definition 3.18.2 for pairs in scope csd, with item 2 asked only at split places.

Lean: `GlobalTheory.GalCut.InScope` (also `GlobalTheory.RoadU.Core`, `GlobalTheory.RoadU.CoreAll`).

**Definition 3.27.3 (Limit statement with Frobenius).** This is the limit statement of Section 25 for odd $a$, with clause 3 replaced by: for each local bridge at $A$ over $w$, $\sigma \in W_A$ and $n$, $\phi_n(\mathrm{WD}_w(r), \sigma) = \phi_n(x_B, \sigma)$.

Lean: `UpperTheory.Gal.Int.Core.LimU` (also `UpperTheory.Gal.Int.Core.LimOdd`).

**Definition 3.27.4 (Stages).** Let $E$ satisfy the strong field conditions, and let $d > 0$ with $-d$ a square in $E$ and in $\mathbb{Q}_\ell$.

1. The *odd unitary row* holds if for each odd $m$ and automorphic $U$ on $\mathrm{U}(m)$ with weights $\lambda$, some $r$ satisfies the four clauses, with jumps from $\lambda$, at each usable $w$ where $U$ has a Satake parameter.
2. The *unitary row* holds if this is true for all $m \geq 1$ when $E$ also satisfies the inertia condition.
3. The *linear row* holds if, when $E$ also satisfies the inertia condition, every $(\pi, \eta_E^a)$ in scope csd has a row on the usable places.

The *full row* holds if, for every CM field $E$, every $(\pi, \eta_E^a)$ in scope all has a row on all places.

Lean: `UpperTheory.Gal.Int.Core.CoreUd` (also `UpperTheory.Gal.Int.Core.AllUd`, `UpperTheory.Gal.Int.Core.CoreGLu`, `UpperTheory.Gal.Int.Core.RowCsd`).

### From the limit to the linear row

**Lemma 3.27.5 (Frobenius above $\ell$).** The closed Frobenius statement and the limit statement for odd $a$ give the limit statement with Frobenius.

Lean: `UpperTheory.Gal.Int.Core.limU_of_limOdd`.

*Proof.* Clause 3 is the hypothesis of the closed Frobenius statement for $r$, $J$, $C$ and $S(n) = \iota^{-1}\phi_n(x_B, \sigma)$, and its conclusion is the new clause. $\square$

**Lemma 3.27.6 (Odd rank).** The limit statement with Frobenius gives the odd unitary row.

Lean: `UpperTheory.Gal.Int.Core.joinU_holds` (also `UpperTheory.Gal.Int.Core.joinU_of`).

*Proof.* $U$ is automorphic off a finite set $T$ of non-split places. For places $u, v$ above $\ell$ that are apart, the limit statement gives $r_{u,v}$ with the Frobenius clause at usable $w \nmid \ell$. At $w \mid \ell$ apart from $u$ and $v$ the four clauses hold, since equal power sums give equal characteristic polynomials. Let $w_1, w_2, w_3$ above $\ell$ be pairwise apart, and $r = r_{w_2, w_1}$. A place $w \mid \ell$ lies over the same place of $E^+$ as at most one $w_i$, so two of them, $u$ and $v$, are apart from $w$. At almost all places of degree one, which are usable and have density one, $r$ and $r_{u,v}$ have the same Frobenius eigenvalues, so $r \cong r_{u,v}$. $\square$

**Lemma 3.27.7 (All ranks).** Assume the *two-lift statement*: for $E$ as in the strong field conditions without the places above $\ell$, with the inertia condition, each automorphic $U$ on $\mathrm{U}(n)$, $n$ even, has two lifts $U_1, U_2$ to $\mathrm{U}(n + t)$, $n + t$ odd, whose Satake parameters at split places are those of $U$ twisted by a character $\kappa$, with the values of different algebraic characters $\psi_1, \psi_2$. Then the odd unitary row gives the unitary row.

Lean: `UpperTheory.Gal.Int.Core.joinAll_holds` (also `UpperTheory.Gal.Int.Core.joinAll_of`).

*Proof.* We did not open this proof (Remark); by the types of its lemmas it runs as follows. The odd unitary row gives representations for $U_1$ and $U_2$, with the Frobenius eigenvalues of $U$ twisted by $\kappa$ and one extra value. Removing the characters of $\psi_1$, $\psi_2$ and twisting by $\kappa^{-1}$ cuts out a representation for $U$. $\square$

**Lemma 3.27.8 (Descent to $\mathrm{GL}_a$).** Assume the *descent statement*: for each $(\pi, \eta_E^a)$ in scope csd and each finite set $Z$, there are a finite set $T$ of non-split places disjoint from $Z$ and a space $U$ on $\mathrm{U}(a)$, automorphic off $T$, whose local components at split places match those of $\pi$ and whose weights give the infinity type of $\pi$. Then the unitary row gives the linear row.

Lean: `UpperTheory.Gal.Int.Core.joinGL_holds`.

*Proof.* Take $Z = \emptyset$, and let $T$, $U$ and its weights $\lambda$ be as given. The unitary row gives $r$ for $U$. A usable place $w$ is split, so $\pi_w$ matches the component of $U$ at $w$ and the Satake parameters agree. The jumps from $\lambda$ are those of the infinity type of $\pi$, so the clauses for $U$ are the clauses for $\pi$. $\square$

### Base change to all places

**Lemma 3.27.9 (Patching).** Let $S$ be an infinite set of quadratic CM extensions $K/F$ of a number field $F$. For $K \in S$ let $r_K$ be a continuous semisimple representation of $G_K$ of dimension $a$ whose Frobenius eigenvalues at almost all places of degree one come from one fixed system of Satake parameters of $F$. Then there is a continuous semisimple $\rho$ of $G_F$ with $\rho|_{G_K} \cong r_K$ for all but finitely many $K \in S$.

Lean: `UpperTheory.Gal.Int.Core.patchOne_holds` (also `UpperTheory.Gal.Int.Core.isoOne_holds`).

*Proof.* By density, semisimple representations with the same Frobenius eigenvalues at almost all places of degree one are isomorphic. So $r_K$ is isomorphic to its $G_F$-conjugates, and $r_K$, $r_{K'}$ have equal traces on $G_K \cap G_{K'}$. The $G_K$ are kernels of different characters of order two, and a patching lemma for such kernels gives $\rho$ with the trace of $r_K$ on $G_K$ for almost all $K$. $\square$

**Lemma 3.27.10 (Descent along quadratic extensions).** Assume that each $\pi$ has a base change to each quadratic extension that ramifies at a place where $\pi$ has a Satake parameter. Let $\pi$ be cuspidal on $\mathrm{GL}_a(\mathbb{A}_E)$, $a \geq 1$. Suppose that for each place $w_0$ there are infinitely many quadratic CM extensions $K/E$ in which $w_0$ splits, with a ramified place over a place where $\pi$ has a Satake parameter, such that every base change $P$ of $\pi$ to $K$ has a row on a set of places containing almost all places of degree one and all places above $w_0$. Then $\pi$ has a row on all places.

Lean: `UpperTheory.Gal.Int.Core.stepDown_holds` (also `UpperTheory.Gal.Int.Core.stepDown_of`).

*Proof.* For each such $K$, let $r_K$ be the row of a base change $P$. At places of degree one $P$ has the parameters of $\pi$, so patching gives $\rho$. Fix $w$ and a clause. Some $K$ for $w_0 = w$ is outside the exceptional set, so $r_K \cong \rho|_{G_K}$ and the clause holds for $\rho|_{G_K}$ above $w$. As the decomposition group at $w$ is in $G_K$, it holds for $\pi$ and $\rho$ at $w$ (Remark). $\square$

**Theorem 3.27.11 (Base change step).** Assume strong multiplicity one (Jacquet and Shalika), the theorem of Gelfand and Kazhdan on contragredients, and quadratic base change as in the last lemma. Then the linear row gives the full row.

Lean: `UpperTheory.Gal.Int.Core.joinUp_holds` (also `UpperTheory.Gal.Int.Core.joinUp_of'`).

*Proof.* Let $(\pi, \eta_E^a)$ be in scope all. For a place $w_0$, the set $Z(w_0)$ of places that are equal to $w_0$, above $\ell$, or without a Satake parameter for $\pi$ is finite. We apply the descent lemma three times.

*Step 1.* There are infinitely many CM fields $K_1 = E(\sqrt{q})$, $q > 0$ an integer, in which the places of $Z(w_0)$ split and a place outside $Z(w_0)$ ramifies. A base change $P_1$ of $\pi$ to $K_1$ is in scope all with $\eta_{K_1}^a$, by the first two hypotheses. So it is enough that each $P_1$ has a row on all places.

*Step 2.* The same argument over $K_1$ gives $K_2 = K_1(\sqrt{q'})$ and $P_2$ in scope all. In each CM extension of $K_2$, three places above a fixed place of $E$ above $\ell$ are pairwise apart.

*Step 3.* We apply the descent lemma to $P_2$. For a place $w_0$ of $K_2$ and $Z = Z(w_0)$, there are infinitely many quadratic CM extensions $K/K_2$ and $d > 0$ such that $K$ satisfies the strong field conditions without the places above $\ell$ and the inertia condition, the places of $Z$ split in $K$, the non-split places of $K$ are not above $Z$, the places above $Z$ are usable, and some place outside $Z$ ramifies. Then $K$ satisfies the strong field conditions, as places above $\ell$ lie over $Z$ and Step 2 gives three of them pairwise apart. A base change $P$ of $P_2$ is in scope all with $\eta_K^a$, and good, as non-split places lie over places outside $Z$. The linear row gives a row of $P$ on the usable places, which contain the places the descent lemma asks for. $\square$

### The core statement

**Theorem 3.27.12 (Full row).** The two-lift and descent statements and the limit statement with Frobenius give the full row.

Lean: `UpperTheory.Gal.Int.Core.rowCsd_of`.

*Proof.* The lemmas on odd rank, all ranks and descent give the linear row. The published inputs hold, with base change from the strong transfer of Arthur and Clozel. [The base change step](/entry/join-up-holds/) gives the full row. $\square$

**Lemma 3.27.13 (End).** The full row gives the core statement.

Lean: `UpperTheory.Gal.Int.Core.joinEnd_holds` (also `GlobalTheory.RoadW.core_of_rowStarCore`).

*Proof.* A pair in scope csd is in scope all; let $r$ be its row. The first clause holds at almost all places, so $r$ is attached to $\pi$. Another attached $r'$ is isomorphic to $r$ by density, and the clauses pass along the isomorphism. $\square$

**Theorem 3.27.14 (Core from the limit).** The two-lift and descent statements and the limit statement with Frobenius give the core statement.

Lean: `UpperTheory.Gal.Int.Core.core_of_limU`.

*Proof.* Apply [the full row theorem](/entry/row-csd-of/) and Lemma (End). $\square$

**Theorem 3.27.15 (Core from the odd limit).** The two-lift, closed Frobenius and descent statements and the limit statement for odd $a$ give the core statement.

Lean: `UpperTheory.Gal.Int.Core.core_of_limOdd`.

*Proof.* Lemma (Frobenius above $\ell$) gives the limit statement with Frobenius; apply [Theorem 3.27.14](/entry/core-of-lim-u/). $\square$

**Corollary 3.27.16 (Core from the limit corollary).** The two-lift, closed Frobenius and descent statements, with the limit statement in the form of [the limit corollary](/entry/lim-fin-odd-of/), give the core statement.

Lean: `UpperTheory.Gal.Int.Core.toCore` (also `UpperTheory.Gal.Int.Core.limOdd_of_limFinOdd`).

*Proof.* The two forms differ only in writing "$a$ odd" for "$a \geq 1$ and $a$ odd". Apply [Theorem 3.27.15](/entry/core-of-lim-odd/). $\square$

**Theorem 3.27.17 (Core from the theta lift).** The theta lift, closed Frobenius and descent statements and the limit statement for odd $a$ give the core statement.

Lean: `UpperTheory.Gal.Int.Core.toCoreK`.

*Proof.* The theta lift statement gives the two-lift statement (Remark), with $t = 2(d_0 + n) + 1$ for its bound $d_0$. Apply [the corollary](/entry/to-core/). $\square$

**Theorem 3.27.18 (Main line).** If the seed statement, the congruence statement and the theta lift statement hold, then the spherical Galois row (Definition 3.18.2) holds.

Lean: `UpperTheory.Gal.Int.coreAll_of`.

*Proof.* [The limit corollary](/entry/lim-fin-odd-of/) gives the limit statement for odd $a$ from the seed and the congruence. [The closed Frobenius theorem](/entry/cong-phi-holds/) gives the closed Frobenius statement, and the descent statement holds (Remark). So [Theorem 3.27.17](/entry/to-core-k/) gives the core statement. The core statement widens to the spherical Galois row in two moves, with published inputs (Remark): a twist removes $\chi = \eta_E^a$, and base change to CM extensions passes from scope good to scope all and from split places to all places. $\square$

**Remark 3.27.19 (Formalization).** `coreAll_of` is in [Development.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L20), `toCoreK` in [ToCoreK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/ToCoreK.lean#L7), and `joinUp_holds`, `rowCsd_of`, `core_of_limU`, `core_of_limOdd` and `toCore` in [LimOddOfLimFinOdd.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/LimOddOfLimFinOdd.lean#L46), lines 46 to 61. Stages are in [LimOddOfLimWU3.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/LimOddOfLimWU3.lean#L17), step types in [PatchOneAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/PatchOneAlt.lean#L85). We read in full the lemmas of the odd rank, descent, patching and end steps ([JoinEndHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/JoinEndHolds.lean#L19)) and `joinUp_of'` ([BadFinite.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/BadFinite.lean#L46)). We did not open the lemmas behind `joinAll_of`, `stepDown_of` and `joinUp_of'` (for example `subtractQ_of`, `IndexTwoPatch.main`, `threeApart_holds`), nor `TP.twoUpOK_of_k`, `Desc.descOffT`, `inp_holds` and the widening lemmas of `Inp.coreAll_of_core_inp`. Odd points. `LimOdd` restates `LimFinOdd`, and `limOdd_of_limFinOdd` (line 59) only moves `1 ≤ a`. `joinGL_holds` uses `DescOffT` only with $Z = \emptyset$ (JoinEndHolds.lean line 66). `rowCsd_of` writes `jacquetShalikaRigidity` twice. File names do not match contents: `JoinEndHolds.lean` holds `joinU_of` and `stepDown_of`, and `core_of_rowStarCore` is in NormalCodimOneStalkDvr.lean line 35. Two `FieldOK` definitions (IsRegAlgTwistOfHalfIntegral.lean line 25, PolFalseIff.lean line 13) are the same. The widening exists twice, as `GlobalTheory.RoadU.coreAll_of_core` (CoreAllOfCore.lean line 24) and as `Inp.coreAll_of_core_inp`, which the main line uses through a wrapper with the same last name.
