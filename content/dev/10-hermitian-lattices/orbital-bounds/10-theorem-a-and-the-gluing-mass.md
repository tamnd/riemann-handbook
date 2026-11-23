---
title: Theorem A and the gluing mass
decls:
  - Formalism.MainNotions.LatticeGluingRadicals.theorem_A_section
  - Formalism.MainNotions.LatticeGluingRadicals.lattice_theorem_A_from_degenerate
  - Formalism.MainNotions.BridgeLemma.word_theorem_a_admissible
  - Formalism.MainNotions.BridgeLemma₂.gluing_mass_of_lift_number_genus
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem A and the gluing mass

This section proves Theorem A for all words. Theorem A bounds the determinant of an intersection lattice of two flags, times two indices, by a power of $2/g$ and the square root of two Gram norms. It has a nondegenerate case and a degenerate case. The section then specializes Theorem A to a pair of words. It ends with a reduction of the mass of the row lattices of a flag to the mass of one lattice in a smaller space. Theorem A is used in the steps that need [nonempty hypotheses](/step/nonempty-hyps/). The mass reduction is used in the computation of the raw mass of the rows. For the background see [unitary groups](/learn/groups/#unitary-groups) and [number fields and their integers](/learn/number-fields/#number-fields-and-their-integers).

### The setting

Let $E$ be the CM field of the data, with ring of integers $\mathcal{O}_E$, and let $f$ and $k$ be the integers of the setting. Let $V$ be the Hermitian space of the data, with form $h$. Put $g = g_0 g_1$, the product of the two integers $g_0, g_1$ of the data. For a word $u$ let $T_u$ be its integer. Flags $F$ of norm $T$ have frame vectors, a vector $z$, and an isotropic span $X(F)$.

For a lattice $\Lambda$ and flags $F$ of norm $T_u$ and $F'$ of norm $T'$, we use the following objects:

1. The $\mathcal{O}_E$-span $U(F, F')$ of the vectors of the two flags.
2. The submodule $\Lambda(g; F, F')$, spanned by the vectors that are orthogonal to $U(F, F')$, lie in the lattices of both flags, and satisfy a gluing relation modulo $g$.
3. The index $i(F, F')$ of $\Lambda(g; F, F')$ relative to $\Lambda \cap U(F, F')^{\perp}$.
4. The Gram norm $G_0(F, F') = \det U(F, F') / N(g)^{r+1}$, where $\det$ is the lattice determinant, $N(g)$ is the norm of $g$ from $E$, and $r$ is the rank of the flags.

For a third flag $F''$ of norm $T'$ and a linear automorphism $\beta$ of $V$, put
$$b(x', x'') = h(x', x'') - h(\beta x', x'').$$
Let $\Theta$ be the space of first coordinates of the pairs $(x', x'')$ with $x' \in U(F, F')^\perp$, $x'' \in U(F, F'')^\perp$, $x' - x'' \in X(F)$ and $\beta x' - x'' \in X(F'')$. Let $\Theta''$ be the space of their second coordinates. Put $s_0 = k - \dim \Theta$ and $M = \Lambda(g; F, F') \cap \Theta$. The pair is *nondegenerate* if every $x' \in U(F, F')^\perp$ with $b(x', \cdot) = 0$ on $U(F, F'')^\perp$ lies in $\Theta$, and every $x''$ with $b(\cdot, x'') = 0$ lies in $\Theta''$. Let $R'$ and $R''$ be the left and right radicals of $b$ on these two spaces.

For an embedding $\tau \colon E \to \mathbb{C}$ there is a hyperbolic cosine $\operatorname{ch}_\tau(F, F')$ of the two flags, with $\operatorname{sh}_\tau = \sqrt{\operatorname{ch}_\tau^2 - 1}$. Put $\gamma_\tau(F, F') = (1 + \operatorname{ch}_\tau)/\operatorname{sh}_\tau$, and $\gamma_\tau(F, F') = 1$ when a certain determinant of the two flags is $0$.

The hypotheses on the data are the following.

1. *Fixed:* $\Lambda$ is a unimodular lattice, $F$ is a lift for $\Lambda$, and $F$ satisfies the fixed convention at $g$.
2. *Prime:* $T_u$ and $T'$ are primes, both at least $3$, that split completely in $E$. Every $g_i$ splits completely in $E$, and $g$ is prime to $T_u T'$. Also $T_u \equiv T' \pmod g$, and every root of unity $\zeta$ in $\mathcal{O}_E$ with $\zeta - 1 \in T_u \mathcal{O}_E$ is $1$.
3. *Terms:* $F'$ and $F''$ are lifts for $\Lambda$, both are admissible for $F$ modulo $g$, and both have a nonzero Gram value with $F$.
4. *Pair:* $\beta$ is an automorphism of $\Lambda$. It maps the flag of $F'$ to that of $F''$ and $z'$ to $z''$, and it is compatible with the gluing relation modulo $g$.

### Theorem A

**Theorem 4.10.1 (Theorem A).** Let $u$ be a word, let $T' \geq 1$, and let $\Lambda$, $F$, $F'$, $F''$ and $\beta$ satisfy the four hypotheses, with $s_0 \geq 2$. If the pair is nondegenerate, then
$$\det(M) \, i(F, F') \, i(F, F'') \leq \Big(\frac{2}{g}\Big)^{(s_0 - 1) f} \sqrt{G_0(F, F') \, G_0(F, F'')}.$$
If the pair is degenerate, then $\dim R' = \dim \Theta + 1$, $\dim R'' = \dim \Theta + 1$, and
$$\det(M) \, i(F, F') \, i(F, F'') \leq \Big(\frac{2}{g}\Big)^{(s_0 - 2) f} \sqrt{G_0(F, F') \, G_0(F, F'')} \; T_u^{-f} \Big( \prod_{\tau} \gamma_\tau(F, F') \, \gamma_\tau(F, F'') \Big)^{1/2},$$
where $\tau$ runs over the embeddings of $E$ into $\mathbb{C}$.

Lean: `Formalism.MainNotions.LatticeGluingRadicals.theorem_A_section` (also `Formalism.MainNotions.LatticeGluingRadicals.lattice_theorem_A_from_degenerate`).

*Proof.* The degenerate inequality, without the rank statements, is proved for all data in a separate theorem. The nondegenerate inequality is derived from the first lattice lemma and the second claim on radicals. A proved lemma then joins the two inequalities into the theorem. In the degenerate case it derives the two rank equalities from a rank computation for the radicals, which uses that $F'$ and $F''$ are lifts for $\Lambda$, that $V$ has the expected rank, and that a radical is positive definite. $\square$

**Corollary 4.10.2 (Theorem A for a pair of words).** Let $u$ and $u'$ be words. Then Theorem A holds for $u$ with $T' = T_{u'}$.

Lean: `Formalism.MainNotions.BridgeLemma.word_theorem_a_admissible`.

*Proof.* This is Theorem A applied with $T' = T_{u'}$. $\square$

**Remark 4.10.3.** In the degenerate case the exponent of $2/g$ drops from $(s_0 - 1) f$ to $(s_0 - 2) f$. Two new factors appear: $T_u^{-f}$ and the square root of the product of the $\gamma_\tau$.

### The gluing mass

Let $u$ be a word. Let $X_0$ be the first of the Hermitian spaces of the data. We use flags $F_0$ of norm $T_u$ whose frame is the fixed hyperbolic basis and whose vector $z$ is the vector of $u$. For such a flag a *row lattice* is a lattice $\Lambda$ of the given kind. Its part $L_0(\Lambda)$ is a lattice in $X_0$. For a finite set $s$ of representatives of the row lattices, $\operatorname{mass}_{\mathrm{rows}}(F_0, s)$ is the mass of the rows. For a lattice $L$ in $X_0$, $\operatorname{mass}(L)$ is its mass. Let $\operatorname{gen}(L)$ be the genus of $L$.

We use three hypotheses for $u$. Each is asked when $T_u$ is a prime, $T_u \geq 3$ and $T_u$ splits completely in $E$, for every flag $F_0$ as above.

1. *Lifts are conjugate:* if two row lattices $\Lambda_1$ and $\Lambda_2$ have the same sublattice for the flag, then there is $n$ in the stabilizer of $F_0$ with $n x - x \in X(F_0)$ for all $x \perp X(F_0)$ and $n \Lambda_1 = \Lambda_2$.
2. *Gluing number:* for every row lattice $\Lambda$ and every $M \in \operatorname{gen}(L_0(\Lambda))$, exactly $(T_u - 1)^f$ lattices obtained from row lattices with their vector $z$ meet the first summand in $M$.
3. *One genus:* for all row lattices $\Lambda$ and $\Lambda'$, $L_0(\Lambda') \in \operatorname{gen}(L_0(\Lambda))$.

**Theorem 4.10.4 (Mass of the rows by gluing).** Assume the three hypotheses for $u$. Let $T_u$ be a prime with $T_u \geq 3$ that splits completely in $E$. Let $F_0$ be a flag as above, and let $\Lambda$ be a row lattice. Then for every finite set $s$ of representatives of the row lattices,
$$\operatorname{mass}_{\mathrm{rows}}(F_0, s) = \operatorname{mass}\big(L_0(\Lambda)\big) \, (T_u - 1)^f.$$

Lean: `Formalism.MainNotions.BridgeLemma₂.gluing_mass_of_lift_number_genus`.

*Proof.* This is a reduction lemma applied to the three hypotheses and to two proved facts. The first fact is that the form on $X_0$ is positive definite. The second is that $L_0(\Lambda)$ is a lattice for every row lattice $\Lambda$. The reduction lemma gets the classes and the automorphism groups of the lattices from the first hypothesis. It gets a finite count from the second, because $(T_u - 1)^f \neq 0$. It uses the third to stay in the genus of $L_0(\Lambda)$. We did not unfold its proof. $\square$

So the mass of the rows is the mass of the lattice $L_0(\Lambda)$ in the smaller space $X_0$, times the gluing number.

**Remark 4.10.5 (Formalization).** Theorem A has two names. The first is equal to the second, and the second is the joining lemma applied to the degenerate inequality; see [LatticeGluingRadicals.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/LatticeGluingRadicals.lean#L9241). The proved degenerate statement asks only the inequality. The ranks of the radicals come from the joining lemma, see [LatticeGluingRadicals.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/LatticeGluingRadicals.lean#L7959) and [LatticeGluingRadicals.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/LatticeGluingRadicals.lean#L6739). The statement of Theorem A is in [CongruenceAtSplitFrobeniusHolds.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/CongruenceAtSplitFrobeniusHolds.lean#L88). The corollary leaves the second word to be inferred and uses only its integer $T_{u'}$; see [MinkowskiDividesFactorialOfBound.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/MinkowskiDividesFactorialOfBound.lean#L26). The gluing theorem is an implication. Its three hypotheses are not proved here; see [GluingMassOfLiftNumberGenus.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/CayleyDegreeNondegeneracy/GluingMassOfLiftNumberGenus.lean#L12). In the gluing number the count is the cardinality of a set, which is $0$ for an infinite set, so the hypothesis also gives finiteness. We did not unfold the definitions of the gluing relation, the fixed convention, the lattice determinant, the hyperbolic cosine, the row lattices, the mass of the rows, or the two lattice lemmas.

## Notes and references

This chapter supplies closed inputs to three steps of the proof: the steps that need [nonempty hypotheses](/step/nonempty-hyps/), the [local matching of theta lifts](/step/theta-local-matching/), and the step on [every character of a row](/step/every-character-of-row/). It also supplies the local bounds of the [four inputs of the net](/entry/inputs4-of-net/). Most statements are the conclusions of theorems proved in other chapters, with their hypotheses discharged here.

For formal groups and their logarithms see Silverman, *The Arithmetic of Elliptic Curves*, Graduate Texts in Mathematics 106, Chapter IV. For the Weyl dimension formula and branching see Goodman and Wallach, *Symmetry, Representations, and Invariants*, Graduate Texts in Mathematics 255, Chapters 7 and 8. The branching rule is from Gelfand and Tsetlin, Doklady Akad. Nauk SSSR 71 (1950), 825 to 828. For Capelli identities and quantum minors see Howe and Umeda, Math. Ann. 290 (1991), 565 to 619. Hermitian lattices over local fields are classified in Jacobowitz, Amer. J. Math. 84 (1962), 441 to 465. The finiteness of class numbers is in Borel, Publ. Math. IHÉS 16 (1963), 5 to 30. Masses of unitary groups are computed in Gan, Hanke and Yu, Duke Math. J. 107 (2001), 103 to 133.
