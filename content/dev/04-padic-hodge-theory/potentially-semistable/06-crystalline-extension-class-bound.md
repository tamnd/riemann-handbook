---
title: The class of a crystalline extension
decls:
  - GlobalTheory.T.crystalline_extension_class_bound
  - GlobalTheory.Cyc.ClassBound.class_bound
  - GlobalTheory.Cyc.ClassBound.mem_HfD_of_lattice
  - GlobalTheory.Cyc.ClassBound.mem_HfD_of_isCob
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The class of a crystalline extension

Let $0 \to Y \to \tilde Y \to \mathbf{1} \to 0$ be an extension of the trivial character by a lattice $Y$ with a Wach module, and let $\tilde Y$ be crystalline. Its extension class, pushed to a twist $V_e/T_e$ by $\chi^{-e}$, need not be a Bloch-Kato class. This section proves that it becomes one after multiplication by an explicit power of $\ell$. The exponent depends only on $\ell$, $s$, $e$, the field $K$ and the Hodge-Tate jumps of $Y$. The proof turns the crystalline condition into a coboundary with coefficients in $A_{\inf}/\xi^{e+1}$, bounds its order of torsion with [Theorem 6.10.8](/entry/torsion-bound-of-weight-hyp/), and then goes from $A_{\inf}$ to $B_{\mathrm{cris}}$ one coordinate at a time with [Lemma 6.9.6](/entry/scalar-of-is-cob/). The result is one half of [Theorem 6.7.3](/entry/tb-assembled/). We use [local Bloch-Kato theory](/learn/padic-hodge/#local-bloch-kato-theory) and [Fontaine's period rings](/learn/padic-hodge/#crystalline-and-semistable-representations) ([[Fontaine's period rings|K6HW8YWCQJ]]).

The results of this section feed the global bound at $\ell$, so the prime is written $\ell$. Let $K$ and $L$ be finite extensions of $\mathbb{Q}_\ell$, let $s \geq 1$ with $s \geq 2$ if $\ell = 2$, put $K_j = K_0(\mu_{\ell^j})$, and assume $K \subseteq K_s$. Then $G_{K_s} \subseteq G_K$. Let $\chi$ be the [cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules). Put
$$g_K = v_\ell [K_s : \mathbb{Q}_\ell] - v_\ell [K : \mathbb{Q}_\ell].$$
A *lattice representation* $V$ of $G_K$ is a finite-dimensional $L$-space with a continuous action and a stable $\mathcal{O}$-lattice $T_V$. Let $B$ be the crystalline period ring of the period data, with its map $\iota : B \to B_{\mathrm{dR}}$.

**Definition 6.6.1 (Bloch-Kato cocycles).** Let $V$ be a lattice representation. A map $c : G_K \to V/T_V$ is a *Bloch-Kato cocycle* if it is the sum of two maps: the reduction modulo $T_V$ of a continuous cocycle $\tilde c : G_K \to V$ such that $\tilde c \otimes 1$ is a coboundary in $V \otimes B$, and a coboundary $g \mapsto g x - x$ with $x \in V/T_V$. They form an $\mathcal{O}$-module $H^1_f(K, V/T_V)$.

Lean: `Formalism.WeaklyAdmissibleFiltrations.HfD` (also `Formalism.WeaklyAdmissibleFiltrations.BD`, the coboundaries).

Let $\xi$ be the fixed element of $A_{\inf}$ given by the period data; it is a unit in $W(\mathbb{C}^\flat)$. For integers $a < b$ put $A_{\inf}[a, b) = \xi^a A_{\inf} / \xi^b A_{\inf}$. The group $G_{\mathbb{Q}_\ell}$ acts on it. For a lattice $T$ the module $T \otimes_{\mathbb{Z}_\ell} A_{\inf}[a, b)$ has the diagonal action.

Lean: `Formalism.MainNotions.LocalSituation.Qab` (also `Formalism.MainNotions.LocalSituation.Mxi`, the module $\xi^a A_{\inf}$).

**Definition 6.6.2 (Wach hypothesis).** Let $M_0, h_0 \in \mathbb{N}$ and let $Y$ be a lattice representation. The *Wach hypothesis* for $(Y, M_0, h_0)$ says three things. First, $Y$ is crystalline on $G_{K_s}$: the $G_{K_s}$-invariants of $V_Y \otimes B$ have $L$-dimension $[K_0 : \mathbb{Q}_\ell] \dim_L V_Y$. Second, every jump of $Y$ lies in $[-M_0, h_0]$. Here a *jump* is an $a$ with $D_{\mathrm{dR}} \cap \mathrm{Fil}^{a+1} \neq D_{\mathrm{dR}} \cap \mathrm{Fil}^a$, and $J(Y)$ is the set of jumps. Third, there is a submodule $N \subseteq D(Y)$ with these properties:

1. $N$ has an $A$-basis whose image in $T \otimes \widetilde A$ is a basis over $\widetilde A$;
2. $Q^{M_0} \varphi(N) \subseteq N$ and $Q^{h_0} N \subseteq A \varphi(N)$;
3. $N$ is stable under $G_{K_s}$, and $(g - 1) N \subseteq \pi N$ for $g \in G_{K_s}$;
4. $N$ is stable under every endomorphism of the lattice $Y$.

Lean: `Formalism.MainNotions.LocalSituation.HypW` (also `Formalism.MainNotions.LocalSituation.WClauses`, the conditions on $N$).

**Definition 6.6.3 (Admitted local facts).** The *admitted local facts* are the following nine statements, for each prime $\ell$ and each finite extension $K$ of $\mathbb{Q}_\ell$:

1. for $u \in B$ and $w \in B_{\mathrm{dR}}$ there are $x \in B$ and $y \in \mathrm{Fil}^0 B_{\mathrm{dR}}$ with $x - \varphi(x) = u$ and $\iota(x) - y = w$;
2. local Tate duality, as in [Theorem 6.1.5](/entry/local-duality-class-field-facts-of-artin-tate-euler/);
3. a statement on local cohomology in the top degree;
4. the local Euler characteristic formula;
5. Tate's theorem on filtered invariants: if $V$ is de Rham, $z \in \mathrm{Fil}^a(V \otimes B_{\mathrm{dR}})$ and $(g - 1) z \in \mathrm{Fil}^b$ for all $g$, then $z - w \in \mathrm{Fil}^b$ for some $w \in D_{\mathrm{dR}}(V) \cap \mathrm{Fil}^a$;
6. a continuity statement: if $f(g) \otimes 1 = \sum_i \beta_i(g) x_i + (g - 1) x'$ with continuous $\beta_i$, then $f$ is continuous;
7. Fontaine's bounds $\dim D_{\mathrm{cris}}(V) \leq [K_0 : \mathbb{Q}_\ell] \dim V$ and $\dim D_{\mathrm{dR}}(V) \leq [K : \mathbb{Q}_\ell] \dim V$, and crystalline implies de Rham;
8. two duality statements for de Rham representations under a duality pairing: one on $D_{\mathrm{dR}}$, and one saying that the dimensions of $\mathrm{Fil}^0 D_{\mathrm{dR}}$ of the two sides add up to $\dim D_{\mathrm{dR}}$;
9. a naturality and a decomposition statement for the comparison datum at each good triple.

Lean: `Formalism.MainNotions.LocalSituation.admitted`.

**Definition 6.6.4 (The exponent).** Let $m = 2s + n_0 + 1$, where $n_0$ is the least $n$ with $M_0 + h_0 \leq \ell^n(\ell - 1)$. For $i \in \mathbb{Z}$ put $r_i = \sum_{u \in J(Y),\, u \neq i} \big(m + v_\ell(u - i)\big)$. Put
$$\begin{aligned} N_Y &= v_\ell [K_m : \mathbb{Q}_\ell] - v_\ell [K_s : \mathbb{Q}_\ell] + \sum_{i = 0}^{e} \big(2 + \max(1, r_i)\big), \\ c(N) &= N + (e + 2) s + v_\ell(e) + \lfloor e/(\ell - 1) \rfloor + 1 + s + v_\ell(e + 1) + g_K. \end{aligned}$$

Lean: `Formalism.MainNotions.LocalSituation.cTB` (also `Formalism.MainNotions.LocalSituation.cTBY`, the exponent $c(N_Y)$, and `Formalism.MainNotions.LocalSituation.cLL`, the number $N_Y$).

**Lemma 6.6.5 (Bloch-Kato classes in coordinates).** Assume local Tate duality and the local Euler characteristic formula. Let $e, N, r \in \mathbb{N}$. Let $Y$ be a $\mathbb{Z}_\ell$-module with a linear action $\rho$ of $G_K$. Let $f : G_K \to Y$ be a cocycle such that, for each $n$, $f(h) - f(g) \in \ell^n Y$ for $h$ near $g$, and such that $\ell^N (f \otimes 1)$ on $G_{K_s}$ is a coboundary in $Y \otimes A_{\inf}[0, e+1)$. Let $V$ be a lattice representation with $g x = \chi(g)^{-e} x$, and let $w_1, \dots, w_n$ be a $\mathbb{Q}_\ell$-basis of $V$ such that $T_V$ is the set of vectors with coordinates in $\mathbb{Z}_\ell$, with continuous inverse coordinate map. Let $\Phi : Y \to V$ be additive with $\Phi(\rho(g) y) - g \Phi(y) \in T_V$, and assume that the coordinates $\psi_i$ of $\Phi$ are $\mathbb{Z}_\ell$-linear with $|\psi_i(y)| \leq \ell^r$. Put $k = c(N) - g_K$. Then
$$\big( g \mapsto \ell^{g_K} \big[ \ell^k \Phi(f(g)) \big] \big) \in H^1_f(K, V/T_V).$$

Lean: `GlobalTheory.Cyc.ClassBound.mem_HfD_of_isCob`.

*Proof.* Since $\Phi$ is equivariant modulo $T_V$ and $g$ acts on $V$ by $\chi(g)^{-e}$, we have $|\psi_i(\rho(g) y) - \chi(g)^{-e} \psi_i(y)| \leq 1$. For each $i$, [Lemma 6.9.6](/entry/scalar-of-is-cob/) gives a continuous cocycle $z_i : G_{K_s} \to \mathbb{Q}_\ell(-e)$ and $x_i \in B$ with $z_i(\sigma) = \chi(\sigma)^{-e} \sigma(x_i) - x_i$ in $B$ and $|z_i(g) - \ell^k \psi_i(f(g))| \leq 1$ on $G_{K_s}$. The map $\ell^k \Phi \circ f$ is a cocycle modulo $T_V$, because $f$ is a cocycle. Put $Z = \sum_i z_i w_i$. Then $Z$ is a continuous cocycle on $G_{K_s}$, $Z \otimes 1$ is the coboundary of $\sum_i w_i \otimes x_i$ in $V \otimes B$, and $Z \equiv \ell^k \Phi \circ f$ modulo $T_V$ on $G_{K_s}$. So $\ell^k \Phi \circ f$ restricts to a Bloch-Kato cocycle on $G_{K_s}$. A restriction statement from the open normal subgroup $G_{K_s}$ back to $G_K$ costs a factor $\ell^{v}$, where $v$ is the valuation of $[G_K : G_{K_s}]$, and $v = g_K$. $\square$

**Lemma 6.6.6 (Bloch-Kato classes from an $A_{\inf}$ coboundary).** Assume local Tate duality and the local Euler characteristic formula. Let $e, N \in \mathbb{N}$, and let $Y$ and $V$ be lattice representations of $G_K$ with $g x = \chi(g)^{-e} x$ on $V$. Let $\phi : T_Y \to V/T_V$ be $\mathcal{O}$-linear and $G_K$-equivariant. Let $f : G_K \to T_Y$ be a cocycle such that, for each $n$, $f(h) - f(g) \in \ell^n T_Y$ for $h$ near $g$, and such that $\ell^N (f \otimes 1)$ on $G_{K_s}$ is a coboundary in $T_Y \otimes_{\mathbb{Z}_\ell} A_{\inf}[0, e+1)$. Then
$$\big( g \mapsto \ell^{c(N)} \phi(f(g)) \big) \in H^1_f(K, V/T_V).$$

Lean: `GlobalTheory.Cyc.ClassBound.mem_HfD_of_lattice`.

*Proof.* Choose a $\mathbb{Q}_\ell$-basis $w$ of $V$ such that $T_V$ is the set of vectors with coordinates in $\mathbb{Z}_\ell$, with continuous coordinate maps, and a basis $u$ of $V_Y$ with the same property for $T_Y$. Since $T_Y$ is free, $\phi$ lifts to an additive map $\Phi : T_Y \to V$. The coordinates $\psi_i$ of $\Phi$ are $\mathbb{Z}_\ell$-linear. They are bounded by some $\ell^r$ on the finitely many $u_j$, so on all of $T_Y$ by the ultrametric inequality. Since $\phi$ is equivariant, $\Phi(g y) - g \Phi(y) \in T_V$. The previous Lemma gives $\ell^{g_K} [\ell^k \Phi(f(g))] \in H^1_f$ with $k + g_K = c(N)$, and $\ell^{g_K} [\ell^k \Phi(y)] = \ell^{c(N)} \phi(y)$. $\square$

**Theorem 6.6.7 (Crystalline extension class bound).** Assume the admitted local facts. Let $(K, s, L)$ be good, with its Wach and comparison data. Let $e, M_0, h_0 \in \mathbb{N}$. Let $Y$, $\tilde Y$, $Z$ and $V_e$ be lattice representations of $G_K$, and let $\iota : Y \to \tilde Y$ and $\pi : \tilde Y \to Z$ form a short exact sequence of lattices. Assume:

1. $\dim Z = 1$ and $G_K$ acts trivially on $Z$;
2. $\dim V_e = 1$ and $g$ acts on $V_e$ by $\chi(g)^{-e}$;
3. $\tilde Y$ is crystalline on $G_{K_s}$, and the Wach hypothesis holds for $(Y, M_0, h_0)$;
4. $\tilde y \in T_{\tilde Y}$ and $\pi(\tilde y)$ generates $T_Z$;
5. $\phi : T_Y \to V_e/T_e$ is $\mathcal{O}$-linear and $G_K$-equivariant;
6. $f : G_K \to T_Y$ satisfies $\iota(f(g)) = g \tilde y - \tilde y$ for all $g$.

Then
$$\big( g \mapsto \ell^{c(N_Y)} \phi(f(g)) \big) \in H^1_f(K, V_e/T_e).$$

Lean: `GlobalTheory.Cyc.ClassBound.class_bound` (also `GlobalTheory.T.crystalline_extension_class_bound`, a second name).

*Proof.* Since $\iota$ is injective and $\iota \circ f$ is the coboundary of $\tilde y$, the map $f$ is a cocycle, and it is locally constant modulo each $\ell^n$. On $G_{K_s}$, $f \otimes 1$ is a continuous cocycle with values in $T_Y \otimes A_{\inf}[0, e+1)$. Since $\tilde Y$ is crystalline on $G_{K_s}$, a result proved elsewhere in this development, which uses the admitted facts 5 and 7, shows that $\ell^k (f \otimes 1)$ is a coboundary for some $k$. By [Theorem 6.10.8](/entry/torsion-bound-of-weight-hyp/) with $a = 0$ and $b = e + 1$, the Wach hypothesis implies that every such cocycle killed in cohomology by a power of $\ell$ is killed by $\ell^{N_Y}$. So $\ell^{N_Y}(f \otimes 1)$ is a coboundary. The previous Lemma with $N = N_Y$ gives the claim. $\square$

**Remark 6.6.8 (Formalization).** The Theorem proves `TBat` in [LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L165) for the local situation `sit` of a good triple. Its intro at [CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L360) discards three hypotheses: $\dim Z = 1$, $\dim V_e = 1$ and the generation of $T_Z$ by $\pi(\tilde y)$. Line 361 keeps only the admitted facts 2, 4, 5 and 7, so facts 1, 3, 6, 8 and 9 are not used. The admitted fact 4 is named `ArchimedeanSignatureMatching` but is defined as `LocalEulerCharK` (LocalSituation.lean, line 613). Facts 2 and 4 are only passed down through the two Lemmas to `scalar_step`, which uses them through `TwistLift.lift_cocycle`. The steps of the proof are `ConnCoc.conn`, `TensorOneCoc.isCoc_tmul_one`, `GlobalTheory.T.ses_lattice_trivial_quotient`, `GlobalTheory.T.torsion_bound_of_weight_hyp` and `mem_HfD_of_lattice`. The Lemmas use `exists_coords`, `lift_equivariant`, `pow_smul_eq_mk`, `scalar_of_isCob`, `mem_HfD_of_coords`, `GlobalTheory.Cyc.LatBasis.exists_basis`, `GlobalTheory.Cyc.LayerGroup.layer_group` and `GlobalTheory.pow_smul_mem_HfD_of_restriction`. We did not open the proofs of `conn`, `ses_lattice_trivial_quotient`, `exists_basis`, `layer_group` or `pow_smul_mem_HfD_of_restriction`, and we did not unfold `LocalTateTopDegree`, `drDualCore`, `FNatW` or `DecW`, so the facts 3, 8 and 9 are given by their role. The group $G_{K_s}$ is `Gj K s`, a subgroup of $G_{\mathbb{Q}_\ell}$. The action on $V_e$ is written $(\chi(g)^{-1})^e$, and `mem_HfD_of_lattice` rewrites it as $\chi(g)^{-e}$. The sum $r_i$ is a `finsum` over $J(Y)$, so it would be $0$ if $J(Y)$ were infinite. The Theorem and both Lemmas run under `maxHeartbeats 800000`, and the second name is proved by `first | exact ...` under `maxHeartbeats 1000000`.
