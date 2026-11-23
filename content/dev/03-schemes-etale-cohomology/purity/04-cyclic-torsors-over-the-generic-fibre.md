---
title: Cyclic torsors over the generic fibre
decls:
  - GlobalTheory.LocAcyc.torsor_trivial
  - GlobalTheory.T.torsor_trivial_strict_henselisation_origin
  - GlobalTheory.KeyOriginCut.keyOrigin
  - GlobalTheory.T.torsor_point_over_strictHenselisation_noetherianNormal
  - GlobalTheory.KeyOriginNoeth.torsor_point_of_essFiniteType
  - GlobalTheory.T.strictHenselisation_enlarge_good_at_origin
  - GlobalTheory.KeyOriginEnlarge.enlarge_good
  - GlobalTheory.T.etale_enlarge_by_uniformiser_roots
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cyclic torsors over the generic fibre

Let $T$ be a local domain with fraction field $K$, and let $O$ be a strict henselisation of the polynomial ring $T[x]$ at a prime. This section proves that every $\mathbb{Z}/q$-torsor over $O \otimes_T K$ has a section, when $q$ is a unit in $T$ and $T$ is absolutely integrally closed. In the language of [étale cohomology](/learn/geometry/#tale-cohomology), the first cohomology of the generic fibre of the strict henselisation with coefficients $\mathbb{Z}/q$ vanishes. This is the degree one case of the local acyclicity of the affine line over $T$, a statement of the kind that Artin proves for smooth morphisms in SGA 4, Exposé XV. The next section uses it to bound the Picard group and $H^1$ of the generic fibre.

**Definition 2.4.1 (Generic fibre).** Let $T$ be a domain and $O$ a $T$-algebra. The *generic fibre* $O_K$ of $O$ is the localization of $O$ at the image of $T \setminus \{0\}$. It is $O \otimes_T K$.

**Definition 2.4.2 (Cyclic torsor).** Let $B$ be a ring and $q \geq 1$. A $\mathbb{Z}/q$-*torsor* over $B$ is a $B$-algebra $D$ that is finite, projective and [[faithfully flat|C31PYYPRGC]] as a $B$-module, with an action $g \mapsto \sigma_g$ of $\mathbb{Z}/q$ by $B$-algebra automorphisms, such that the map
$$
D \otimes_B D \to \prod_{g \in \mathbb{Z}/q} D, \qquad a \otimes b \mapsto (a\, \sigma_g(b))_g,
$$
is bijective. A *section* of $D$ is a $B$-algebra map $D \to B$. We say that $\mathbb{Z}/q$-torsors over $B$ are *trivial* if every $\mathbb{Z}/q$-torsor over $B$ has a section.

This is the affine form of a principal homogeneous space under the constant group $\mathbb{Z}/q$; see Milne, *Étale Cohomology*, Chapter III, §4.

**Definition 2.4.3 (Strict henselisation).** A ring map $\varphi : R \to O$ is a *strict henselisation* if $O$ is a henselian local ring, the residue field of $O$ is [[separably closed|8B57B7EGK4]], $\varphi$ is a local map of local rings, and $\varphi$ is ind-étale: it lies in the closure of the class of étale maps under filtered colimits. For $R$ local this is the strict henselisation of EGA IV$_4$, §18.8.

**Definition 2.4.4 (Absolutely integrally closed).** A ring $T$ is *absolutely integrally closed* if every monic polynomial of positive degree over $T$ has a root in $T$.

If $T$ is an absolutely integrally closed domain, then $T$ is [[integrally closed|H20P600HQS]] and its fraction field is [[algebraically closed|0PF6TM8TWT]]. Indeed a monic $f$ over $T$ splits into linear factors over $T$, by induction on the degree, so all its roots in $K$ lie in $T$; and a monic polynomial over $K$ becomes monic over $T$ after the substitution $x = y/c$ for a common denominator $c$. If $T$ is also local, its residue field is algebraically closed.

**Theorem 2.4.5 (Cyclic torsors over the generic fibre).** Let $T$ be an absolutely integrally closed domain with fraction field $K$, let $P$ be a prime of $T[x]$, and let $\varphi : T[x]_P \to O$ be a strict henselisation, compatible with the maps from $T[x]$. Let $q \geq 1$ be a unit in $T$. Then $\mathbb{Z}/q$-torsors over $O_K$ are trivial.

Lean: `GlobalTheory.LocAcyc.torsor_trivial`.

The proof reduces the theorem to one prime of $T[x]$, the origin. We state the reductions first, and then the case of the origin.

**Lemma 2.4.6 (Reduction to a local base).** If the theorem holds for every local $T$ and every prime $P$ with $P \cap T = \mathfrak{m}_T$, then it holds in general.

Lean: `GlobalTheory.T.torsorTrivialGenericFibre_of_strictHenselClosedFibre` (also `GlobalTheory.LocAcyc.keyAll_of_keyLocal`).

*Proof.* Let $\mathfrak{p} = P \cap T$ and replace $T$ by the [[localization|X6JD4AG973]] $T_{\mathfrak{p}}$. It is again an absolutely integrally closed domain, now local, with the same fraction field. The prime $P$ gives a prime of $T_{\mathfrak{p}}[x]$ over the maximal ideal, with the same local ring, so $O$ is a strict henselisation of it. Inverting $T \setminus \{0\}$ and $T_{\mathfrak{p}} \setminus \{0\}$ in $O$ gives the same ring. $\square$

Now let $T$ be local with maximal ideal $\mathfrak{m}$ and residue field $k$. The primes of $T[x]$ over $\mathfrak{m}$ are the primes of $k[x]$: the generic point $\mathfrak{m}[x]$ of the closed fibre and its closed points. The *origin* is the prime $\mathfrak{m}[x] + (x)$.

**Lemma 2.4.7 (Closed points from the origin).** If the theorem holds when $T$ is local and $P$ is the origin, then it holds when $T$ is local, $P \cap T = \mathfrak{m}$ and $P \neq \mathfrak{m}[x]$.

Lean: `GlobalTheory.T.torsorTrivialClosedPoints_of_origin_closedFibre` (also `GlobalTheory.LocAcyc.Translate.keyClosedPts_of_keyOrigin`).

*Proof.* The image of $P$ in $k[x]$ is a nonzero prime, and $k$ is algebraically closed, so $P$ contains $x - c$ for some $c \in T$. Then $P = \mathfrak{m}[x] + (x - c)$. The $T$-algebra automorphism $x \mapsto x + c$ of $T[x]$ sends $x - c$ to $x$, so it carries $P$ to the origin. Composing with it turns a strict henselisation at $P$ into one at the origin, and it does not change the generic fibre. $\square$

**Lemma 2.4.8 (The generic point of the closed fibre).** If the theorem holds when $T$ is local, $P \cap T = \mathfrak{m}$ and $P \neq \mathfrak{m}[x]$, then it holds for $P = \mathfrak{m}[x]$.

Lean: `GlobalTheory.T.keyGeneric_of_keyClosedPts'` (also `GlobalTheory.LocAcyc.keyGeneric_of_keyClosedPts`).

*Proof.* A torsor over $O_K$ comes from a torsor over the generic fibre of an étale $T[x]$-algebra $E$, with a prime $Q$ of $E$ over $P = \mathfrak{m}[x]$. In the closed fibre of $E$ choose a maximal ideal $y$ that contains $Q$. The torsor has a section over the generic fibre of the strict henselisation of $E$ at $y$, by the case of closed points. Since $y$ specializes $Q$, there is a map from the strict henselisation at $y$ to the strict henselisation $O$ at $Q$, compatible with $E$. Composing gives a section over $O_K$. $\square$

*Proof of the theorem.* By the two lemmas on the closed fibre, the case of the origin gives all primes over $\mathfrak{m}$, by cases on whether $P = \mathfrak{m}[x]$. The reduction to a local base then gives all $P$. The case of the origin is the next theorem. $\square$

**Theorem 2.4.9 (The origin).** The theorem holds when $T$ is local, $P \cap T = \mathfrak{m}$ and $P = \mathfrak{m}[x] + (x)$.

Lean: `GlobalTheory.T.torsor_trivial_strict_henselisation_origin` (also `GlobalTheory.KeyOriginCut.keyOrigin`).

*Proof.* The condition $P \cap T = \mathfrak{m}$ follows from $P = \mathfrak{m}[x] + (x)$, and the argument uses only the second. Let $D$ be a $\mathbb{Z}/q$-torsor over $O_K$. There are three steps, and we take the first two as given.

First, $O$ is a filtered colimit of local rings $E_Q$ of étale $T[x]$-algebras $E$ at primes $Q$ over the origin (EGA IV$_4$, §18.8). The torsor $D$ comes from a torsor $D_1$ over the generic fibre of some $E_Q$, and a section of $D_1$ over $O_K$, compatible with the map of generic fibres, gives a section of $D$.

Second, the data descend to a noetherian model: a [[noetherian|0670T59HGE]], normal, local domain $A$, essentially of finite type over $\mathbb{Z}$, with an injective local map $A \to T$ and $q$ a unit in $A$; an étale $A[x]$-algebra $E_A$ with a prime $Q_A$ over the origin of $A[x]$, and a map $(E_A)_{Q_A} \to O$ compatible with $A[x] \to T[x]$; and a torsor $D_A$ over the generic fibre of $(E_A)_{Q_A}$, where now only $A \setminus \{0\}$ is inverted. Sections of $D_A$ give sections of $D_1$.

Third, the theorem on noetherian models below gives a section of $D_A$ over $O_K$. $\square$

Lean: `GlobalTheory.T.strict_henselisation_prime_eq` (also `GlobalTheory.KeyOriginCut.exists_stage_torsor`) and `GlobalTheory.T.exists_noetherian_model_torsor_origin` (also `GlobalTheory.KeyOriginNoeth.exists_noetherian_model`).

For a noetherian model we need the integral closure of the base in the torsor. Let $A$ be a domain, $R$ a local $A$-algebra and $D$ an algebra over the generic fibre $R_K$. The *closure* $C$ of $R$ in $D$ is the integral closure of the image of $R$ in $D$. Let $\rho : R \to A$ be a ring map. We say that $(R, D, \rho)$ is *good* if:

1. for every prime $\mathfrak{P}$ of $R$ such that $\mathfrak{P} \cap A$ has height at most $1$, the algebra $R_{\mathfrak{P}} \otimes_R C$ is étale over $R_{\mathfrak{P}}$;
2. there is a ring map $s : C \to \operatorname{Frac}(A)$ with $s|_R = \rho$, followed by $A \subset \operatorname{Frac}(A)$.

**Definition 2.4.10 (Fitting data and retractions).** Let $T$ be a local, absolutely integrally closed domain, let $P = \mathfrak{m}[x] + (x)$, let $\varphi : T[x]_P \to O$ be a strict henselisation compatible with the maps from $T[x]$, and let $q \geq 1$ be a unit in $T$. *Fitting data* consist of a noetherian, normal, local domain $A$, essentially of finite type over $\mathbb{Z}$, a ring map $i : A \to T$, an étale $A[x]$-algebra $E_A$ with a prime $Q_A$, a ring map $j : R \to O$ with $R = (E_A)_{Q_A}$, a ring map $\psi : R_K \to O_K$ of generic fibres, and a $\mathbb{Z}/q$-torsor $D_A$ over $R_K$, such that: $i$ is injective and local; $q$ is a unit in $A$; $Q_A$ lies over the origin of $A[x]$; $j$ restricted to $A[x]$ is $A[x] \to T[x] \to O$, the first map given by $i$; and $\psi$ extends $j$. A *retraction* for fitting data is a ring map $\rho : R \to A$ that is the identity on $A$, has kernel $xR$, and satisfies $i(\rho(y)) - j(y) \in xO$ for every $y \in R$.

**Theorem 2.4.11 (Sections over a noetherian model).** Let $T$, $O$, $q$ be as in the definition of fitting data, and let $(A, i, E_A, Q_A, j, \psi, D_A)$ be fitting data. Then there is a ring map $\sigma : D_A \to O_K$ that extends $\psi$.

Lean: `GlobalTheory.T.torsor_point_over_strictHenselisation_noetherianNormal` (also `GlobalTheory.KeyOriginNoeth.torsor_point_of_essFiniteType`).

*Proof.* By the enlargement theorem below there are $A'$, $E_{A'}$, $Q_{A'}$, $D_{A'}$, a map $\rho' : R' = (E_{A'})_{Q_{A'}} \to A'$, maps $j'$ and $\psi'$, and maps $\beta$ of generic fibres and $h : D_A \to D_{A'}$ with $\psi' \circ \beta = \psi$ and $h$ over $\beta$, such that $(R', D_{A'}, \rho')$ is good. We take as given that the closure $C'$ of $R'$ in $D_{A'}$ is then finite, étale and nonzero over $R'$. Now $O$ is strictly henselian, so the nonzero finite étale $O$-algebra $C' \otimes_{R'} O$ has a section, and the map $R' \to O$ extends to $C' \to O$. We take as given that this gives a map $\sigma' : D_{A'} \to O_K$ that extends $\psi'$. Then $\sigma = \sigma' \circ h$ extends $\psi' \circ \beta = \psi$. $\square$

Lean: `GlobalTheory.T.integralClosure_finiteEtale_originKeyLemma_essFiniteType` (also `GlobalTheory.GoodEtale.closure_finiteEtale`) and `GlobalTheory.T.exists_point_closureFiniteEtale_strictHenselian` (also `GlobalTheory.KeyOriginNoeth.exists_point_of_closureFiniteEtale`).

**Theorem 2.4.12 (Enlargement to a good model).** Let $T$, $O$, $q$ be as in the definition of fitting data, and let $(A, i, E_A, Q_A, j, \psi, D_A)$ be fitting data. Then there are: a noetherian, normal, local domain $A'$, essentially of finite type over $\mathbb{Z}$; an étale $A'[x]$-algebra $E_{A'}$ with a prime $Q_{A'}$ over the origin of $A'[x]$, such that $q$ is a unit in $A'$; a ring map $\rho' : R' = (E_{A'})_{Q_{A'}} \to A'$ that is the identity on $A'$ and has kernel $xR'$; ring maps $j' : R' \to O$ and $\psi' : R'_K \to O_K$ with $\psi'$ extending $j'$; a $\mathbb{Z}/q$-torsor $D_{A'}$ over $R'_K$ such that $(R', D_{A'}, \rho')$ is good; and ring maps $\beta : R_K \to R'_K$ and $h : D_A \to D_{A'}$ with $\psi' \circ \beta = \psi$ and $h$ extending $\beta$.

Lean: `GlobalTheory.T.strictHenselisation_enlarge_good_at_origin` (also `GlobalTheory.KeyOriginEnlarge.enlarge_good`).

*Proof.* Three enlargements, each of the same shape. The first gives fitting data with a retraction. The second keeps the retraction and adds a point at zero: a map $s$ from the closure to $\operatorname{Frac}(A)$ that restricts to $\rho$ on $R$, which is condition 2 of goodness. The third is the next theorem, which gives fitting data with a retraction $\rho'$ such that the data are good. Compose the maps $\beta$ and $h$ of the three steps, and keep from the result only the properties listed in the statement. $\square$

Lean: `GlobalTheory.T.enlarge_strictHenselisation_retract_mod` (also `GlobalTheory.KeyOriginEnlarge.enlarge_retract`) and `GlobalTheory.T.enlarge_base_separable_point_integralClosure` (also `GlobalTheory.KeyOriginEnlargePoint.enlarge_point`).

**Theorem 2.4.13 (Étale enlargement by roots of uniformisers).** Let $T$, $O$, $q$ be as in the definition of fitting data, let $(A, i, E_A, Q_A, j, \psi, D_A)$ be fitting data with a retraction $\rho$, and suppose that there is a ring map $s : C \to \operatorname{Frac}(A)$ from the closure $C$ of $R$ in $D_A$ with $s|_R = \rho$. Then there are fitting data $(A', i', E_{A'}, Q_{A'}, j', \psi', D_{A'})$ with a retraction $\rho'$ such that $(R', D_{A'}, \rho')$ is good, and ring maps $\beta : R_K \to R'_K$ and $h : D_A \to D_{A'}$ with $\psi' \circ \beta = \psi$ and $h$ extending $\beta$.

Lean: `GlobalTheory.T.etale_enlarge_by_uniformiser_roots` (also `GlobalTheory.KeyOriginEnlarge.etale_enlarge`).

*Proof.* This is [the theorem on étale enlargement](/entry/etale-enlarge/), proved in the section on Abhyankar's lemma and base change. $\square$

**Remark 2.4.14 (Formalization).** The origin case assumes both $P \cap T = \mathfrak{m}$ and $P = \mathfrak{m}[x] + (x)$, and the proof does not use the first: [TorsorTrivialStrictHenselisationOrigin.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorTrivialStrictHenselisationOrigin.lean#L17). The name of the first step of that proof speaks of a prime that is equal to something, while its statement descends a torsor to a finite stage. The first enlargement step returns its retraction property in a conjunction with the trivial statement True, which the proof of the enlargement theorem discards: [EnlargeStrictHenselisationRetractModStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EnlargeStrictHenselisationRetractModStatement.lean#L35). The conclusion of the enlargement theorem keeps only two of the three clauses of a retraction and has no map $A' \to T$. The hypothesis of a point at zero in the last theorem is, word for word, condition 2 of goodness ([PointAtZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PointAtZero.lean#L38) and [ClosureFiniteEtale.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClosureFiniteEtale.lean#L32)). The lemma that produces the section from the closure does not require the map $R' \to O$ to be local. We opened the statements of the lemmas used in the proofs, not their proofs.
