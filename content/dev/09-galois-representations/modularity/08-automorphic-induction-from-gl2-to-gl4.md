---
title: Automorphic induction from GL2 to GL4
decls:
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.IwahoriBlocks.zSimple
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.irreducible_cuspidal_weight_component
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.irrW
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.archEx
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.famNe
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.coreInd
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.indCs_of_gm
  - UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.indCs_of_bcfl
  - UpperTheory.V.Z.Bc.indCs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Automorphic induction from GL2 to GL4

This section proves automorphic induction from $\mathrm{GL}_2$ over a quadratic extension $M/K$ of totally complex fields to $\mathrm{GL}_4$ over $K$, for cuspidal representations with distinct weights. The [seed of case II](/entry/seed-iis-alt/) uses it. The proof follows the plan of Arthur and Clozel (*Simple algebras, base change, and the advanced theory of the trace formula*, Ann. of Math. Stud. 120, 1989, Chapter 3): compare the twisted trace formula for $\mathrm{GL}_4$ over $M$ with the trace formula for $\mathrm{GL}_4$ over $K$. In this comparison, the pair $(\pi, \pi^\sigma)$ contributes to the twisted side through Eisenstein series of the parabolic of type $(2, 2)$. Most of the section shows that this Eisenstein term is not zero. The [trace identity with an Eisenstein term](/entry/cix/) of Section 9 is the comparison itself.

### Swapped pairs and their Eisenstein sections

Let $E/F$ be a Galois extension of degree $2$ of totally complex fields, with generator $\sigma$. A *swapped pair* is a pair $\tau_1, \tau_2$ of irreducible cuspidal subspaces of $L^2$ for $\mathrm{GL}_2$ over $E$ that are orthogonal, with a Galois twist $\theta_2$ for $\sigma$ such that $\tau_1\theta_2 = \tau_2$ and $\tau_2\theta_2 = \tau_1$. Let $K_n$ be the maximal compact subgroup of $\mathrm{GL}_n$ at the infinite places. An *idempotent* on $K_n$ is a Haar probability measure $\kappa$ with a continuous function $e$ such that $e(k^{-1}) = \overline{e(k)}$ and $e * e = e$.

An *Eisenstein section* for $(\tau_1, \tau_2)$ is a continuous bounded function $f$ on $\mathrm{GL}_4$ over $E$ that is left invariant under the unipotent radical of the parabolic of type $(2,2)$ and under $\mathrm{diag}(r, r, r^{-1}, r^{-1})$ for $r > 0$, such that each function $(m_1, m_2) \mapsto f(\mathrm{diag}(m_1, m_2)g)$ is a finite sum of products of functions in $\tau_1$ and $\tau_2$.

**Theorem 8.8.1 (Archimedean test data).** Let $(\tau_1, \tau_2, \theta_2)$ be a swapped pair and fix a datum at infinity for $\sigma$, which splits $K_4$ over $E$ into two components. Then there are idempotents $(\kappa_F, e_F)$ on $K_4$ over $F$ and $(\kappa, e)$ on $K_4$ over $E$, a measure $\kappa_2$ and functions $p_1, p_2$ on $K_2$ over $E$, and $k_0 \in K_4$, such that:

1. $e(k) = e_F(k_1)e_F(k_2)$, where $k_1, k_2$ are the components of $k$;
2. each $p_i$ is an idempotent with a nonzero fixed vector in $\tau_i$, and acts by scalars on these fixed vectors;
3. if $f$ is an Eisenstein section fixed by $e$, then $m_1 \mapsto f(\mathrm{diag}(m_1, m_2)k_0 h)$ is fixed by $p_1$, and the same holds in $m_2$ for $p_2$;
4. an Eisenstein section fixed by $e$ that vanishes at all points $\mathrm{diag}(m_1, m_2)k_0 h$ is zero;
5. if $\tau_1$ and $\tau_2$ have spherical vectors outside a finite set $S$, there are a level and a nonzero Eisenstein section fixed by $e$ and by this level.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.archEx`.

*Proof.* Choose coordinates at infinity and minimal $K$-types of $\tau_1$ and $\tau_2$ at each infinite place. The twist $\theta_2$ moves the type of $\tau_1$ to that of $\tau_2$. Extend the two types to $K_4$; the projectors onto them give $e$ and $p_1, p_2$, and items 2 to 5 follow from the properties of minimal types. The product formula 1 is a computation on the two components. $\square$

We call the data of the theorem *archimedean test data* for the pair.

### Irreducibility on the Eisenstein space

Let $K$ be totally complex, $(\tau_1, \tau_2)$ a swapped pair over $K$ with archimedean test data, and $S$ a finite set of finite places. Put $G_S = \prod_{w \in S}\mathrm{GL}_4(K_w)$. Let $Z_S$ be the span of the Eisenstein sections, restricted to the norm one group, that are fixed by $e$, by an open compact subgroup at the places of $S$, and by $\mathrm{GL}_4(\mathcal{O}_w)$ at the places outside $S$. The group $G_S$ acts on $Z_S$ by right translation.

**Theorem 8.8.2 (Irreducibility of the Eisenstein space).** The space $Z_S$ is stable under $G_S$, and each nonzero stable subspace of $Z_S$ is $Z_S$.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.IwahoriBlocks.zSimple`.

*Proof.* Let $\mathrm{ev}$ send $\varphi \in Z_S$ to the function $(g, m_1, m_2) \mapsto \varphi(\mathrm{diag}(m_1, m_2)k_0 g)$ on $G_S \times \mathrm{GL}_2 \times \mathrm{GL}_2$. By item 4 of the test data, $\mathrm{ev}$ is injective on $Z_S$, and it commutes with right translation by $G_S$. By item 3, its image lies in the representation of $G_S$ induced from the tensor product of the spaces $X_1, X_2$ of $p_i$-fixed vectors in $\tau_1, \tau_2$. The cuspidal pieces $\tau_1, \tau_2$ are irreducible and the $p_i$ act by scalars, so this induced representation is irreducible on the image, and the image of a nonzero stable subspace $Q$ is the whole image. As $\mathrm{ev}$ is injective, $Q = Z_S$. $\square$

A *type datum* $D$ at level $U$, fixed by $(\kappa, e)$, picks out the Eisenstein sections fixed by $e$ and by $U$. A *line* of type $D$ and dimension $d$ is a linear injective map $A$ from $\mathbb{C}^d$ onto the Eisenstein sections of type $D$. For $h \in G_S$, a Hecke matrix of $A$ at $h$ is an $M \in \mathrm{End}(\mathbb{C}^d)$ with $A(Mv) = T_h A(v)$, where $T_h$ is the Hecke operator of the level $U$ at $h$.

**Theorem 8.8.3 (Irreducibility of a line).** Let $A$ be a line of type $D$ at a level that is $U_w$ at $w \in S$ and maximal outside $S$. If a subspace $P \subseteq \mathbb{C}^d$ is stable under all Hecke matrices of $A$ at the elements of $\mathrm{GL}_4(K_w)$, $w \in S$, then $P = 0$ or $P = \mathbb{C}^d$.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.irrW` (also `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.irreducible_cuspidal_weight_component`, the form with $S$ given as an injective list of places).

*Proof.* Write $S$ as an injective list of places. The map $\Phi(v) = A(v)$, restricted to the norm one group, is injective with values in $Z_S$, and its values are fixed by $U_S = \prod_{w \in S} U_w$. The Hecke operators of $U_S$ preserve $\Phi(P)$, because $P$ is stable under the Hecke matrices. For a simple smooth representation $V$ of $G_S$, the space $V^{U_S}$ is a simple module over the Hecke algebra of $U_S$. By the previous theorem $Z_S$ is simple, so $\Phi(P)$ is $0$ or all of $Z_S^{U_S}$. In the first case $P = 0$. In the second case each $\Phi(v)$ lies in $\Phi(P)$, so $P = \mathbb{C}^d$. $\square$

### The Eisenstein term is not zero

Fix a Galois twist $\theta$ of $L^2$ for $\mathrm{GL}_4$ over $E$. The twisted trace formula uses a *side*: a finite set $S$ of places of $E$, a level $U$ on $S$, test functions $a$ and $g$, and a Hecke operator $U_q$ at a split place. A *family* over a side holds a swapped pair with parameters $(m_i, B_i)$ outside $S$, a type datum $D$, lines $A$ for $(\tau_1, \tau_2)$ and $A'$ for $(\tau_2, \tau_1)$, the isometry $s$ from the first line to the second that $\theta$ induces, the operators $\beta_a$ and $\beta_g$ by which $a$ and $g$ act on $A'$, and the operators $u$ and $v$ by which $U_q$ acts on $A'$ and $A$. For an isometry $N$ from $\mathbb{C}^{d'}$ to $\mathbb{C}^d$, $x \in \mathbb{R}$ and $j \geq 0$, the *Eisenstein term* is

$$
\mathrm{tr}_N(x, j) = \operatorname{tr}\bigl(N \circ P_x \circ u^j \circ \beta_g \circ s\bigr),
$$

where $P_x$ is the orthogonal projection onto the eigenspace of $a_0 = \beta_a$ with eigenvalue $x$, and $u$, $\beta_a$, $\beta_g$ are taken at the central point.

**Theorem 8.8.4 (Nonvanishing of the Eisenstein term).** Let $E/F$ be quadratic with Galois twist $\theta$ and let a family over a side be given, with archimedean test data. Assume that each place of $S$ lies over a place of $F$ that splits in $E$ and that $S$ holds both places over it; that the level is the one of the side and is stable under $\theta$; that $U$ is an Iwahori subgroup at a place $w_0 \in S$ and $U_q$ is the Iwahori Hecke operator of a decreasing cocharacter at $w_0$; that $g$ is the product of an archimedean function $a_0$ and the indicator function of the level, with $a = cg$ for some $c \neq 0$; that $a_0$ does not kill the line; and that $N$ intertwines the actions of all operators on the two lines. Then there is $x > 0$ with $\mathrm{tr}_N(x, j) \neq 0$ for infinitely many $j$.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.famNe`.

*Proof.* The function $a$ acts on the line by an operator, and by the irreducibility of a line it is a scalar: there is $x > 0$ with $a_0 = x \cdot 1$ and $d > 0$. Then $g = c^{-1}a$ acts by $x/c$. The Hecke matrices $M_h$ of $A$ exist and are unique. The twist $\theta$ exchanges the two places of $E$ over each split place of $F$ in $S$, so the Hecke matrices fall into two commuting families $M_0(y)$ and $M_1(y)$, and the isometry $\Phi = N \circ s$ satisfies $\Phi M_{i+1}(y) = M_i(y)\Phi$. By the irreducibility of a line, $\mathbb{C}^d$ is irreducible under the two families. The Iwahori Hecke matrix at $w_0$ of a decreasing cocharacter is injective, and it equals $v$, which $N$ intertwines with $u$. A lemma of linear algebra now gives $\operatorname{tr}(\Phi M^j) \neq 0$ for infinitely many $j$, where $M$ is this injective matrix. Since $\mathrm{tr}_N(x, j) = (x/c)\operatorname{tr}(\Phi M^j)$, the claim follows. $\square$

### Induction of a swapped pair

For a subspace $V$ of automorphic forms, say that $V$ has parameters $(\Lambda, t)$ off $S$ if at each complex embedding the archimedean operators act on $V$ through the multiset $\Lambda$, and at each place outside $S$ the space $V$ has spherical vectors on which the Satake operators act through the multiset $t$.

**Theorem 8.8.5 (Induction of a swapped pair).** Assume the trace identity with an Eisenstein term, the comparison of geometric sides, and weak base change for all $\mathrm{GL}_n$. Let $E/F$ be quadratic, $(\tau_1, \tau_2, \theta_2)$ a swapped pair, and $S$ a finite set of places of $F$ that split in $E$, with $E/F$ unramified outside $S$. Assume that $\tau_i$ has parameters $(m_i, B_i)$ off the places over $S$. Then for each Haar measure on $\mathrm{GL}_4$ over $F$ there is a summand $V$ of the spectrum of $\mathrm{GL}_4$ over $F$ with parameters $(\Lambda, t)$ off a finite set, such that $m_1(\tau) + m_2(\tau) = \Lambda(\tau|_F)$ for each embedding $\tau$ of $E$, and $B_1(w) + B_2(w) = \{b^{f_w} : b \in t(w|_F)\}$ for almost all $w$, with $f_w$ the residue degree.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.coreInd`.

*Proof.* Choose a split place $q \notin S$. The archimedean test data, local levels with an Iwahori subgroup over $q$, a twist $\theta$ that preserves the type, lines $A$, $A'$ and test functions at infinity give a family. The comparison of geometric sides gives a constant $c$ such that the two geometric sides agree up to $c$. Weak base change shows that no automorphic datum over $F$ has parameters whose base change is that of the family, which is the hypothesis of the trace identity. The trace identity gives $N$ and, for $x > 0$ and all large $j$,

$$
\mathrm{tr}_E(x, j) + \tfrac{1}{2}\,\mathrm{tr}_N(x, j) = c\,\mathrm{tr}_F(x, j).
$$

By rigidity over $E$, no summand over $E$ has the parameters of the family, so the cuspidal term $\mathrm{tr}_E$ is zero. By the previous theorem, $\mathrm{tr}_N(x, j) \neq 0$ for some $x > 0$ and infinitely many $j$. So $\mathrm{tr}_F(x, j) \neq 0$, and some summand $V$ over $F$ with the required parameters exists. $\square$

### Automorphic induction

**Theorem 8.8.6 (Automorphic induction from a comparison of geometric sides).** Assume the comparison of geometric sides. Let $M/K$ be a quadratic extension of totally complex fields and $\pi$ an irreducible cuspidal subspace for $\mathrm{GL}_2$ over $M$. Assume that above each embedding of $K$ there are two embeddings $\tau \neq \tau'$ of $M$ at which the four integers of the infinitesimal characters of $\pi$ are distinct, and that at each place of $K$ that does not split in $M$ the extension is unramified and $\pi$ has Satake parameters at the places above it. Then there is a cuspidal $P$ on $\mathrm{GL}_4$ over $K$ such that:

1. for almost all places $w$ of $M$ over $v$: if $w' \neq w$ is the other place over $v$, the Satake parameters of $P$ at $v$ are $B_w \cup B_{w'}$; if $\mathrm{N}w = (\mathrm{N}v)^2$, the parameters of $\pi$ at $w$ are $\{b^2 : b \in B'\}$ and those of $P$ at $v$ are $B' \cup (-B')$ for some $B'$;
2. if $\tau \neq \tau'$ lie over the same embedding $\varphi$ of $K$ and $\pi$ has infinitesimal characters $m, m'$ at $\tau, \tau'$, then $P$ has infinitesimal character $m + m'$ at $\varphi$.

Lean: `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.indCs_of_gm`.

*Proof.* The trace identity with an Eisenstein term of Section 9 and the spectral comparison for base change give base change of one summand, then base change for all $n$ by induction on $n$, and so weak base change for all $\mathrm{GL}_n$. The previous theorem then inducts a swapped pair. For $\pi$ normalized and not isomorphic to its conjugate, apply it to $\tau_1 = \pi$ and $\tau_2 = \pi^\sigma$, and read off items 1 and 2. For general $\pi$, twist by a Hecke character $\chi$ so that $\pi \otimes \chi$ is normalized. The distinct weights show that the twist is not isomorphic to its conjugate. Apply the normalized case and twist back by a character of $K$. $\square$

**Theorem 8.8.7 (Automorphic induction).** The conclusion of the previous theorem holds without the hypothesis.

Lean: `UpperTheory.V.Z.Bc.indCs` (also `UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.indCs_of_bcfl`, the form with the fundamental lemma as hypothesis).

*Proof.* The fundamental lemma for base change of the unit element (Kottwitz, *Base change for unit elements of Hecke algebras*, Compositio Math. 60, 1986) says: for an unramified cyclic extension of local fields, the twisted orbital integrals of the unit of the spherical Hecke algebra over the larger field match the orbital integrals of the unit over the smaller field at norms, and the orbital integrals at elements that are not norms vanish. At a split place the units match by a direct computation, and at a place with one place above it they match by the fundamental lemma. This gives the comparison of geometric sides, and the previous theorem applies. $\square$

**Remark 8.8.8 (Formalization).** The irreducibility of a line is proved in [IrreducibleCuspidalWeightComponent.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/IrreducibleCuspidalWeightComponent.lean#L20) as a private theorem, and the public `irrW` at line 91 only lists $S$ as an injective map from `Fin r`. The private abbreviation `Zs` at [FiniteAdeleInclusionInjective.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/FiniteAdeleInclusionInjective.lean#L213), a type of places of $F$ under $S$, has the same name as the Eisenstein space `Zs` of `SimpleIn.lean`. The statement [IndC](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/BaseChangeUnits/QuadraticInductionGL2Alt.lean#L80) is the automorphic induction without the hypothesis at the non-split places, so the proved `IndCs` is a weaker form of it. The theorem [Bc.indCs](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/BaseChangeUnits/WsIIOfPrintsH.lean#L11) has the same short name as `E.indCs : IndNorm → IndCs` in [NotConjIso.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/NotConjIso.lean#L186), which the proof of `indCs_of_gm` calls. The side, the family, `GeoPair`, `IsSummand`, `LiftAll` and the rigidity lemmas `rigidE` and `rigidF` are stated in words here and not unfolded.
