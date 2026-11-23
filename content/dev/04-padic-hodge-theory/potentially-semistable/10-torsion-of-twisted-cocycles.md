---
title: Torsion of cocycles with coefficients in A_inf
decls:
  - GlobalTheory.Cyc.FrameTorsion.torsion_killed
  - GlobalTheory.Cyc.Decomp.exists_decompletion
  - GlobalTheory.TorsLL.torsion_bound_at_level
  - GlobalTheory.T.torsion_bound_of_weight_hyp
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Torsion of cocycles with coefficients in $A_{\inf}$

Let $T$ be a lattice with a Wach module. This section bounds the torsion of the cohomology of $G_{K_s}$ with coefficients in $T \otimes A_{\inf}[a, b)$: if some power of $\ell$ kills the class of a cocycle, then an explicit power $\ell^{N}$ kills it, where $N$ depends only on $\ell$, $s$, $a$, $b$ and the Hodge-Tate jumps of $T$. The proof has three steps. On each graded piece $\xi^i A_{\inf}/\xi^{i+1}$, which is a twist of $\mathcal{O}_C$, we use a decompletion of the Galois action, in the style of Sen and Tate, and a basis of Hodge-Tate vectors. A dévissage then passes to $A_{\inf}[a, b)$, and a restriction argument descends from $G_{K_m}$ to $G_{K_s}$. The result is the torsion bound in [Theorem 6.6.7](/entry/crystalline-extension-class-bound/). We use [Fontaine's period rings](/learn/padic-hodge/#crystalline-and-semistable-representations) and the [cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules).

We keep the notation of the previous sections. Let $C$ be the completion of $\Omega$ and $\mathcal{O}_C$ its ring of integers. The group $G_{\mathbb{Q}_\ell}$ acts on $C$ by continuous ring automorphisms that extend its action on $\Omega$ and preserve the norm. Let $\chi$ be a character with the cyclotomic property: if $\zeta^{\ell^n} = 1$, then $g\zeta = \zeta^a$ for some $a \in \mathbb{N}$ with $|\chi(g) - a| \leq \ell^{-n}$. Let $K_\infty = K_0(\mu_{\ell^\infty})$, let $H_\infty \subseteq G_{\mathbb{Q}_\ell}$ be its fixer, and let $\widehat{\mathcal{O}}_\infty$ be the closure in $C$ of the integers of $K_\infty$. For a field $F \subseteq \Omega$ let $\mathcal{O}_F$ be its elements of norm at most $1$. Put $\rho_1 = \ell^{-1/(\ell - 1)}$. For $m \geq 1$, with $m \geq 2$ if $\ell = 2$, let $G_{K_m}$ be the fixer of $K_m$.

**Definition 6.10.1 (Frame).** Let $r \in \mathbb{N}$. A *frame at level $m$* is a pair $(U, g)$ of a map $U : G_{\mathbb{Q}_\ell} \to M_r(C)$ and an element $g \in G_{\mathbb{Q}_\ell}$ such that:

1. $g \in G_{K_m}$ and $|\chi(g) - 1| = \ell^{-m}$;
2. the entries of $U$ are continuous on $G_{K_m}$ and lie in $\mathcal{O}_{K_m}$ there;
3. $U(\sigma\tau) = U(\sigma) U(\tau)$ for $\sigma, \tau \in G_{K_m}$, and $U(h) = 1$ for $h \in H_\infty$;
4. every entry of $U(g) - 1$ has norm less than $\rho_1$.

For $i \in \mathbb{Z}$ the *twisted action* of $\sigma$ on $C^r$ is $\sigma \ast_i y = \chi(\sigma)^i\, U(\sigma)\, \sigma(y)$, where $\sigma(y)$ acts on each coordinate.

Lean: `GlobalTheory.Cyc.Frame` (also `GlobalTheory.Cyc.twAct`, the twisted action).

Condition 1 says that $g$ generates the procyclic group $G_{K_m}/H_\infty$ at level $m$. Condition 4 says that $U(g)$ is close to $1$, so that the series for $\log U(g)$ converges well. A frame is the matrix form of a representation of $\mathrm{Gal}(K_\infty/K_m)$ over $\mathcal{O}_{K_m}$.

**Definition 6.10.2 (Hodge-Tate basis).** Let $G \subseteq G_{\mathbb{Q}_\ell}$ be a subgroup, $U : G_{\mathbb{Q}_\ell} \to M_r(C)$ and $J \subseteq \mathbb{Z}$. A *Hodge-Tate basis of $U$ on $G$ with weights in $J$* is a family $e_1, \dots, e_r \in C^r$, linearly independent over $C$, with integers $u_k \in J$ such that $\chi(\sigma)^{u_k} U(\sigma) \sigma(e_k) = e_k$ for all $\sigma \in G$ and all $k$.

Lean: `GlobalTheory.Cyc.HTBasis`.

**Definition 6.10.3 (Decompletion).** Let $M : G_{\mathbb{Q}_\ell} \to M_d(C)$. A *decompletion of $M$ at level $m$* is a triple $(D, U, g)$ with $D \in M_d(C)$ such that $\det D \neq 0$, every entry of $D$ and of $\ell D^{-1}$ has norm at most $1$, $(U, g)$ is a frame at level $m$, and
$$D\, U(\sigma) = M(\sigma)\, \sigma(D) \qquad (\sigma \in G_{K_m}).$$

Lean: `GlobalTheory.Cyc.IsDec`.

So $M$ and $U$ are cohomologous on $G_{K_m}$ through $D$, and the change of basis distorts the lattice $\mathcal{O}_C^d$ by at most a factor $\ell$.

**Definition 6.10.4 (Matrices of a lattice).** Let $(K, s, L)$ be a good triple and $T$ a lattice representation of $G_K$ over $L$. Maps $M : G_{\mathbb{Q}_\ell} \to M_d(C)$ and $A : \mathcal{O}_L \to M_d(C)$ are *matrices of $T$* if there is a $\mathbb{Z}_\ell$-basis of $T$ in which $M(g)$ is the matrix of $g$ for $g \in G_K$ and $A(a)$ is the matrix of multiplication by $a \in \mathcal{O}_L$.

Lean: `GlobalTheory.Cyc.IsMat`.

**Theorem 6.10.5 (Torsion of twisted cocycles on the ball).** Let $(U, g)$ be a frame at level $m$, and let $J \subseteq \mathbb{Z}$ be a finite set such that $U$ has a Hodge-Tate basis on $G_{K_m}$ with weights in $J$. Let $i \in \mathbb{Z}$ and put
$$N_i = \max\Big(1, \sum_{u \in J,\, u \neq i} \big(m + v_\ell(u - i)\big)\Big).$$
Let $c : G_{\mathbb{Q}_\ell} \to \mathcal{O}_C^r$ be continuous on $G_{K_m}$ with $c(\sigma\tau) = c(\sigma) + \sigma \ast_i c(\tau)$ for $\sigma, \tau \in G_{K_m}$. If for some $k$ there is $x \in \mathcal{O}_C^r$ with $\ell^k c(\sigma) = \sigma \ast_i x - x$ on $G_{K_m}$, then there is $y \in \mathcal{O}_C^r$ with $\ell^{1 + N_i} c(\sigma) = \sigma \ast_i y - y$ on $G_{K_m}$.

Lean: `GlobalTheory.Cyc.FrameTorsion.torsion_killed`.

*Proof.* We use four results proved elsewhere in this development, all in the theory of Tate and Sen:

- (a) if $a \in K_\infty$ and $|a| < 1$, then $a$ times any continuous cocycle $H_\infty \to \mathcal{O}_C^r$ for the plain action is a coboundary of an element of $\mathcal{O}_C^r$;
- (b) an element of $\mathcal{O}_C$ is fixed by $H_\infty$ exactly when it lies in $\widehat{\mathcal{O}}_\infty$;
- (c) if $w, w' \in \widehat{\mathcal{O}}_\infty^r$ and $g \ast_i w' - w' = \ell^k w$, then $g \ast_i y - y = \ell^{N_i} w$ for some $y \in \widehat{\mathcal{O}}_\infty^r$;
- (d) a continuous cocycle on $G_{K_m}$ for $\ast_i$ that vanishes on $H_\infty$ and at $g$ vanishes on $G_{K_m}$.

Write $\delta x$ for the coboundary $\sigma \mapsto \sigma \ast_i x - x$. For $h \in H_\infty$ we have $U(h) = 1$ and $\chi(h) = 1$, so $\ast_i$ is the plain action on $H_\infty$. By (a) with $a = \ell$, there is $x_1 \in \mathcal{O}_C^r$ with $\ell c = \delta x_1$ on $H_\infty$. Then $c_1 = \ell c - \delta x_1$ is a continuous cocycle on $G_{K_m}$ with values in $\mathcal{O}_C^r$ that vanishes on $H_\infty$. For $h \in H_\infty$, normality of $H_\infty$ in $G_{K_m}$ gives $h' = g^{-1} h g \in H_\infty$, and
$$h(c_1(g)) = c_1(hg) = c_1(g h') = c_1(g).$$
By (b), $c_1(g) \in \widehat{\mathcal{O}}_\infty^r$. Let $\ell^k c = \delta x_0$ and put $x_2 = \ell x_0 - \ell^k x_1$. Then $\ell^k c_1 = \delta x_2$, and $x_2$ is fixed by $H_\infty$ because $c_1$ vanishes there; by (b), $x_2 \in \widehat{\mathcal{O}}_\infty^r$. Now (c) with $w = c_1(g)$ and $w' = x_2$ gives $y_0 \in \widehat{\mathcal{O}}_\infty^r$ with $g \ast_i y_0 - y_0 = \ell^{N_i} c_1(g)$. The cocycle $d = \ell^{N_i} c_1 - \delta y_0$ vanishes on $H_\infty$, since $y_0$ is fixed there, and at $g$. By (d), $d = 0$. So $\ell^{N_i} c_1 = \delta y_0$ and $\ell^{1 + N_i} c = \delta(y_0 + \ell^{N_i} x_1)$, with $y_0 + \ell^{N_i} x_1 \in \mathcal{O}_C^r$. $\square$

**Theorem 6.10.6 (Decompletion of a lattice with a Wach module).** Let $(K, s, L)$ be good, with its Wach and comparison data, and fix Fontaine data over the datum. Let $T$ be a lattice representation of $G_K$ over $L$, and let $M_0, h_0 \in \mathbb{N}$ be such that the Wach hypothesis holds for $(T, M_0, h_0)$. Let $m = 2s + n_0 + 1$, where $n_0$ is the least $n$ with $M_0 + h_0 \leq \ell^n(\ell - 1)$. Let $M$ and $A$ be matrices of $T$. Then there is a decompletion $(D, U, g)$ of $M$ at level $m$ such that every entry of $D^{-1} A(a) D$ lies in $\mathcal{O}_{K_m}$ for every $a \in \mathcal{O}_L$.

Lean: `GlobalTheory.Cyc.Decomp.exists_decompletion` (also `GlobalTheory.T.exists_decompletion_frame_of_lattice`, a second name).

*Proof.* We build $D$ and $U$ from the module $N$ of the Wach hypothesis, through results proved elsewhere in this development. First, $N$ and the lattice $T \otimes A_{\inf}$ are sandwiched between each other up to explicit factors, through the comparison datum. Property 1 of $N$ gives a basis of $N$, and with the basis of $T$ that gives $M$ and $A$ we obtain a basis of the tensor product as a product of copies indexed by the letters. Next, a ring map $\theta \circ \varphi^{-n} : A_{\inf} \to \mathcal{O}_C$, with $n = n_0$ and $m = s + (s + n + 1)$, specialises $T \otimes A_{\inf}$ to $T \otimes \mathcal{O}_C$. The specialised basis of $N$ defines $D$, and the action of $G_K$ on it defines $U$. A generator $g$ of the cyclotomic tower at level $m$ gives condition 1 of a frame. Property 3 of $N$, stability under $G_{K_s}$ and $(g - 1) N \subseteq \pi N$, show with the choice of $n$ that the entries of $U(g) - 1$ lie in a power of an ideal whose elements have norm less than $\rho_1$. The coordinates of $U$ and of $D^{-1} A(a) D$ are power series in $\pi$ evaluated at the specialisation, so they lie in $K_m$; their invariance shows that they lie in $\mathcal{O}_{K_m}$. The sandwich gives the bounds on $D$ and $\ell D^{-1}$. $\square$

**Lemma 6.10.7 (Torsion on a graded piece).** Assume Fontaine's bounds, the admitted fact 7. In the setting of the previous Theorem, assume $G_{K_m} \subseteq G_K$. Let $J(T)$ be the set of jumps of $T$, and for $i \in \mathbb{Z}$ let $r_i = \sum_{u \in J(T),\, u \neq i} (m + v_\ell(u - i))$. Then every continuous cocycle $f : G_{K_m} \to T \otimes A_{\inf}[i, i+1)$ such that $\ell^k f$ is a coboundary for some $k$ satisfies: $\ell^{2 + \max(1, r_i)} f$ is a coboundary.

Lean: `GlobalTheory.Cyc.GradedTorsion.torsion_killed`.

*Proof.* Choose matrices $M$ and $A$ of $T$. The previous Theorem gives a decompletion $(D, U, g)$ of $M$ at level $m$. Since $T$ is crystalline on $G_{K_s}$, a result proved elsewhere, which uses Fontaine's bounds, shows that $J(T)$ is finite and that $M$ has a Hodge-Tate basis on $G_{K_m}$ with weights in $J(T)$. If $(e_k)$ is such a basis for $M$, then $(D^{-1} e_k)$ is one for $U$, by the relation $D U(\sigma) = M(\sigma) \sigma(D)$. So the Theorem on the ball applies to $U$ and gives the exponent $1 + \max(1, r_i)$ for cocycles with values in $\mathcal{O}_C^d$ under $\ast_i$. Conjugation by $D$ moves between $U$ and $M$; since $D$ and $\ell D^{-1}$ are integral, this costs one more factor $\ell$. Finally the graded piece $\xi^i A_{\inf}/\xi^{i+1} A_{\inf}$ is isomorphic to $\mathcal{O}_C$ with the action $\chi^i$ times the action on $C$, compatibly with $G_{K_m}$, which fixes $\zeta_1$. In the basis of $T$, the coefficients $T \otimes A_{\inf}[i, i+1)$ become $\mathcal{O}_C^d$ with the action $\sigma \mapsto \chi(\sigma)^i M(\sigma) \sigma(\cdot)$, and the bound transfers. $\square$

**Theorem 6.10.8 (Torsion bound under the Wach hypothesis).** Assume the admitted facts 5 and 7: Tate's theorem on filtered invariants and Fontaine's bounds. In the setting of the decompletion Theorem, assume $G_{K_s} \subseteq G_K$, and let $a < b$ be integers. Give $T \otimes_{\mathbb{Z}_\ell} A_{\inf}[a, b)$ the $\ell$-adic topology. Put
$$N = v_\ell [K_m : \mathbb{Q}_\ell] - v_\ell [K_s : \mathbb{Q}_\ell] + \sum_{i = a}^{b-1} \big(2 + \max(1, r_i)\big).$$
Then for every continuous cocycle $f : G_{K_s} \to T \otimes A_{\inf}[a, b)$ such that $\ell^k f$ is a coboundary for some $k$, the cocycle $\ell^N f$ is a coboundary.

Lean: `GlobalTheory.TorsLL.torsion_bound_at_level` (also `GlobalTheory.T.torsion_bound_of_weight_hyp`, a second name).

*Proof.* Since $s \leq m$ and $s \geq 1$, we have $[K_m : K_s] = \ell^{m - s}$, so the first term of $N$ is $m - s$. We first work over $G_{K_m} \subseteq G_{K_s} \subseteq G_K$. For each $i$, the previous Lemma kills the torsion of $T \otimes A_{\inf}[i, i+1)$ by $\ell^{2 + \max(1, r_i)}$. We then induct on $b$. For $a < b$ the sequence
$$0 \to T \otimes A_{\inf}[b, b+1) \to T \otimes A_{\inf}[a, b+1) \to T \otimes A_{\inf}[a, b) \to 0$$
is exact and $G_{K_m}$-equivariant, since $A_{\inf}[a, b)$ is torsion-free and $T$ is flat. The action is continuous on each term, by a result proved elsewhere. A second result, which uses Tate's theorem on filtered invariants, Fontaine's bounds and the crystallinity of $T$ on $G_{K_s}$, shows that the invariants of $T \otimes A_{\inf}[a, e)$ lift, after multiplication by a power of $\ell$, to invariants of $T \otimes A_{\inf}[a, b)$ for $a \leq e \leq b$. With these two facts, the torsion exponents add along the exact sequence. So $\ell^{N'}$ with $N' = \sum_{i=a}^{b-1}(2 + \max(1, r_i))$ kills the torsion over $G_{K_m}$. Finally, $G_{K_m}$ has index $\ell^{m - s}$ in $G_{K_s}$. If $\ell^k f$ is a coboundary on $G_{K_s}$, then $\ell^{N'} f$ is a coboundary on $G_{K_m}$, and restriction followed by corestriction multiplies by the index. So $\ell^{m - s + N'} f$ is a coboundary on $G_{K_s}$. $\square$

**Remark 6.10.9 (Formalization).** The number $r_i$ is the finite sum `rI`, which is $0$ when $J(T)$ is infinite; here $J(T)$ is finite. The Theorem on the ball has exponent $1 + \max(1, r_i)$, and the Lemma on a graded piece adds one for the sandwich $D$, $\ell D^{-1}$ ([CoordEquivariant.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CoordEquivariant.lean#L249), lines 249 to 252). In [ExistsDecompletionFrameOfLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsDecompletionFrameOfLattice.lean#L331) the proof keeps only the module $N$ of the Wach hypothesis and drops the crystallinity and the bound on the jumps; the theorem runs under `synthInstance.maxHeartbeats 400000` and `maxHeartbeats 2000000` (lines 325 and 326). The proof sketch of the decompletion Theorem names the roles of `GlobalTheory.T.wach_lattice_sandwich_Ainf`, `GlobalTheory.T.exists_basis_and_equiv_fin_prod_of_basis`, `GlobalTheory.T.exists_fontaineTheta_frobeniusInverse_shift`, `GlobalTheory.T.exists_ainf_tensor_lattice_specialisation`, `GlobalTheory.T.exists_cyclotomicTowerLevelGenerator_properties`, `GlobalTheory.T.norm_lt_rho1_of_mem_ideal_power`, `GlobalTheory.T.ocTensorCoeffBasisCoords_mem_cyclotomicLevel_of_powerSeries` and `GlobalTheory.T.kap_mem_inC_of_invariant`; we read their statements only in part and did not open their proofs. We also did not open the proofs of the facts (a) to (d), which are `GlobalTheory.T.cyclotomic_tate_maximalIdeal_kills_first_cohomology`, `GlobalTheory.T.cyclotomicTower_fixed_iff_mem_completedIntegers`, `GlobalTheory.T.torsion_coinvariants_twistedCyclotomicGenerator` and `GlobalTheory.T.cocycle_vanishing_on_fixingSubgroup_determined_by_generator`, nor of `GlobalTheory.T.exists_hodgeTateBasis_of_crystalline_over_Ks`, `GlobalTheory.T.xiGradedPiece_iso_twistedOC` and the extension lemma behind `tors_induction`. The lifting of invariants, `GlobalTheory.T.xiQuotient_invariants_lift_rationally`, receives only the first part of the Wach hypothesis (crystallinity) at [TorsionBoundOfWeightHyp.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TorsionBoundOfWeightHyp.lean#L325). The $\ell$-adic topology on the coefficients is put in by `letI` in the statement. The second names are proved by `first | exact ...` under `maxHeartbeats 1000000`.
