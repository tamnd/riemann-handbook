---
title: The twist place law for all tuples
decls:
  - GlobalTheory.LevPrimeAll.exists_choice
  - GlobalTheory.T.seesaw_levelPrime_law_all_tuples
  - GlobalTheory.LevPrimeAll.lawLevelPrime_all
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The twist place law for all tuples

The last two sections proved the twist place law at one index of the chain: at [an inner double step](/entry/law-level-prime-double/) and at [the last steps](/entry/tlast-all-main/). This section puts them together. It chooses, once and for every index $j$, the units, the operator and the constants, and then proves the law for every tuple and every decoration whose constants are the monomials of the choice. The choice does not depend on the tuple. The result is step 1 of [the finite integral laws from pinned level data](/entry/pins-finite-integrals/).

**Setting.** We keep the notation of the last two sections: common see-saw data $c$, data $v$ with twist places $P_T$, lattices $N_j$ and $N_T$, coefficients $d_T(j)$, and a lattice shape datum $o$ that fits $v$. The data $v$ carry, for each $j$, a ramified set $R_j$ of functions on the group of $X_j$, an operator $S_j$ on such functions, and a bi-operator $\mathrm{op}_j$. Validity of $v$ asks, among other things, that $d_T(j)$ and $\mathrm{op}_j$ be at $P_T$, and that every $\varphi \in R_j$ be continuous automorphic with $S_j \varphi \in R_j$. For families $S'$ and $\mathrm{op}'$, let $v[S', \mathrm{op}']$ be $v$ with $S_j$ and $\mathrm{op}_j$ replaced. A decoration $w$ of a tuple $t$ has, in addition to the fields of the section on see-saw laws, a constant $c_T(j)$ for each $j$.

**Definition 2.15.1 (Twist place law).** The decoration $w$ satisfies the *twist place law* for $v$ if the following hold.

1. For every inner position $j + 2(\sigma + 1) + 2 = m$, and all $\Psi_1$ vacuum for $(N_j, N_{j+1})$ and $\Psi_2$ vacuum for $(N_{j+1}, N_{j+2})$ at $P_T$: the function $\mathrm{op}_j(\mathrm{ctr}(\Psi_1, \Psi_2))$ is bi-vacuum for $(L_j, L_{j+1}, L_{j+2})$ at $P_T$, and for $d, d'$ off $P_T$ and $\varphi \in R_j$,
$$\mathrm{bl}\big(\varphi, d, d', \mathrm{ctr}(\Psi_1, \Psi_2)\big) = c_T(j)\ \mathrm{bl}\Big(S_j \varphi, d, d', \mathrm{bc}\big(d_T(j), d_T(j+1), \mathrm{op}_j(\mathrm{ctr}(\Psi_1, \Psi_2))\big)\Big).$$
2. For $j + 2 = m$, and $\Psi_1$ vacuum for $(N_j, N_{j+1})$ and $\Psi_2$ vacuum for $(N_{j+1}, N_T)$ at $P_T$: the function $\mathrm{op}_j(\mathrm{lst}(\Psi_1, \Psi_2))$ is bi-vacuum at $P_T$, and for $d, d'$ off $P_T$, $\varphi \in R_j$, and every continuous automorphic $f$ on the top group that is invariant under the stabiliser of $N_T$ at $P_T$, the integral identity of item 2 of [the law at the last steps](/entry/tlast-all-main/) holds with $c_T(j)$ in place of the monomial, $S_j$ in place of $S_\varepsilon$ and $\mathrm{op}_j$ in place of $\mathrm{op}$.

**Lemma 2.15.2 (Twist data at one index).** Assume the validity of $c$ and $v$, and let $o$ fit $v$. Fix $j$. Then there are units $\varepsilon_i$ of $\mathcal{O}_k$, a bi-operator $\mathrm{op}$ at $P_T$, reals $r_i > 0$ and integers $e_i$ such that:

1. for every $\sigma$ with $j + 2(\sigma + 1) + 2 = m$ and every tuple $t$ that is valid, satisfies WeilOK for $v$ and is unramified at $P_T$ on its Bessel data, the conclusion of [the law at a double step](/entry/law-level-prime-double/) holds for $\varepsilon$, $\mathrm{op}$, $r$ and $e$;
2. if $j + 2 = m$, then for every such tuple that is also unramified at $P_T$ on its Weil representations, the conclusion of [the law at the last steps](/entry/tlast-all-main/) holds for $\varepsilon$, $\mathrm{op}$, $r$ and $e$.

Lean: `GlobalTheory.LevPrimeAll.exists_choice`.

*Proof.* There are three cases.

1. *There is $\sigma$ with $j + 2(\sigma + 1) + 2 = m$.* The law at a double step gives the data and item 1 for this $\sigma$. The equation determines $\sigma$, so item 1 holds for every $\sigma'$ that satisfies it. Item 2 is empty, since $j + 2 = m$ contradicts the equation.
2. *$j + 2 = m$.* The law at the last steps gives the data and item 2. Item 1 is empty by the case hypothesis.
3. *Neither.* Both items are empty. Take $\varepsilon_i = 1$, the empty bi-operator, $r_i = 1$ and $e_i = 0$. $\square$

**Theorem 2.15.3 (Twist place law for all tuples).** Assume the validity of $c$ and $v$, and let $o$ be a lattice shape datum that fits $v$. Then there are units $\varepsilon_j(i)$, bi-operators $\mathrm{op}_j$, reals $r_j(i) > 0$ and integers $e_j(i)$, for all $j$ and $i$, such that:

1. $v' = v[S_\varepsilon, \mathrm{op}]$ is valid, where $S_\varepsilon$ is the family of twisting operators of $o$ for $\varepsilon$;
2. for every tuple $t$ and decoration $w$ of $t$ such that $t$ is valid, satisfies WeilOK for $v$, and is unramified at $P_T$ on its Bessel data and on its Weil representations, and such that $c_T(j) = \mathrm{mono}(r_j, e_j, \chi_{W, j, \rho})$ for all Bessel positions $(j, \rho)$, the decoration $w$ satisfies the twist place law for $v'$.

Lean: `GlobalTheory.LevPrimeAll.lawLevelPrime_all` (also `GlobalTheory.T.seesaw_levelPrime_law_all_tuples`, a second name).

*Proof.* We choose the data index by index and check the two items.

1. *The choice.* Apply the lemma to each $j$, and let $\varepsilon_j$, $\mathrm{op}_j$, $r_j$ and $e_j$ be the data it gives. Then $r_j(i) > 0$ and $\mathrm{op}_j$ is at $P_T$.
2. *Validity of $v'$.* All conditions of validity except two do not involve $S$ and $\mathrm{op}$, and hold since $v$ is valid. The condition that $\mathrm{op}_j$ is at $P_T$ is step 1. For the condition on $R_j$, let $\varphi \in R_j$. It is continuous automorphic since $v$ is valid. Since $o$ fits $v$, $R_j = \mathrm{Ram}_j$, so it remains to show that $S_\varepsilon$ maps $\mathrm{Ram}_j$ into itself. The operator $S_\varepsilon$ is a composite over the list $I$ of local twisting operators at $p_i$, so by induction on the list it suffices to treat one factor. By the lemma on the ramified operator, the local twisting operator at $p_i$ is a finite combination of right translations by elements of the group at $p_i$, and it is a bijection on the functions ramified at $p_i$. Right translations keep continuous automorphic functions. They also keep the ramified condition at $p_{i'}$ for $i' \neq i$: the places are distinct, so the translating elements commute with the group at $p_{i'}$.
3. *The law at inner positions.* Let $t$ and $w$ be as in item 2, and let $j + 2(\sigma + 1) + 2 = m$. Rewrite $c_T(j)$ as the monomial at the position $(j, \sigma + 1)$. Since $R_j = \mathrm{Ram}_j$, item 1 of the lemma at $j$ gives item 1 of the law.
4. *The law at the last steps.* For $j + 2 = m$, rewrite $c_T(j)$ as the monomial at $(j, 0)$. Item 2 of the lemma at $j$ gives item 2 of the law, for every continuous automorphic $f$. $\square$

The law at the last steps asks for the identity only when $f$ is invariant under the stabiliser of $N_T$ at the twist places. The proof gives it for all continuous automorphic $f$, so this invariance is not needed. Also, the constants $c_T(j)$ are asked to match the monomial at every Bessel position $(j, \rho)$, although the proof only uses $\rho = \sigma + 1$ at inner positions and $\rho = 0$ at the last steps.

**Remark 2.15.4 (Formalization).** The lemma and the theorem are at [SeesawLevelPrimeLawAllTuples.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeesawLevelPrimeLawAllTuples.lean#L77) (lines 42 and 77), with the one-factor step of step 2 at line 18 and the induction at line 34. The second name is a restatement in [SeesawLevelPrimeLawAllTuplesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeesawLevelPrimeLawAllTuplesStatement.lean#L6). The statement of the theorem is in [VacOfShape.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/VacOfShape.lean#L114), and the twist place law and the validity of $v$ are in [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L207). In the formal proof, the invariance hypothesis on $f$ is introduced and not used (line 94). We have read the statements, not the proofs, of the law at a double step, the law at the last steps and the lemma on the ramified operator. We have not unfolded the local twisting operator and the ramified condition; their descriptions above follow their names and the statements that use them.
