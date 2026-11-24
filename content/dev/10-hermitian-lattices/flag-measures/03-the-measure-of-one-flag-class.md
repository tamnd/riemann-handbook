---
title: The measure of one flag class
decls:
  - GlobalTheory.FlagBase.OneClass.bound
  - GlobalTheory.T.flagClass_measure_bound_lattice_stabiliser
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The measure of one flag class

This section bounds the measure of the set of points of $G_\infty$ at which a fixed rational isotropic flag has sizes in a given set $B$, modulo the stabiliser of the flag. The bound is a product of four factors: the Iwasawa constant of the first section, the radical covolume and the Levi integral of the second section, and an integral over $B$ of an explicit density. The unfolding bound of the next section sums this bound over all classes of flags.

### Setting

We keep the global setting of the second section. Suppose that every infinite place $v$ has the same signature $(p, q)$, so that $G_v = U(J_{\varepsilon_v}) \cong U(p,q)$ for each $v$, with Haar measure $\mu_{G_v}$. Let $S$ be a flag in $\Lambda_{x_f}$ that comes from an adapted model $(J_0, \Lambda_i, T_i, T'_i, T_0, x_0)$ as in the second section, with $j_i \ge 1$. Let $\Gamma_S$ be the set of elements of $\Gamma_{x_f}$ that fix each complex flag $W^{(v)}$, and for $g \in G_\infty$ let $\sigma(g) = (\sigma_1(g), \dots, \sigma_a(g))$ be the sizes of the pieces $S_i / S_{i-1}$ at $(g, x_f)$.

Let
$$H_a = \{ \tau \in \mathbb{R}^a : 0 < \tau_1 < \tau_2 < \dots < \tau_a < \tfrac12 \}.$$
For $\tau \in (0,\infty)^a$ define the *flag density*
$$\rho_j(\tau) = \Pi_{n,f,j}(\tau; \mathrm{id}) \prod_{i=1}^a \frac{2 f j_i}{\tau_i}.$$

### An abstract unfolding lemma

The proof uses a general lemma about a group with three closed subgroups $N$, $M$, $K$ and a decomposition $g = umk$. We state it first.

**Lemma 3.3.1 (Unfolding along a decomposition).** Let $H$ be a Polish topological group with three closed subgroups $N$, $M$, $K$. Suppose that $M$ normalises $N$, that $um \in K$ with $u \in N$, $m \in M$ implies $u = 1$, and that every $g \in H$ is $umk$ with $u \in N$, $m \in M$, $k \in K$. Let $\mu$, $\mu_N$, $\mu_M$, $\mu_K$ be measures, with $\mu_N$, $\mu_M$, $\mu_K$ carried by $N$, $M$, $K$, $\mu_K(K) = 1$, and $\mu_M$ and a measurable $\delta \colon M \to [0,\infty]$ invariant under right translation by $K \cap M$. Let $C$, $c$, $R$, $t$ be nonzero and finite, and suppose that for every measurable $\varphi \ge 0$
$$C \int \varphi \, d\mu = c \int_N \int_M \delta(m) \int_K \varphi(umk)\, d\mu_K\, d\mu_M\, d\mu_N.$$
Let $\Gamma \subseteq H$ be closed under products, let $\Gamma_N \subseteq \Gamma \cap N$, and let $\Gamma_M$ be a set of $m \in M$ with $g = um$ for some $g \in \Gamma$ and $u \in N$. Let $A \subseteq H$ be stable under $\Gamma$, let $Z \subseteq M$ be measurable with $m \in Z$ whenever $umk \in A$, and let $w \colon M \to [0,\infty]$ satisfy $t\,\delta(m) \le w(m)$ for $m \in Z$. If $\operatorname{covol}_{\Gamma_N}(\mu_N, N) \le R t$, then
$$C \operatorname{covol}_\Gamma(\mu, A) \le c R \operatorname{covol}_{\Gamma_M}(w\,\mu_M, M).$$

Lean: `GlobalTheory.FlagBase.OneClass.covol_le`.

*Proof.* Take a measurable section $\varsigma$ of $K \to K / (K \cap M)$. Let $D_N$ and $D_M$ be fundamental sets of $\Gamma_N$ in $N$ and of $\Gamma_M$ in $M$. Let $D$ be the set of $umk$ with $u \in D_N$, $m \in D_M \cap Z$ and $k$ in the image of $\varsigma$; it is measurable.

Let $x = umk \in A$. There is $\gamma_M \in \Gamma_M$ with $\gamma_M m k \varsigma(k)^{-1} \in D_M$, and $\gamma_M = u_0^{-1} g$ for some $g \in \Gamma$ and $u_0 \in N$. Since $M$ normalises $N$, $u_0^{-1} \gamma_M u \gamma_M^{-1}$ is in $N$, so there is $\gamma_N \in \Gamma_N$ that moves it into $D_N$. Then $\gamma_N g \in \Gamma$ and $\gamma_N g x \in D$. So $D$ meets every orbit in $A$.

The integration formula with $\varphi = 1_D$ gives
$$C \operatorname{covol}_\Gamma(\mu, A) \le c\, \mu_N(D_N) \int_{D_M \cap Z} \delta \, d\mu_M.$$
On $Z$ we have $\delta \le w / t$. Let $\mu_N(D_N)$ go down to $\operatorname{covol}_{\Gamma_N}(\mu_N, N) \le Rt$ and $\int_{D_M} w\, d\mu_M$ go down to $\operatorname{covol}_{\Gamma_M}(w\mu_M, M)$. $\square$

### The bound for one class

**Theorem 3.3.2 (Measure of one flag class).** In the setting above let $c_v$ be gauge constants for $G_v$, let $c_{0,v}$ be gauge constants for the groups of the model, and let $B \subseteq H_a$ be measurable. Then
$$
\begin{aligned}
& \prod_v c_v \cdot \operatorname{covol}_{\Gamma_S}\Big(\bigotimes_v \mu_{G_v}, \{ g : \sigma(g) \in B \}\Big) \\
& \le c_{\mathrm{Iw}}(p,q,j)^f\, (2 v_E)^{f d_N/2} \prod_i 2^{f j_i^2} \operatorname{vol}_{\mathrm{sl}}(\Lambda_i) \\
& \quad \cdot \prod_v c_{0,v} \operatorname{covol}_{\Gamma_{0,x_0}}(\mu_{G_0}, G_{0,\infty}) \cdot \int_B \rho_j(\tau)\, d\tau.
\end{aligned}
$$

Lean: `GlobalTheory.FlagBase.OneClass.bound` (also `GlobalTheory.T.flagClass_measure_bound_lattice_stabiliser`, a second name).

*Proof.* If the set $\{ g : \sigma(g) \in B \}$ is empty, its covolume is $0$ and the bound holds. Otherwise the proof has seven steps.

1. The adapted model makes $S$ a saturated isotropic flag of type $j$ in $\Lambda_{x_f}$. At each place $v$ its complex flag $W^{(v)}$ is isotropic for $J_{\varepsilon_v}$.
2. The degree of $F$ and the rank of $E$ give $[E : \mathbb{Q}] = 2f$ and $(2v_E)^f = \sqrt{|d_E|}$.
3. At each place take gauge measures $\mu_{N_v}$, $\mu_{M_v}$ of the dimensions $d_N$ and $d_M$ on the groups $N_v$, $M_v$ of $W^{(v)}$, and the probability Haar measure $\mu_{K_v}$ of $K_v$. These groups are closed, $M_v$ normalises $N_v$, and $N_v \cap M_v K_v = \{1\}$ in the sense of the lemma. The Iwasawa decomposition gives $G_v = N_v M_v K_v$.
4. Take $H = G_\infty$ and $N$, $M$, $K$ the products over $v$. The Iwasawa integration formula of the first section at each place, multiplied over the $f$ places, gives the formula of the lemma with $C = \prod_v c_v$, $c = c_{\mathrm{Iw}}(p,q,j)^f$, and $\delta(m) = \prod_v \delta(m_v)$.
5. For $u \in N$, $m \in M$, $k \in K$ the sizes satisfy $\sigma_i(umk)^f = \sigma_i(1)^f \prod_v \tau_i(m_v)$, with the local sizes $\tau_i$ of the first section. So $\sigma(umk)$ depends only on $m$, and the layer product satisfies
$$\Pi_{n,f,j}(\sigma(m); \mathrm{id}) = \Pi_{n,f,j}(\sigma(1); \mathrm{id}) \prod_v \delta(m_v).$$
6. Apply the lemma with $\Gamma = \Gamma_S$, $\Gamma_N = \Gamma_S \cap N$, $\Gamma_M$ the Levi group of the second section, $A = \{ g : \sigma(g) \in B \}$, $Z = \{ m : \sigma(m) \in B \}$, $t = \Pi_{n,f,j}(\sigma(1); \mathrm{id})$, $R = (2 v_E)^{f d_N / 2}$ and $w(m) = 1_B(\sigma(m))\, \Pi_{n,f,j}(\sigma(m); \mathrm{id})$. The set $A$ is stable under $\Gamma_S$, because an element of $\Gamma_S$ fixes the flag and its sizes. Step 5 gives $t\delta \le w$ on $Z$, and the radical covolume theorem gives $\operatorname{covol}_{\Gamma_N}(\mu_N, N) \le Rt$.
7. The Levi integral of the second section with $\Phi = 1_B\, \Pi_{n,f,j}(\cdot\,; \mathrm{id})$ bounds $\operatorname{covol}_{\Gamma_M}(w\mu_M, M)$. Its final integral is $\int_{(0,\infty)^a} 1_B(\tau) \rho_j(\tau)\, d\tau = \int_B \rho_j$, since $B \subseteq H_a \subseteq (0,\infty)^a$. $\square$

The factors of the bound have these roles in the later steps. The constant $c_{\mathrm{Iw}}(p,q,j)^f$ and the power of $2 v_E$ depend only on $E$, $p$, $q$ and $j$. The product of slab volumes depends on the classes of the lattices $\Lambda_i$, and the next section sums it over these classes. The factor $\prod_v c_{0,v} \operatorname{covol}(\Gamma_{0,x_0})$ is a gauge volume of the smaller unitary group, and the next section sums it over the double cosets of the model.

**Remark 3.3.3 (Formalization).** The set $H_a$ is `simplexH` (DefClassNum.lean, line 30), the group $\Gamma_S$ is `flagGroup`, $\Gamma_M$ is `leviGroup` and the sizes $\sigma$ are `sizesAt`. The flag density is written out in the statement as `layerProd n f j τ id` times the product of $2 f j_i / \tau_i$. The steps of the proof use results not unfolded here: `isSaturatedIsotropicFlag_of_adaptedBasis`, `isTotallyIsotropicFlag_complexified_saturatedFlag`, `autInst_degree_rootDiscriminant_rank`, `exists_gauge_measures_isotropicFlag_parabolic`, `iwasawa_decomposition`, `gradedPieceSizes_unipotent_levi_compact_move`, `flagLayerProductMeasure_mul_prod_local` and `iwasawaNMKIntegration_pi_product`. The empty case is treated first, by an explicit infimum argument (FlagClassMeasureBoundLatticeStabiliser.lean, line 177). The lemma on unfolding needs a Polish group because the measurable section of $K \to K/(K \cap M)$ comes from `exists_measurable_coset_section'`.
