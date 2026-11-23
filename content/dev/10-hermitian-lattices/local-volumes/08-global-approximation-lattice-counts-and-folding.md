---
title: Global approximation, lattice counts and folding
decls:
  - Formalism.L2.SG.Pf.SlabNDensePf.nilradical_strong_approximation
  - Formalism.L2.SG.Pf.NormSteps.levi_onto_reduction
  - Formalism.L2.SG.Closed.LatCount_holds
  - Formalism.L2.SG.Closed.MultPoly_holds
  - Formalism.L2.SG.Closed.FoldOKC_holds
  - Formalism.L2.SG.Closed.KExpansionC_holds
  - Formalism.L2.SG.Closed.KppOffC_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Global approximation, lattice counts and folding

Three facts about rational points make the local results global. Rational points of a unipotent radical are dense in its finite adelic points. The reduction of the Levi block at the places of good reduction is onto. The number of rational points in a compact set of the adelic group grows at most polynomially. This section states them and three closed statements that use them: folding of the Poincare series, the expansion of the kernel into terms, and the vanishing of the off diagonal terms of degenerate type. The closed statements feed the [local matching step](/step/theta-local-matching/).

### Strong approximation in the nilradical

Fix a setting $X$ for a datum $D$ and a word $u$. Let $G = G_\infty \times G_f$ be the adelic unitary group of $X$, and let $G(F) \subseteq G$ be the subgroup of rational points, embedded diagonally. For $u$ let $N_\infty(u) \subseteq G_\infty$ and $N_f(u) \subseteq G_f$ be the archimedean and the finite points of the unipotent radical attached to $u$.

**Definition 5.8.1 (Density of rational unipotents).** The *density property* holds if for every datum $D$, setting $X$, word $u$, point $n \in N_f(u)$ and open set $U \subseteq G_f$ with $n \in U$, there is $\nu \in G(F)$ with $\nu_\infty \in N_\infty(u)$, $\nu_f \in N_f(u)$ and $\nu_f \in U$.

Lean: `Formalism.L2.SG.Pf.SlabCoverPf.NDense` (also `Formalism.L2.SG.Pf.RegroupPf.NDense`, a second copy with the same body).

This is the form of [strong approximation](/learn/groups/#strong-approximation) for a unipotent group that the counting argument needs. Here the proof goes through the Cayley transform.

**Theorem 5.8.2 (Strong approximation in the nilradical).** The density property holds.

Lean: `Formalism.L2.SG.Pf.SlabNDensePf.nilradical_strong_approximation` (also `Formalism.L2.SG.Pf.SlabNDensePf.nDense_of`, the reduction to six inputs).

*Proof.* Let $n \in N_f(u)$ and let $U$ be an open set that contains $n$. Write $M(x)$ for the matrix of $x \in G_f$ in the frame of the setting. The first input (`pattern_of_nilradical`) says that $M(n) - 1$ has the block pattern of the nilradical. The Cayley inverse (`cayley_inverse_right`) then gives a matrix $Z$ over the finite adeles of $E$, with the same pattern, skew-Hermitian for the form of the frame, and with $\mathrm{cay}(Z) = M(n)$, where $\mathrm{cay}$ is the Cayley transform of the earlier section on [Haar measure in Cayley coordinates](/entry/haar-measure-in-cayley-and-exponential-coordinates/).

The congruence subgroups $K_g$ form a basis of neighbourhoods of $1$, so there is $g \geq 1$ with $n K_g \subseteq U$. By `level_of_close_element` there is $c \geq 1$ such that $n^{-1} y \in K_g$ for each $y$ whose matrix is congruent to $M(n)$ at level $c$. By Cayley continuity (`cayley_continuous`) there is $c' \geq 1$ such that $Z' \equiv Z$ at level $c'$ implies $\mathrm{cay}(Z') \equiv \mathrm{cay}(Z)$ at level $c$.

The approximation input (`skew_hermitian_approximation`) gives a matrix $Y$ with entries in $E$, with the nilradical pattern, skew-Hermitian, and congruent to $Z$ at level $c'$. Let $\nu = \mathrm{cay}(Y)$, a rational point. Since $Y$ is skew-Hermitian with the pattern, $\nu \in G(F)$ and $\nu_\infty \in N_\infty(u)$. The matrix $M(\nu_f) - 1 = \mathrm{cay}(Y) - 1$ has the pattern, so $\nu_f \in N_f(u)$ by the converse input (`nilradical_of_pattern`). Finally $M(\nu_f) = \mathrm{cay}(Y) \equiv \mathrm{cay}(Z) = M(n)$ at level $c$, so $n^{-1} \nu_f \in K_g$ and $\nu_f \in n K_g \subseteq U$. $\square$

### The Levi reduction is onto

**Definition 5.8.3 (Typed reduction).** A *typed reduction* for $X$ is a finite set $P$ of places, a finite field $\mathbb{F}_v$ for each $v \in P$ with $\# \mathbb{F}_v$ equal to $g_0$ or $g_1$, and ring maps $\mathrm{res}_v$ from the integral finite adeles of $E$ onto $\mathbb{F}_v$. The joint map to $\prod_v \mathbb{F}_v$ is onto, its kernel is the set of $x$ with $e x \equiv 0$ at the level of $X$, and the data contain additive characters $\psi_{0,v}$ of $\mathbb{F}_v$ whose product recovers the character of $X$. For $\kappa \in G_f$ the *reduced Levi matrix* at $v$ is the $k \times k$ matrix
$$\mathrm{leviM}(\kappa)_{v, ij} = \mathrm{res}_v\, h(b^\vee_i, \kappa\, b_j),$$
where $h$ is the Hermitian form and $b$, $b^\vee$ are the frame vectors of $X$. The *Levi reduction* $\mathrm{levi}(\kappa)_v \in \mathrm{GL}_k(\mathbb{F}_v)$ is $\mathrm{leviM}(\kappa)_v$ if its determinant is a unit, and $1$ in the other case.

Lean: `Formalism.L2.SG.TermOp.TypedRed` (also `Formalism.L2.SG.TermOp.levi`, the Levi reduction).

Let $H_f(u)$ be the finite part of the stabilizer group of $u$, and let $x_u \in G_f$ be the element of $X$ attached to $u$. For $h, h' \in H_f(u)$ put $\mathrm{col}(h, h') = (h x_u)^{-1} (h' x_u)$. A column system $cs$ for a finite set of lattices assigns to each lattice $\Lambda$ a base element $h_\Lambda \in H_f(u)$.

**Theorem 5.8.4 (The Levi reduction is onto).** Let $TR$ be a typed reduction and let $cs$ be a column system. For each lattice $\Lambda$ of the system and each $s \in \prod_{v \in P} \mathrm{GL}_k(\mathbb{F}_v)$ there is $h \in H_f(u)$ such that $\mathrm{col}(h_\Lambda, h)$ and $\mathrm{col}(h, h_\Lambda)$ lie in the level group $K$ of $X$ and $\mathrm{levi}(\mathrm{col}(h_\Lambda, h)) = s$.

Lean: `Formalism.L2.SG.Pf.NormSteps.levi_onto_reduction` (also `Formalism.L2.SG.Pf.NormSteps.LeviOntoS`, the statement).

*Proof.* The proof has four inputs. The first (`idempotent_places_exists`) is an integral idempotent $\varepsilon$, fixed by the involution, with $1 - \varepsilon \equiv 0$ at the level $g$ of $X$, such that each $1 + g s$ with $s$ integral becomes a unit after multiplication by $\varepsilon$. The second (`exact_dual_frame_exists`) gives, from such an idempotent, a dual frame for $u$ with an idempotent $\eta$. The third (`integral_matrix_lift_exists`) gives, for each $s$, integral matrices $C$ and $C'$ with $\eta C C' = \eta$, $\eta C' C = \eta$ and reduction of $C$ at each $v$ equal to $s_v$. The fourth (`levi_element_exists`) gives, from the dual frame and such a pair, an element $\kappa$ of the level group $K$ that fixes the vectors of the fixed space of $u$ and has $\mathrm{leviM}(\kappa)_v$ equal to the reduction of $C$ at each $v$. Since $s_v$ is invertible, the Levi reduction of $\kappa$ is $s$. The step `leviOntoS_of_steps` then turns $\kappa$ into the element $h$ of the statement. We did not unfold the construction of the dual frame, of $\kappa$ and of $h$. $\square$

### Counting rational points

Let $I$ be an automorphic instance with field $F$ of degree $f = [F : \mathbb{Q}]$ and rank $n$. Let $L_f$ be its lattice and let $K \subseteq G_f$ be the stabilizer of $L_f$. For $x \in G$ let $\tau_1(x)$ be the size invariant of $x$: the minimum of $1/2$ and the infimum, over sublattices $B$ of the lattice of $x$ with basis $b$ of size $j$, of $\bigl(\prod_v \det \mathrm{Gram}_v(b) / [B : \langle b\rangle]\bigr)^{1/(2fj)}$.

**Theorem 5.8.5 (Lattice count).** Let $x, y \in G$ with $\tau_1(x) > 0$ and $\tau_1(y) > 0$, let $r_v \geq 0$ for each archimedean place $v$, and let $S$ be a finite set of rational points such that for each $\gamma \in S$ the finite part of $x^{-1}\gamma y$ lies in $K$ and the Cartan distance of its component at $v$ is at most $r_v$. Then
$$\# S \leq \left(\frac{3\sqrt{n}}{\tau_1(x)\, \tau_1(y)}\right)^{2 n^2 f} \exp\Bigl(2 n^2 \sum_v r_v\Bigr).$$

Lean: `Formalism.L2.SG.Closed.LatCount_holds` (also `Formalism.L2.SG.Count.LatCount`, the statement).

*Proof.* This is [the lattice count for all instances](/entry/lattice-count-all/) applied to $I$. That statement uses a second definition of $\tau_1$, an infimum over the same sublattices written with another index type. The two infima agree under the equivalence of index types, so the two statements are the same. $\square$

For a subgroup $\Gamma$ of a group $G$, a set $\Omega$ and $x \in G$, the *multiplicity* is $\mathrm{mult}(\Gamma, \Omega, x) = \sup_y \#\{\gamma \in \Gamma : x^{-1}\gamma y \in \Omega\}$. For $g \in G_\infty$ let $\|g\|$ be the product over the archimedean places of the operator norms of $g_v$, and let $N_1 = 4 n^2 \sqrt{2q}$, where $q$ is the largest of the numbers $q_v$ of the instance.

**Theorem 5.8.6 (Polynomial multiplicity).** For compact sets $\Omega$ and $C$ of $G$ there is a constant $c_0$ such that $\mathrm{mult}(G(F), \Omega, c\,(g, 1)) \leq c_0 \|g\|^{N_1}$ for all $c \in C$ and $g \in G_\infty$.

Lean: `Formalism.L2.SG.Closed.MultPoly_holds` (also `Formalism.L2.SG.PoincareInHH.Cut.MultPoly`, the statement).

*Proof.* This is [the multiplicity bound](/entry/mult-poly-holds-of/) applied to the covering property, and that theorem combines six inputs in `multPoly_of`. The covering property (`OmCover_holds`) says that each compact $\Omega$ lies in a finite union of right translates by elements $(1, a)^{-1}$ of sets
$$\Omega(r, K') = \{\omega : \text{the Cartan distance of } \omega_{\infty, v} \text{ is at most } r_v \text{ for each } v,\ \omega_f \in K'\},$$
with $r_v \geq 0$ and $K' \subseteq K$ a subgroup. The rational points in one such set are counted by the lattice count above. The other inputs are the triangle inequality for the Cartan distance (`DistTri_holds`), the reduction theory statement `reduction_theory`, the bound $\tau_1(x) \leq \tau_1(x\,(g, 1))\, \|g\|^{1/f}$ for $n \geq 1$ (`tauTrans_holds`), and the bound $\|g\|^{4n^2} \leq \|g\|^{N_1}$ for $n \geq 1$ (`normPow_holds`). We did not unfold `multPoly_of` or the statement of reduction theory. $\square$

### Folding and the kernel expansion

For a word $u$ let $S(u)$ be the group of rational points of the stabilizer, and for each test vector $T$ let $\Phi_T$ be the function on $G$ whose sum over $S(u) \backslash G(F)$ is the Poincare series of $T$. *Folding holds* for $u$ if $S(u)$ has a fundamental domain $F_s$ for the Haar measure of $G$, and there are a compact $\Omega_0 \ni 1$ and $a \geq 0$ such that for every $T$:

1. for each compact $\Omega \supseteq \Omega_0$, $\Phi_T$ is measurable, invariant under $S(u)$ on the left, and $|\Phi_T(y)| \leq a \int_\Omega |\Phi_T(y\omega)|\, d\omega$ for all $y$;
2. for each compact $\Omega$ and each fundamental domain $F_s$, the integral $\int_{F_s} \mathrm{mult}(G(F), \Omega, y)\, |\Phi_T(y)|\, dy$ is finite.

Lean: `Formalism.L2.SG.WuDecay.FoldOK` (also `Formalism.L2.SG.Full.FoldOKC`, the closed form for all data).

**Theorem 5.8.7 (Folding).** Assume that for every datum, setting $X$ and word $u$, each element of the finite stabilizer $S_f(u)$ is a product $h n$ with $h \in H_f(u)$ and $n \in N_f(u)$. Then for every datum, setting $X$ with a full system $Y$, and word $u$, if the level group is normalized and the decay condition of $X$ holds, folding holds for $u$.

Lean: `Formalism.L2.SG.Closed.FoldOKC_holds` (also `Formalism.L2.SG.Closed.FoldOKC_outright`, the form without hypothesis).

*Proof.* This is [the folding theorem](/entry/fold-okc-holds-of/) applied to five inputs. The first (`KsetSplit_holds`) says that if $n \in N_f(u)$, $h \in H_f(u)$ and $n h \in K$, then $h \in K$. The second (`unipotent_in_level_subgroup`) says that for $n \in N_f(u) \cap K$ the conjugate $x_u^{-1} n x_u$ lies in the second level group of $X$, and its character value there equals the value of the character of $u$ at $n$. The third is the rational Levi statement `RatLevi_holds`, and the fourth is the product formula for the character (`psiProd_all`). The fifth gives the finiteness in item 2 (`iUnfoldAll_of`), from the factorization hypothesis, the input `noCocompactC_holds` and the strong approximation theorem above. We did not unfold `foldOKC_holds_of` or `iUnfoldAll_of`. $\square$

The hypothesis is proved in the tree, and `FoldOKC_outright` is the theorem with this proof inserted.

For words $u$, $u'$ the kernel form compares test vectors $T$ for $u$ and $T'$ for $u'$, and it is a sum of terms $a_t$.

**Theorem 5.8.8 (Kernel expansion).** For every datum, setting $X$ with full system $Y$ and words $u$, $u'$, assume folding for $u$ and for $u'$, the integrability of both Poincare series, the existence of fundamental domains for the pair, the integrability of the orbital integrals, their independence of the fundamental domain, the fact that the amplitudes are well defined, and absolute convergence of the term sum. Then there is a bounded operator $K$ from the column space of $u'$ to that of $u$ such that the terms $a_t$ have sum $K$, and the kernel form satisfies $\mathrm{Kform}(T, T') = \langle K(T'^\sharp), T^\sharp\rangle$ for all $T$ and $T'$.

Lean: `Formalism.L2.SG.Closed.KExpansionC_holds` (also `Formalism.L2.SG.TermOp.KExpansion`, the conclusion).

*Proof.* The input `kExpansionC_holds_of` reduces the theorem to five facts. The first is the slab covering `SlabCoverC_holds`: for a normalized level group with the neat property, and for fundamental sets of the column groups, the slabs of the column system cover as in `SlabCover`. It comes from the strong approximation theorem above, the conjugation statement `nilradical_conj_level`, `RatLevi_holds` and the character condition `PsiDd_holds`. The other four are the regrouping statement `regroupC_all`, the neat property of the level group (`NeatKu_holds`), the bridge between fundamental domains (`fundBridge_holds`) and the measurability of the Poincare series (`pserMeas_holds`). We did not unfold `kExpansionC_holds_of` or `SlabCover`. $\square$

**Theorem 5.8.9 (Off diagonal degenerate terms vanish).** For all constants $C_g$, $c_b$, $C_w$, $c_T$, $C_T$ and $C_0$ there are thresholds $C'_0$ and $C_{l,0}$ with this property. Let $C' \geq C'_0$ and $C_l \geq C_{l,0}$. For every datum $D$ with size data, setting $X$ with full system $Y$ and words $u \neq u'$, assume the size hypotheses of the second kernel theorem with these constants, and the tie conditions between $X$ and $Y$. Then every term $t$ of degenerate type in the kernel for $(u, u')$, that is, every $t$ with $G(t) = 0$ that is not the identity term, has $\mathrm{op}(t) = 0$.

Lean: `Formalism.L2.SG.Closed.KppOffC_holds` (also `Formalism.L2.SG.RowsConc.KppOffC`, the statement).

*Proof.* The proof is `kppOffC_of_steps0` applied to folding (`FoldOKC_outright`), the existence of fundamental domains, the integrability of the orbital integrals, the vanishing lemma `LemmaVC_holds` and the orthogonality relations `schurNFC`. The main input is that the covariant representation of a degenerate term is zero (`covariantRepZero_of_lemmaV`). Its core is the averaging lemma `AvgCore_holds`. Let $\Gamma \leq R$ be subgroups of a locally compact group with $R$ closed, $\Gamma$ discrete and $\Gamma \backslash R$ covered by a compact set. Let $\chi$ be a continuous character of $R$, trivial on $\Gamma$ and not trivial on $R$, and let $f$ satisfy $f(r x) = \chi(r) f(x)$ for $r \in R$. Then the integral of $f$ over a fundamental set $\Omega$ for $\Gamma$ is zero. The other inputs are the unimodularity of $G_\infty$ and six statements from `nLamNinf_holds` to `rational_cocompact_holds`. We did not unfold `kppOffC_of_steps0` or the way a degenerate term gives such $R$, $\Gamma$ and $\chi$. $\square$

**Remark 5.8.10 (Formalization).** Strong approximation is in [SlabNDensePf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/SlabNDensePf.lean#L49), and the Levi reduction is in [NormStepsLeviOntoSEnd.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/NormStepsLeviOntoSEnd.lean#L23). The lattice count is in [LevelSubgroupProperties.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/LevelSubgroupProperties.lean#L78), the multiplicity bound in [WuDefiniteHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/WuDefiniteHolds.lean#L39). Folding and the kernel expansion are in [UnipotentInLevelSubgroup.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/UnipotentInLevelSubgroup.lean#L63), and the vanishing theorem is in [FullExistsTiedHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/FullExistsTiedHolds.lean#L36). The density property is defined twice with the same body, and a third copy for one setting is `NDenseAt`. The statement of the lattice count also has two copies, one in the namespace `PI.LatCountG` and one in `Formalism.L2.SG.Count`, and `LatCount_holds` converts the first to the second by unfolding and one rewrite of $\tau_1$. The proof of `OmCover_holds` is `first | exact … | exact …` with two branches that are the same term. The Levi reduction takes the matrix itself as a unit when its determinant is a unit and the value $1$ in the other case, so the theorem is a statement about surjectivity onto units only. `FoldOKC_holds` keeps the factorization hypothesis `FinLeviC` as an argument, and `FoldOKC_outright` discharges it with `FinLeviC_holds`. We did not unfold the definitions of the tie conditions and of the size hypotheses.
