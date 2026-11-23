---
title: Plans
decls:
  - UpperTheory.Gal.Int.Geo.Pl.exists_unitaryGroupDatum_of_vector_exponent_spectral
  - UpperTheory.Gal.Int.Geo.Pl.planEx_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Plans

The proof of Theorem 3.7.3 used three inputs, and the third was the existence of plans. A plan is the group-theoretic input of a Hecke tower: moduli data at an auxiliary prime $p$, a level, a Hecke eigensystem, a Hecke character that removes the central character, and a test function that detects the eigensystem. The six facts of Theorem 3.12.7 turn a plan into a pack. This section defines plans and proves that they exist, from the data and frames of Section 14, the vectors of Section 14 and the test functions of Section 15. The result, Theorem 3.16.6, is the input of [Theorem 3.7.3](/entry/geometric-realization-of-weight-one/).

We keep the setting of Definition 3.7.1: $E$ is a CM field, $\ell$ a prime, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $a$ odd, $d > 0$ and $x \in E$ with $x^2 = -d$, and $U$ a space of automorphic forms on $\mathrm{U}(a)$. For a finite place $w$ and a multiset $B$ of Satake parameters, $\operatorname{sat}_a(B)$ is as in Section 07, and for coefficients $\vartheta = (\vartheta_i)$, $P_{N(w), a, \vartheta}$ is the Hecke polynomial of Section 06. Two places $w, w'$ are *linked through* $x$ if they induce the same place of $\mathbb{Q}(x)$, and *apart* if they lie over different places of $E^+$.

### Plans

**Definition 3.16.1 (plan).** A *plan* for $U$ consists of:

1. a prime $p$, moduli data $D$ at $p$ with group $G$ in the standard range of Section 12, with $D$ of rank $a$, and an isomorphism $e : F \cong E$ from the field of $D$;
2. a level $N$, Hecke elements $g_j$ at level $N$ for $j$ in a set $J$, and numbers $\theta_j \in \overline{\mathbb{Q}}_\ell$;
3. an algebraic Hecke character $\kappa$ of $E$ with infinity type $m$;
4. a weight $\lambda$ with each $\lambda_\tau$ non-increasing;
5. an integral Hecke function $f$ at level $N$ such that $\iota \circ \theta$ is an eigensystem of weight $\lambda$ detected by $f$;
6. a finite set $X$ of places such that every usable place $w \notin X$ with $w \nmid \ell$ satisfies the *congruence condition* for each multiset $B$ of Satake parameters of $U$ at $w$: $\kappa$ is unramified at $w$, and there are a prime $\mathfrak{w}$ of $F$ that corresponds to $w$ under $e$ and coefficients $\vartheta = (\vartheta_i)$ such that $(g, \theta)$ satisfies the group conditions for a congruence relation at $\mathfrak{w}$ with coefficients $\vartheta$, $\vartheta_0 \neq 0$, and
$$\iota\, P_{N(w), a, \vartheta} = \iota(\vartheta_0) \prod_{\beta \in \operatorname{sat}_a(B)} \bigl(X - \beta\, \kappa(w)^{-1}\bigr).$$

Lean: `UpperTheory.Gal.Int.Geo.Plan` (also `UpperTheory.Gal.Int.Geo.CongP`).

The group conditions for a congruence relation are those of item 5 of Theorem 3.12.7: the deck elements of the level group at $\mathfrak{w}$ have eigenvalue $1$, and for each $i \le a$ some $g_j$ is a Hecke element of type $i$ at $\mathfrak{w}$, with the index of the double coset equal to the number of points of the Grassmannian $\mathrm{Gr}_i$ over the residue field and $\theta_j$ equal to this index times $\vartheta_i$.

**Definition 3.16.2 (Hodge-Tate and congruent plans).** A plan is *Hodge-Tate at* a place $v$ if:

1. $\kappa$ is unramified at $v$;
2. $(g, \theta)$ satisfies the group conditions for good reduction (Definition 3.13.7) at a prime $\mathfrak{w}$ of $F$ that corresponds to $v$ under $e$;
3. for each embedding $\tau : E \to \mathbb{C}$ inducing $v$ there is $\sigma \in \operatorname{Aut}(\mathbb{C})$ with $\sigma \circ \tau \circ e = t_i$ for every embedding $t_i$ of $D$, such that for each weight $\lambda_U$ of $U$ at $\tau$ and each jump $j$ of $\lambda_U$ there are an index $i_0$, a list $h$ of Hodge degrees for $\sigma\lambda$ at $t_{i_0}$, and an index $i$ with $h_i = j + m(\tau)$.

A plan is *congruent at* $w$ if the congruence condition holds at $w$ for every multiset $B$ of Satake parameters of $U$ at $w$.

Lean: `UpperTheory.Gal.Int.Geo.Plan.HTFor` (also `UpperTheory.Gal.Int.Geo.Plan.ExpAt`, `UpperTheory.Gal.Int.Geo.Plan.CongAll`).

A pack made from a plan that is Hodge-Tate at $v$ is Hodge-Tate at $v$ in the sense of Section 07, and one made from a plan congruent at $w$ has a congruence model at $w$, by items 4, 5 and 6 of Theorem 3.12.7.

**Definition 3.16.3 (existence of plans).** *Plans exist* if, for all data and all $U$ as in Definition 3.7.1:

1. there is a plan that is Hodge-Tate at $v'$;
2. for each usable place $w \nmid \ell$ at which $U$ has Satake parameters, there is a plan that is Hodge-Tate at $v'$ and congruent at $w$;
3. for each place $w \mid \ell$ linked to $v'$ through $x$, apart from $w_0$ and from $v'$, at which $U$ has Satake parameters, there are a plan that is Hodge-Tate at $v'$ and at $w$, and a plan that is Hodge-Tate at $v'$ and congruent at $w$.

Lean: `UpperTheory.Gal.Int.Geo.PlanEx`.

### The three inputs

The vectors of Section 14 and the test functions of Section 15 are two of the inputs. The third says that the weight of a vector matches the weights of $U$.

**Definition 3.16.4 (exponent condition).** The *exponent condition* holds if, for every setup $S$ for $(A, n, p)$ with $\omega$ and $x$ generating the same field, and every vector $V$ for $(x, U, w_0, \mathrm{Up})$ with weight $\lambda$ and Hecke character of infinity type $m$, each $\lambda_\tau$ is non-increasing, and for each $\tau : E \to \mathbb{C}$ there is $\sigma \in \operatorname{Aut}(\mathbb{C})$ with $\sigma \circ \tau = \tau_0$ such that every jump $j$ of every weight of $U$ at $\tau$ is $h_i - m(\tau)$ for some list $h$ of Hodge degrees for $\sigma\lambda$ at $\tau_0$ and some $i$.

Lean: `UpperTheory.Gal.Int.Geo.Pl.ExpOf`.

**Theorem 3.16.5 (plans from vectors, exponents and test functions).** Suppose that vectors exist in the sense of Theorem 3.14.9, that the exponent condition holds, and that spectral test functions exist in the sense of Theorem 3.15.7. Then plans exist.

Lean: `UpperTheory.Gal.Int.Geo.Pl.exists_unitaryGroupDatum_of_vector_exponent_spectral`.

*Proof.* Fix the data and $U$. The main step is the following claim. Let $H$ and $C$ be disjoint finite sets of places such that every $w \in H \cup C$ is usable, apart from $w_0$, and has Satake parameters for $U$; $w$ is linked to $w_0$ through $x$ when $w \mid \ell$; and two places of $H \cup C$ over the same prime are linked through $x$. Then there is a plan that is Hodge-Tate at every $v \in H$ and congruent at every $w \in C$.

To prove the claim, write $q_w$ for the prime under $w$. Each $q_w$ and $\ell$ have $-d$ as a square, so [Theorem 3.14.4](/entry/dat-ex-holds/) with $Q = \{\ell\} \cup \{q_w\}$ gives an arithmetic datum $A$ with $\mathbb{Q}(\omega) = \mathbb{Q}(x)$ at which all these primes are good, and an $e_0 > 0$ outside whose prime factors every prime with $-d$ a square is good.

Let $\mathrm{Up}$ be the set of places $u$ such that $c(u)$ is linked through $x$ to no place of $H \cup C$. Since $\ell$ and the $q_w$ split in $\mathbb{Q}(x)$, a split place $u$ and $c(u)$ induce different places of $\mathbb{Q}(x)$; with the linking hypothesis this shows that $\mathrm{Up}$ contains $u$ or $c(u)$ for every split $u$, and contains $w_0$. The vectors give a vector $V$ for $(x, U, w_0, \mathrm{Up})$. Each $w \in H \cup C$ is split and apart from $w_0$ with Satake parameters, so by item 6 of Definition 3.14.7 it lies outside $S_V$ with $c(w)$, and by the choice of $\mathrm{Up}$ it is free in the sense of Definition 3.15.4.

Choose $g_0$ with $\Phi(g_0) \neq 0$; it is integral at almost all places. Item 4 of Theorem 3.14.4 gives a prime $p$ outside the primes under $H \cup C$, $S_V$ and the places where $g_0$ is not integral, with a setup $S$ in the standard range. Then $S_V$ is prime to $p$ and $\Phi(g_0) \neq 0$ with $g_0$ integral over $p$. [Theorem 3.14.6](/entry/frame-ex-holds/) gives a frame $F$. The spectral test functions, applied with the good prime $\ell$ under $w_0$ and the finite set $\{q_w\}$, give a prime $r_0 \neq p$ outside this set.

We take as given a site lemma: there are a level $N$ with $r_0 \mid N$ whose group consists of stable elements and pairwise compatible sites $\sigma_w$ of $N$ at each $w \in H \cup C$, over $q_w$, whose level groups consist of stable elements. Let $J$ be the set of seen pairs $(g, \theta)$ such that $g$ is a deck element or a Hecke element of type $i$ at a site, compatible with all $\sigma_w$, at a place outside $H$. The spectral test functions give an integral $f$ at level $N$ such that $\theta$ is detected by $f$. The plan has $p$, the data of $S$, $e = \mathrm{id}$, $N$, $J$, $\theta$, the character $\kappa$ of $V$ with its infinity type $m$, the weight $\lambda$ of $V$, and $f$. The exponent condition gives item 4.

For $v \in H$, $\kappa$ is unramified at $v$ since $v$ is free. Every $k$ in the level group of $\sigma_v$ is stable and lies in $K_{r_0}$, since $q_v \neq r_0$, so it is a seen deck element with $\theta = 1$. The other members of $J$ are deck elements or of type $i$ at places different from $v$, and from this a lemma that we take as given gives the group conditions for good reduction at $v$. The exponent condition gives item 3 of Definition 3.16.2, with $i_0 = 0$.

For $w \in C$ and Satake parameters $B$, put $\vartheta_i = \iota^{-1}(\mathrm{sat}_i(N(w), B)\, \kappa(w)^{-i})$. For each $i \le a$ a Hecke element of type $i$ at $\sigma_w$ exists, and it is seen with $\theta = [K_N : K_N \cap hK_Nh^{-1}]\, \vartheta_i$. A lemma that we take as given turns this into the group conditions for a congruence relation at $w$. The polynomial identity of Definition 3.16.1 follows from the expression of the Hecke polynomial through the eigenvalues $\mathrm{sat}_i$, together with the fact that $B$ has $a$ elements; we take both as given.

For item 6 of Definition 3.16.1, let $X$ be the set of places over the prime factors of $N e_0 p$ and over the primes under $S_V$. A usable $w \notin X$ with $w \nmid \ell$ lies over a good prime $q_w \nmid N$, there is a trivial site of $N$ at $w$ whose level group is that of $N$, and the argument for $C$ applies to it.

The three clauses of Definition 3.16.3 follow from the claim with $(H, C) = (\{v'\}, \emptyset)$, $(\{v'\}, \{w\})$, $(\{v', w\}, \emptyset)$ and $(\{v'\}, \{w\})$. The hypotheses of the claim hold: a place over $\ell$ is split and usable, since the non-split places are prime to $\ell$ and $-d$ is a square in $\mathbb{Q}_\ell$; $v'$ is apart from $w_0$ and linked to it; in clause 2, $w$ is not over $\ell$, so $w$ and $v'$ lie over different primes, and $w$ is apart from $w_0$; in clause 3, $w$ is linked to $v'$ and so to $w_0$. $\square$

**Theorem 3.16.6 (plans exist).** Plans exist.

Lean: `UpperTheory.Gal.Int.Geo.Pl.planEx_holds`.

*Proof.* This is Theorem 3.16.5 applied to [Theorem 3.14.9](/entry/vec-ex-holds/), the exponent condition and [Theorem 3.15.7](/entry/spec-top-holds/). $\square$

**Remark 3.16.7 (Formalization).** `exists_unitaryGroupDatum_of_vector_exponent_spectral` builds the structure `All` from its three inputs and twelve proved facts (`frameEx_holds`, `sides_holds`, `levBasic_holds`, `memEx_holds`, `siteTriv_holds`, `siteEx_holds`, `goodOf_holds`, `congOf_holds`, `datEx_holds`, `CertificateRingHomMap.rootsAlg_holds`, `satCard`, `intCof_holds`) and applies `planEx_of`, which applies the lemma `master` four times; the claim in the proof is `master`. We read `master` and `planEx_of` and the statements `SiteEx`, `GoodOf`, `CongOf` and `DatEx`, but not the proofs of the twelve facts, so the site lemma, the two group lemmas and the root identity are taken as given. Its name speaks of a unitary group datum, but it concludes `PlanEx`. `planEx_of` discards two hypotheses of `PlanEx` with `_`: `NonSplitSet T` and `SphOffU w₀ S U`; of `AutOffT T U` it uses only the automorphy `hU.1`, so the set $T$ and the Satake hypothesis away from $S$ play no part, and the Satake parameters at the places of $H \cup C$ are asked for directly. The exponent condition is proved by `expOf_holds`, which we did not open, and `planEx_holds` is `exists_unitaryGroupDatum_of_vector_exponent_spectral vecEx_holds expOf_holds specTop_holds`.
