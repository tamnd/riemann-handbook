---
title: Holomorphic arcs and theta sections with large jets
decls:
  - GlobalTheory.T.holomorphic_degenerationArc_of_uniformisation
  - GlobalTheory.HolomorphicArc.main
  - GlobalTheory.ArcPts.nonempty_holArc
  - GlobalTheory.ThetaTorus.I_holds
  - GlobalTheory.ThetaTorus.J_holds
  - GlobalTheory.ThetaTorus.propA_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Holomorphic arcs and theta sections with large jets

This section proves two groups of results. The first group says that every formal arc into a compactified model at the boundary is the expansion of a holomorphic family of abelian varieties on a half plane. This is the toroidal archimedean condition, and it is the input of [the closed arc clause](/entry/arc-clause-closed/). The second group builds theta sections on a polarized torus with prescribed jets at $0$ and small norm. It gives the lower bound for sums over translates used in [the theta rule sum](/entry/theta-rule-sum-lower/).

### Formal arcs and holomorphic arcs

Let $E$ be a CM field with host data $H$, let $D$ be a datum, that is, a finite projective $\mathcal{O}_E$ module with a unimodular alternating form, let $l$ be a level and $X_o$ the fine moduli scheme. Let $Y$ be a model over a ring $O$ with a dense open immersion $j$ of the moduli space and a semiabelian scheme over it. Let $b_F : F \to \mathbb{C}$ be a ring map from the coefficient field.

A formal arc is a map $\chi : \operatorname{Spec} \mathbb{C}[[X]] \to Y$ whose points off $X = 0$ lie in the image of $j$. Arc data $a$ record the degeneration of the semiabelian scheme along $\chi$. A family uniformization $F_u$ of type $t$ is a holomorphic family of period lattices of complex abelian varieties with $\mathcal{O}_E$ acting through the embeddings $t_1, \dots, t_g$.

A holomorphic arc for $(\chi, F_u)$ consists of the following data.

1. An index $i$, a bound $T$ and maps $P_w = P_0 + w N$ from the lattice to $\mathbb{C}^g$, such that $P_w$ is a period map of the family for $\operatorname{Im} w > T$.
2. A surjective additive holomorphic map $\operatorname{ex}_0$ from $\mathbb{C}^g$ to the points of the degeneration. It is $\mathcal{O}_E$ linear for $t$, and $\operatorname{ex}_0(z) = 0$ exactly when $z = P_0(v)$ with $y(v) = 0$.
3. The shift: $\operatorname{ex}_0(w N v)$ is the torus point with coordinates $\exp(2\pi i w \, b(y v, x))$.
4. Level structures at the points $l^{-1} P_0(v)$, for the two levels of $l$.
5. Convergence: for every function $f$ regular along $\chi$, the power series of $f$ along $\chi$ converges at $\exp(2\pi i w)$ for large $\operatorname{Im} w$, and its value is $f$ at the point of the family given by $P_w$.
6. Compatibility of the Riemann form, of first order deformations and of theta values with the family.

The toroidal archimedean condition says that a holomorphic arc exists for every formal arc and every family uniformization of a type that fits the signature of $D$.

### The holomorphic arc theorem

**Theorem 10.20.1 (Holomorphic arcs).** Assume the laws of abelian schemes, the four further laws on base change of sections, twists, character pairs and dense smooth loci, and the analytic uniformization of complex abelian varieties. Then the toroidal archimedean condition holds.

Lean: `GlobalTheory.HolomorphicArc.main` (also `GlobalTheory.T.holomorphic_degenerationArc_of_uniformisation`, a second name).

*Proof.* Step 1: the analytic degeneration. The analytic uniformization gives an analytic degeneration $\Lambda$ for the arc data $a$: a torus, a lattice, the map $\operatorname{ex}_0$ and the periods $P_0$ and $N$. This is the only use of the uniformization.

Step 2: the chain. The universal family and the witness of $\chi$ give a chain $C$ that links $\Lambda$ to the semiabelian scheme along $\chi$.

Step 3: levels. Choose lattice representatives of the level points for the two levels. The chain carries these levels.

Step 4: finiteness and rationality. The spaces of theta sections of $\Lambda$ are finite, and the theta data of the chain are rational.

Step 5: germs. There are rings of convergent Laurent germs in $\exp(2\pi i w)$ that contain the expansions of the regular functions. They give special points $\Psi(w)$ for $w$ in a half plane.

Step 6: fibres. The linear part of $\Psi$ and a bound $T_1$ make $\Psi$ holomorphic, with $\Psi(w)$ the fibre of the family at $w$ for $\operatorname{Im} w > T_1$. The two level structures hold on the fibres beyond bounds $T_A$ and $T_M$.

Step 7: the half plane. The dimension of the fibre is $g$. Shrink the half plane to $\operatorname{Im} w > \max(T_1, T_A, T_M)$.

Step 8: comparison. A comparison $K$ between $\Psi$ and $F_u$ exists. The lemma below assembles a holomorphic arc. $\square$

**Lemma 10.20.2 (Assembling a holomorphic arc).** Assume the laws of abelian schemes and the further laws. Let $\Lambda$ be an analytic degeneration for $a$, let $C$ be a chain with rational theta data, let $\Psi$ be special points, let $K$ be a comparison of $\Psi$ with $F_u$ through a linear isomorphism $h$ and a lattice isomorphism $\gamma$, and let the level points have representatives. Assume that $\Psi(w)$ is the fibre at $w$ for $\operatorname{Im} w > T_1$. Then a holomorphic arc exists.

Lean: `GlobalTheory.ArcPts.nonempty_holArc`.

*Proof.* Step 1: the analytic facts on $\Lambda$. The map $\operatorname{ex}_0$ of $\Lambda$ is additive, surjective and equivariant. The exponential of the analytic dictionary is holomorphic. The kernel of $\operatorname{ex}_0$ is described by the torus part. The theta spaces are finite, and orthogonality to the kernel is given by the Riemann form.

Step 2: the data. Put $i$ and $P_w$ from $K$. Put $P_0 = h \circ P_0^\Lambda \circ \gamma$ and $N = h \circ N^\Lambda \circ \gamma$, and $\operatorname{ex}_0(z) = \operatorname{ex}_0^\Lambda(h^{-1} z)$. Then $P_w = P_0 + w N$, since $h$ is linear.

Step 3: the half plane. The theta values agree with the expansions for $\operatorname{Im} w > T_2$, by the level one section formula. Put $T = \max(T_K, T_2)$.

Step 4: the fields. Additivity, surjectivity and linearity move from $\Lambda$ to $\operatorname{ex}_0$ through $h$. The kernel condition follows from the kernel of $\operatorname{ex}_0^\Lambda$ and the bijectivity of $\gamma$. The levels come from the representatives and $h^{-1}(s h(v)) = s v$. The Riemann condition is the orthogonality of Step 1. Convergence and deformations come from the point and derivative lemmas for the arc. $\square$

### Theta sections on a polarized torus

Let $V = \mathbb{C}^g$ with the standard hermitian form $H$, and let $L \subset V$ be a lattice on which $\operatorname{Im} H$ is integral and perfect. Let $\kappa : L \to \mathbb{C}$ have $\lvert\kappa\rvert = 1$ and satisfy the cocycle rule for level $q$. The space $\operatorname{Sec}(q)$ is the space of holomorphic $F$ on $V$ with
$$
F(v + \gamma) = \kappa(\gamma) \exp\bigl(q\pi H(v, \gamma) + \tfrac{q\pi}{2} H(\gamma, \gamma)\bigr) F(v)
$$
for $\gamma \in L$. The norm $\lVert F\rVert_q^2$ is the mean of $\lvert F(v)\rvert^2 \exp(-q\pi \lVert v\rVert^2)$ over a fundamental domain. The $n$ variable spaces $\operatorname{Sec}(q, n)$ are defined in the same way on $V^n$.

**Theorem 10.20.3 (Theta sections with a given jet).** Let $q \geq 1$ and $c \geq 0$, and let $R_0 > 0$ satisfy
$$
R_0 \leq \sqrt{q\pi} \, \lVert\gamma\rVert \quad (\gamma \in L, \ \gamma \neq 0) ,
$$
with $R_0^2 \geq 270$ and $R_0^2 \geq 90(g + c)$. Then for every polynomial $p$ of degree at most $c$ there is $\beta \in \operatorname{Sec}(q)$ whose derivatives at $0$ of order at most $c$ are those of $p$, and
$$
\lVert\beta\rVert_q^2 \leq 6 \int_V \lvert p(v)\rvert^2 \exp(-q\pi \lVert v\rVert^2) \, dv .
$$

Lean: `GlobalTheory.ThetaTorus.propA_holds`.

*Proof.* Step 1: averaging. For a polynomial $F$ of degree at most $c$, let $\theta_F = \sum_{\gamma} \kappa(\gamma) U_\gamma F$, where $U_\gamma$ is the translation by $\gamma$ with the factor of automorphy. The series converges with all derivatives, and $\theta_F \in \operatorname{Sec}(q)$.

Step 2: the tail. Let $\langle\cdot,\cdot\rangle$ be the Gaussian inner product on polynomials with weight $\exp(-q\pi\lVert v\rVert^2)$. Unfolding gives $\langle \theta_F, G\rangle = \sum_\gamma \kappa(\gamma) \langle U_\gamma F, G\rangle$. The term $\gamma = 0$ is $\langle F, G\rangle$, since $\kappa(0) = 1$. The other terms are bounded by Gaussian factors in $\lVert\gamma\rVert$. A packing count for lattice points in balls and a Gaussian tail bound give
$$
\lvert \langle \theta_F, G\rangle - \langle F, G\rangle \rvert \leq \tfrac12 \lVert F\rVert \lVert G\rVert ,
$$
under the bounds on $R_0$.

Step 3: the jet map. Let $T$ send $F$ to the jet of order $c$ of $\theta_F$. Step 2 gives $\operatorname{Re} \langle T F, F\rangle \geq \frac12 \lVert F\rVert^2$. So $T$ is injective. The space of polynomials of degree at most $c$ is finite dimensional, so $T$ is onto.

Step 4: the section. Choose $F$ with $T F = p$ and put $\beta = \theta_F$. Its jet is $p$. Unfolding gives $\lVert\beta\rVert_q^2$ as $\langle p, F\rangle$. Step 3 and the Cauchy-Schwarz inequality give $\lVert F\rVert \leq 2 \lVert p\rVert$, and the bound follows. $\square$

Now let a block be an embedding $\tau$, a size $i$, a power $c \geq 1$ and $i$ distinct columns in $\{1, \dots, n\}$. Its polynomial is the $c$ th power of an $i \times i$ minor in the coordinates of type $\tau$. For a family of blocks with disjoint columns let $D$ be the differential operator of the product of their polynomials, and let $J(n)$ be an explicit constant depending on the parameters.

**Theorem 10.20.4 (One good section).** Let $X$ be a polarized torus for a CM field $E$ and let the blocks be disjoint. Then there is $F \in \operatorname{Sec}(q, n)$ with $\lVert F\rVert_q^2 = 1$ and $J(n) \leq \lvert D F(0)\rvert^2$.

Lean: `GlobalTheory.ThetaTorus.J_holds`.

*Proof.* Step 1: splitting. A greedy splitting gives a saturated isotropic sublattice $I \subseteq L$, stable under $\mathcal{O}_E$, with $\kappa = 1$ on $I$ and bounded rank.

Step 2: block columns. The theorem above, applied on the torus part, on the abelian part and to the character statement, gives for each column $b$ of each block a vector $y_b$ with $\lvert y_b\rvert \leq 2$, a section $s_b \in \operatorname{Sec}(q, 1)$ and $\mu_b \neq 0$. The derivative of order $c$ of $s_b$ is close to $\mu_b \prod_k H(x_k, y_b)$, and $\lVert s_b\rVert_q^2$ is at most a constant times $\lvert\mu_b\rvert^2$. Each block minor of the $y_b$ is at least $2^{-r/2}/2$ in absolute value.

Step 3: free columns. The same theorem with $p = 1$ gives $s_e \in \operatorname{Sec}(q, 1)$ with $\lvert s_e(0)\rvert \geq \frac12$ and a bound on its norm.

Step 4: tensor. Put $s_b$ on the columns of the blocks and $s_e$ on the other columns. The tensor product $F_0$ lies in $\operatorname{Sec}(q, n)$, and its norm is the product of the norms of the factors.

Step 5: expand. The derivative $D F_0(0)$ is a signed sum over choices of products of one variable derivatives. It is close to the ideal sum, which is the product of $\lvert s_e(0)\rvert$, the $\lvert\mu_b\rvert$ and the minors. So $\lvert D F_0(0)\rvert$ is at least half the ideal value.

Step 6: normalize. Steps 2 and 3 bound the norm of $F_0$, which gives $J(n) \lVert F_0\rVert_q^2 \leq \lvert D F_0(0)\rvert^2$. Put $F = F_0/\lVert F_0\rVert_q$. $\square$

**Theorem 10.20.5 (Lower bound for translates).** Let $\pi$ be a linear map on $V$ that commutes with $\mathcal{O}_E$, keeps $L$, multiplies $H$ by $q$, and has $\kappa(\pi x) = \kappa(x)^q$. Let $s \neq 0$ in $\operatorname{Sec}(1, 1)$, and let $K$ be a set of representatives of the $b$ with $q b \in L^n$, modulo $\pi^{-1} L^n$. Put $s_0(v) = \prod_k s(\pi v_k)$ and let $U_b$ be the translation by $b$. Then
$$
J(n) \lVert s\rVert_1^{2n} \leq \sum_{b \in K} \lvert D(U_b s_0)(0)\rvert^2 .
$$

Lean: `GlobalTheory.ThetaTorus.I_holds`.

*Proof.* The translates $U_b s_0$ for $b \in K$ lie in $\operatorname{Sec}(q, n)$, are pairwise orthogonal, have norm squared $\lVert s\rVert_1^{2n}$, and span $\operatorname{Sec}(q, n)$. Take $F$ from the theorem on one good section and write $F = \sum_b l_b U_b s_0$. Orthogonality gives $1 = \lVert s\rVert_1^{2n} \sum_b \lvert l_b\rvert^2$. Since $D$ is linear,
$$
\lvert D F(0)\rvert \leq \sum_b \lvert l_b\rvert \, \lvert D(U_b s_0)(0)\rvert .
$$
The Cauchy-Schwarz inequality gives $\lvert DF(0)\rvert^2 \leq \sum_b \lvert l_b\rvert^2 \sum_b \lvert D(U_b s_0)(0)\rvert^2$. Multiply by $\lVert s\rVert_1^{2n}$ and use $J(n) \leq \lvert DF(0)\rvert^2$. $\square$

**Remark 10.20.6 (Formalization).** The arc theorem is at `Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/HolomorphicDegenerationArcOfUniformisation.lean:29`. Its `intro` (line 31) drops the hypothesis on the image of the fixed root under $b_F$ with `_`, and no later line uses it. The second name is at `HolomorphicDegenerationArcOfUniformisationStatement.lean:6`; it is proved by `first | exact @GlobalTheory.HolomorphicArc.main | ...` with two fallbacks that are never reached, under `maxHeartbeats 1000000` (line 5). The assembly lemma is at `IsHolToCompClm.lean:27` in the same folder, and its file is named after the helper `isHolTo_comp_clm` (line 12). The theta results are one term each at `Development/AbelianVarietyTheory/Proofs/TorusSplitting/GCauchyHolds.lean:22`, `:26` and `:34`. The jet theorem is `propA` (`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/PaThDiffLe.lean:259`) with the proved packing count and Gaussian tail bound (`GaussianTailBound.lean:7` and `:12`); the core is `propA_core` at line 114 of that file, and the inner product bound is `paTh_diff_le` at line 23. The file `GCauchyHolds.lean` holds no theorem named `GCauchy`.
