---
title: Independence of the sections
decls:
  - GlobalTheory.KaIndep.valAt_generic
  - GlobalTheory.KaIndep.kaVal_independent
  - GlobalTheory.T.keyInvariant_independent_of_sections
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Independence of the sections

This section proves that the key value of a key input over an algebraically closed field of characteristic $0$ does not depend on the sections. All key values of all tuples of sections, over all algebraically closed fields that receive the key input, are the images of one unit $\kappa$ of the base field. This unit is the *key invariant* of the key input, and it is the value that [the key invariant theorem](/entry/ka-st/) assigns to a principally polarized abelian variety. The previous section treated pairs of generic tuples. Here an abstract argument removes the word "generic": a value defined at generic coordinates, stable under base change and liftable over discrete valuation rings, is a constant. The background is in [fields and extensions](/learn/algebra/#fields-and-extensions) and in [discrete valuation rings and lattices](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices).

Throughout, $K$ is an algebraically closed field of characteristic $0$, $x$ is a key input over $K$ of dimension $g$ with line bundle $L$, and $(n, l, l', \alpha)$ is admissible for $g$. We assume the laws. By the basis theorem for powers of $L$, the space $\Gamma(A, L^n)$ has a basis $b_1, \dots, b_N$ with $N = n^g$, and for every ring map $f : K \to R$ and every pullback $x'$ of $x$ along $f$, the pullbacks $b'_k$ of the $b_k$ are a basis of the sections of $L'^n$. Let $I = \{1, \dots, g\} \times \{1, \dots, N\}$. A family $T \in R^I$ is a tuple of coordinates for $g$ sections.

**Definition 2.8.1 (Framed sections and values at coordinates).** Let $R$ be a $K$-algebra and let $T \in R^I$. A key input $x'$ over $R$ with sections $s_1, \dots, s_g$ of $L'^n$ is *framed by* $T$ if $x'$ is a pullback of $x$ along $K \to R$ and, for the pulled back basis $b'$, each $s_i$ has coordinates $T(i, \cdot)$ in $b'$. An element $a \in R$ is a *value at* $T$ if there are a key input $x'$ and sections $s$ framed by $T$ and a key value $\kappa \in R^\times$ of $s$ with $a = \kappa$. We write $V(R, T, a)$ for this relation.

Lean: `GlobalTheory.KaIndep.Framed`, `GlobalTheory.KaIndep.ValAt`.

Framings exist for every $T$, since a key input has a pullback along every ring map and the sections with given coordinates in a basis exist. Two framings are related by pullback: if $(x', s)$ is framed by $T$ over $R$ and $(x'', s'')$ is framed by $j \circ T$ over $R'$, for a $K$-algebra map $j : R \to R'$, then $x''$ is a pullback of $x'$ along $j$ and each $s''_i$ is the pullback of $s_i$. This holds because a pullback of $x$ along $j \circ f$ is a pullback along $j$ of any pullback of $x$ along $f$, and pullback of sections is linear.

The abstract argument works in the algebraic closure $\overline{K(X)}$ of the field of rational functions in variables $X_i$, $i \in I$. We call $X$ the *generic point* of $\overline{K(X)}$.

**Lemma 2.8.2 (Fixed elements).** Let $\Omega$ be an algebraically closed field that contains the algebraically closed field $K$. If $a \in \Omega$ satisfies $\sigma(a) = a$ for every $K$-algebra endomorphism $\sigma$ of $\Omega$, then $a \in K$.

Lean: `GlobalTheory.GenericValue.mem_range_of_fixed`.

*Proof.* Assume $a \notin K$. Since $K$ is algebraically closed, $a$ is transcendental over $K$. Extend $\{a\}$ to a transcendence basis $B$ of $\Omega$ over $K$. The family $(\beta + 1)_{\beta \in B}$ is again algebraically independent over $K$, so the $K$-algebra map $K[B] \to \Omega$ with $\beta \mapsto \beta + 1$ extends to the fraction field $K(B)$. Since $\Omega$ is algebraic over $K(B)$ and algebraically closed, it extends further to an endomorphism $\sigma$ of $\Omega$. Then $\sigma(a) = a + 1 \neq a$, a contradiction. $\square$

**Lemma 2.8.3 (Generic values).** Let $K$ be an algebraically closed field, let $I$ be a set, and let $V(R, T, a)$ be a relation between a $K$-algebra $R$, a family $T \in R^I$ and an element $a \in R$. Assume:

1. *Base change.* If $j : R \to R'$ is a $K$-algebra map of local rings with $R$ noetherian and $V(R, T, a)$ holds, then $V(R', j \circ T, j(a))$ holds.
2. *Uniqueness.* If $F$ is a field and $V(F, T, a)$ and $V(F, T, a')$ hold, then $a = a'$.
3. *Existence.* If $\Omega$ is an algebraically closed field and $T \in \Omega^I$ is algebraically independent over $K$, then $V(\Omega, T, a)$ holds for some $a$.
4. *Generic pairs.* If $\Omega$ is algebraically closed, the joint family $(T, T')$ is algebraically independent over $K$, and $V(\Omega, T, a)$ and $V(\Omega, T', a')$ hold, then $a = a'$.
5. *Lifting.* If $O$ is a discrete valuation ring, $r : O \to \Omega$ is a $K$-algebra map to an algebraically closed field with kernel the maximal ideal, $T \in O^I$ and $V(\Omega, r \circ T, a)$ holds, then there are a discrete valuation ring $O'$, an injective $K$-algebra map $j : O \to O'$, a map $r' : O' \to \Omega$ with $r' \circ j = r$, and $u \in O'$ with $V(O', j \circ T, u)$.

Then there is $\kappa \in K$ such that $a = \kappa$ whenever $V(F, T, a)$ holds over a field $F$, and $V(\overline{K(X)}, X, \kappa)$ holds at the generic point.

Lean: `GlobalTheory.GenericValue.exists_value`.

*Proof.* First, values at two independent families agree, even when the families are not jointly independent. Let $\Omega$ be algebraically closed and let $T, T' \in \Omega^I$ be each algebraically independent over $K$, with values $a$ and $a'$. Let $\Omega_1 = \overline{\Omega(X)}$ and $j : \Omega \to \Omega_1$ the inclusion. The generic point $X$ is algebraically independent over $\Omega$, hence over $K$, so by existence there is $c$ with $V(\Omega_1, X, c)$. For a family $S \in \Omega^I$ that is independent over $K$ with a value $e$, the joint family $(j \circ S, X)$ is independent over $K$, and base change gives $V(\Omega_1, j \circ S, j(e))$. By generic pairs $j(e) = c$. Applied to $T$ and $T'$ this gives $j(a) = c = j(a')$, so $a = a'$.

Second, let $G = \overline{K(X)}$ and take $a_1$ with $V(G, X, a_1)$, by existence. Every $K$-algebra endomorphism $\sigma$ of $G$ is injective, so $\sigma \circ X$ is independent, and base change gives $V(G, \sigma \circ X, \sigma(a_1))$. By the first step $\sigma(a_1) = a_1$. By the lemma on fixed elements $a_1 = \kappa$ for some $\kappa \in K$. This gives the second claim.

Third, let $F$ be a field and $V(F, T, a)$. Let $\Omega = \overline{F(X)}$ with the inclusion $e : F \to \Omega$, let $O = \Omega[[t]]$, let $r : O \to \Omega$ be the constant term, and put
$$S_i = T_i + (X_i - T_i)\, t \in O.$$
Then $r \circ S = e \circ T$. The family $S$ is algebraically independent over $K$: a polynomial relation among the $S_i$ would give, after the substitution $t = 1$ in $\Omega[t]$, a relation among the $X_i$. Base change along $e$ gives $V(\Omega, r \circ S, e(a))$. Lifting gives $O'$, $j$, $r'$ and $u$ with $V(O', j \circ S, u)$, and base change along $r'$ gives $V(\Omega, r \circ S, r'(u))$. By uniqueness $e(a) = r'(u)$.

It remains to show $u = \kappa$. Let $i : O' \to \Omega'$ be the inclusion into an algebraic closure of the fraction field of $O'$. The family $i \circ j \circ S$ is independent over $K$, since $i$ and $j$ are injective. As $G$ is algebraic over $K(X)$ and $\Omega'$ is algebraically closed, there is a $K$-algebra map $m : G \to \Omega'$ with $m \circ X = i \circ j \circ S$. Base change along $m$ gives $V(\Omega', i \circ j \circ S, \kappa)$, and base change along $i$ gives $V(\Omega', i \circ j \circ S, i(u))$. By uniqueness $i(u) = \kappa$, so $u = \kappa$ in $O'$. Then $e(a) = r'(\kappa) = \kappa$, and $a = \kappa$ since $e$ is injective. $\square$

The third step is where special sections enter. The line $S$ over $\Omega[[t]]$ joins the special coordinates $T$ to the generic coordinates $X$, and lifting carries the value at $t = 0$ to the disc.

**Lemma 2.8.4 (Properties of values).** The relation $V$ of framed key values satisfies base change, uniqueness, existence and lifting, as in the lemma on generic values, for $K$-algebras $R$.

Lean: `GlobalTheory.KaIndep.valAt_map`, `GlobalTheory.KaIndep.valAt_unique`, `GlobalTheory.KaIndep.exists_valAt`, `GlobalTheory.KaIndep.valAt_lift`.

*Proof.* Base change: let $(x', s)$ be framed by $T$ over $R$ with key value $\kappa$, and choose a framing $(x'', s'')$ of $j \circ T$ over $R'$. By the relation between framings, $x''$ is a pullback of $x'$ along $j$ and $s''$ is the pullback of $s$. The base change property of key values over the local noetherian ring $R$ shows that $j(\kappa)$ is a key value of $s''$.

Uniqueness: two framings $(x_1, s_1)$ and $(x_2, s_2)$ of the same $T$ over a field $F$ are related by pullback along the identity of $F$. Base change moves a key value of $s_1$ to a key value of $s_2$. The field $F$ has characteristic $0$, since it receives $K$, and the uniqueness of key values over such fields gives the claim.

Existence: let $(x', s)$ be a framing of $T$ over $\Omega$. Since $T$ is algebraically independent over $K$ and $n \geq 4$, the generic sections $s$ meet transversally: there are transversal zeros $z_1, \dots, z_d$ of $s$ with charts. Then a key value exists, since $\prod_j (l - jn)(l' - jn) \neq 0$ in $\Omega$.

Lifting: let $(x_\Omega, s_\Omega)$ be framed by $r \circ T$ with key value $\kappa$, and let $(x_O, s_O)$ be framed by $T$ over $O$. Then $x_\Omega$ is a pullback of $x_O$ along $r$, and $s_\Omega$ is the pullback of $s_O$. The key value $\kappa$ comes with transversal zeros of $s_\Omega$. The product $\prod_j (l - jn)(l' - jn)$ is a nonzero element of $K$, hence a unit of $O$. The existence of a key value after an extension of the discrete valuation ring gives $O'$, an injective local map $j : O \to O'$ with $r' \circ j = r$, a pullback $x'$ of $x_O$ along $j$ with pulled back sections $s'$, and a key value $u \in O'^\times$ of $s'$. A framing $(x'', s'')$ of $j \circ T$ over $O'$ is a pullback of $x_O$ along $j$ as well, so $x''$ is a pullback of $x'$ along the identity of $O'$, with $s''$ pulled back from $s'$. Base change gives that $u$ is a key value of $s''$. $\square$

**Proposition 2.8.5 (Values at generic pairs).** Let $\Omega$ be an algebraically closed field that contains $K$, let $T, T' \in \Omega^I$ be such that the joint family $(T, T')$ is algebraically independent over $K$, and let $a$ and $a'$ be values at $T$ and $T'$. Then $a = a'$.

Lean: `GlobalTheory.KaIndep.valAt_generic`.

*Proof.* Let $(x_1, s_1)$ be framed by $T$ with key value $\kappa_1 = a$, and $(x_2, s_2)$ framed by $T'$ with key value $\kappa_2 = a'$. Let $b'$ be the pulled back basis on $x_1$, and let $s_3$ be the sections of $x_1$ with coordinates $T'(i, \cdot)$ in $b'$. Then $(x_1, s_3)$ is also framed by $T'$, so $x_1$ is a pullback of $x_2$ along the identity with $s_3$ pulled back from $s_2$, and base change shows that $\kappa_2$ is a key value of $s_3$. Now $s_1$ and $s_3$ are tuples on the same key input $x_1$, a pullback of $x$, with coordinates $T$ and $T'$ in the pulled back basis of $b$, and $(T, T')$ is independent over $K$. By [the theorem on generic tuples](/entry/key-invariant-eq-of-independent-generic-tuples/), $\kappa_1 = \kappa_2$. $\square$

**Theorem 2.8.6 (Independence of the sections).** Assume the laws. Let $K$ be an algebraically closed field of characteristic $0$, let $x$ be a key input over $K$ of dimension $g$, and let $(n, l, l', \alpha)$ be admissible for $g$. Then there is a unit $\kappa \in K^\times$ with the following two properties.

1. For every algebraically closed field $K'$, every ring map $f : K \to K'$, every pullback $x'$ of $x$ along $f$, every tuple $s'$ of $g$ sections of $L'^n$ and every key value $\kappa'$ of $s'$, we have $\kappa' = f(\kappa)$.
2. There are an algebraically closed field $K'$, a ring map $f : K \to K'$, a pullback $x'$ of $x$ along $f$ and sections $s'$ of $L'^n$ that have a key value.

Lean: `GlobalTheory.KaIndep.kaVal_independent` (also `GlobalTheory.T.keyInvariant_independent_of_sections`, a second name).

*Proof.* Fix the basis $b$ of $\Gamma(A, L^n)$ as above; it exists since $n \geq 4 \geq 1$. By the lemma on properties of values and the proposition on generic pairs, the relation $V$ satisfies the five hypotheses of the lemma on generic values. That lemma gives $\kappa_0 \in K$ such that every value over a field is $\kappa_0$, and such that $\kappa_0$ is a value at the generic point $X$ of $G = \overline{K(X)}$. The last statement gives a framing $(x_G, s_G)$ of $X$ and a key value $\kappa_G$ of $s_G$ with $\kappa_G = \kappa_0$ in $G$. Since $\kappa_G$ is a unit, $\kappa_0 \neq 0$. Let $\kappa = \kappa_0 \in K^\times$.

For the first property, make $K'$ a $K$-algebra through $f$. The pulled back basis $b'$ is a basis of the sections of $L'^n$, so each $s'_i$ has coordinates $c(i, \cdot)$ in $b'$, for some $c \in K'^I$. Then $(x', s')$ is framed by $c$, and $\kappa'$ is a value at $c$. Hence $\kappa' = f(\kappa_0)$. For the second property take $K' = G$, $f$ the inclusion, $x' = x_G$ and $s' = s_G$. $\square$

**Remark 2.8.7.** A tuple of sections over $K$ itself need not have a key value, since this needs $d = g!\, n^g$ transversal zeros; so $\kappa$ is reached through extensions of $K$. Both properties are used in [the key invariant theorem](/entry/ka-st/). With $K' = K$ and $f$ the identity, the first property identifies $\kappa$ with every key value that can be computed on $x$ itself, for instance a key value over $\mathbb{C}$ given by theta functions. The second property gives a witness over a larger field, and the first property for that witness is what makes $\kappa$ compatible with changes of $\theta$ and with extensions of the base field.

**Remark 2.8.8 (Formalization).** The proof is in [KeyInvariantIndependentOfSections.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/KeyInvariantIndependentOfSections.lean#L232), and the lemma on generic values is in [ExistsAlgHomOfIsTranscendenceBasis.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsAlgHomOfIsTranscendenceBasis.lean#L101), with the deformation $S$ in `exists_generization` (line 74). The basis theorem is `KeyBasis.main`, the relation between framings is `Framed.via` (line 88), built on `KaLift.keyVia_cancel`, and the facts used for the properties of values are `T.keyInvariant_baseChange`, `T.keyInvariantFromIntersection_unique`, `T.generic_sections_meet_transversally`, `T.exists_keyInvariant_algClosed_transversal` and `T.exists_keyInvariant_after_dvr_extension`; we used their statements. The field $K'$ there carries no characteristic assumption; it has characteristic $0$ because it receives $K$. The lemmas `exists_coords` (line 31) and `degProd_ne_zero` (line 54) have copies in KeyInvariantEqOfIndependentGenericTuples.lean. The second name is proved by a `first | exact … | …` block, under a raised heartbeat limit ([KeyInvariantIndependentOfSectionsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/KeyInvariantIndependentOfSectionsStatement.lean#L18)).
