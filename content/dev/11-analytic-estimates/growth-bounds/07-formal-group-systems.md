---
title: Formal group systems
decls:
  - Formalism.MainNotions.FormalGroupSystem.Pf.rests
  - Formalism.MainNotions.FormalGroupSystem.Pf.prv_and_kernel_commutation_up_to_units_of_rests
  - Formalism.MainNotions.FormalGroupSystem.Pf.packet_statements_hold
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Formal group systems

This section proves the packet statements: eleven valuation bounds for a chain of kernel maps between modules of lattice functions, built from theta series of formal groups. They hold for every admissible formal group system. The packet statements are used by [the service bound for sums over primes](/entry/sum-over-primes-service/) in the chapter on sharp restriction of this volume. The lattice functions and the Hecke operators $y_v$ are those of Section 6.

### Systems and pending data

Let $p$ be a prime.

**Definition 5.7.1 (Formal group system).** A *formal group system* at $p$ consists of the following objects.

1. A datum $G$ at $p$ (Section 6), over a discrete valuation ring $\mathcal{O}$ with fraction field $K$.
2. A filling of $G$: integers $t$ and $m_* \geq 0$, and for each $j \leq m_*$ a system of places $P_j$ with the same places as $G$, and a set $T_v$ and weights $w_v$ at each place. The filling satisfies a standard condition at each place.
3. For each $j$, a module $\mathrm{Fm}_j$ of lattice functions for $P_j$ and levels of $P_j$, an integral submodule $\mathrm{Int}_j$, its $K$-span $\mathrm{FQ}_j$, and Hecke operators $T_{v,i,j}$ on $\mathrm{Fm}_j$. At level $0$, $\mathrm{Fm}_0$ is the module of lattice functions of $G$.
4. Kernel maps $K_j : \mathrm{Fm}_j \to \mathrm{Fm}_{j+1}$, linear over $K$, and their composites $\kappa_j : \mathrm{Fm}_0 \to \mathrm{Fm}_j$.
5. A uniformizer $\varpi$ of $\mathcal{O}$ and $e \geq 0$ with $p = \varpi^e$ up to a unit.
6. Integers $d_j$ such that $v_p$ of the order of each stabiliser at level $j$ is at most $d_j$.
7. A basis datum $\omega_v$ for each place.

For $F \in \mathrm{Fm}_j$ and a real $g$, we say that *$F$ has valuation at least $g$* if $F \in \varpi^{\lceil ge\rceil}\,\mathrm{Int}_j$. The filling fixes real numbers $g_{v,j}$, $g^0_{v,j}$, $P_{v,j}$, $S_v$ and $\alpha_v$ for each place $v$ and level $j$. We do not unfold them; they are the gains, the base gains, the losses, the shift and the even weight at $v$.

**Definition 5.7.2 (Pending data).** *Pending data* for a formal group system consist of a field $K_c$ that contains $K$ and the field of $p$-adic Witt vectors, a valuation ring $\mathcal{O}_c$ of $K_c$ of rank one that contains the Witt vectors and meets $K$ in $\mathcal{O}$, a power series $\beta$ in two variables, a finite set of representatives of the classes of lattice tuples at each level, with positive stabiliser orders, and for each pair of lattice tuples at levels $j$ and $j + 1$ a type of frames. Each frame $\varphi$ gives a theta series $\Theta_\varphi$, a linear substitution, and a kernel series. The kernels $\ker_j$ attach to a class at level $j$ and a tuple at level $j + 1$ a linear map from polynomials at level $j$ to polynomials over $K_c$ at level $j + 1$.

### Admissibility and the packet statements

**Definition 5.7.3 (Admissible system).** A formal group system with pending data is *admissible* if these twelve conditions hold. (The formal statement has thirteen parts: condition 2 is two parts.)

1. The Dwork lemma holds at every prime.
2. The theta series $\Theta_\varphi$ at each place satisfy a local extension condition, and the $\Theta_\varphi$ satisfy an extension generator condition, both relative to $\beta$.
3. The power series $\beta$ has a fixed property.
4. For each frame, the coefficients of the column products applied to the theta series have valuation at least $0$.
5. $K_j$ maps $\mathrm{FQ}_j$ into $\mathrm{FQ}_{j+1}$.
6. The kernel maps have an expansion over representatives: for $j + 1 < m_*$, $K_jF$ is a unit times the sum of $\ker_j$ applied to the values of $F$, weighted by the inverse stabiliser orders; at the last level the same holds with weights of $p$-adic valuation at most $d_j$, and the expansion is compatible with the Hecke operators.
7. The theta series $\Theta_\varphi$ equal a fixed series up to a unit factor and a power of $p$ fixed by the lengths of the tuples.
8. The kernels are invariant under the action of the levels.
9. Sums over edges, over representatives and weighted by inverse stabiliser orders, can be taken from either end of the edges.
10. For each pair of tuples joined by edges there is a frame for which an integrality bound for the kernel holds.
11. The Hecke operators $y_v$ commute and preserve the module $M$ of Section 6.
12. A lower bound holds at level $0$ at each place and level.

**Definition 5.7.4 (Packet statements).** The *packet statements* for an admissible system are the following, for all places $v$ and all $j < m_*$.

1. $K_j$ maps $\mathrm{Int}_j$ to elements of valuation at least $-d_j$.
2. The theta series at each place satisfy a local conclusion for the basis datum $\omega_v$.
3. After the substitution $\varpi \mapsto$ a root of $p$ of order $p^2 - 1$, each theta series lies in a product of fixed series attached to the places (the *expansions multiply*).
4. $K_j$ maps $\mathrm{Int}_j$ to elements of valuation at least $\sum_vg^0_{v,j+1} - d_j$.
5. The coefficients of the column products applied to the theta series have valuation at least $\sum_vg^0_{v,j+1}$.
6. A lower bound holds at level $j$ and place $v$ with $g^0_{v,j+1}$.
7. $K_j$ maps $\mathrm{Int}_j$ to elements of valuation at least $g_{v,j+1} - \alpha_v + \sum_{v' \neq v}g^0_{v',j+1} - d_j$.
8. The Hecke operators $T_{v,i,j+1}$ with $1 \leq i \leq r$ preserve $\mathrm{Int}_{j+1}$, and $T_{v,i,j+1}K_j$ maps $\mathrm{Int}_j$ to valuation at least $g_{v,j+1} + \sum_{v' \neq v}g^0_{v',j+1} - d_j$.
9. There are units $u_l$ and elements $m_l$ of fixed valuation such that a Hecke polynomial $Z_v$ in the $T_{v,i}$ satisfies
$$Z_v\,\kappa_{j+1}(F) = p^{P^Z_{v,j+1}}\,\kappa_{j+1}(y_vF), \qquad F \in \mathrm{FQ}_0,$$
with integral coefficients, and $Z_vK_j$ satisfies the bound of part 8.
10. $S_v \leq m_*\gamma_p\sum_{s \in T_v}\alpha_{v,s}$, and for every set $V$ of places and every $F$ in the product ideal of the $y_v^{m_*}$, $v \in V$, with shifts $S_v$, the element $\kappa_{m_*}(F)$ has valuation at least
$$\sum_{j=1}^{m_*}\Big(\sum_{v \in V}\max(g_{v,j} - P_{v,j}, g^0_{v,j}) + \sum_{v \notin V}g^0_{v,j}\Big) - \sum_{j < m_*}d_j.$$
11. The bound of part 10 holds for all smaller gains, larger losses and shifts that satisfy the lower bounds of part 6 (the *low term bound*).

**Definition 5.7.5 (Kernel commutation up to units).** The system has *kernel commutation up to units* if, for each place $v$, there are units $u_l$ and elements $m_l$ of fixed valuation such that the normalized Hecke operators $e_{v,i}$ satisfy
$$e_{v,i,j+1}(K_jF) = u_{j+1}^i\,K_j\Big(\sum_{l \leq i}c_l\,e_{v,i-l,j}F\Big), \qquad F \in \mathrm{FQ}_j,$$
where $c_l$ is the elementary symmetric polynomial of degree $l$ evaluated at the $m_{j+1}q_{v,x}$, and part 9 holds with the normalized $\hat m_l = m_l/(u_1\cdots u_{l-1})$.

So the kernel maps commute with the Hecke operators, up to units and lower terms.

### The proof

**Definition 5.7.6 (Remaining inputs).** The *remaining inputs* for an admissible system are parts 2, 3 and 6 of the packet statements and an entry condition on the pending data.

**Lemma 5.7.7 (Remaining inputs).** Every admissible formal group system satisfies the remaining inputs.

Lean: `Formalism.MainNotions.FormalGroupSystem.Pf.rests`.

*Proof.* Part 2 is a theorem on the theta series of a formal group with the extension conditions. Part 3 is a product formula for the theta series. Part 6 follows from a first place bound, and the entry condition from a second place bound and a Hecke place bound; the three place bounds use a common constant and a jet condition. $\square$

**Proposition 5.7.8 (Packet statements and kernel commutation).** Every admissible formal group system that satisfies the remaining inputs satisfies the packet statements and has kernel commutation up to units.

Lean: `Formalism.MainNotions.FormalGroupSystem.Pf.prv_and_kernel_commutation_up_to_units_of_rests`.

*Proof.* Admissibility gives a form statement for the kernel maps and a Hecke condition. From the form statement, the entry condition and part 6 we get part 7, and with an integrality fact for restricted Hecke operators also part 8. Parts 7 and 8, the Hecke condition and condition 5 of admissibility give an alternate expansion of the kernel maps, which is kernel commutation up to units, and from it part 9. Part 1 follows from the form statement and condition 4. Parts 4 and 5 follow from the entry condition and part 6, part 4 with the form statement as well.

For part 11 there are two cases. If $e = 0$, then $p$ is a unit in $\mathcal{O}$. Each place forces $e \geq 1$, so there are no places, the product ideal lies in $\mathrm{Int}_0$, and part 1 at each level gives the bound, since the valuation condition does not depend on $g$ when $e = 0$. If $e \geq 1$, a lift bound from integrality gives part 11, from the form statement, the entry condition, part 9 and condition 11. Part 10 follows from part 6 and part 11. $\square$

**Theorem 5.7.9 (Packet statements).** Every admissible formal group system satisfies the packet statements.

Lean: `Formalism.MainNotions.FormalGroupSystem.Pf.packet_statements_hold`.

*Proof.* Apply [the Proposition](/entry/prv-and-kernel-commutation-up-to-units-of-rests/) with [the Lemma](/entry/rests/). $\square$

**Remark 5.7.10 (Formalization).** The packet statements are `Conclusion₂ D X Y` and admissibility is `admitted D X Y` (FormalGroupSystem.lean:771, 775). All their parts take a datum `_D` and do not use it (FormalGroupSystem.lean:546 to 708); only `adm8` passes `D` on, to the `SelectionLemmas.adm3` of Section 6, which also ignores it. The name `Conclusion₂` is used twice: for the eleven-part conjunction (line 775) and for the real number `Sys.Conclusion₂ v j`, the loss $P_{v,j}$ (line 327). Several names do not describe their content: `ArchimedeanSignatureMatching` is the expansion condition 6 (line 587), `MinkowskiCounting` is the invariance condition 8 (line 597), and `DegreeDichotomyWithModelBounds` is kernel commutation for all systems (line 782). Condition 1, the Dwork lemma at every prime, does not depend on the system (line 546); it is a hypothesis, not proved here. Part 2 comes from `theta_kernel_expansion` in MultisetValuation/CommonEigenvectorThird.lean:32, one of three theorems with this name. `Rests` (MultisetValuation/PrvAndKernelCommutationUpToUnitsOfRests.lean:70) has four fields; the proof of the Proposition unpacks admissibility and uses only conditions 4, 5 and 11 directly. In the case $e = 0$ the proof derives a contradiction from each place, so this case is vacuous whenever a place exists. The filling numbers `gB`, `gA`, `Pr`, `Sv`, `al`, `gam`, the predicates `SConcl`, `InProdA`, `LowAt`, `EntCondition`, `DworkLemma`, `ExtensionLocalCondition`, `ExtensionGeneratorCondition`, `BeProp`, `Std`, and the lemmas `formB`, `heckeCondition_of_adm`, `hecke_integral_of_forms`, `latticeChain_succ_of_partial`, `alternate_expansion_of_relations`, `theorem_of_alternate_form`, `lift_bound_of_integrality`, `ramifiedLattice_of_chain_estimates`, `slopeEstimate_of_lemmaB_slopeLine`, `theorem_A_entries_of_corollary`, `expansions_multiply`, `auxU_of_firstTheoremPlaceBound` and `restEnt_of` were not unfolded.
