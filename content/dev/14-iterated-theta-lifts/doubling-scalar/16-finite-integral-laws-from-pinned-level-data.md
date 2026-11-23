---
title: Finite integral laws from pinned level data
decls:
  - GlobalTheory.SeeSawLaws.gLaws
  - GlobalTheory.T.seeSawUnfolded_support_and_value_at_fixed_level
  - GlobalTheory.SeeSaw.placeLaws_finiteIntegrals
  - GlobalTheory.T.seesaw_place_laws_give_finite_integral_laws
  - GlobalTheory.SeeSaw.pins_finiteIntegrals
  - GlobalTheory.T.seeSaw_latticeFramePins_finiteIntegralLaws
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finite integral laws from pinned level data

The last section proved the twist place law for all tuples. The section on [see-saw laws at twist places](/entry/laws-of-pin-resc/) proved the laws at the places of a decoration. This section adds the laws at the level places, collects all the place laws, and derives from them the *finite integral laws*: the cells of each integrand are finite in number, and the double step and last step integrals are a constant times a period. The constants are chosen once, from pinned local data and a lattice shape, and serve every family of tuples. The result is used in [the laws of the links of the geometric rows and columns](/entry/laws-links-of-geo-rows-cols-alt/), for the multiplicity condition in branch 3 of the [unitary hypotheses](/proof/unitary-hypotheses/).

**Setting.** We keep the notation of the last three sections: common see-saw data $c$, data $v$ with twist places $P_T$ and lattices $N_j$ and $N_T$, a tuple $t$ and a decoration $w$ of $t$ with set of places $Q$. The data $v$ also carry a finite set $P_G$ of *level places*, disjoint from $P_T$. For each $j$ they carry a compact open subgroup $J_j$ of the group of $V_j$ at $P_G$, combinations $e_G(j)$ and $e_{G,T}(j)$ at $P_G$, coefficients $d_G(j)$ at $P_G$ and a constant $c_G(j)$. For a family $a$ of complex numbers, let $v[a]$ be $v$ with $c_G(j)$ replaced by $a_j$. Let $K_j$ be the set of products $\kappa k$ of the group of $V_j$, with $\kappa$ in the stabiliser of $N_j$ at the places off $P_G$ and $k \in J_j$. For a closed subgroup $R$ and a Haar measure $\rho$ on its finite adelic points, the *volume ratio* is $\mathrm{vr}_j(R, \rho) = \mu_j(K_j) / \rho(K_j \cap R)$, where $\mu_j$ is the Haar measure of $c$. For an inner position $(j, \sigma)$, let $\mathrm{vr}(j, \sigma)$ be the product of $\mathrm{vr}_{j+1}$ for the Jacobi subgroup and $\mathrm{vr}_{j+2}$ for the Bessel subgroup of the position, with the measures of $c$.

**Definition 2.16.1 (Laws at the level places).** Let $t$ be a tuple. The data $v$ satisfy the *support law* at the level places for $t$ if, for every inner position $(j, \sigma)$, every $\Psi_1$ vacuum for $(N_j, N_{j+1})$ at $P_G$ and every $\Psi_2$ vacuum for $(N_{j+1}, N_{j+2})$ at $P_G$, the following hold for $x$ in the group at $P_G$.

1. If the flattened function of $\omega_j(1, x)\, e_G(j) \cdot \Psi_1$ for the Bessel to Fourier-Jacobi map is not zero, then $x = r k$ with $r$ in the Jacobi subgroup at $P_G$ and $k \in J_{j+1}$.
2. If $\mathrm{ctr}\big(e_G(j) \cdot \Psi_1,\ \omega_{j+1}(1, x)\, e_G(j+1) \cdot \Psi_2\big) \neq 0$, then $x = r k$ with $r$ in the Bessel subgroup at $P_G$ and $k \in J_{j+2}$.

The data $v$ satisfy the *value law* at the level places for $t$ if, for the same $\Psi_1, \Psi_2$,
$$\mathrm{ctr}\big(e_G(j) \cdot \Psi_1,\ e_G(j+1) \cdot \Psi_2\big) = c_G(j)\ \mathrm{bc}\big(d_G(j), d_G(j+1), \mathrm{ctr}(\Psi_1, \Psi_2)\big),$$
and if, for $j + 2 = m$, $\Psi_1$ vacuum for $(N_j, N_{j+1})$ and $\Psi_2$ vacuum for $(N_{j+1}, N_T)$ at $P_G$,
$$\mathrm{lst}\big(e_G(j) \cdot \Psi_1,\ e_{G,T}(j) \cdot \Psi_2\big) = c_G(j)\ \mathrm{bc}\big(d_G(j), d_G(j+1), \mathrm{lst}(\Psi_1, \Psi_2)\big).$$

The support law does not read the constants $c_G$. So $v$ satisfies it if and only if $v[a]$ does.

*Pinned level data.* A *local level datum* $G_i$ for $v$ is a split point $q_i$ of a nonarchimedean local field $k_i$, with a symmetric chain datum over $k_i$, frames and local combinations $e_g(i, j)$, $e_{g,T}(i)$ and $c_g(i, j)$. A family $G_1, \dots, G_n$ is *pinned* if the places of the $q_i$ are distinct and their union is $P_G$, if $J_j$ is the set of elements whose local matrices lie in the local level groups of the chain data, and if $e_G(j)$, $e_{G,T}(j)$ and $d_G(j)$ act on theta functions as the composites over $i$ of the local combinations. The characters of a tuple $t$ *fit* $G_i$ if there are tame characters $\mu_j$ of $k_i^\times$ that agree on units with the characters of the chain datum, such that the local components at $q_i$ of the Weil characters of the Bessel data of $t$ are $\mu_{j+1}^{-1}$ and $\mu_{j+2}^{-1}$, and the other Weil characters are their inverses on units.

**Theorem 2.16.2 (Laws at the level places).** Assume the validity of $c$ and $v$, and let $G_1, \dots, G_n$ be pinned. Then there are constants $a_j \neq 0$ such that, for every valid tuple $t$ that satisfies WeilOK for $v$ and whose characters fit every $G_i$, the data $v[a]$ satisfy the support law and the value law at the level places for $t$.

Lean: `GlobalTheory.SeeSawLaws.gLaws` (also `GlobalTheory.T.seeSawUnfolded_support_and_value_at_fixed_level`, a second name).

*Proof.* We use two theorems on the unfolded see-saw at a fixed level.

1. *The value law.* The theorem on the unfolded value with common constants at a fixed level gives $a$ with $a_j \neq 0$, and the value law for $v[a]$ and every valid $t$ that satisfies WeilOK.
2. *Local inputs.* The theorem on the unfolded support at the level places takes three local inputs. The first is the support of the first half at a level place. It follows from the local model formula of the Weil datum, the local model of the Bessel to Fourier-Jacobi flat map and the symmetric collapse at all positions. The second is the support of the second half of a symmetric chain at a level place. It follows from the same inputs, from the local model of the Fourier-Jacobi to Bessel flat map and from the line contraction at a split place. The third is the convergence of the flat theta maps to theta functions.
3. *The support law.* With these inputs, the theorem on the unfolded support gives the support law for $v$ and every valid $t$ whose characters fit every $G_i$. By the remark after the definition, it holds for $v[a]$. $\square$

**Definition 2.16.3 (Place laws).** A decoration $w$ of $t$ satisfies the *place laws* for $v$ if it satisfies all of the following:

1. the form conditions of $w$ for $v$: the places $Q$ are disjoint from $P_G$ and $P_T$, the theta functions of $t$ factor through the combinations of $v$ and $w$, and the row functions lie in the sets of $w$;
2. WeilOK for $v$;
3. the support law off the level places;
4. the support law and the value law at the level places;
5. the vacuum law at the twist places: the contractions and the last see-saw data of functions that are vacuum off $P_T$ are bi-vacuum off $P_T$;
6. the twist place law of the last section;
7. the iterated integral law, the last step law and the law of finite cells at $Q$;
8. the equation of constants: the constant $c_V(j)$ of $t$ is $\mathrm{vr}(j, \sigma)\, s(j)\, s(j+1)\, c_Q(j)\, c_G(j)\, c_T(j)$ at inner positions, and the same without $\mathrm{vr}$ at the last steps, where $s(j)$ are the scales of $w$;
9. top sphericity: the top functions of $t$ are invariant under the stabiliser of $N_T$ at $P_T$.

For a family of tuples $t_s$, the *finite integral laws* are three statements.

- *Local finiteness.* For each $s$ and each inner position $(j, \sigma)$ there are a compact open subgroup $K_1$ and a finite set $T_1$ of the finite adelic group of $V_{j+1}$ such that, for every point $h_1$ where the flattened integrand is not zero, $h_1$ lies in a cell of $T_1$ and $K_1$ over the Jacobi subgroup, and $K_1$ acts on the theta functions of $t_s$ by inverse scalars.
- *The double step value.* For each inner position, there is a real constant $C$, the same for all $s$, such that the integrand of the double step of $t_s$ has iterated quotient integral equal to $c_V(j)$ times the Bessel period of the two-step lift with constant $C$.
- *The last step value.* For $j + 2 = m$, there is a real constant $C$, the same for all $s$, such that the period of the last lift equals $c_V(j)$ times the top period of the two-step lift with constant $C$.

**Theorem 2.16.4 (Place laws give finite integral laws).** Assume the validity of $c$ and $v$, and that at the last step the measure of $V_{j+1}$ is the push forward of the measure of the top datum. Let $t_s$ be valid tuples, and let $w_s$ be decorations of $t_s$ that satisfy the place laws for $v$. Then the finite integral laws hold for the family $t_s$.

Lean: `GlobalTheory.SeeSaw.placeLaws_finiteIntegrals` (also `GlobalTheory.T.seesaw_place_laws_give_finite_integral_laws`, a second name).

*Proof.* Each law is one theorem of the global theory.

1. *Local finiteness.* The theorem on local finiteness from the tuple conditions gives it for each $t_s$. It uses the form conditions, the support law off the level places, the support law at the level places and the law of finite cells.
2. *The double step value.* The theorem on the value of the double step of the see-saw finite integrals gives it, from all the place laws. Its inputs are the identity of a double step with two theta column lifts, the convergence of the flat theta maps and the commutation of the see-saw Weil bi-action.
3. *The last step value.* The theorem on the double lift period at the last two steps gives it, from the place laws and the hypothesis on the last measure. Its inputs are the last law of the last steps, the theta identity of the last see-saw, the convergence of the flat theta maps and the commutation of the Weil bi-action. $\square$

**Theorem 2.16.5 (Finite integral laws from pinned level data).** Assume the validity of $c$ and $v$, and that the last measure is a push forward as above. Let $o$ be a lattice shape datum that fits $v$, and let $G_1, \dots, G_n$ be pinned level data for $v$. Then there are units $\varepsilon_j(i)$, bi-operators $\mathrm{op}_j$, reals $r_j(i) > 0$, integers $e_j(i)$ and constants $a_j \neq 0$ such that:

1. $\mathrm{vr}(j, \sigma) \neq 0$ for every inner position;
2. $v' = v[S_\varepsilon, \mathrm{op}][a]$ is valid;
3. let $t_s$ be tuples and $w_s$ decorations of $t_s$ such that, for each $s$: $t_s$ is valid; $w_s$ satisfies the form conditions for $v'$; $t_s$ satisfies WeilOK and top sphericity for $v$; $t_s$ is unramified at the places off $P_G$ and $Q$, and its Weil representations are unramified at $P_T$; the characters of $t_s$ fit every $G_i$; $w_s$ satisfies the iterated integral law, the last step law and the law of finite cells for $v$; $c_T(j) = \mathrm{mono}(r_j, e_j, \chi_{W, j, \rho})$ for all Bessel positions $(j, \rho)$; and $w_s$ satisfies the equation of constants for $v'$. Then the finite integral laws hold for the family $t_s$.

Lean: `GlobalTheory.SeeSaw.pins_finiteIntegrals` (also `GlobalTheory.T.seeSaw_latticeFramePins_finiteIntegralLaws`, a second name).

*Proof.* We choose the constants and then assemble the place laws for $v'$.

1. *The twist data.* [The twist place law for all tuples](/entry/law-level-prime-all/) gives $\varepsilon$, $\mathrm{op}$, $r$ and $e$, the validity of $v[S_\varepsilon, \mathrm{op}]$, and the twist place law for $v[S_\varepsilon, \mathrm{op}]$ for every tuple and decoration that meet its conditions.
2. *The level constants.* The first theorem gives $a$.
3. *Validity of $v'$.* Validity does not read the constants $c_G$, so $v'$ is valid by step 1.
4. *The volume ratios.* The finite adelic group of $V_j$ is the product of its points at $P_G$ and its points off $P_G$, and the two factors commute. Under this product, $K_j$ is the image of $J_j$ times the stabiliser of $N_j$ off $P_G$. Both factors are compact open, since $N_j$ is self-dual and by the validity of $v$. So $K_j$ is open, compact and contains $1$, and $\mu_j(K_j) > 0$. The Jacobi and Bessel subgroups are closed, so $K_j \cap R$ is compact and open in $R$ and contains $1$, and $\rho(K_j \cap R) > 0$. Hence each ratio is positive, and $\mathrm{vr}(j, \sigma) \neq 0$.
5. *The family.* Let $t_s$ and $w_s$ be as in item 3. By the last theorem, applied to $v'$, it suffices to show that $w_s$ satisfies the place laws for $v'$. Fix $s$.
6. *Laws given by hypothesis.* The form conditions and the equation of constants are hypotheses for $v'$. WeilOK, top sphericity, the iterated integral law, the last step law and the law of finite cells are hypotheses for $v$. They read only fields that $v$ and $v'$ share.
7. *The support law off the level places.* The theorem on the see-saw support off the level, from the lattice shape, gives it for $v$. It uses that $t_s$ is valid, that $Q$ is disjoint from $P_T$ and that $t_s$ is unramified off $P_G$ and $Q$.
8. *The vacuum law.* The theorem on the unfolded vacua of the shape gives it for $v$ and $t_s$.
9. *The twist place law.* The places of $P_T$ are not in $P_G$, by the validity of $v$, and not in $Q$, by the form conditions. So $t_s$ is unramified at $P_T$ on its Bessel data. Step 1 then gives the twist place law for $v[S_\varepsilon, \mathrm{op}]$. It does not read $c_G$, so it holds for $v'$.
10. *The laws at the level places.* Step 2 gives the support law and the value law for $v'$ and $t_s$.

The laws of steps 6, 7 and 8 are stated for $v$ and used for $v'$. This is correct because they read no field that the changes of $S$, $\mathrm{op}$ and $c_G$ touch. $\square$

Item 1 is stated for $v$, not $v'$. The two ratios are equal, since they read only $N_j$, $J_j$ and the measures.

**Remark 2.16.6 (Formalization).** The laws at the level places are at [SeeSawUnfoldedSupportAndValueAtFixedLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawUnfoldedSupportAndValueAtFixedLevel.lean#L44), with the two local support inputs of step 2 at lines 39 and 28. The place laws theorem is at [SeesawPlaceLawsGiveFiniteIntegralLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeesawPlaceLawsGiveFiniteIntegralLaws.lean#L21). The last theorem is at [SeeSawLatticeFramePinsFiniteIntegralLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawLatticeFramePinsFiniteIntegralLaws.lean#L109), with the open compact set $K_j$ of step 4 at line 29, the positivity of the ratios at lines 69 and 84, the validity of $v'$ at line 91, the transfer of WeilOK at line 94 and the change of unramified places of step 9 at line 98. The second names are restatements in the matching files with the suffix `Statement`. The place laws, the laws at the level places and the volume ratio are in [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L272); the finite integral laws are in [ValLastX.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean#L158); pinned level data and the fit of characters are in [HzUnit.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/HzUnit.lean#L88); and the fit of a lattice shape is in [VacOfShape.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/VacOfShape.lean#L88). In the formal proof of the first theorem, the support law is proved for $v$ and used for $v[a]$ without a rewrite, since the two laws are equal by definition. We have read the statements, not the proofs, of the theorems on the unfolded value and support, the local support inputs, local finiteness, the double step value, the last step value, the support off the level and the unfolded vacua. We have not unfolded the flat maps, the cells, the two-step lift and the periods; their descriptions above follow their names and the statements that use them.
