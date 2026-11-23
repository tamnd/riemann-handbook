---
title: Joints from joint inputs
decls:
  - GlobalTheory.TwV.jointsAt_of_jIn
  - GlobalTheory.T.comparison_data_statements_at_site
  - GlobalTheory.HP.cmpJHyp_inTw_site
  - GlobalTheory.T.trueColumn_exists_chainCharts_kernelData_forms
  - GlobalTheory.Port.jIn_nonempty_true
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Joints from joint inputs

This section proves the two facts that Section 1 took from later in the chapter. The first is the theorem on joints from joint inputs: if a tied kernel entry has joint inputs for every word, then it has joints at the tuple. The second is the existence of joint inputs over true columns. Together they give [the theorem on joints over true columns](/entry/joints-all-true/), and through it the local models of Section 5. On the way we prove that a good comparison site satisfies the comparison hypotheses.

### Comparison sites

We keep the notation of Section 1. Let $t$ be a tied kernel entry for $\mathrm{ex}$, $u$ a word, $\mu$ a tuple and $w$ a place of residue characteristic $p$ with its index condition. A Hermitian base $X_0$ for $D$ fixes, for each word and place, the gate at $(u, w)$: this is the Hermitian column of rank $k$ from which the chain of $D$ grows. A *filling* $F_l$ of the gate is a choice of $t_F$ further vectors for each step. We always assume $t_F = t_D$, where $t_D$ is the number of vectors that $D$ adds at each step. Then the space at step $i + 1$ has rank $k + (i + 1)(t_D + 1) = N(i + 1)$.

**Definition 5.7.1 (Comparison site datum).** Let $M$ be a family of member forms for the word $u$. A *comparison site datum* $Z$ for $(X_0, u, w, M)$ gives, for each $i$ with $i + 1 \le m$:
1. forms $\mathrm{Fo}_i$ of $M$ at level $i + 1$, with a finite set $\mathrm{Ch}_i$ of chart classes;
2. a step datum $S_i$ at $(u, w)$ over $\mathrm{Fo}_i$: for each class $\beta \in \mathrm{Ch}_i$ a chart and a unit character $\psi_\beta$, and a basis $B_i$ of the space at level $i + 1$.

A comparison site datum and a filling give levels $L_v(Z)$. At step $i + 1$ the components of $L_v(Z)$ are the components of the charts of the classes in $\mathrm{Ch}_i$. There are no components at a step $j > m$. At each step the site also gives local inputs with the basis $B_i$, the characters $\psi_\beta$ and the lattices and unit groups of the forms. Over a twist $\tau$ and a choice of ties of the gates, the site gives comparison inputs $I(Z)$ for the levels $L_v(Z)$.

**Definition 5.7.2 (Good site).** The comparison site datum $Z$ is *good* if for every $i$ with $i + 1 \le m$:
1. $p$ does not divide the torsion order $T_i$ of the forms $\mathrm{Fo}_i$;
2. $p$ does not lie in any bad prime of $\mathrm{Fo}_i$, that is, the image of $p$ in $\mathcal{O}_F$ is not in the prime;
3. the forms $\mathrm{Fo}_i$ are in order at $w$.

**Definition 5.7.3 (Rest conditions).** Let $c$ be a lattice comparison for $D$. The datum $Z$ satisfies the *rest conditions* for $c$ if for every $i$ with $i + 1 \le m$:
1. the basis is orthonormal: ${}^t\overline{B_i}\, G_{i+1}\, B_i = 1$, where $G_{i+1}$ is the Gram matrix of the Hermitian form at level $i + 1$ and the bar is the complex conjugation of $E$;
2. each unit character $\psi_\beta$ is compatible with the embedding of $c$ at $(u, w)$;
3. each value of the character of the twisted forms at a class lies in the image of the number field $L$ in $\mathbb{C}$.

The first rest condition says that $B_i$ is a unitary frame for the form at level $i + 1$. The third one is the same algebraicity condition that appears in the joints.

**Theorem 5.7.4 (Comparison hypotheses at a site).** Let $X_0$ be a Hermitian base, $u$ a word, $w$ a place with its index condition, $\tau$ a twist and $\mu$ a tuple. Let $Z$ be a comparison site datum for the member forms of $\tau$ at $(u, \mu)$. Let $F_l$ be a filling with $t_F = t_D$, let $G_t$ be ties of the gates, $T$ the forms at level $0$ and $c$ a lattice comparison. Assume that $c$ is tied to $(X_0, T, G_t)$, that $F_l$ fills the tie of $G_t$ at $(u, w)$, that $Z$ is good, and that $Z$ satisfies the rest conditions for $c$. Then the comparison hypotheses hold for $c$ and the comparison inputs $I(Z)$.

Lean: `GlobalTheory.HP.cmpJHyp_inTw_site` (also `GlobalTheory.T.comparison_data_statements_at_site`, a second name)

*Proof.* The comparison hypotheses follow from [the tie hypotheses](/entry/hyp/), which ask for data at every level $j < m$. At level $j$ we give the forms $\mathrm{Fo}_j$ and the local inputs of $Z$. The frames of the local inputs are rational by definition, and the unit groups of the local inputs are the unit groups of the forms. The tie hypothesis at level $j$ comes from the site. The condition on bad primes, the condition that the forms are in order at $w$, and the condition that $p$ does not divide the torsion order are the three conditions of a good site. The orthonormal basis, the compatibility of $\psi_\beta$ and the rationality of the character values are the three rest conditions. The lattices of the local inputs agree with the lattices of the forms by symmetry of the definition. $\square$

### Joints from joint inputs

**Theorem 5.7.5 (Joints from joint inputs).** Let $t$ be a tied kernel entry for $\mathrm{ex}$ and $\mu$ a tuple. Assume the lattice tie of the extra data, and assume that for every word $u$ there are joint inputs for $(t, u, \mu)$. Then $t$ has joints at $\mu$.

Lean: `GlobalTheory.TwV.jointsAt_of_jIn`

*Proof.* Fix a word $u$, a place $w$ with its index condition, and assume $p \notin Q_p(\mu)$. Let $J$ be joint inputs for $(t, u, \mu)$. We build the levels, the inputs, the hypotheses, the labels and the joint in six steps.

Step 1. A lemma on chain charts gives a comparison site datum $Z$ over the chain charts of $J$, for the twisted member forms of $\mathrm{ex}$ at $(u, \mu)$. The same lemma says that $Z$ is good and satisfies the rest conditions for the comparison map of $\mathrm{ex}$. We take the levels $L_v(Z)$ and the comparison inputs $I(Z)$.

Step 2. The previous theorem gives the comparison hypotheses $H$ for $I(Z)$.

Step 3. A lemma on joints gives the statements at step $0$ from $J$. A second lemma gives labels $X$ at level $0$ whose class at step $0$ is the class of level $0$. It uses the rationality of the twist from $J$ and the fact that the determinant group of the chain twist divides into the group $D_\Gamma$.

Step 4. The charts and the twists of the site are the charts and the twists of the tuple chain.

Step 5. The local identifications at the site agree with those at step $0$. This gives the identification of the frames, the levels and the bases at step $0$, the positivity at step $0$, and the algebraicity at step $0$.

Step 6. We assemble the joint. The group compatibility data, the chain charts, the adelic datum, $\mathrm{dt}_U$, $a$, the pins and the tie come from $J$. The sharp form at every level comes from the pins and the valuation data of $J$. The norm of $\mathfrak{c}$ is prime to $p$ by the index condition. There are no components above level $m$ by the construction of $L_v(Z)$. The basis at each step spans the first factor of the lattice at $p$, and so does the basis at level $0$. The identifications at step $0$ come from Steps 4 and 5. The lattice tie is the hypothesis, and $p \notin Q_p(\mu)$ is the assumption on $p$. $\square$

### Joint inputs over true columns

**Theorem 5.7.6 (Joint inputs over true columns).** Let $I$, $l$, $l_0$, $Z$, $\mathrm{ex}$, $t$, $C$ and $g$ be as in [the theorem on joints over true columns](/entry/joints-all-true/), and assume its hypotheses 1 to 6. Then for every word $u$ and every tuple $a$ there are joint inputs for $(t, u, a)$.

Lean: `GlobalTheory.Port.jIn_nonempty_true` (also `GlobalTheory.T.trueColumn_exists_chainCharts_kernelData_forms`, a second name)

*Proof.* Fix $u$ and $a$. Let $Q$ be the set of places of $F$ that lie under the primes of the tuple $a$. The proof has four steps.

Step 1. A lemma on true columns chooses good charts at every stage. It gives chart classes, a choice map from the classes of the member to the chart classes, a bijection of the points at step $0$, a set of level classes, and the facts at step $0$: the level and the points at step $0$ are the expected ones.

Step 2. The bad set of the chain is contained in the union of the bad set of $D$ and the places under $Q$. So the places under the primes of $a$ are the only new bad places.

Step 3. A second lemma on true columns gives an adelic datum $A$ on the step charts, with pins and a tie, that is compatible with the kernel data. Its determinant condition comes from the full columns. At each level class, the determinant point of the full columns is the determinant of an element of $U^1(\mathbb{A}_f)$. Every element of the norm one group has a lift, and the standard determinant of hypothesis 5 gives the class of the lift.

Step 4. We fill in the joint inputs. The group compatibility data are $g$. The Hermitian columns are the base of the full columns, with their relative determinant. The element of $\mathcal{O}_E$ is the conjugate of the element $\pi_T(u)$ of the error part. The valuation data come from the tied valuations of the true columns. The chart classes are finite and the level characters have finite order by Step 1. The base lattice of each chart class, read in the coordinates of $A$, is the standard lattice. This holds because the orthonormal coordinates agree and because the companion lattice of a true column is the standard base lattice. The joint at step $0$ is the joint of the two sides of the service datum. The identification at step $0$ is the class map at step $0$ of $I$, and the comparison embedding is the identity. The level, the characters, the points and the frames at step $0$ come from Step 1. The point at step $0$ lies over the place under the twist prime, because that place lies over a prime of the tuple. The twist is rational at every step $j < m$, because the kernels of the true-column tuples are rational. The kernel coefficient field lies in the coefficient field. The values of $\chi_D$ lie in the image of $L$ by hypothesis 6. $\square$

**Remark 5.7.7 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.comparison_data_statements_at_site` and `GlobalTheory.T.trueColumn_exists_chainCharts_kernelData_forms` are second names. Each is proved by the tactic `first | exact @… | …` under `maxHeartbeats 1000000`.
2. In `GlobalTheory.HP.cmpJHyp_inTw_site` the twist `Tw` enters only through the type of the site datum `Z` (ComparisonDataStatementsAtSite.lean:15). The comparison hypotheses `CmpJHyp`, the comparison inputs `SiteD.inTw` and the tie hypotheses `HypTiesI` (BlockRowSubstitutionPreservesComplexSpan.lean:2066) are not unfolded here. The site datum `SiteD` and the conditions `SiteRest` and `SiteGood` are at MemberChainFormsLevelPrimeEqMember.lean:91, :520 and :529.
3. In `GlobalTheory.TwV.jointsAt_of_jIn` the field `sharp` is built with the predicate `(fun _ _ => True)` as one argument (JointsAtSplitUnramifiedPlacesOfChainCharts.lean:64). The joint is the structure `Joint` with 35 fields, and the proof runs under `maxHeartbeats 4000000`. The name of the file says "split unramified places", but the only condition on the place is $p \notin Q_p(\mu)$.
4. `GlobalTheory.Port.jIn_nonempty_true` does not use the lattice tie. Hypothesis 7 of the theorem on joints over true columns is used only later, in the theorem on joints from joint inputs.
