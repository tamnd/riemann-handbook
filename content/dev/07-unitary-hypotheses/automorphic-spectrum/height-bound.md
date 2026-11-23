---
id: height-bound
title: One height whose Siegel Eisenstein sum has at most a simple pole at the edge
kind: theorem
decl: GlobalTheory.CompanionTheory.SphPole.height_bound
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.SphericalBoundOfHeights
covers: 416
status: drafted
drafted_by: writer@claude
---
This theorem builds one height on $U(p,p)(\mathbb{A}_F)$ for which the Siegel Eisenstein sum at $g = 1$ grows at most like $1/(\sigma - p/2)$ as $\sigma \to p/2$. [`sphBound_of_htExist`](/entry/sph-bound-of-ht-exist/) compares every other height with this one and gets the bound `SphBound` of [`sphBound`](/entry/sph-bound/). The analysis is here and in the lemma `frame_bound` of the same file.

## Statement

Let $G = U(p,p)(\mathbb{A}_F)$ with Siegel parabolic $P$, and call $H \colon G \to \mathbb{R}_{>0}$ a height if it is continuous and $H(qg) = |\det a_q| H(g)$ for $q \in P$ with Levi block $a_q$.

**Theorem.** For each datum and each $r \ge 0$, put $p = r + 1$. There are a height $H'$ on $G$ and a real $B$ such that for each $\varepsilon \in (0, 1]$ the series $\sum_{\gamma \in P(F) \backslash G(F)} H'(\gamma)^{p + \varepsilon}$ converges and

$$\varepsilon \sum_{\gamma \in P(F) \backslash G(F)} H'(\gamma)^{p + \varepsilon} \le B.$$

## Proof

**The model.** Let $A$ be the standard Hermitian space of rank $p$ (`posSpace`) and $V$ its double (`dblSp A`), of rank $2p$. Then $V$ is a sum of $p$ hyperbolic planes, with an isotropic frame $X$ of rank $p$. A chart $\kappa \colon U(V)(\mathbb{A}) \to G$ carries the stabilizer of $X$ to $P$ and rational points to rational points. `wittDecomposition_isotropicFrameEisenstein_dictionary` gives, for a good level $K$, the Iwasawa decomposition $U(V) = P_X K$ and the height $h(qk) = |\det \beta_q|$, where $q$ acts on $X$ by $\beta_q$. Put $H' = h \circ \kappa^{-1}$. The equivariance of $H'$ comes from `standardUnitaryChart_siegelLeviDet_eq`, which matches $\det \beta_q$ with the determinant of the Levi block. The images $\kappa^{-1}(\gamma)$ of the representatives of $P(F) \backslash G(F)$ form a set of representatives of $\Lambda \backslash U(V)(F)$, with $\Lambda$ the rational stabilizer of $X$. Convergence for exponents above $p$ is `godement_summable_height_rpow_representatives`.

**The bound** (`frame_bound`). Let $d = n - (r+1) > 0$ for a frame of rank $r + 1$ in a space of rank $n$, and $\Phi_\varepsilon(g) = \sum_{t \in T} f_\varepsilon(tg)$ with $f_\varepsilon = h^{d+\varepsilon} \mathbf{1}_{h \le 1}$. Let $\mathcal{F}$ be a fundamental domain for $U(V)(F)$.

1. Unfolding (`setLIntegral_tsum_unfold_of_cosetRepresentatives`): $\int_{\mathcal{F}} \Phi_\varepsilon = \int_{\mathcal{F}_\Lambda} f_\varepsilon$ for a fundamental domain $\mathcal{F}_\Lambda$ of $\Lambda$.
2. Shells (`measure_heightShell_le_isotropicFrame_quotient`): the part of $\mathcal{F}_\Lambda$ where $e^{-j-1} < h \le e^{-j}$ has measure at most $B_0 e^{dj}$. Summation over $j$ (`mul_lintegral_rpow_le_of_shell_bound'`) gives $\varepsilon \int_{\mathcal{F}} \Phi_\varepsilon \le 2B_0$.
3. A compact neighbourhood $U$ of $1$ with $\gamma U \cap U = \emptyset$ for rational $\gamma \ne 1$ gives $\int_U \Phi_\varepsilon \le \int_{\mathcal{F}} \Phi_\varepsilon$. By $U(V) = P_X K$ and compactness of $K \times U$, there are $M, m \ge 1$ with $m^{-1} h(g) \le h(gu) \le M h(g)$ for $u \in U$. So each $t$ with $h(t) \le M^{-1}$ has $h(tu) \le 1$ and $h(t)^{d+\varepsilon} \le m^{d+1} f_\varepsilon(tu)$ for $u \in U$. Integration over $U$ gives $\varepsilon\, \mu(U)\, m^{-d-1} \sum_{h(t) \le 1/M} h(t)^{d+\varepsilon} \le 2B_0$.
4. For $h(t) > M^{-1}$, $h(t)^{d+\varepsilon} \le M h(t)^{d+1}$, and $\sum_t h(t)^{d+1}$ converges by `godement_summable_height_rpow_representatives`.

So $\varepsilon \sum_t h(t)^{d+\varepsilon} \le 2 B_0 m^{d+1} / \mu(U) + M \sum_t h(t)^{d+1}$, since $\varepsilon \le 1$. With $n = 2p$ and $r + 1 = p$, this is the claim.

## In the Lean code

The theorem is in [SphericalBoundOfHeights.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SphericalBoundOfHeights.lean#L269), and `frame_bound` at [line 78](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SphericalBoundOfHeights.lean#L78). Besides the lemmas named above, the chart uses `chart_exists`, `chart_mem_GF_iff` and `continuous_chart_symm`, and `frame_bound` uses `wittFrame_rank_le_and_exists_rational_swap` for $2(r+1) \le n$. We have not read the proofs of the lemmas in other files.

The bound is at $g = 1$ only; [`sphBound_of_htExist`](/entry/sph-bound-of-ht-exist/) passes to compact sets of $g$. The name "height bound" is generic: the statement bounds an Eisenstein sum, not a height.
