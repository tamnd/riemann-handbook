---
title: Limits of Frobenius traces
decls:
  - UpperTheory.Gal.Lim.limWU4_of
  - UpperTheory.Gal.Lim.limFinOdd_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Limits of Frobenius traces

The seed statement of Section 24 gives Galois representations only for spaces $U'$ with extra local conditions. A congruence statement approximates the Hecke eigenvalues of a general $U$ by those of such $U'$. This section makes, for each $U$, a Galois representation $r$ as a limit of the representations of the $U'$, with the Frobenius clause prime to $\ell$ and the crystalline and power sum clauses above $\ell$. The results are [Theorem 3.26.10](/entry/lim-wu4-of/) and its case for odd rank, [Corollary 3.26.11](/entry/lim-fin-odd-of/), an input of [the main line](/entry/core-all-of/).

We keep the notation of Section 24. The integer $d > 0$ satisfies the *field conditions*: $-d$ is a square in $E$ and in $\mathbb{Q}_\ell$, $[E^+ : \mathbb{Q}]$ is even, and every non-split place is prime to $\ell$ and unramified over $E^+$. Two places are *apart* if they lie over different places of $E^+$. For a finite set $T$ of non-split places, a space $U$ on $\mathrm{U}(a)$ is *automorphic off $T$* if it is automorphic and unramified at the non-split places outside $T$. Local components at split places are unique, so a Satake parameter is unique if it exists.

### Polynomial approximation and Hecke operators

**Definition 3.26.1 (Polynomial approximation).** Let $k$ be a field with an ultrametric norm, $J$ a set, $\theta \in k^J$ and $S \subset k^J$. Then $\theta$ is *polynomially approximated* by $S$ if for each $\varepsilon > 0$ there are a finite $s \subset S$ and $c_\eta \in k$ with $\lVert P(\theta) - \sum_{\eta \in s} c_\eta P(\eta) \rVert \leq \varepsilon$ for every $P \in \mathbb{Z}[X_j : j \in J]$.

Lean: `GlobalTheory.Cong.PolyApprox` (also `GlobalTheory.Cong.trc`, `GlobalTheory.Cong.LinApprox`).

Trace approximation (Section 23) is the case of degree one for the families $(\mathrm{tr}\, \rho(g))_g$.

**Definition 3.26.2 (Local operators and eigen-systems).** A *level* $K$ is a family of subgroups $K_w \subset \mathrm{GL}_a(E_w)$, $w$ split. A *family of local operators* for $K$, indexed by $J$, gives for each $j$ a split place $w_j$ prime to $\ell$, a function $f_j$ of finite support on $\mathrm{GL}_a(E_{w_j})$ with $\lVert \iota^{-1} f_j \rVert \leq 1$, and numbers $z_j(\sigma)$ such that $f_j$ acts on the $K_{w_j}$-fixed vectors of each smooth irreducible $\sigma$ by $z_j(\sigma)$. The *eigen-system* of $U$ is the family $\theta$ with $\theta_j = \iota^{-1} z_j(\sigma)$ for the local component $\sigma$ of $U$ at $w_j$. The *Satake power sum* $p_n(U, w)$, for $n \in \mathbb{Z}$, is $\sum_{b \in \mathrm{sat}_a(B)} b^n$ if $U$ has a Satake parameter $B$ at $w$, and $0$ if not.

Lean: `GlobalTheory.Cong.LocOps` (also `GlobalTheory.CongL.IsSysU`, `GlobalTheory.CongL.PowSatU`).

$U$ *has level $K$ off $w_0$ and $v'$* if each local component of $U$ at a split place apart from $w_0$ and $v'$ has a nonzero $K_w$-fixed vector.

### The congruence statement and the limit statement

The seed statement of Section 24 is the case of a statement with four parameters, a condition $\mathrm{Rk}$ on $a$, a type $\mathrm{Ty}$ at $w_0$, a genericity $\mathrm{Gen}$ and a weight relation $\mathrm{Wt}$, where $a$ is odd, the type is that of Definition 3.7.1, and the weight is lacunary.

**Definition 3.26.3 (Congruence statement).** The *congruence statement* for $\mathrm{Rk}, \mathrm{Ty}, \mathrm{Gen}, \mathrm{Wt}$ says the following. Let $a \geq 1$ with $\mathrm{Rk}(a)$, let $U$ be automorphic off a finite set $T$ of non-split places, and let $w_0, v'$ be split places above $\ell$ that are apart. Then there is a level $K$ such that:

1. $U$ has level $K$ off $w_0$ and $v'$, and $K_w$ is open and compact at each split $w$ apart from $w_0$;
2. $K_w = \mathrm{GL}_a(\mathcal{O}_w)$ at each split $w$ apart from $w_0$ and $v'$ where $U$ has a Satake parameter;
3. for finite sets $Z$ and $W$ of split places apart from $w_0$ and $v'$ where $U$ has Satake parameters, with $W$ above $\ell$, there are constants $c(w, n) \neq 0$ such that for each family of local operators for $K$, with $\theta$ the eigen-system of $U$, the family $\big(\theta, (\iota^{-1}(c(w, n)\, p_n(U, w)))_{(w, n) \in W \times \mathbb{Z}}\big)$ is polynomially approximated by the same families for the $U'$ that are automorphic off $T$, have level $K$ off $w_0$ and $v'$, have a Satake parameter at $v'$, have the weights of $U$ at the embeddings over places apart from $w_0, v'$, satisfy $\mathrm{Wt}$, have type $\mathrm{Ty}$ at $w_0$ and are generic at $Z \cup W$;
4. if all values of the $f_j$ are rational, all $\theta_j$ lie in one finite extension of $\mathbb{Q}_\ell$.

Lean: `GlobalTheory.CongL.CongUW4` (also `GlobalTheory.CongL.CongFinOdd`).

**Definition 3.26.4 (Limit statement).** The *limit statement* for $\mathrm{Rk}$ says: for $a, T, U, w_0, v'$ as in the congruence statement and $d$ with the field conditions, there is a continuous semisimple $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ such that:

1. at each usable $w \nmid \ell$ with Satake parameter $B$, $r$ is trivial on inertia and $\iota$ of the characteristic polynomial of $r(s^{-1})$ is $P_B$ for each Frobenius $s$ at $w$;
2. at each $w \mid \ell$ apart from $w_0$ and $v'$ where $U$ has a Satake parameter, $r$ is crystalline and de Rham with the Hodge-Tate jumps given by the weights of $U$;
3. at each such $w$ with parameter $B$, each local bridge at $A$ over $w$ and each $\sigma \in W_A$, there are a jump function $J$ and a set $C$ of continuous representations, crystalline at $w$ with jumps $J$, such that $C$ approximates $r$ jointly with $(\rho, n) \mapsto \iota^{-1} \phi_n(\mathrm{WD}_w(\rho), \sigma)$ to $n \mapsto \iota^{-1} \phi_n(x_B, \sigma)$.

Here $x_B$ is the unramified Weil-Deligne representation attached to $B$, with $\phi_n(x_B, \sigma) = \sum_{b \in \mathrm{sat}_a(B)} b^{-\deg(\sigma) n}$, where $\deg(\sigma)$ is the degree of $\sigma$ in the Weil group.

Lean: `GlobalTheory.CongL.LimWU4` (also `GlobalTheory.CongL.LimFinOdd`).

Clause 3 is the hypothesis of [the closed Frobenius theorem](/entry/cong-phi-holds/), which turns it into $\phi_n(\mathrm{WD}_w(r), \sigma) = \phi_n(x_B, \sigma)$.

### Lemmas on limits

**Lemma 3.26.5 (Trace limit).** Let $\Gamma$ be a topological group, $x : J \to \Gamma$, and $\theta \in L^J$ for a finite extension $L$ of $\mathbb{Q}_\ell$. For $i \in I$ let $\rho_i$ be continuous of dimension $a$, $\eta_i \in \overline{\mathbb{Q}}_\ell^J$ and $D_i \subset J$ with $\eta_i(j) = \mathrm{tr}\, \rho_i(x_j)$ on $D_i$. Assume that $x(\bigcap_{i \in s} D_i)$ is dense for each finite $s \subset I$, and that $\theta$ is polynomially approximated by $\{\eta_i\}$. Then there is $t : \Gamma \to L$ such that:

1. if $\lVert P(\theta) - \sum_{i \in F} c_i P(\eta_i) \rVert \leq \varepsilon$ for all $P$, then $\lVert t(g) - \sum_{i \in F} c_i\, \mathrm{tr}\, \rho_i(g) \rVert \leq \varepsilon$ for all $g$;
2. if $\theta$ is polynomially approximated by $\{\eta_i : i \in A\}$, then $t$ is polynomially approximated by $\{\mathrm{tr}\, \rho_i : i \in A\}$, and $t(x_j) = \theta_j$ for each $j \in \bigcap_{i \in A} D_i$.

Lean: `UpperTheory.Gal.Lim.exists_trace_limit`.

Here $t(g)$ is the limit of $\theta_j$ as $x_j \to g$ with $j$ in finite intersections of the $D_i$; it is a Cauchy limit in the complete field $L$.

**Lemma 3.26.6 (Limit representation).** Let $\Gamma$ be compact and $C$ a set of continuous representations of dimension $a$. If $t : \Gamma \to L$ is polynomially approximated by $\{\mathrm{tr}\, \rho : \rho \in C\}$, then $t = \mathrm{tr}\, r$ for a continuous semisimple $r$, and $r$ is trace approximated by each $C' \subset C$ whose traces polynomially approximate $t$.

Lean: `GlobalTheory.Cong.exists_limit_rep` (also `GlobalTheory.Cong.linApprox_of_polyApprox_trc`).

Here $t$ is a continuous pseudo-character, hence a trace.

**Lemma 3.26.7 (Joint limit).** Let $\rho_i, \eta_i$ be as above, $\eta'_i \in k^{J'}$, and let $t = \mathrm{tr}\, r$ satisfy clause 1 of the trace limit lemma. Let $A \subset I$ and $\theta' \in k^{J'}$ with $(\theta, \theta')$ polynomially approximated by $\{(\eta_i, \eta'_i) : i \in A\}$. Let $p : \mathbb{N} \to J'$, $u : \mathbb{N} \to k$, $S(n) = u_n \theta'(p_n)$, and $s(\rho_i, n) = u_n \eta'_i(p_n)$ for $i \in A$. Then $\{\rho_i : i \in A\}$ approximates $r$ jointly with $s$ to $S$.

Lean: `UpperTheory.Gal.Lim.joint` (also `UpperTheory.Gal.Lim.approx_left`).

*Proof.* Fix $n$ and $\varepsilon$. Let $M = 1 + \sum_{j \leq n} \lVert u_j \rVert$, and take $F \subset A$ and $c_i$ that approximate $(\theta, \theta')$ within $\varepsilon / M$. For polynomials in the variables of $J$, clause 1 gives the trace bound $\varepsilon / M \leq \varepsilon$. For $j \leq n$, the polynomial $X_{p_j}$ gives $\lVert S(j) - \sum c_i\, s(\rho_i, j) \rVert \leq \lVert u_j \rVert \varepsilon / M \leq \varepsilon$. Equal $\rho_i$ are joined by adding their coefficients. $\square$

**Lemma 3.26.8 (Inertia and crystalline limits).** Let $r$ be semisimple and trace approximated by $C$.

1. If $s$ is in the kernel of each $\rho \in C$, then $r(s) = 1$.
2. Let $w \mid \ell$ and $r$ continuous. If each $\rho \in C$ is continuous, crystalline and de Rham at $w$ with the jumps of a space $U'$ that has the weights of $U$ over $w$, then so is $r$, with the jumps of $U$.

Lean: `GlobalTheory.Cong.ker_of_linApprox` (also `GlobalTheory.CongL.crysDRU_of_linApprox`).

**Lemma 3.26.9 (Frobenius operators).** Let $K$ be a level and $W_0$ a set of split places prime to $\ell$ with $K_w = \mathrm{GL}_a(\mathcal{O}_w)$ on $W_0$. There are local operators for $K$ indexed by $J$, Frobenius elements $\mathrm{fr}_j$ at $w_j \in W_0$, $n_j \geq 1$ and $x_j = \mathrm{fr}_j^{-n_j}$, such that:

1. each Frobenius $s$ at each $w \in W_0$ is $\mathrm{fr}_j$ for some $j$ with $w_j = w$ and $n_j = 1$;
2. all values of the $f_j$ are rational;
3. if $\sigma$ at $w_j$ is spherical with parameter $B$ and $\iota$ of the characteristic polynomial of $\rho(\mathrm{fr}_j^{-1})$ is $P_B$, then $\iota^{-1} z_j(\sigma) = \mathrm{tr}\, \rho(x_j)$;
4. if $\sigma$ at $w \in W_0$ is spherical with parameter $B$ and $\mathrm{tr}\, r(x_j) = \iota^{-1} z_j(\sigma)$ for all $j$ with $w_j = w$, then $\iota$ of the characteristic polynomial of $r(s^{-1})$ is $P_B$ for each Frobenius $s$ at $w$.

Lean: `GlobalTheory.FrobOpsIdx.frobOpsIdx` (also `GlobalTheory.Cong.SphOps`, `GlobalTheory.Cong.SphOpsProof.sphOps`).

Here $f_j$ is the spherical Hecke operator acting on an unramified $\sigma$ with parameter $B$ by $\sum_{b \in \mathrm{sat}_a(B)} b^{n_j}$, and power sums fix characteristic polynomials.

### The limit theorem

**Theorem 3.26.10 (Limit).** For all $\mathrm{Rk}, \mathrm{Ty}, \mathrm{Gen}, \mathrm{Wt}$, the seed statement and the congruence statement for them give the limit statement for $\mathrm{Rk}$.

Lean: `UpperTheory.Gal.Lim.limWU4_of`.

*Proof.* Fix the data, and let $K$ be the level from the congruence statement. Places above $\ell$ are split by the field conditions.

*Step 1.* The split places where $U$ has no Satake parameter form a finite set $S$, and a split place has a parameter if and only if it is apart from $S$, since parameters pass to the conjugate place.

*Step 2.* Let $W_0$ be the set of split places prime to $\ell$ with a parameter for $U$. On $W_0$, $K_w = \mathrm{GL}_a(\mathcal{O}_w)$, and the Frobenius lemma gives $J$, $\mathrm{fr}_j$ and $x_j$. Let $\theta$ be the eigen-system of $U$.

*Step 3.* If $U'$ is automorphic, of level $K$ off $w_0$ and $v'$, with a parameter at $v'$, then $U'$ has parameters at all split $w$ apart from $w_0$ and $S$: by conjugation from $v'$, or from a $\mathrm{GL}_a(\mathcal{O}_w)$-fixed vector. This is the hypothesis of the seed statement on parameters.

*Step 4.* For each finite $Y$, the seed statement gives $Z_0(Y)$ and representations $r_{Y, U'}$. Let $Z(Y) = Z_0(Y) \cup (Y \cap W_0)$, and $W(Y)$ the places of $Y$ above $\ell$, apart from $w_0, v'$, with a parameter for $U$. Clause 3 of the congruence for $Z(Y), W(Y)$ gives constants $c_Y$. Let $I$ be the set of triples $i = (Y, U', \theta')$ with $U'$ as in that clause and $\theta'$ its eigen-system; put $\rho_i = r_{Y, U'}$ and $\eta_i = \theta'$. For each $Y$, $\big(\theta, \iota^{-1} c_Y\, p_n(U, w)\big)$ is polynomially approximated by the families of the $i$ with first entry $Y$. Clause 4 of the congruence puts all $\theta_j$ in one finite $L$.

*Step 5.* Let $D_i$ be the set of $j$ with $\eta_i(j) = \mathrm{tr}\, \rho_i(x_j)$, and fix a finite $s \subset I$. The seed statement gives each $\rho_i$ an open dense $V_i$ and a finite $X_i$. The Frobenius elements in $\bigcap_{i \in s} V_i$ at usable places prime to $\ell$ and apart from $S \cup \bigcup_{i \in s} X_i$ are dense. Their inverses are $x_j$ with $n_j = 1$, and clause 1 of the seed statement with clause 3 of the Frobenius lemma puts these $j$ in each $D_i$.

*Step 6.* The trace limit lemma for $Y = \emptyset$ gives $t$, and the limit representation lemma gives $r$ with $\mathrm{tr}\, r = t$, trace approximated for each $Y$ by the $\rho_i$ with first entry $Y$.

*Step 7: clause 1.* Let $w \nmid \ell$ be usable with parameter $B$, and $Y = \{w\}$. As $w \in Z(Y)$, each $U'$ there is generic at $w$, and the seed statement gives the Frobenius clause for each $\rho_i$, so $r$ is trivial on inertia by the inertia lemma. For $j$ with $w_j = w$, clause 3 of the Frobenius lemma puts $j$ in each $D_i$, so $t(x_j) = \theta_j = \iota^{-1} z_j(\sigma)$ for the component $\sigma$ of $U$ at $w$. Clause 4 of that lemma gives the characteristic polynomials of $r$.

*Step 8: clause 2.* Let $w \mid \ell$ be apart from $w_0$ and $v'$ with a parameter, and $Y = \{w\}$. By the seed statement each $\rho_i$ is crystalline and de Rham at $w$ with the jumps of its $U'$, and part 2 of the inertia lemma applies.

*Step 9: clause 3.* Let $w$ be as in step 8 with parameter $B$, $Y = \{w\}$, so $w \in W(Y)$. Let $J$ be the jumps of the weights of $U$ and $C$ the set of $\rho_i$ with first entry $\{w\}$, crystalline with jumps $J$ by step 8. Put $m_n = -\deg(\sigma)\, n$ and $u_n = \iota^{-1}(c_Y(w, m_n))^{-1}$. Then $\phi_n(x_B, \sigma) = p_{m_n}(U, w)$, so $\iota^{-1}\phi_n(x_B, \sigma) = u_n \cdot \iota^{-1}(c_Y(w, m_n)\, p_{m_n}(U, w))$. As $U'$ is generic at $w$, the seed statement gives the same identity for $\mathrm{WD}_w(\rho_i)$ and $U'$. The joint limit lemma, with $p_n = (w, m_n)$, gives clause 3. $\square$

**Corollary 3.26.11 (Limit for odd rank).** If the seed statement and the congruence statement hold for the parameters of Section 24, then the limit statement holds for odd $a$.

Lean: `UpperTheory.Gal.Lim.limFinOdd_of`.

*Proof.* This is the theorem for these parameters. With [the seed theorem](/entry/seed-fin-odd-of-geo-one/) and [Theorem 3.33.5](/entry/cong-fin-odd-of-ex/), both hypotheses hold. $\square$

**Remark 3.26.12 (Formalization).** The two theorems are in [LimFinOddOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TraceLimits/LimFinOddOf.lean#L16), lines 16 and 197. `SeedWU4`, `CongUW4`, `LimWU4`, `SeedFinOdd`, `CongFinOdd` and `LimFinOdd` are in [LimWU4OfLimWU3.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/LimWU4OfLimWU3.lean#L15). `PolyApprox` is in [PolyApproxZeroPadic.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/PolyApproxZeroPadic.lean#L10) and `LocOps` in [HasLevel.lean](lean:Development/AbelianVarietyTheory/Statements/EllipticCurveLevels/HasLevel.lean#L36). We read `limWU4_of` in full, and `joint`, `approx_left`, `phiSum_satWD` and `powSatU_eq` in [SlopeTestRemainingChoices.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TraceLimits/SlopeTestRemainingChoices.lean#L50). We read the outlines of `exists_trace_limit`, `exists_limit_rep`, `frobOpsIdx` and `crysDRU_of_linApprox`, and only the statements of `ker_of_linApprox`, `linApprox_of_polyApprox_trc`, `finite_not_sph`, `dense_frob_usable_off`, `sphOps`, `exists_comp_and_unique`, `exists_satU_of_under_eq`, `sameWtAt_of_off` and `z_eq_of_equiv`; we did not open the pseudo-character lemmas inside `exists_limit_rep`. Some odd points. The proof of `limWU4_of` uses $\mathrm{Rk}(a)$ only to pass it on, drops the clause of `CongUW4` that the $K_w$ are open and compact (line 22), applies `exists_limit_rep`, which is stated for a dense family $x$, with $x = \mathrm{id}$ (line 125), and takes $L$ from the congruence for $Z = W = \emptyset$ (line 90). Of the triples in $I$, only those with $Y = \emptyset$ or $Y = \{w\}$ are used.
