---
title: Künneth by Mayer-Vietoris
decls:
  - GlobalTheory.T.pairing_restriction_natural
  - GlobalTheory.CompanionTheory.KunGlue.kun_glue
  - GlobalTheory.T.cosieve_pairing_family_compat
  - GlobalTheory.CompanionTheory.KunGlue.glue_gen
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Künneth by Mayer-Vietoris

A Künneth formula on a space that is covered by finitely many opens can be proved from the Künneth formula on the opens and on their intersections. This is the Mayer-Vietoris argument. This section proves it in two forms. The first form is pure homological algebra: it is about systems of complexes indexed by the subsets of a finite set, and a pairing with a fixed family of complexes. The second form applies the first to cochain complexes of functors on the full subcategories that a family of cosieves cuts out of a category. The [next section](/entry/kuenneth-product-proper-smooth/) applies the second form to the thickening site of a product of schemes.

Let $K$ be a field. A *complex* is a sequence of $K$-vector spaces $C^0, C^1, \dots$ with linear maps $d : C^n \to C^{n+1}$ and $d \circ d = 0$. We write $H^n(C)$ for its cohomology and $[x] \in H^n(C)$ for the class of a cocycle $x$.

**Definition 1.7.1 (Pairing of complexes).** Let $P$, $Q$ and $T$ be complexes. A *pairing* $\mu : P \times Q \to T$ is a family of bilinear maps $\mu : P^i \times Q^j \to T^{i+j}$ with
$$d \mu(x, y) = \mu(dx, y) + (-1)^i \mu(x, dy) \qquad (x \in P^i).$$

By the Leibniz rule, $\mu$ takes two cocycles to a cocycle and a cocycle and a coboundary to a coboundary. So $\mu$ induces a map $H^i(P) \otimes H^j(Q) \to H^{i+j}(T)$.

**Definition 1.7.2 (Künneth property).** Let $(P_a)$, $(Q_a)$ and $(T_c)$, for $a, c \geq 0$, be families of complexes, with pairings $\mu : P_a \times Q_{a'} \to T_{a + a'}$. The family has the *Künneth property* if for all $c, n \geq 0$ there is an isomorphism
$$\bigoplus_{a + a' = c} \; \bigoplus_{i + j = n} H^i(P_a) \otimes_K H^j(Q_{a'}) \xrightarrow{\ \sim\ } H^n(T_c)$$
that sends $[x] \otimes [y]$ to $[\mu(x, y)]$ for all cocycles $x$ and $y$.

The index $a$ is the weight, as in the Hodge degree of $\Omega^a$. The index $i$ is the cohomological degree.

**Definition 1.7.3 (Systems and descent).** Let $\iota$ be a finite set. A *system of complexes* over $\iota$ is a complex $A(S)$ for each subset $S \subseteq \iota$, with maps of complexes $A(S) \to A(S')$ for $S \subseteq S'$ that compose correctly and are the identity for $S = S'$. Fix a degree $n$. The *Čech complex* of the system in degree $n$ has in degree $m$ the product of the spaces $A(\{s_0, \dots, s_m\})^n$ over all tuples $(s_0, \dots, s_m)$ in $\iota$, with the alternating sum of restrictions as its differential. The system has *descent* if for every $n$ the augmented Čech complex
$$0 \to A(\emptyset)^n \to \prod_{s_0} A(\{s_0\})^n \to \prod_{s_0, s_1} A(\{s_0, s_1\})^n \to \cdots$$
is exact.

Think of $A(S)$ as the cochains on the intersection $U_S$ of the opens $U_s$, $s \in S$, and of $A(\emptyset)$ as the cochains on the union. Descent says that cochains on the union are the same as compatible families of cochains on the opens.

**Definition 1.7.4 (Mayer-Vietoris principle).** The *Mayer-Vietoris principle* is the statement: let $A \to B$ be a map of systems of complexes over a finite set $\iota$, with values in modules over a commutative ring, and assume that $A$ and $B$ have descent. If $H^n(A(S)) \to H^n(B(S))$ is bijective for all nonempty $S$ and all $n$, then it is bijective for $S = \emptyset$ and all $n$.

Lean: `CrystallineSemistableComparison.Onto.MVBij` (a proposition, used as a hypothesis).

Classically this is proved by the spectral sequence of the double complex formed by the Čech complex, or by induction on the number of opens with the long exact Mayer-Vietoris sequence and the five lemma.

**Theorem 1.7.5 (Künneth glues).** Assume the Mayer-Vietoris principle. Let $\iota$ be a finite set and $(P_a)$ a family of complexes over $K$. Let $(Q_a)$ and $(T_c)$ be families of systems of complexes over $\iota$, all with descent. For each $S \subseteq \iota$ let $\mu_S : P_a \times Q_{a'}(S) \to T_{a+a'}(S)$ be pairings, compatible with restriction:
$$\operatorname{res}_{S \subseteq S'} \mu_S(x, y) = \mu_{S'}(x, \operatorname{res}_{S \subseteq S'} y).$$
If the families $(P_a)$, $(Q_a(S))$, $(T_c(S))$ have the Künneth property for every nonempty $S$, then they have it for $S = \emptyset$.

Lean: `GlobalTheory.T.pairing_restriction_natural` (also `GlobalTheory.CompanionTheory.KunGlue.kun_glue`, the same statement).

The proof first turns the Künneth property into a statement that has the form of the Mayer-Vietoris principle. The trick is to fix a basis of the cohomology of the fixed factor. Then the tensor product with $H^i(P_a)$ becomes a direct sum of copies of the cohomology of $Q$, one for each basis vector.

**Lemma 1.7.6 (Künneth as a sum of shifted maps).** Fix $c$. For each $a$ and $i$ choose a basis $(\beta)$ of $H^i(P_a)$ and a cocycle $z_\beta$ in the class $\beta$. Let $u$ run over the tuples $(a, a', i, \beta)$ with $a + a' = c$, and put
$$g_u : Q_{a'}(S)^m \to T_c(S)^{m + i}, \qquad g_u(y) = \mu_S(z_\beta, y).$$
For fixed $S$ and $n$, the Künneth isomorphism for $c$ and $n$ exists if and only if there is an isomorphism
$$\bigoplus_{u} \; \bigoplus_{m + i = n} H^m\bigl(Q_{a'}(S)\bigr) \xrightarrow{\ \sim\ } H^n\bigl(T_c(S)\bigr)$$
that sends $[y]$ in the summand of $(u, m)$ to $[g_u(y)]$.

Lean: `GlobalTheory.CompanionTheory.KunGlue.Glue.kun_iff_mv`.

*Proof.* The basis gives an isomorphism of $\bigoplus_{t} H^i(P_a) \otimes H^j(Q_{a'})$ with $\bigoplus_{t, \beta} H^j(Q_{a'})$, where $t$ runs over the tuples $(a, i, a', j)$ with $a + a' = c$ and $i + j = n$. It sends $\beta \otimes [y]$ to $[y]$ in the summand of $(t, \beta)$. After a change of index set from $(t, \beta)$ to $(u, m)$, compose with the given isomorphism. In one direction, $\beta \otimes [y]$ goes to $[\mu(z_\beta, y)] = [g_u(y)]$. In the other direction, both $[x] \otimes [y] \mapsto [\mu(x, y)]$ and the composite map are linear in $[x]$ and agree on the basis, so they agree everywhere. $\square$

**Lemma 1.7.7 (Gluing sums of shifted maps).** Assume the Mayer-Vietoris principle. Let $\iota$ be finite, $I$ a set, $k : I \to \mathbb{N}$ and $\varsigma : I \to \{\pm 1\}$. Let $A_u$, for $u \in I$, and $T$ be systems of complexes over $\iota$ with descent, and let
$$g_u(S) : A_u(S)^m \to T(S)^{m + k(u)}$$
be linear maps with $d \, g_u(S) = \varsigma(u) \, g_u(S) \, d$ that commute with restriction. If for every nonempty $S$ and every $n$ the map $\bigoplus_{u} \bigoplus_{m + k(u) = n} H^m(A_u(S)) \to H^n(T(S))$, $[x] \mapsto [g_u(S)(x)]$, is an isomorphism, then the same holds for $S = \emptyset$.

Lean: `GlobalTheory.T.mvE_empty_of_mvE_nonempty`.

We have read the statement of this lemma, not its proof. Our reading: the maps $g_u$ assemble to a map of systems from the direct sum of the systems $A_u$ shifted by $k(u)$, with the sign $\varsigma(u)$ in the differential, to $T$. A direct sum of systems with descent has descent. Then the Mayer-Vietoris principle applies.

*Proof of the theorem.* Fix $c$. Choose bases and representing cocycles as in the first lemma, and define the maps $g_u$.

1. *Signs.* For $y \in Q_{a'}(S)^m$, the Leibniz rule and $dz_\beta = 0$ give $d g_u(y) = (-1)^i g_u(dy)$. So the maps $g_u$ satisfy the condition of the second lemma with $k(u) = i$ and $\varsigma(u) = (-1)^i$.
2. *Restriction.* The maps $g_u$ commute with restriction, by the compatibility of the pairings $\mu_S$ applied to $x = z_\beta$.
3. *Nonempty $S$.* By the first lemma, the Künneth property for nonempty $S$ gives the isomorphisms that the second lemma asks for.
4. *Gluing.* The systems $Q_{a'}$ and $T_c$ have descent. The second lemma gives the isomorphism for $S = \emptyset$.
5. *Back to Künneth.* The first lemma for $S = \emptyset$ turns this isomorphism into the Künneth isomorphism. $\square$

**Remark 1.7.8.** The basis is chosen once, from the axiom of choice, for each space $H^i(P_a)$. The index set $I$ of the second lemma is then as large as these bases, and no finiteness condition on $H^i(P_a)$ is needed. The base ring must be a field so that a basis exists. The fixed factor $P_a$ does not depend on $S$; the variable factor is the second one. In the application the roles of the two factors are swapped by a sign $(-1)^{ij}$, so that the factor that varies over the cover sits in the second place.

We now apply the theorem to cochains on categories. Let $\mathcal{C}$ be a category and $F$ a functor from $\mathcal{C}$ to $K$-vector spaces. For a full subcategory $U$, the *cochain complex* $C^\bullet(U, F)$ has as $n$-cochains the functions that send each chain $T_0 \to T_1 \to \dots \to T_n$ of maps in $U$ to an element of $F(T_n)$. The differential is the alternating sum of the face maps, where the face that drops $T_{n+1}$ is followed by the map $F(T_n) \to F(T_{n+1})$. A *cosieve* is a full subcategory $U$ such that $T \in U$ and $T \to T'$ imply $T' \in U$.

**Definition 1.7.9 (Families of cosieves).** Let $(V_s)_{s \in \iota}$ be cosieves of $\mathcal{C}$, with $\iota$ finite. For $S \subseteq \iota$ let $V_S$ be the full subcategory of the objects that lie in some $V_s$ and in all $V_s$ with $s \in S$. So $V_S = \bigcap_{s \in S} V_s$ for $S$ nonempty, and $V_\emptyset = \bigcup_s V_s$. *Covering descent* is the statement that the system $S \mapsto C^\bullet(V_S, F)$ has descent for all such families and all $F$.

Lean: `CrystallineSemistableComparison.Onto.CovDesc` (a proposition, used as a hypothesis).

**Theorem 1.7.10 (Künneth on a union of cosieves).** Assume the Mayer-Vietoris principle and covering descent. Let $\mathcal{C}$ and $\mathcal{D}$ be categories, $F_a$ functors on $\mathcal{C}$ and $E_c$ functors on $\mathcal{D}$, and $(P_a)$ complexes. Let $R$ be a relation between full subcategories of $\mathcal{C}$ and of $\mathcal{D}$. For each pair $U \mathrel{R} U'$ let
$$\mu_{U, U'} : P_a \times C^\bullet(U, F_{a'}) \to C^\bullet(U', E_{a + a'})$$
be pairings, compatible with restriction along $U_2 \subseteq U_1$ and $U'_2 \subseteq U'_1$. Let $(V_s)$ be cosieves of $\mathcal{C}$ and $(W_s)$ cosieves of $\mathcal{D}$, with $V_S \mathrel{R} W_S$ for all $S \subseteq \iota$. If the Künneth property holds for $(P_a)$, $C^\bullet(V_S, F_a)$, $C^\bullet(W_S, E_c)$ for all nonempty $S$, then it holds for $V_\emptyset$ and $W_\emptyset$.

Lean: `GlobalTheory.T.cosieve_pairing_family_compat` (also `GlobalTheory.CompanionTheory.KunGlue.glue_gen`, the same statement).

*Proof.* Let $Q_a(S) = C^\bullet(V_S, F_a)$ and $T_c(S) = C^\bullet(W_S, E_c)$, with restriction of cochains as the maps of the systems. Both systems have descent by covering descent. The pairings $\mu_{V_S, W_S}$ are compatible with restriction by hypothesis. The theorem on gluing Künneth gives the Künneth property for $S = \emptyset$. $\square$

**Remark 1.7.11.** In Lean the systems are built from relative cochain complexes: cochains on $U$ that vanish on chains whose first object lies in a given cosieve $Q$. The proof takes $Q$ empty. Then the relative complex is the full cochain complex, and the inclusion is bijective in each degree. A transfer lemma (Lean: `GlobalTheory.CompanionTheory.KunGlue.GlueGen.kun_iff`) moves the Künneth property across this bijection in both directions. The name `pairing_restriction_natural` describes the naturality hypothesis, not the conclusion, and the name `cosieve_pairing_family_compat` describes a hypothesis too. Both statements are proved by a single `first | exact` that cites the companion theorem ([PairingRestrictionNaturalStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PairingRestrictionNaturalStatement.lean#L10)).

**Remark 1.7.12.** The Mayer-Vietoris principle and covering descent enter only as hypotheses. The file that proves the gluing theorem turns the unused variable linter off ([PairingRestrictionNatural.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PairingRestrictionNatural.lean#L11)).

The method is the Mayer-Vietoris argument of R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Graduate Texts in Mathematics 82, Chapter I, §5, where it proves the Künneth formula for de Rham cohomology from a finite good cover. Here no good cover is needed: the cover is arbitrary, and the local Künneth formula on the intersections is a hypothesis.
