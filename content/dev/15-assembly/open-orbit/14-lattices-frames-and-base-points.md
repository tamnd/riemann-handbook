---
title: Lattices, frames and base points
decls:
  - GlobalTheory.Fam.LatShape.exists_shape_integral_in_normal_frames_alt
  - GlobalTheory.T.local_component_measure_identity_alt_bis
  - GlobalTheory.Fam.lattices_frames_basePoints_exist_alt
  - GlobalTheory.T.local_component_vector_relation_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattices, frames and base points

This section proves step 6 of [the Theorem on core data of a point](/entry/core-data-of-point/). Given the rational data, the measures, the first level data and the type data of a geometric family, we must find the lattices $N_j$ of the spaces $Y_j$, the base points $b_j$ and a twist $d_T$, together with local frames at the places of $P_g$ and $Q$ that fit all of these. The frames come first, from the local structure of a split place. The lattices are then chosen so that the frames are integral for them. A shape result of another chapter fixes the twist. At the end the base points move the package lattices to the new lattices off the level places.

We keep the notation of [the section on true family data](/entry/all-true-family-datum-alt/). $W$ satisfies the package hypotheses, $u$ is a word and $T_u$ its twist number. The geometric datum is $a$ with the line vector $\zeta_0$, $y$ are rational data, $m$ measures, $v$ level data with level places $P_G$ and twist places $P_T$, and $o$ type data. At each place $\mathfrak P$ of $P_g$ or $Q$ we have local data over a split nonarchimedean local field $k_{\mathfrak P}$, and a family of bases that is $1$ off $P_g$. $\Lambda_Y^j$ is the lattice of $Y_j$ of the package and $\beta_Y^j$ its frame.

**Definition 4.14.1 (Self-dual lattice, integral frame).** A lattice $N$ of a hermitian space $S$ over the ring of integers $\mathcal O_E$ is *self-dual* if $y \in N$ exactly when $\langle x, y \rangle \in \mathcal O_E$ for all $x \in N$. A frame $F$ of $S$ at a split place $q$ is *integral* for $N$ if, for $y \in k_q^n$, $y$ is integral exactly when $F y$ lies in the completion of $N$ at $q$.

**Definition 4.14.2 (Normal frames).** At a place $\mathfrak P$ of $P_g$ or $Q$, *normal frames* are frames $F_Y^j$ of the spaces $Y_j$ over $k_{\mathfrak P}$ and units $s_j$ such that the Bessel frame conditions and the Jacquet frame conditions hold for $y$, and the local image of the twist element $\tau$ sends $\zeta_0$ to a multiple of the Bessel vector.

We use the following standing hypotheses, which hold at every use. The conditions on the common datum hold. The twist condition of $y$ holds, $\langle \zeta_0, \zeta_0 \rangle = T_u$, $v.\tau = y.\tau$, $v.N_T = L_T$ and $o.\zeta_0 = \zeta_0$, and $L_T$ is self-dual. $P_G$ is the set of places under $P_g$ and $P_T$ the set of places that divide $T_u$. The pre-type condition holds for $v$ and $o$, and the orthogonality condition holds off $P_T$.

**Theorem 4.14.3 (Integral lattices in normal frames).** Under the standing hypotheses, assume also that $P_G$ and $P_T$ are disjoint. Let normal frames $F_Y$ and units $s$ be given at each place of $P_g$ or $Q$. Then there are lattices $N_j$ of $Y_j$, a finitely supported twist $d_T$, and lattices $M$ and frames $\beta_0$ on the Bessel spaces of $y$, such that:

1. the shape condition holds for $v$ and $o$ updated by $N$, $d_T$, $M$ and $\beta_0$;
2. each matrix in the support of $d_T$ has the required form at $P_T$;
3. $N_j$ is self-dual for $j < m$;
4. at each place of $P_g$ or $Q$, each frame $F_Y^j$ is integral for $N_j$.

Lean: `GlobalTheory.Fam.LatShape.exists_shape_integral_in_normal_frames_alt` (also `GlobalTheory.T.local_component_measure_identity_alt_bis`, a second name).

*Proof.* We first choose the lattices to fit the frames, and then let the shape result choose the twist.

1. Let $I$ be the set of places of $P_g$ or $Q$. It is finite, and distinct elements of $I$ lie over distinct places of the base field, so the local fields $k_{\mathfrak P}$ for $\mathfrak P \in I$ are independent.
2. The scales of the normal frames are nonzero, and so is the norm $\xi$ of each split place. Both follow from the unit conditions of the normal frames.
3. Fix $j$. For $j < m$ the package hypotheses give a self-dual lattice $L_0$ of $Y_j$. A result of another chapter moves a self-dual lattice so that given frames at finitely many independent split places become integral, and keeps it self-dual. Apply it to $L_0$ and the frames $F_Y^j$ at the places of $I$. This gives $N_j$ with clauses 3 and 4.
4. Do the same for the Bessel spaces. For each $j$ and each Bessel index, a result of another chapter gives a self-dual lattice $L_0$ of the Bessel space $V_0$. The local data give core frames at each place of $I$. Moving $L_0$ gives a self-dual lattice $M_j$ in which the core frames are integral.
5. Four results of another chapter give the remaining local facts for the shape condition: the values off $P_T$, a bound and its reverse, and a splitting equation at the places of $I$.
6. Let $G'$ be the set of places of the base field under the places of $I$. It is disjoint from $P_T$: under $P_g$ by hypothesis, and under $Q$ by the level condition.
7. [The see-saw lattice shape theorem](/entry/see-saw-lattice-shape-exists-proof/), applied to the common datum, to $v$ with level places $G'$ and lattices $N$, and to $o$ with lattices $M$, gives $N$, $d_T$, $M$, $\beta_0$ with the shape condition and the form of $d_T$. The lattices of step 3 and 4 are kept. $\square$

**Theorem 4.14.4 (Lattices, frames and base points).** Under the standing hypotheses, there are lattices $N_j$ of $Y_j$, elements $b_j \in G_f(Y_j)$, a finitely supported twist $d_T$, and lattices $M$ and frames $\beta_0$ on the Bessel spaces of $y$, such that:

1. the shape condition holds for $v$ with $N$, $d_T$ and for $o$ with $M$, $\beta_0$;
2. each matrix in the support of $d_T$ has the required form at $P_T$;
3. for $j < m$, $N_j$ is self-dual, and $b_j$ moves $\Lambda_Y^j$ to $N_j$ at each set of places outside $P_G$;
4. at each place $\mathfrak P$ of $P_g$ or $Q$ there are normal frames $F_Y$ that are integral for the $N_j$, and $b_j$ moves the frame $\beta_Y^j$ to $F_Y^j$ times the basis family, after an ordering of the index set.

Lean: `GlobalTheory.Fam.lattices_frames_basePoints_exist_alt` (also `GlobalTheory.T.local_component_vector_relation_alt`, a second name).

*Proof.* We construct the frames, then the lattices, then the base points.

1. $T_u$ lies in no place under $P_g$. Indeed $T_u$ and the primes $g_k$ that define $P_g$ are distinct primes, so they are coprime. So $P_G$ and $P_T$ are disjoint.
2. The same argument with the level condition shows that $T_u$ lies in no place of $Q$.
3. At each $\mathfrak P$, a result of another chapter on the rational decompositions over a split local field gives normal frames $F_Y$ and units $s$. It uses the twist condition of $y$, the norm of $\zeta_0$ and step 2.
4. The Theorem on integral lattices in normal frames, with steps 1 and 3, gives $N$, $d_T$, $M$, $\beta_0$ with clauses 1 and 2, the self-duality of $N_j$, and the integrality of $F_Y$ for $N_j$.
5. A result of another chapter on base points gives $b_j \in G_f(Y_j)$. Since $\Lambda_Y^j$ and $N_j$ are both self-dual, they are locally conjugate at every place, and the local conjugating elements can be chosen to move $\beta_Y^j$ to the integral frame $F_Y^j$ at the places of $P_g$ and $Q$. This gives the moves of clause 3 and the frame condition of clause 4.
6. The normal frames of step 3 are the first part of clause 4, and steps 4 and 5 give the rest. $\square$

The base points $b_j$ are the only place where the self-duality of the package lattices is used. The frames at the places of $P_g$ and $Q$ are fixed first, and every later choice respects them. This is what makes the local groups $G_1, \dots, G_n$ of the family readable from the base points.

**Remark 4.14.5 (Formalization).** The theorems are at [ExistsShapeIntegralInNormalFrames.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsShapeIntegralInNormalFrames.lean#L24) and [LatticesFramesBasePointsExist.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LatticesFramesBasePointsExist.lean#L39). The second names are relays at [LocalComponentMeasureIdentityAltBis.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalComponentMeasureIdentityAltBis.lean#L16) and [LatticesFramesBasePointsExistStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LatticesFramesBasePointsExistStatement.lean#L16). In the second file, step 1 is the lemma `level_prime_not_mem_under_Pg_alt` at line 20, the disjointness is at line 43, step 2 at line 46, the normal frames at lines 47 to 49, step 4 at line 50, step 5 at line 52 and the assembly at line 56. Some details:

- The names mislead. `local_component_vector_relation_alt` speaks of a vector relation, and the nearest clause is the relation for $\tau$ inside the normal frames. `local_component_measure_identity_alt_bis` and `local_component_measure_identity_alt_alt` (step 5) speak of a measure identity, but their conclusions are about lattices, frames and base points.
- In the same way the four lemmas of step 5 of the first proof, `local_component_measure_value_alt`, `local_component_measure_bound_alt`, `local_component_measure_scalar_alt` and `local_component_measure_equation_alt` (lines 83 to 86), state nothing about measures.
- The shape theorem is applied at line 98 with the level places replaced by the new set $G'$, which contains the places under $Q$ as well as those under $P_g$. One of its conclusions is discarded (the `-` in the pattern at line 98).
- The disjointness of $P_G$ and $P_T$ is a hypothesis of the first theorem and is proved again in the second, after it was already proved in CoreDataOfPoint.lean.
- Step 5 of the second proof describes `local_component_measure_identity_alt_alt` by its conclusion. We have not opened its proof, nor the results of steps 3 and 5 of the first proof, nor unfolded the shape condition, the pre-type condition and the move condition of frames.
