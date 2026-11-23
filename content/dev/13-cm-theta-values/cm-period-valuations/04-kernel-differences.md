---
title: Kernel differences at a joint site
decls:
  - GlobalTheory.TwV.DelB.delPolAt_site
  - GlobalTheory.T.kernelSite_contractionIdentity_operatorHalf
  - GlobalTheory.TwV.DelA.tieDel_all_steps
  - GlobalTheory.T.kernelSite_frameValues_all_steps_lt_m
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kernel differences at a joint site

The pending tuple of a joint site carries a difference operator at each level. This section proves the *kernel difference law*: at each level $j < m$, the difference operator applied to the series of the pending tuple equals, up to one constant of norm $1$, the reading of the kernel entry of the joint. The constant is the same for all tuples at the level. This law is the last of the ties that Section 5 needs to show that the system at $p$ is admitted. The proof has two parts. First we prove the identity in a polynomial form, for given operator data. Then we produce the operator data from the sharp forms of the joint.

### The kernel difference law

Let $\mathcal{S}$ be a joint site for a joint $J$ with standard data, as in Section 2, at a place of residue characteristic $p$. Let $Y$ be its pending tuple, with field $K_c$, series $\mathrm{Sr}_j(L_a, L_a')$ and difference operators $\Delta_j$. A ring map $\iota : \mathbb{C} \to \mathbb{C}_p$ *agrees with* $\lambda$ if $\iota(z) = \lambda(z)$ for every algebraic number $z$. Each lattice tuple $L_a$ at level $j$ has a class $\mathrm{cls}_j(L_a)$ of the twisted chain, and a lattice vector $x$ of the twist at level $j$ has a comparison value $\mathrm{cmp}_j(x, L_a)$. The kernel entry $t$ has a record $\mathrm{ent}_j(c, x)$ for each class $c$ and vector $x$. The joint gives a reading $\mathrm{Rd}_j(c', L')$ of such records into $K_c$, for each component $c'$ and tuple $L'$ at level $j+1$. It depends on $\iota$.

**Definition 5.4.1 (Kernel difference law).** The site satisfies the *kernel difference law at level* $j$ if for every $\iota$ that agrees with $\lambda$ there is $c_K \in \mathbb{C}_p$ with $|c_K| = 1$ such that
$$\mathrm{Rd}_j(c', L')\bigl(\mathrm{ent}_j(\mathrm{cls}_j(L_a), x)\bigr) = c_K \cdot \Delta_j\bigl(\mathrm{cmp}_j(x, L_a)\bigr)\bigl(\mathrm{Sr}_j(L_a, (c', L'))\bigr)$$
for every representative $L_a$ at level $j$, every lattice vector $x$, every component $c'$ and every lattice tuple $L'$ at level $j+1$.

There is also a polynomial form of the law. A *sharp form* $Q$ at a lattice vector $x$ attaches a form to each class at level $j$; the joint gives one. The record of $t$ gives series $\Theta^t_j(c, c'')$ for classes $c$ at level $j$ and $c''$ at level $j+1$, and the joint gives a class $\kappa_j(c', L')$ for each tuple at level $j+1$. The *frame polynomial* $F(Q(c), \Theta^t_j(c, c''))$ is a polynomial in the frame variables of rank $N(j+1)$. We write $\rho_j(c)$ and $\rho'_{j}(c'')$ for the values of the characters $\mathrm{mt}_j$ of the record at the determinants of $c$ and $c''$.

**Definition 5.4.2 (Polynomial difference law).** Let $\Phi_R(j, c', L')$ be maps from polynomials in the frame variables to the series space of the tuple $L'$, and let $c_K \in K_c$. The *polynomial difference law* at level $j$ for $(\Phi_R, c_K)$ says: for every representative $L_a$ at level $j$, lattice vector $x$, sharp form $Q$ at $x$, component $c'$ and lattice tuple $L'$ at level $j + 1$, with $c = \mathrm{cls}_j(L_a)$ and $c'' = \kappa_j(c', L')$,
$$\Phi_R(j, c', L')\bigl(\rho_j(c)\, \rho'_j(c'')\, F(Q(c), \Theta^t_j(c, c''))\bigr) = c_K \cdot \Delta_j\bigl(\mathrm{cmp}_j(x, L_a)\bigr)\bigl(\mathrm{Sr}_j(L_a, (c', L'))\bigr).$$

### The operator half of the contraction identity

The polynomial law follows from a contraction identity of frames. We give its operator half: the case where the reading $\Phi_R$ is built from given operator data. An *adelic decomposition* $d$ of the site writes every lattice tuple as a translate of a standard tuple by an adelic element. It gives changed frames and a scalar $u_S, u_T$ at the source and at the target of each pair.

**Theorem 5.4.3 (Operator half of the contraction identity).** Let $\mathcal{S}$ be a joint site. Assume the dictionary of the joint, the pair condition, the positions and the kappa law of Section 3. Let $d$ be an adelic decomposition of the site, and $\iota$ a ring map that agrees with $\lambda$. Let $\Phi_0$ be a reading, $\tau$ a family of linear operators on the series spaces, $\mathrm{sc}$ and $s_O$ families of scalars, and $G_m$ further data. Let $j < m$ and $c_K \in K_c$. Assume:
1. the rank condition at $j$;
2. the move hypothesis, which says how the level groups act on the changed frames;
3. the operator tie, which ties $\tau$ to the sharp forms;
4. the degree condition: every monomial of the sharp polynomial of a representative has a good degree after the change of variables;
5. the difference equation: $\tau$ computes the coefficients of the substituted difference polynomials;
6. the scalar identity $c_K \cdot c_A(L_a) \cdot s_O(j, L_a) \cdot \iota(u_S) \cdot \iota(u_T) = \mathrm{sc}$, with $c_A(L_a)$ the constant of the pending tuple at the base of $L_a$.

Then the polynomial difference law holds at level $j$ for the reading $\Phi_R = \varphi_H(\Phi_0, \tau, \mathrm{sc})$ and the constant $c_K$.

Lean: `GlobalTheory.TwV.DelB.delPolAt_site` (also `GlobalTheory.T.kernelSite_contractionIdentity_operatorHalf`)

*Proof.* We collect five facts about the site.
1. The ranks of the system of the site are the ranks of $D$.
2. The frames of the site and the changed frames of $d$ are invertible.
3. By the dictionary, the pair condition and the positions, the theta series of the site at level $j$ is the class series read through the changed frame of $d$. This holds for every $\iota$ that agrees with $\lambda$.
4. By the rank condition, the coefficients of the series at the site are the coefficients of the class series.
5. By the dictionary and the scalar identity, the kernel scalar is the product of the source part and the target part.

The contraction identity of frames with an operator scalar is a theorem on general systems. Its inputs are the kappa law, the invertible frames of fact 2, the series of fact 3, the moves, the operator tie, the degree condition, the coefficients of fact 4, the scalar of fact 5 and the difference equation. Its conclusion is the polynomial difference law. $\square$

### The law at every level

The next theorem removes the operator data. It produces them from the sharp form of the joint and from the frame polynomials.

**Theorem 5.4.4 (Kernel differences at every level).** Let $\mathcal{S}$ be a joint site. Assume the dictionary of the joint, the pair condition, the positions and the kappa law. Then the kernel difference law holds at every level $j < m$.

Lean: `GlobalTheory.TwV.DelA.tieDel_all_steps` (also `GlobalTheory.T.kernelSite_frameValues_all_steps_lt_m`)

*Proof.* Fix $j < m$ and $\iota$ that agrees with $\lambda$. If the level $j$ or the level $j+1$ has no component, there are no lattice tuples at that level, and $c_K = 1$ works. So assume both levels have a component, and choose components $a$ at level $j$ and $a'$ at level $j + 1$.

A lemma on step determinants gives a constant $c_K = c_{K}(j, a, a')$ with $|c_K| = 1$. The same lemma shows that it does not depend on the choice of $a$ and $a'$. We take this $c_K$. The ranks of the system are the ranks of $D$, so the frame variables at level $j+1$ have $N(j+1)$ entries. The dictionary gives an adelic decomposition $d_0$ of the lattice tuples.

Now fix a representative $L_a$ at level $j$, a lattice vector $x$, a component $c'$ and a tuple $L'$ at level $j+1$. The joint gives a sharp form $Q$ at $x$. Put $c = \mathrm{cls}_j(L_a)$ and $c'' = \kappa_j(c', L')$, and form the polynomial
$$P = \rho_j(c)\, \rho'_j(c'')\, F\bigl(Q(c), \Theta^t_j(c, c'')\bigr).$$
Its weight is known from a lemma on frame polynomials. A lemma on operators on frames writes the class summand as
$$\phi_\kappa(y) = \Bigl(\prod_{e} d_e^{s_e}\Bigr)^{-1} \mathrm{fr}(P)(y),$$
a frame value of $P$ divided by a product of powers of the divisors $d_e$.

For each adelic decomposition $d$, a lemma on transported frame polynomials gives the complex values $V_d$ of $P$ at the point of the site. Two further lemmas give the degrees of the moved forms at the kernel source and the scalar at the next level. With these inputs, the theorem on the operator half of the contraction identity applies to $d$, with the constant $c_K$. It gives the polynomial difference law for a reading built from $V_d$.

The map $\iota$ is injective, since it is a ring map out of a field. So the values $V_d$ do not depend on $d$, and the readings agree for all decompositions. A lemma on lattice tuple readings now identifies the reading of the polynomial $P$ with the reading $\mathrm{Rd}_j(c', L')$ of the record $\mathrm{ent}_j(c, x)$. This gives the kernel difference law at level $j$. $\square$

**Remark 5.4.5 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.kernelSite_contractionIdentity_operatorHalf` and `GlobalTheory.T.kernelSite_frameValues_all_steps_lt_m` are second names, each proved by the tactic `first | exact @… | …` under `maxHeartbeats 1000000`.
2. The kernel difference law is the field `Del j` of a site, which unfolds to `KernelDifferenceAtLevel` (SecondKernelEntrywiseLastLevel.lean:55). The polynomial law is `DelPolAt` (Formalism/LocalToGlobal/InertKernelTheory/KernelDifferenceOfFrame.lean:101).
3. The constant $c_K$ is chosen once per level, before the representative, the vector and the tuple at the next level. So the theorem gives a uniform constant, which is stronger than a constant for each tuple.
4. When a level has no component, the proof takes $c_K = 1$, and the condition is vacuous (KernelSiteFrameValuesAllStepsLtM.lean:28).
5. The development also has a version for positive levels, `GlobalTheory.TwV.StepDel.del_of_pos`. It assumes $1 \le j$, does not use this assumption, and only calls the theorem of this section (KernelSiteFrameValuesPositiveSteps.lean:11). So the split of the levels into $j = 0$ and $j \ge 1$ in Section 5 is not needed.
