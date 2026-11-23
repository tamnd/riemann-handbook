---
title: Comparison data and twisted columns
decls:
  - GlobalTheory.HP.HypTiesI.hyp
  - GlobalTheory.Mem.Col2.TC.canon_ok
  - GlobalTheory.Mem.Col2.TC.twIdx_ok_of_ok
  - GlobalTheory.Mem.LocalPack.Test.comparison_statements
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Comparison data and twisted columns

This section collects four results of assembly type. Each one puts conditions that earlier results supply into the form that a later result asks for. The first gives the comparison hypotheses for a tower of lattice charts at one site; the [comparison theorem at a twisted site](/entry/cmp-jhyp-in-tw-site/) uses it. The second and third show that the twisted form of a column of characters satisfies the column conditions; the [base lattice theorem at a prime](/entry/exists-base-lattice-of-prime-alt/) uses them. The fourth gives the level-zero comparison hypotheses for the recursive record of local data; the [theorem on recursive local families](/entry/is-rec-g-of-is-local-family/) uses it.

**Definition 8.9.1 (Chart tower and comparison hypotheses).** Fix a word $u$, a place $w$ of the host field, a level datum $L_v$ and a lattice comparison $c$ with embedding $\iota_c = \iota_c(u,w)$. A chart tower $I$ gives, for each $j$ with $j + 1 \leq m$, a module $M_j$ with a lattice at level $j+1$ and a chart state $s_j$. The comparison hypotheses for $I$ are the seven conditions that follow, for all $j$ with $j+1 \leq m$ and all classes $\beta$.

1. The core condition for $s_j$ holds with respect to $\iota_c$ and $\beta$.
2. The state $s_j$ is good at $w$.
3. The twisted unit condition for $s_j$ holds at $w$ and $\beta$.
4. The normalized integrality of values for $s_j$ holds with respect to $\iota_c$ at $w$.
5. The Iwasawa form condition for $s_j$ holds at $\beta$.
6. The local gate $J_{j+1}$ of $L_v$ at level $j+1$ has finitely many classes.
7. The number of basis vectors of the lattice of $M_j$ at level $j+1$ equals the rank of $J_{j+1}$ over the ring of integers of the local gate.

**Definition 8.9.2 (Tied steps).** Let $X_0$ be a hermitian datum at level zero and let $G_t$ be a family of gate ties. A step at level $j$ consists of forms $F_j$ on $M_j$ at level $j+1$ and a local chart $\Lambda_j$ over $X_0$ for the characters of $F_j$. The step is tied to $G_t$ and $c$ when, for every class $\beta$:

1. the chart of $\Lambda_j$ at $\beta$ is rational for Frobenius with respect to the basis matrix $B$ of $\Lambda_j$;
2. the unit level of $F_j$ at $\beta$ and the unit local level of $\Lambda_j$ at $\beta$ agree;
3. the two type conditions on the chart of $\Lambda_j$ at $\beta$ hold;
4. the unitary character of $\Lambda_j$ at $\beta$ is compatible with the chart and with $\iota_c$;
5. each value of the twisted character of $F_j$ at $\beta$ is the image of an element of the field $L_L$ of the record;

and in addition no bad prime of $F_j$ contains the residue characteristic of $w$, and the basis matrix $B$ is unitary for the Gram matrix $G_{j+1}$:
$$
{}^t\bar{B}\, G_{j+1}\, B = 1,
$$
where the bar is the nontrivial automorphism of the CM field $E$ of the host.

**Definition 8.9.3 (Tied tower).** A chart tower $I$ is tied to $X_0$, $G_t$ and $c$ when three conditions hold. First, the parameter $t$ of the filling equals the parameter $t$ of the record. Second, the filling is tied to $G_t$ at $(u, w)$. Third, for each $j$ with $j+1 \leq m$ there is a step $(F_j, \Lambda_j)$ that is tied to $G_t$ and $c$, such that the chart state $s_j$ of $I$ is the state that this step builds.

**Theorem 8.9.4 (Comparison hypotheses from tied steps).** Let $I$ be a chart tower that is tied to $X_0$, $G_t$ and $c$. Let $c$ be tied to the record, the datum $X_0$, the forms $T$ and $G_t$. Then $I$ satisfies the comparison hypotheses.

Lean: `GlobalTheory.HP.HypTiesI.hyp`.

*Proof.* For each $j$, choose a tied step $(F_j, \Lambda_j)$ and replace $s_j$ by the state that it builds. A lemma of the source gives the comparison hypotheses from conditions 1 to 6 together with three further inputs: the type conditions of each state, a forms-on-classes condition and a lift condition. It also uses the block rationality of the local fields, which is proved once for all data. We supply the inputs as follows. The core condition comes from the tied step together with the tie of $c$, the equality of the two parameters $t$ and the tie of the filling. The good state condition and the type conditions are parts of the tied step. The twisted unit condition and the integrality of values come from the tied step with the same three extra facts. The Iwasawa form condition holds for every state that a step builds. Finiteness of classes follows from the core condition and the type conditions. The forms-on-classes condition and the lift condition hold for every state. $\square$

The next results are about columns of characters. Let $E$ be the CM field of a base $\mathcal{B}$, and let $V_G$ be a finite set of primes of $E$ fixed by the base. For a prime $P$ of $E$, write $q(P)$ for its absolute norm. A column $I$ over $\mathcal{B}$ has an index set; for each index $a$ it has a character tuple $\mu_a$, a set $Q_a$ of primes, a constant $C_a$ and an index datum $N_a$. It also has a global datum $G$ with an embedding $\sigma_0 : K \to \mathbb{C}$ of the coefficient field, an element $\xi_0$ of $E$ and characters $\mu^0_j$. A column can be good, and goodness includes a condition on each $N_a$.

**Definition 8.9.5 (Twisted column).** The twisted constant $C^{\mathrm{tw}}_a$ and the twisted index $N^{\mathrm{tw}}_a$ are built from the characters of $I$, the selection, $\mu_a$ and $G$, and the twisted index uses the depth $m-2$. The column $I$ is twisted when $C_a = C^{\mathrm{tw}}_a$ and $N_a = N^{\mathrm{tw}}_a$ for every $a$. The canonical form $I^{\mathrm{can}}$ of $I$ is $I$ with every $C_a$ and $N_a$ replaced by the twisted values.

**Definition 8.9.6 (Deep column).** The column $I$ is deep when, for every index $a$ and every prime $P$ in the row set of $\mu_a$ with $P \notin V_G$, the exponent $D_P$ of the constant $C_a$ at $P$ satisfies $D_P \geq 2m$.

**Lemma 8.9.7 (Norms modulo four).** Every prime $w \in V_G$ has $q(w) \equiv 1 \pmod 4$.

Lean: `GlobalTheory.Mem.Col2.TC.qOf_mod_four`.

*Proof.* The prime $w$ lies in one of two sets $V_{G,0}$ or $V_{G,1}$, say $V_{G,k}$. The prime data of the base are good, so $q(w)$ equals a fixed integer $g_k$, and $g_k \equiv 1$ modulo $Q_S\, q\, d$, where $Q_S$, $q$ and $d$ are integers of the host. The host has $2^{e+2} \mid Q_S$ for an integer $e \geq 0$, so $4 \mid Q_S\, q\, d$. Thus $q(w) \equiv 1 \pmod 4$. $\square$

**Lemma 8.9.8 (Roots of unity in a deep column).** Let $I$ be a good and deep column, let $a$ be an index and let $P$ be a prime in the row set of $\mu_a$ with $P \notin V_G$. Then there is $z \in K$ with
$$
\sigma_0(z) = \exp\!\left( \frac{2\pi i}{q(P)^{2m}} \right).
$$

Lean: `GlobalTheory.Mem.Col2.TC.root_of_ok`.

*Proof.* Write $D_P = 2m + k$ with $k \geq 0$. Goodness of $N_a$ gives that $\xi_0$ is integral at $P$ with nonzero reduction, so $\xi_0 \neq 0$ and $\xi_0^{-1}$ is integral at $P$. We apply the Weil relation of $N_a$ at $P$ to $x = \xi_0^{-1} q(P)^{-2m}$ and the integer $q(P)^k$. Its first hypothesis holds since $x \cdot q(P)^{D_P} = \xi_0^{-1} q(P)^k$ is integral at $P$, and its second hypothesis reduces to the integrality of $0$. The Weil relation gives an element $z$ of $K$, and a computation in $\mathbb{C}$ shows that $\sigma_0(z)$ is the root of unity above. $\square$

**Theorem 8.9.9 (Twisted index of a deep column).** Let $I$ be a good and deep column. Then for every index $a$ the twisted index $N^{\mathrm{tw}}_a$ is good for the characters of $I$, the selection, $\mu_a$, the twisted constant $C^{\mathrm{tw}}_a$, the global datum $G$ and the depth $m-2$.

Lean: `GlobalTheory.Mem.Col2.TC.twIdx_ok_of_ok`.

*Proof.* We apply the [closure theorem for twisted indices](/entry/tw-idx-ok-closed/). It asks for the following inputs, and we give each one.

1. The fields and the prime data of the base are good. This holds for every base.
2. The characters of $I$ are good, tied to $G$ and satisfy the Weil relation for $\xi_0$. These are parts of goodness of $I$.
3. Every $w \in V_G$ has $q(w) \equiv 1 \pmod 4$. This is the lemma on norms.
4. For every $j$ and every $w \in V_G$ there is $y \in K$ with $\sigma_0(y)$ equal to the inverse of the local value of $\mu^0_j$ at $w$. The goodness of the index datum at the distinguished index gives $y$.
5. The rank $m$ is of the form $m_2 + 2$. This is part of goodness of $I$.
6. No prime in $Q_a$ lies in $V_G$.
7. Every prime $P$ in the row set of $\mu_a$ has residue degree one in the sense of the source.
8. For every such $P$ with $P \notin V_G$ there is $z \in K$ with $\sigma_0(z) = \exp(2\pi i / q(P)^{2m})$. This is the lemma on roots of unity, and it is the only input that uses depth.
9. For every such $P$ there is $z \in K$ with $z^2 = q(P)$. The goodness of $N_a$ gives it.
10. For every such $P$ the element $\xi_0$ is integral at $P$ with nonzero reduction. The goodness of $N_a$ gives it.

Inputs 6 and 7 come from results of the source on the prime data. $\square$

**Theorem 8.9.10 (Canonical form of a deep column).** Let $I$ be a good and deep column. Then its canonical form $I^{\mathrm{can}}$ is good.

Lean: `GlobalTheory.Mem.Col2.TC.canon_ok`.

*Proof.* The canonical form keeps all data of $I$ other than the constants and the index data, so all conditions of goodness on these data stay true. The condition that each constant is the twisted constant holds by the definition of $I^{\mathrm{can}}$. The condition on the index data is the theorem on twisted indices. $\square$

The last result is about the recursive record of local data. Fix a record $D$, a scale, column levels $L_c$, local identifications, characters $\psi$, a hermitian datum $H_0$ at level zero, forms $T$ and a unitary basis matrix $B$ over $E$. The recursive record carries a family of gate ties and a comparison input built from $B$. Also fix, for each $(u, w)$, an embedding $\iota_{u,w}$ of the algebraic closure of $\mathbb{Q}$ in $\mathbb{C}$ into $\mathbb{C}_\ell$, where $\ell$ is the residue characteristic of $w$, and an element $\lambda_{u,w}$, such that $\iota_{u,w}$ agrees with $\lambda_{u,w}$ on the field $L_L$ and the local package at $(u, w)$ is positive for $\iota_{u,w}$ and $\lambda_{u,w}$.

**Theorem 8.9.11 (Level-zero comparison for the recursive record).** Assume the following for every word $u$:

1. the hermitian level-zero datum of $H_0$ and the forms $T_u$ are jointly tied at $u$;
2. the character of $T_u$ at level zero is rational;
3. for every place $w$ and gate index, the character $\psi$ at $(u, w)$ is tied to the level of $T_u$, the column level $L_c(u)$ and the comparison embedding at $(u, w)$.

Then the forms $T$, the gate ties and the comparison input of the recursive record satisfy the level-zero comparison hypotheses.

Lean: `GlobalTheory.Mem.LocalPack.Test.comparison_statements`.

*Proof.* A result of the source gives the level-zero hypotheses from a left datum and the positivity of the local packages. A left datum has five parts, and we give each one.

1. The unit local levels of the hermitian datum and of $T_u$ agree. This follows from hypothesis 1.
2. Block rationality holds at each place. It comes from the block rationality of the local fields, which is proved once.
3. The character of $T_u$ at level zero is rational. This is hypothesis 2.
4. Character values away from the block are images of elements of $L_L$ with the expected product with $\iota_{u,w}$. This follows from hypothesis 3.
5. The recursive integrality of values holds. It follows from the descent of Weyl lattices, which is proved once, together with five local inputs: an existence result for the blocks from parts 1 to 3, the fractional property of the gates, a restriction of existence, a restriction of lattices from the positivity and hypothesis 1, and a restriction of characters from hypothesis 2.

$\square$

**Remark 8.9.12 (Formalization).** The comparison hypotheses are the structure `CmpJHyp` in [ChartComparison.lean](lean:Formalism/SharpRestriction/GrowthBounds/ChartComparison.lean#L82), and the theorem on tied steps is in [BlockRowSubstitutionPreservesComplexSpan.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/BlockRowSubstitutionPreservesComplexSpan.lean#L2092), a file of 2118 lines in a folder named Definitions. Its proof is `cmpJHyp_of_two` with `blockRationality_holds`; we read `cmpJHyp_of_two` only as a statement, and the seventh condition comes through `cmpJHyp_of_lift` and `valLiftOf_of`, which we did not open. The same file declares `cmpJHyp_of_two` at line 713 and `StepTies` at line 1998, and copies with the same names are in [HypInvLe.lean](lean:Formalism/SharpRestriction/GrowthBounds/ChartRank/HypInvLe.lean#L410) and [SiteGoodPrimeTorsion.lean](lean:Formalism/SharpRestriction/GrowthBounds/ChartRank/SiteGoodPrimeTorsion.lean#L34) in other namespaces. The column results are in [IsTwIffCanonEq.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsTwIffCanonEq.lean#L107), also in a Definitions folder; `twCst`, `twIdx`, the goodness `Ok` and the Weil relation were not unfolded, and the proofs of inputs 6 and 7 are `notMem_vGs_of_mem_QE` and `degOneUnram_rowSG`, read as statements. The level-zero theorem is in [ExistsEmbeddingOfRingTie.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ExistsEmbeddingOfRingTie.lean#L148), in a namespace named `Test`, with `maxHeartbeats` set to 32000000; `CmpLeft.toHyp0P` and the five local inputs of part 5 were read as statements only. None of the four results uses the theta values of the earlier sections.

## Notes and references

The results of this chapter feed the main line through two entries. The [local jets at all primes](/entry/loc-jets-all/) use the integral jets at two, and through them the theta values at two with complex multiplication. The [inputs of the algebraic step](/entry/inputs-of-alg-t/) copy these jets, and the step on [nonempty hypotheses](/step/nonempty-hyps/) uses both entries. The [kernel bound](/entry/kernel-bound/) uses the kernel bound for the law of height two, the [integral inert kernels](/entry/integral-inert-of-approx-basis/) use the hermitian frames, and the [row theorem of the unitary hypotheses](/entry/all-rows-of-open0-alt/) uses the local standard lattices. The results of this last section feed the [comparison theorem at a twisted site](/entry/cmp-jhyp-in-tw-site/), the [base lattice theorem at a prime](/entry/exists-base-lattice-of-prime-alt/) and the [theorem on recursive local families](/entry/is-rec-g-of-is-local-family/).

- J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Mathematics 106, Springer, 2009. Chapter III for the Weierstrass equations and the $2$-torsion, Chapter IV for formal groups and their logarithms, Chapter VI for elliptic curves over $\mathbb{C}$, and Chapter VII for reduction over local fields.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*, 4th ed., Cambridge University Press, 1927. Chapter XX for the Weierstrass functions $\wp$ and $\sigma$ and the addition formulas.
- D. A. Cox, *Primes of the Form $x^2 + ny^2$*, 2nd ed., Wiley, 2013. Section 5 for primes in quadratic fields, Section 7 for orders in imaginary quadratic fields, and Sections 10 and 11 for complex multiplication and the values of the $j$-function.
- G. Frobenius and L. Stickelberger, Zur Theorie der elliptischen Functionen, *J. reine angew. Math.* 83 (1877). This paper gives the determinant formula for the products of $\sigma$ functions that Section 1 uses.
- G. Frobenius and L. Stickelberger, Ueber die Addition und Multiplication der elliptischen Functionen, *J. reine angew. Math.* 88 (1880).
