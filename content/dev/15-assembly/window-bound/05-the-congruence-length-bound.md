---
title: The congruence length bound
decls:
  - Formalism.MainNotions.N.K.Final.plugOpen3_B
  - Formalism.MainNotions.N.K.Final.theorem_n5_of_ring_inputs
  - Formalism.MainNotions.N.K.Final.theorem_n5_of_open_b
  - Formalism.MainNotions.N.K.Closed.theorem_n5_from_inputs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The congruence length bound

This section proves the closed form of the Selmer bound at a point: the congruence length $\ell(\mathcal{O}/\eta_\pi)$ is bounded by the sum of the Selmer, Tate-Shafarevich, class number and local terms of [the Selmer bound at a point](/entry/selmer-bound-at-point-main/). That theorem of Volume 4 applies the result here to its remaining hypotheses. The proof puts together the ring of [Theorem 2.3.6](/entry/normalized-ring-data/), the local clauses of [Theorem 2.4.5](/entry/open-inputs-at-normalized/), and a reduction of the bound to one inequality.

We keep the notation of the last two sections. Let $\mathrm{len}_{\mathrm{row}}$, $e'$ and $c_B$ be as in the Selmer bound at a point. The conditions of that theorem that we use are named by their numbers there, with the names of the last section for the parts of conditions 3, 4 and 7. Three of them we call the *last conditions*: the length condition at the row places with $\mathrm{len}_{\mathrm{row}}$, the lift condition at the column places with $e'$, and the local torsion bound with $c_B$ at the row places.

**Definition 2.5.1 (Selmer length inequality).** The *Selmer length inequality* says: there are lengths $\mathrm{len}_w$ at the row places, $h_{0,w}$ at the column places, and $v_\delta$, with $v_\delta = e_{\mathcal{O}} \sum_{0<k<t} (s_0 + v_\ell(k))$, such that $\ell(\mathcal{O}/\eta_\pi)$ is at most the right side of the display bound with $n_V = r + t$, $s = \ell(\mathrm{Sel}_\pi)$, $\text{Ш}_e$ the length of the Tate-Shafarevich group of the $e$-th twist, and $H_0$ the largest length of invariants at the column places; and such that the $\mathrm{len}_w$ are tied to $\mathrm{len}_{\mathrm{row}}$ and the $h_{0,w}$ bound the invariants of $\rho_\pi \otimes \chi_1^{-1}$ at the column places.

Lean: `Formalism.MainNotions.N.K.SelmerLengthInequality`.

The Selmer length inequality names $\rho_\pi$ and $\pi$, but not $r$. This is why we may change $r$ at $\pi$.

**Definition 2.5.2 (Selmer tuple).** For a ring datum of a family $r$, the *Selmer tuple* is the list of local inputs of the display bound that the ring datum does not give: the classes $\kappa$, $\kappa_z$, a function $u$ on the column places and cocycles $u_z$ with $u_z = \delta_{\mathcal{O}} u$; the finiteness of the unramified classes $u_z$; a bound, at each point $x'$ with $p(x') \notin Z$ and each column place, on the rank of the column classes; the five open clauses; a clause from the Bloch-Kato annihilator condition; the unramified character clause at the columns; and the tie of the row lengths to $\mathrm{len}_{\mathrm{row}}$. It has fourteen parts.

Lean: `Formalism.MainNotions.N.K.St.SelmerInequalityThree`.

**Theorem 2.5.3 (Tuple from the open clauses).** Let $r$ be normal at $\pi$, with a ring datum as in the last section. Assume the Bloch-Kato dimension condition and the gain conditions of 7, Fontaine's conditions, the decomposition of $r_\pi$, the finiteness of local $H^1$, the Bloch-Kato annihilator condition, the good-coefficient condition, the length condition at the rows, and condition 8 in the form: at each column place $w$, the unramified $1$-cocycles of the local Galois group with coefficients in the local coefficient field lie in the finite part. If the five open clauses hold, then the Selmer tuple holds.

Lean: `Formalism.MainNotions.N.K.Final.plugOpen3_B`.

*Proof.* The $\rho$-clause, the row clause, the character clauses and the first local clause are four parts of the tuple. The classes $\kappa$, $\kappa_z$, $u$ and $u_z$ are the fixed classes of the datum; the finiteness of $u_z$ follows from condition 8. The rank bound at the columns follows from the Bloch-Kato dimension condition, the gain conditions, Fontaine's conditions, the decomposition and the finiteness of local $H^1$. The annihilator clause follows from the annihilator condition, the good-coefficient condition, and a row comparison that Fontaine's conditions, the gain conditions, the decomposition and the normal form give. The unramified character clause holds with no hypothesis. The tie of the row lengths follows from the good-coefficient condition, the length condition at the rows and the row tie. $\square$

**Theorem 2.5.4 (Bound from the tuple).** Assume conditions 1, 2 and 5, the gain conditions, the tame generator conditions, the continuity of $r$, the decomposition of $r_\pi$, the admissibility condition 7 at $\pi$ on congruence objects, and the good-coefficient condition. Assume: if the last conditions hold for $r^{\mathrm{N}}$ and $\pi \in Z$, then for each $g_0$, each idempotent pair, each corner perturbation, and each ring datum of $r^{\mathrm{N}}$ that is continuous, has the properties (T) and has $e_1$ of rank one on block $0$, the Selmer tuple holds. Then the last conditions for $r$ imply the conclusion of the Selmer bound at a point.

Lean: `Formalism.MainNotions.N.K.Final.theorem_n5_of_ring_inputs`.

*Proof.* The three last conditions pass from $r$ to $r^{\mathrm{N}}$: each is a condition on $r_\pi \otimes L$ up to conjugacy at the places above $\ell$, and the decomposition gives $r_\pi \otimes L \cong r^{\mathrm{N}}_\pi \otimes L$. A reduction lemma proves the conclusion of the Selmer bound at a point from the Selmer length inequality, under the hypotheses $\ell \neq g_0, g_1$, $\pi \in Z$, $\mathrm{Sel}_\pi$ of finite length and $\text{Ш}(e)$ of finite length, together with the gain conditions and the tame generator conditions. So assume $\pi \in Z$. The admissibility condition at $\pi$ gives an element $g_0$ of $G_E$ with $\varepsilon(g_0) = 1 + \ell^{s_0} u_0$, $u_0$ a unit, an idempotent pair $(e_B, e_1)$ and a corner perturbation $s$ for $r^{\mathrm{N}}$. Condition 1 passes to $r^{\mathrm{N}}$, since the characteristic polynomials agree. Condition 2 gives that $\bar\rho_\pi$ spans $M_r(k)$. Then [Theorem 2.3.6](/entry/normalized-ring-data/) gives a ring datum of $r^{\mathrm{N}}$ with the display bound for $\ell(\mathcal{O}/\eta_\pi)$. The continuity of $r$ and of $\rho_\pi$ gives the continuity of $r^{\mathrm{N}}$, and $e_1$ has rank one on block $0$ by the idempotent pair. The hypothesis gives the Selmer tuple. Finally, a general lemma proves the Selmer length inequality from the display bound, the normal form, the formula for $\varepsilon(g_0)$, condition 5 for $r^{\mathrm{N}}$, the lift condition, the good-coefficient condition and the Selmer tuple. $\square$

**Theorem 2.5.5 (Bound from the open clauses).** Assume conditions 1, 2 and 5, the gain conditions, the tame generator conditions, the Bloch-Kato dimension and annihilator conditions, the continuity of $r$, the decomposition of $r_\pi$, Fontaine's conditions, the finiteness of local $H^1$, the admissibility condition at $\pi$, condition 8 in the form above, and the good-coefficient condition. Assume: if the last conditions hold for $r^{\mathrm{N}}$ and $\pi \in Z$, then the five open clauses hold for each ring datum of $r^{\mathrm{N}}$ as in the last theorem. Then the last conditions for $r$ imply the conclusion of the Selmer bound at a point.

Lean: `Formalism.MainNotions.N.K.Final.theorem_n5_of_open_b` (also `Formalism.MainNotions.N.K.Final.RemainingInputsLastLayer`).

*Proof.* We apply the last theorem. For a ring datum of $r^{\mathrm{N}}$, the hypothesis gives the five open clauses. The family $r^{\mathrm{N}}$ is normal at $\pi$, its decomposition holds, and the gain conditions pass to it. The theorem on the tuple from the open clauses, applied to $r^{\mathrm{N}}$, gives the Selmer tuple. $\square$

The open clauses need one more fact, on the characters at the places of $Q$. It comes from the structure of inertia.

**Lemma 2.5.6 (Wild inertia).** Let $v$ be a finite place of $E$ not above $\ell$, and let $\varphi$ be a homomorphism from $G_E$ to a group, with open kernel, such that each value $\varphi(g)$ has order a power of $\ell$. Let $\sigma \in G_E$ be in the wild inertia group at a place of $\Omega$ above $v$, that is, $\sigma(y)/y \equiv 1$ modulo the maximal ideal for each $y \neq 0$. Then $\varphi(\sigma) = 1$.

Lean: `Formalism.MainNotions.N.K.Closed.wildTriv_holds`.

*Proof.* Let $p$ be the residue characteristic of $v$, so $p \neq \ell$. The wild inertia group is a pro-$p$ group [Serre, *Local Fields*, Chapter IV, §2]. Its image in the finite quotient $G_E / \ker \varphi$ is a $p$-group, so $\sigma^{p^k} \in \ker \varphi$ for some $k$. The order of $\varphi(\sigma)$ divides $p^k$ and a power of $\ell$, so it is $1$. $\square$

We use the lemma through one consequence. Let $v \in Q$. On the inertia group at $v$, the character $\chi_1$ agrees with a character $\psi$ of the twist family, with open kernel and values of $\ell$-power order. By the lemma, $\psi$ is trivial on wild inertia. The inertia group at $v$ is the closed subgroup generated by $\gamma_v$ and the wild inertia group. The elements $g$ with $\psi(g) = \psi(\gamma_v)^n$ for some $n$ form an open, hence closed, subgroup, since $\psi(\gamma_v)$ has finite order and $\psi$ has open kernel. So for each $g$ in the inertia group at $v$ there is $n$ with $\chi_1(g) = \chi_1(\gamma_v)^n$.

**Theorem 2.5.7 (Congruence length bound from the local inputs).** Assume the facts of class field theory and Galois cohomology and the finiteness of local invariants of [the Selmer bound at a point](/entry/selmer-bound-at-point-main/). Assume conditions 1 to 7, except the parts of 7 named below, for $r$: conditions 1, 2 and 5, the gain conditions, the unramified condition, the inertia condition, the tame generator conditions, the Bloch-Kato dimension and annihilator conditions, the continuity of $r$, the decomposition of $r_\pi$, Fontaine's conditions, the finiteness of local $H^1$, the compatibility of local coefficient fields, and the admissibility condition at $\pi$. Assume condition 8 in the form: at each column place $w$, the unramified $1$-cocycles of the local Galois group with coefficients in the local coefficient field lie in the finite part. Then the last conditions for $r$ imply the conclusion of the Selmer bound at a point.

Lean: `Formalism.MainNotions.N.K.Closed.theorem_n5_from_inputs`.

*Proof.* We apply the theorem on the bound from the open clauses. The good-coefficient condition is part of the datum of the Selmer bound at a point. It remains to prove the five open clauses for each ring datum of $r^{\mathrm{N}}$, when the last conditions hold for $r^{\mathrm{N}}$ and $\pi \in Z$. The scalar actions of $\mathbb{T}'$ and $R'$ on the blocks are compatible: for $f \in \mathbb{T}'$ and $a \in R'$, the evaluation at $\pi'$ sends $f a$ to $f(\pi') a(\pi')$, and $f$ acts on each block by $f(\pi')$. The condition on $\chi_1$ at the places of $Q$ holds by the wild inertia lemma, as above. Then [Theorem 2.4.5](/entry/open-inputs-at-normalized/) gives the five open clauses, with the local torsion bound for $r^{\mathrm{N}}$. $\square$

**Remark 2.5.8 (Formalization).** The conclusion of the Selmer bound at a point is `GlobalLatticeIndexTheorem`; the name "n5" in the four theorems does not say what is bounded, and the file names speak of "statement one B". The reduction lemma is `H0.theorem_of_display_and_g2` ([KernelLengthHigherColumns.lean](lean:Formalism/AdmissibleDesigns/KernelLengthHigherColumns.lean#L185)) and the general lemma is `selmer_inequality_three` ([TheoremFromNormalizedOpenThree.lean](lean:Formalism/AdmissibleDesigns/TheoremFromNormalizedOpenThree.lean#L129)); the choice of $g_0$ is `design_normalized_of_admitted`. We read their statements, not their proofs. Odd points, all in [StatementOneBChangedOfOpen.lean](lean:Formalism/AdmissibleDesigns/StatementOneBChangedOfOpen.lean#L271) unless noted:

- In `theorem_n5_of_ring_inputs` the reduction lemma offers five hypotheses, and the proof uses only $\pi \in Z$ (line 282). It discards with `-` the fact that $g_0$ lies in an inertia group above $\ell$ (line 285), and the equation for the congruence length of $p(\pi')$ (line 286). Of condition 2 it uses only the span of $\bar\rho_\pi$.
- In `theorem_n5_from_inputs` ([StatementOneBFromUnramified.lean](lean:Formalism/AdmissibleDesigns/StatementOneBFromUnramified.lean#L142)) the proof drops the length condition, the lift condition for $r^{\mathrm{N}}$ and $\pi \in Z$ when it proves the open clauses; only the torsion bound for $r^{\mathrm{N}}$ is used. The compatibility of scalar actions is proved inline at lines 152 to 172 from four equations of the ring datum.
- The good-coefficient condition is not proved: `selfGood_rec` reads it from the field `self_good` of the datum `D7` ([RhoDetPrimeEqMuTildeMulChiPow.lean](lean:Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L266)).
- The condition on $\chi_1$ at $Q$ is `qPow_rec`, from `qpow_of_tw` and the wild inertia lemma; the lemma's proof uses `wildProP` for the pro-$p$ step.
- The file defines `RemainingInputsRankFive` (line 160) and `RemainingInputsAfterColumns` (line 259), which nothing uses, and the empty sections `StmtsA` and `StmtsB`. [StatementOneBFromUnramified.lean](lean:Formalism/AdmissibleDesigns/StatementOneBFromUnramified.lean#L179) also has an empty section.
- All four theorems run under `maxHeartbeats 4000000`.
