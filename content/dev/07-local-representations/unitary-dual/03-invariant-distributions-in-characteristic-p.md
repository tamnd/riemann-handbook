---
title: Bernstein's vanishing theorem in characteristic p
decls:
  - PositivityTheory.RgUd.TP.Final.thmT
  - PositivityTheory.RgUd.TP.Final.desc
  - PositivityTheory.RgUd.TP.Desc.Final.desc
  - PositivityTheory.RgUd.TP.Desc.Piece.Final.pieceGood
  - PositivityTheory.RgUd.TP.Desc.Piece.PTr.transfer
  - PositivityTheory.RgUd.TP.Desc.Piece.TrI.transfer_of
  - PositivityTheory.RgUd.TP.Final.nilCore
  - PositivityTheory.RgUd.TP.Nil.Final.nilCore
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bernstein's vanishing theorem in characteristic p

This section proves the vanishing property of the [previous section](/entry/t-final-thm-t/) when the local field $k$ has characteristic $p > 0$. The argument in characteristic zero cuts $B_Z$ by the traces of powers. In characteristic $p$ these traces do not fix the characteristic polynomial, and the Jordan decomposition need not be defined over $k$. So the proof cuts $B_Z$ by the characteristic polynomial into closed pieces, each with a fixed type of semisimple part, and it runs the induction on a measure of the size of $Z$ in place of the dimension of $B_Z$. The nilpotent part is treated with a trace form. Together with the previous section this gives Theorem T for every nonarchimedean local field, which feeds [Theorems A and B](/entry/thm-a/) and the step [EveryCharacter](/step/every-character/).

Background: [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups).

### Pieces and the size of an algebra

We keep the notation of the previous section: $W = M_n(k) \times k^n$, a commutative reduced subalgebra $Z \subseteq M_n(k)$, its centralizer $B_Z$, the group $G_Z = B_Z^\times$, the set $Z_N$ of elements of $B_Z$ with semisimple part in $Z$, and the vanishing property $(\mathrm{V}_Z)$. Let $N_Z$ be the set of nilpotent elements of $B_Z$.

For a closed set $F \subseteq B_Z$, say that *$F$ is null for $Z$* if every functional $\xi$ on the functions $W \to \mathbb{C}$ that is supported in $F \times k^n$ and invariant under $G_Z$ on test functions kills the test functions supported in $\{v \neq 0\}$.

For a monic $\chi \in k[X]$, a finite family of sets $F_1, \dots, F_m$ is a *family of pieces for $\chi$* if each $F_i$ is closed, contained in $B_Z$ and stable under conjugation by $G_Z$, if the $F_i$ are pairwise disjoint, and if every $x \in B_Z$ with characteristic polynomial $\chi$ lies in some $F_i$.

**Definition 7.3.1 (Size).** Let $e$ run over the primitive idempotents of $Z$. Put
$$\mu(Z) = \sum_e \frac{\dim_k (e B_Z)}{\dim_k (e Z)}.$$

Lean: `PositivityTheory.RgUd.TP.Desc.mu`.

Here $Z = \prod_e eZ$ is a product of fields, $e k^n$ is a vector space of some dimension $m_e$ over the field $eZ$, and $e B_Z$ is the matrix algebra $M_{m_e}(eZ)$. So each quotient is the integer $m_e^2$, and $\mu(Z) = \sum_e m_e^2$.

### The four general facts

The next four facts hold over every nonarchimedean local field.

**Proposition 7.3.2 (Localization off $Z_N$).** Let $Z$ be commutative and reduced. Assume that for each $\chi$ there is a family of pieces for $\chi$ in which each piece $F$ is null for $Z$, or has some $c \in Z$ with $x - c$ nilpotent for all $x \in F$. Let $\xi$ be supported in $B_Z \times k^n$ and invariant under $G_Z$. Then $\xi$ kills the test functions supported in every open set $U$ whose points $(x, v)$ have $v \neq 0$ and $x \notin Z_N \cap B_Z$.

Lean: `PositivityTheory.RgUd.TP.Final.locOff`.

**Proposition 7.3.3 (Gluing).** If for each $\chi$ there is a family of pieces for $\chi$ that are all null for $Z$, then $Z$ has the vanishing property $(\mathrm{V}_Z)$.

Lean: `PositivityTheory.RgUd.TP.Final.locAll`.

**Proposition 7.3.4 (Translation).** If $N_Z$ is null for $Z$, then so is every set $F \subseteq B_Z$ such that $x - c$ is nilpotent for all $x \in F$, for one $c \in Z$.

Lean: `PositivityTheory.RgUd.TP.Final.transl`.

**Theorem 7.3.5 (Nilpotent core).** Assume that for every commutative reduced $Z$ there is a linear form $\tau$ on $M_n(k)$ with $\tau(xy) = \tau(yx)$ for $x, y \in B_Z$, nondegenerate on $B_Z$ and zero on $N_Z$. Assume that $G_Z$ is unimodular for every such $Z$. Let $Z$ be commutative and reduced, and assume that every $\xi$ supported in $B_Z \times k^n$ and invariant under $G_Z$ kills the test functions on open sets of points with $v \neq 0$ and $x \notin Z_N \cap B_Z$. Then $N_Z$ is null for $Z$.

Lean: `PositivityTheory.RgUd.TP.Final.nilCore` (also `PositivityTheory.RgUd.TP.Nil.Final.nilCore`).

Both hypotheses hold: the trace form is the reduced trace of the product of matrix algebras $\prod_e M_{m_e}(eZ)$, and the unimodularity holds because conjugation by $G_Z$ on $B_Z$ has determinant $1$. The proof of the nilpotent core is the homogeneity argument of the previous section, with the Fourier transform on $B_Z$ defined by $\tau$, the homogeneity degree $\dim B_Z$, and the dilations $x \mapsto t x$.

### The descent

**Theorem 7.3.6 (Descent).** Let $k$ have characteristic $p$, and assume that $G_Z$ is unimodular for every commutative reduced $Z$. Then for every commutative reduced $Z$ and every monic $\chi$ there is a family of pieces $F_1, \dots, F_m$ for $\chi$ such that each $F_i$ satisfies one of the following.

1. There is $c \in Z$ with $x - c$ nilpotent for all $x \in F_i$.
2. If $(\mathrm{V}_{Z'})$ holds for every commutative reduced $Z'$ with $\mu(Z') < \mu(Z)$, then $F_i$ is null for $Z$.

Lean: `PositivityTheory.RgUd.TP.Final.desc` (also `PositivityTheory.RgUd.TP.Desc.Final.desc`).

The proof has two parts. The first is a reduction. Call a piece *good* if it satisfies 1, or if there is a commutative reduced $S$, in a matrix algebra of any size, with $\mu(S) < \mu(Z)$ and such that $(\mathrm{V}_S)$ implies that the piece is null for $Z$. Let $q$ be a power of $p$. By an extension of scalars and a restriction back to $k$, $Z$ is replaced by an algebra $Z'$ with $\mu(Z') = \mu(Z)$ that contains a $q$-th root of every scalar and such that $y^q = 0$ for every nilpotent $y \in B_{Z'}$. A family of good pieces for $Z'$ and finitely many polynomials then gives a family of good pieces for $Z$ and $\chi$.

The second part treats such a $Z'$.

**Theorem 7.3.7 (Good pieces).** Let $k$ have characteristic $p$ and assume the unimodularity of all $G_Z$. Let $Z$ be commutative and reduced, $q$ a power of $p$, every scalar a $q$-th power in $Z$, and $y^q = 0$ for every nilpotent $y \in B_Z$. Then for every monic $\chi$ there is a family of good pieces for $\chi$.

Lean: `PositivityTheory.RgUd.TP.Desc.Piece.Final.pieceGood`.

*Proof.* Let $\chi$ have degree $n$. Under the hypotheses on $q$, the Jordan decomposition is given by polynomials. There are elements $a_{jl}, b_l \in Z$ such that for every $x \in B_Z$ with $\chi(x) = 0$ the elements $s_j(x) = \sum_l a_{jl} x^l$ span a commutative reduced algebra $S(x)$, the element $\varepsilon(x) = \sum_l b_l x^l$ commutes with them and has $\varepsilon(x)^q = 0$, and $x$ is a fixed linear combination of the products $s_j(x) \varepsilon(x)^l$. Fixed linear combinations $\kappa_t(x)$ of the $s_j(x)$ are the primitive idempotents of $S(x)$. The *type* of $x$ is the vector of ranks of the $\kappa_t(x)$. For each type $\tau$, let
$$P_\tau = \{ x \in B_Z : \chi(x) = 0,\ \text{the type of } x \text{ is } \tau \}.$$
Every $x$ with characteristic polynomial $\chi$ has $\chi(x) = 0$ by the theorem of Cayley and Hamilton, so the $P_\tau$ form a family of pieces for $\chi$. Each $P_\tau$ is closed and stable under $G_Z$, and $S(x)$ is commutative and reduced for $x \in P_\tau$. Fix $x_0 \in P_\tau$. Then $\mu(S(x_0)) < \mu(Z)$, or $x_0 - c$ is nilpotent for some $c \in Z$. In the second case all of $P_\tau$ has this form. In the first case, the transfer theorem below shows that $(\mathrm{V}_{S(x_0)})$ implies that $P_\tau$ is null for $Z$. $\square$

**Theorem 7.3.8 (Transfer).** Assume [Frobenius reciprocity](/entry/frobenius-reciprocity/) and the unimodularity of all $G_Z$, and let $k$ have characteristic $p$. Let $P_\tau$ be a piece as above and $x_0 \in P_\tau$. If $(\mathrm{V}_{S(x_0)})$ holds, then $P_\tau$ is null for $Z$.

Lean: `PositivityTheory.RgUd.TP.Desc.Piece.PTr.transfer` (also `PositivityTheory.RgUd.TP.Desc.Piece.TrI.transfer_of`).

*Proof.* The map $x \mapsto (s_j(x))_j$ is an algebra map from a fixed reduced commutative algebra $A$ into $B_Z$. Two such maps with the same ranks on the primitive idempotents of $A$ are conjugate, so $P_\tau$ maps onto one $G_Z$-orbit $G_Z / H$, where $H$ is the centralizer of $S(x_0)$ in $G_Z$. This orbit is closed. Its points are the images of the fixed tuple under conjugation, and the orbit of a tuple of commuting semisimple elements is closed. So $P_\tau \times k^n$ is fibred over $G_Z / H$, with fibre over the base point the set of $x \in P_\tau$ with $S(x) = S(x_0)$. Frobenius reciprocity is used twice, once for $G_Z / H$ and once for the corresponding orbit of the centralizer of $S(x_0)$ in $\mathrm{GL}_n(k)$. It turns an invariant functional on $P_\tau \times k^n$ into an $H$-invariant functional on the fibre, with the same support in $\{v = 0\}$. The fibre lies in $B_{S(x_0)} \times k^n$, and $H = G_{S(x_0)}$. So $(\mathrm{V}_{S(x_0)})$ gives the vanishing on the fibre, and the support property of Frobenius reciprocity carries it back to $P_\tau$. $\square$

### The induction

**Theorem 7.3.9 (Theorem T in characteristic $p$).** Let $k$ have characteristic $p$. Then every commutative reduced subalgebra $Z \subseteq M_n(k)$ has the vanishing property $(\mathrm{V}_Z)$.

Lean: `PositivityTheory.RgUd.TP.Final.thmT`.

*Proof.* Use strong induction on $\mu(Z)$. Let $Z$ be commutative and reduced, and assume $(\mathrm{V}_{Z'})$ for all commutative reduced $Z'$ with $\mu(Z') < \mu(Z)$. For each $\chi$, the descent theorem with the induction hypothesis gives a family of pieces for $\chi$, each null for $Z$ or of the form $c + {}$nilpotent. Localization off $Z_N$ then applies. The nilpotent core shows that $N_Z$ is null for $Z$, and translation shows that every piece of the form $c + {}$nilpotent is null for $Z$. So every piece is null, and gluing gives $(\mathrm{V}_Z)$. $\square$

**Remark 7.3.10 (Formalization).** The induction is in [TraceFormAlt.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceFormAlt.lean#L29), and the statements of the four general facts are in [TraceForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceForm.lean). In the proof of the final theorem, a bound variable of a nested function has the same name as the prime $p$ ([TraceFormAlt.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/TraceFormAlt.lean#L42)). The descent theorem is proved in a module named for its imports ([Imports.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/Imports.lean#L11)). The size $\mu$ uses division of natural numbers, which is exact here ([PieceGood.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/PieceGood.lean#L19)). The pieces are cut out by the condition $\chi(x) = 0$, not by the characteristic polynomial ([PieceTop.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/ClosedOrbitPieces/PieceTop.lean#L66)), and the transfer theorem takes Frobenius reciprocity as a hypothesis. The proof of the transfer raises the elaboration limit to one million ([TransferOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/FiniteDimensionalDescent/ClosedOrbitPieces/TransferOf.lean#L23)). The group $G_Z$ as a subgroup of $\mathrm{GL}_n(k)$ is defined twice, in [IsClosedGzS.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/Descent/SliceVanishing/IsClosedGzS.lean#L17) and in [ZNClosed.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CompactOrbits/NilpotentOrbits/OrbitIntegrals/ZNClosed.lean#L13). The nilpotent core in characteristic $p$ also takes its element $t$ with $0 < |t| < 1$ from the lemma with an étale name ([ContinuousHom.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TwistedPieces/IntegralParts/BezoutHypotheses/ContinuousHom.lean#L145)).
