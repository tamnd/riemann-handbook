---
title: Hecke operators and the unimodular genus
decls:
  - Formalism.L2.Col.heckeOperators_commute
  - Formalism.L2.Col.unimodGenus_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke operators and the unimodular genus

This section proves two facts on hermitian lattices that the column construction needs beside the unfolding. The first is that the [[Hecke operators|S4SV3QZ8B1]] at split primes, acting on functions on decorated lattices, commute with each other. It feeds [the large coefficient field that contains the twist values](/entry/large-coefficient-field-contains-twist-values/) of Volume 14, since commuting operators can be diagonalized together. The second is that every unimodular lattice for the standard form is an adelic translate of the standard lattice. It feeds [the nonempty hypotheses with unramified exponents](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) of Volume 15.

### Decorated lattices and Hecke neighbours

Let $E$ be a number field with an involution $a \mapsto \bar a$, and let $n \geq 1$. For a prime $P$ of $\mathcal{O}_E$ let $\bar P$ be its conjugate. We use [lattices in hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces): an $\mathcal{O}_E$-lattice $N \subset E^n$ is *unimodular* for a [[Hermitian form|48P4A1CX85]] $h$ if its dual for $h$ is $N$.

**Definition 5.4.1 (Decorated lattice).** Fix two finite sets $S_T$ and $S_G$ of primes. A *decorated lattice* is a triple $(N, f, \beta)$ where $N$ is a lattice in $E^n$, unimodular for the standard form; for each $P \in S_T$, $f_P$ is an additive map on the localization $N_P$ with $f_P(ax) = \bar a f_P(x)$, zero off $N_P$ and nonzero somewhere on $N$; and for each $w \in S_G$, $\beta_w$ is a linear map, zero off $N_w$, surjective from $N$, whose kernel in $N$ lies in $wN$.

**Definition 5.4.2 (Hecke neighbour).** Let $P$ be a prime and $i \geq 0$. A lattice $N'$ is a *Hecke neighbour of index $i$* of $N$ at $P$ if
$$P N' \subseteq N, \qquad \bar P N \subseteq N', \qquad N / (N \cap N') \cong (\mathcal{O}_E/\bar P)^i.$$
For a decorated lattice $d = (N, f, \beta)$, the *neighbour set* $\mathrm{nb}(P, i, d)$ is the set of decorated lattices $(N', f, \beta)$ with $N'$ a Hecke neighbour of index $i$ of $N$, if this set is finite, and the empty set otherwise.

**Definition 5.4.3 (Hecke operator).** Let $D$ be a set with an action of a group $G$, and let $D$ be identified with the decorated lattices in a $G$-equivariant way, where $G$ acts on decorated lattices through a homomorphism to the unitary group of the form and the general linear group at $S_G$. Let $\rho$ be a representation of $G$ on a vector space $W$ over a field $K$. Let $\mathcal{F}$ be the space of functions $\varphi \colon D \to W$ with $\varphi(gd) = \rho(g)\varphi(d)$. The *Hecke operator* $T_{P,i}$ on $\mathcal{F}$ is
$$(T_{P,i}\varphi)(d) = \sum_{e \in \mathrm{nb}(P, i, d)} \varphi(e).$$

The operator is well defined because $g$ maps the neighbours of $d$ to the neighbours of $gd$. For a finite set $S_0$ of primes, the primes *of good level* are the primes $P$ with $\bar P \neq P$, $P \notin S_0 \cup S_T \cup S_G$, and $\bar P \neq Q$ for all $Q \in S_0 \cup S_T \cup S_G$. These are split primes away from the level.

### Commutation

Let $d$ and $f$ be decorated lattices. The *path count* $c(P, Q, i, j; d, f)$ is the number of decorated lattices $e$ with $e \in \mathrm{nb}(P, i, d)$ and $f \in \mathrm{nb}(Q, j, e)$, counted as $0$ when there are infinitely many. Then
$$(T_{P,i} T_{Q,j} \varphi)(d) = \sum_{f} c(P, Q, i, j; d, f)\, \varphi(f).$$
So the operators commute if the path count is symmetric in $(P, i)$ and $(Q, j)$.

**Lemma 5.4.4 (Symmetry of path counts).** Let $P$ and $Q$ be primes with $\bar P \neq P$ and $\bar Q \neq Q$, such that $P$, $\bar P$, $Q$, $\bar Q$ are not in $S_T \cup S_G$. Then for all $i, j$ and all decorated lattices $d$, $f$,
$$c(P, Q, i, j; d, f) = c(Q, P, j, i; d, f).$$

*Proof.* There are three cases. The Lean proof `pathCount_symmetric_holds` splits into the same three cases, with the lemmas `pathCount_symm_same_prime`, `pathCount_conj_symm` and `pathCount_symm_distinct`. We sketch each case and do not follow the formal proofs line by line.

Case $Q = P$. If $f$ does not have the decorations of $d$, or $P^2 N_f \not\subseteq N_d$, both counts are $0$. Otherwise put $X = N_d / (N_f \cap N_d)$, a module over $\mathcal{O}_E/P^2$. The paths $d \to e \to f$ are in bijection with the submodules $Y \subseteq X$ with $\bar P X \subseteq Y$, $\bar P Y = 0$, $|X/Y| = q^i$ and $|Y| = q^j$. The map $Y \mapsto$ (its annihilator in $X$ for the pairing that $h$ induces) exchanges the roles of $i$ and $j$. So the two counts agree.

Case $Q = \bar P$. Let $n$ be the dimension. Counts with $i > n$ or $j > n$ are $0$ on both sides. Otherwise the top neighbour at $\bar P$ gives an involution $d \mapsto d^*$, and $c(P, \bar P, i, j; d, f) = c(P, P, i, n-j; d^*, f)$. The first case then gives the symmetry.

Case $Q \notin \{P, \bar P\}$. A path $d \to e \to f$ is determined by $d$ and $f$, since $N_e$ agrees with $N_d$ away from $P$, $\bar P$ and with $N_f$ away from $Q$, $\bar Q$, and the lattice is the intersection of its localizations. So both counts are at most $1$. A path in one order exists if and only if the lattice glued from $N_f$ at $P$, $\bar P$ and from $N_d$ elsewhere is a neighbour in the other order. So the two counts are $0$ or $1$ together. $\square$

**Theorem 5.4.5 (Commutation of Hecke operators).** For every finite set $S_0$ of primes, the Hecke operators $T_{P,i}$, for $P$ of good level and $i \geq 0$, commute with each other on $\mathcal{F}$.

Lean: `Formalism.L2.Col.heckeOperators_commute`.

*Proof.* By the formula for $T_{P,i}T_{Q,j}$ in terms of path counts, it suffices that the path counts are symmetric. Primes of good level satisfy the hypotheses of the lemma. $\square$

### The unimodular genus

Let $F$ be a totally real number field and $E/F$ a CM extension: a totally imaginary quadratic extension with complex conjugation as involution, such that $a = \bar a$ exactly for $a \in F$, and $E/F$ unramified at all finite places. Let $h$ be the standard hermitian form on $E^n$, with Gram matrix the identity, and $L_0 = \mathcal{O}_E^n$ the standard lattice. Two lattices $L$, $M$ are in the same [genus](/learn/hermitian-lattices/#genus-class-and-spinor-genus) if for each finite prime $v$ there is an isometry $g$ with $g L_v = M_v$.

**Theorem 5.4.6 (Uniqueness of the unimodular genus).** Let $E$ be a number field with an involution that is a CM field unramified over its fixed field, and let $n \geq 0$. Every lattice $N \subset E^n$ that is unimodular for $h$ is in the genus of $L_0$.

*Proof.* We take this as given. At a prime $v$ of $F$ that splits in $E$, a unimodular lattice is a self dual lattice for $\mathrm{GL}_n$ and all of them are conjugate. At an inert prime, the [local classification](/learn/hermitian-lattices/#local-classification) of Jacobowitz says that unimodular lattices of the same rank are isometric. Since $E/F$ is unramified, there are no ramified primes. $\square$

For the adelic form, let $U(\mathbb{A}_f)$ be the unitary group of the identity form over $E \otimes_F \mathbb{A}_{F,f}$. For $x \in U(\mathbb{A}_f)$ let $x L_0$ be the global lattice whose localization at each $v$ is $x_v L_{0,v}$, that is, the set of $y \in E^n$ with $x^{-1}y \in \prod_v L_{0,v}$.

**Theorem 5.4.7 (Unimodular lattices are translates).** Let $E/F$ be a CM extension as above and $n \geq 1$. Every lattice $N \subset E^n$ that is unimodular for $h$ is $x L_0$ for some $x \in U(\mathbb{A}_f)$.

Lean: `Formalism.L2.Col.unimodGenus_holds`.

*Proof.* By the previous theorem, $N$ is in the genus of $L_0$. By [the equivalence of genus and adelic orbit](/entry/unimod-genus-iff/), a lattice in the genus of $L_0$ is an adelic translate $x L_0$: choose local isometries $g_v$ with $g_v L_{0,v} = N_v$, almost all equal to $1$, and put $x = (g_v)_v$. $\square$

**Remark 5.4.8 (Formalization).** The uniqueness of the unimodular genus is a proved theorem that we did not unfold; the proof sketch above follows the classical argument and not the formal one. The CM condition is a hypothesis of the local statement, and the global statement supplies it from the CM data. The data of a CM extension are defined twice, in two separate places. The neighbour set is empty when it is infinite, and the path count is $0$ for an infinite set; for lattices both are finite. See [PathCountSymmetricHolds.lean](lean:Formalism/LocalToGlobal/Columns/PathCountSymmetricHolds.lean#L25) and [InputsGenus.lean](lean:Formalism/LocalToGlobal/Columns/InputsGenus.lean#L17).
