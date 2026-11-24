---
title: The unipotent radical and the Levi factor
decls:
  - GlobalTheory.RadCov.radicalCovolume
  - GlobalTheory.T.unipotentRadical_integral_points_covolume
  - GlobalTheory.T.complementary_block_unitary_forms
  - GlobalTheory.LeviIso.exists_charts
  - GlobalTheory.LeviIso.levi_product
  - GlobalTheory.T.flagLevi_realPlaces_product_measure
  - GlobalTheory.FlagBase.LeviInt.covol_leviGroup_le
  - GlobalTheory.T.levi_factor_integral_mod_integral_points_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The unipotent radical and the Levi factor

This section gives the two global inputs of the bound for one flag class. The first is a bound for the covolume of the integral points of the unipotent radical $N$ of a rational isotropic flag. The second is a bound for the integral over the Levi factor $M$, modulo its integral points, of a function of the local sizes. Together with the Iwasawa integration formula of the first section, they split the covolume of the flag stabiliser into a radical part, a Levi part and a compact part. The next section uses both bounds.

### The global setting

Let $E/F$ be a CM extension of [number fields](/learn/number-fields/#number-fields-and-their-integers) and put $f = [F : \mathbb{Q}]$. Let $J \in M_n(E)$ be a nondegenerate [[Hermitian form|8NJ7XY6F1S]] and let $\Lambda$ be a self-dual $\mathcal{O}_E$-lattice in $E^n$ (see [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces)). At each infinite place $v$ of $F$ fix an embedding $\varphi_v \colon E \to \mathbb{C}$ above $v$ and a matrix $P_v$ with $P_v^* \varphi_v(J) P_v = J_{\varepsilon_v}$. Let $G_\infty = \prod_v U(J_{\varepsilon_v})$, let $G_f$ be the finite [adelic points](/learn/groups/#adelic-points-and-compact-open-subgroups) of the [unitary group](/learn/groups/#unitary-groups) of $J$, let $K_f \subseteq G_f$ be the stabiliser of $\Lambda$, and let $\Gamma$ be the rational points, embedded diagonally. For $x_f \in G_f$ let $\Lambda_{x_f}$ be the lattice attached to $(1, x_f)$, and for $g \in G_\infty$ and a sublattice quotient $Q$ of $\Lambda_{x_f}$ let $\operatorname{sz}_{g,x_f}(Q)$ be its size at $(g, x_f)$.

Let $d_E$ be the discriminant of $E$ and put
$$v_E = \tfrac12 |d_E|^{1/(2f)}, \qquad (2 v_E)^f = \sqrt{|d_E|}.$$

**Definition 3.2.1 (Covolume).** Let $H$ be a group with a measure $\nu$, let $\Gamma' \subseteq H$ and let $A \subseteq H$. The *covolume* $\operatorname{covol}_{\Gamma'}(\nu, A)$ is the infimum of $\nu(D)$ over measurable sets $D$ such that for every $x \in A$ there is $\gamma \in \Gamma'$ with $\gamma x \in D$.

So a fundamental set for $\Gamma'$ on $A$ has measure at least the covolume, and the covolume is monotone: a larger $\Gamma'$ gives a smaller covolume.

**Definition 3.2.2 (Saturated isotropic flag).** A *saturated isotropic flag of type $j$* in $\Lambda_{x_f}$ is a chain $0 = S_0 \subseteq S_1 \subseteq \dots \subseteq S_a$ of $\mathcal{O}_E$-submodules with rank jumps $j_1, \dots, j_a$, such that $S_i = \Lambda_{x_f} \cap \operatorname{span}_E S_i$ for each $i$ and $S_a$ is totally isotropic for $J$.

At each infinite place $v$ the complex spans $P_v^{-1} \varphi_v(\operatorname{span}_E S_i)$ form an isotropic flag $W^{(v)}$ of type $j$ for $J_{\varepsilon_v}$, as in the first section. We write $N_v$ and $M_v$ for its unipotent radical and its Levi factor, and $d_N$ for the real dimension of $N_v$.

### The radical covolume

**Theorem 3.2.3 (Radical covolume).** Let $S$ be a saturated isotropic flag of type $j$ in $\Lambda_{x_f}$ and let $\nu_v$ be a gauge measure on $N_v$ of dimension $d_N$ for each $v$. Let
$$\Gamma_N = \{ g \in G_\infty : \exists \gamma \in \Gamma,\ \gamma_\infty = g,\ x_f^{-1} \gamma_f x_f \in K_f \},$$
intersected with $\prod_v N_v$. Put $\tau_i = \operatorname{sz}_{1,x_f}(S_i / S_{i-1})$. Then
$$\operatorname{covol}_{\Gamma_N}\Big(\bigotimes_v \nu_v, \prod_v N_v\Big) \le (2 v_E)^{f d_N / 2}\, \Pi_{n,f,j}(\tau; \mathrm{id}).$$

Lean: `GlobalTheory.RadCov.radicalCovolume` (also `GlobalTheory.T.unipotentRadical_integral_points_covolume`, a second name).

*Proof.* The proof has five steps.

1. Extend $S$ to a self-dual flag $F_0 \subseteq F_1 \subseteq \dots \subseteq F_m = \Lambda_{x_f}$, in which each $F_b$ is saturated and the dual of each step is a later step. The heights of the pieces $F_b / F_{b-1}$ are the sizes $\tau_i$ and their inverses, in the order of the layer product.
2. At each place $v$ the complex flag of $F$ gives a self-dual flag in $\mathbb{C}^n$. The Lie algebra of $N_v$ is the space of $X$ with $X^* J_{\varepsilon_v} + J_{\varepsilon_v} X = 0$ that lower this flag. Filter it by the degree by which $X$ lowers the flag. Each layer is the set of $X$ that lower by exactly $c$ steps, modulo those that lower by $c + 1$ steps.
3. The integral points of $N$ meet each layer in a lattice. A choice of biorthogonal frames for the flag $F$ identifies the layer of degree $c$ with a product of spaces of homomorphisms between pieces $F_b / F_{b-1}$ and $F_{b+c+1} / F_{b+c}$. The skew condition selects a real form. The covolume of the conjugation stable lattice in this real form is at most the square root of $2^{\dim}$ times the covolume of the complex lattice.
4. The covolume of the lattice of homomorphisms between two pieces is the product of a power of $(2 v_E)^f$ and the product of the heights of the two pieces.
5. The covolume of the integral points of a unipotent group is at most the product of the covolumes of its layers. Multiply the bounds of steps 3 and 4 over all layers. The powers of $2 v_E$ add up to $f d_N / 2$, and the heights collect into $\Pi_{n,f,j}(\tau; \mathrm{id})$. $\square$

### Charts for the Levi factor

The Levi factor of an isotropic flag of type $j$ is a product of general linear groups and a smaller unitary group. A chart makes this explicit.

**Definition 3.2.4 (Levi chart).** Let $W$ be an isotropic flag of type $j$ for $J_\varepsilon$, with $n = n_0 + 2s$. Let $B_1, \dots, B_a$ be $n \times j_i$ matrices whose columns span the steps of $W$, and let $B_0$ be an $n \times n_0$ matrix with $B_0^* J_\varepsilon B_0 = J_{\varepsilon_0}$, orthogonal to the $B_i$. A *Levi chart* is a map
$$\theta \colon \prod_i GL_{j_i}(\mathbb{C}) \times U(J_{\varepsilon_0}) \to M(W)$$
with these properties:

1. $\theta(x, g) = \sum_i B_i x_i B_i^* + \sum_i J_\varepsilon B_i (x_i^{-1})^* B_i^* J_\varepsilon + B_0 g B_0^*$, up to the fixed twists by complex conjugation at each block;
2. $\theta$ is a bijection onto $M(W)$ and $\theta(zz') = \theta(z) \theta(z')$;
3. the local sizes satisfy $\tau_i(\theta(x,g)) = |\det x_i|^{-1/j_i}$;
4. a gauge measure on $M(W)$ is the image under $\theta$ of $\prod_i 2^{j_i^2} \mu_{GL_{j_i}} \times c_0 \mu_{G_0}$, where $c_0$ is a gauge constant for $U(J_{\varepsilon_0})$ and $\mu_{GL_{j_i}}$ is the Haar measure of $GL_{j_i}(\mathbb{C})$ with density $|\det|^{-2 j_i}$ for Lebesgue measure.

**Theorem 3.2.5 (Complementary block forms).** Let $W$ be an isotropic flag of type $j$ for $J_\varepsilon$ and let $n = n_0 + 2s$. Let $A_i$ be $n \times j_i$ matrices whose columns span the steps of $W$, let $C_i$ be $j_i \times n$ matrices with $C_i A_i = 1$ and $C_i A_k = 0$ for $i \ne k$, and let $A_0$ be an $n \times n_0$ matrix with $A_i^* J_\varepsilon A_0 = 0$ and $A_0^* J_\varepsilon A_0 = J_{\varepsilon_0}$. Then a Levi chart for $W$ exists.

Lean: `GlobalTheory.T.complementary_block_unitary_forms`.

The construction is the classical block form of a Levi factor of a [parabolic subgroup](/learn/groups/#parabolic-subgroups) of $U(p,q)$: $M(W)$ acts on each piece $W_i / W_{i-1}$ by an element of $GL_{j_i}(\mathbb{C})$, on the dual piece by its inverse adjoint, and on the complement $A_0 \mathbb{C}^{n_0}$ by a unitary matrix of signature $(p - s, q - s)$.

**Theorem 3.2.6 (Charts at the infinite places).** Let the flag $S$ come from an adapted model: an $n_0$-dimensional Hermitian space $(E^{n_0}, J_0)$ over the same field, lattices $\Lambda_i \subseteq E^{j_i}$, and matrices $T_i, T'_i, T_0$ with
$$T_i^* J T_k = 0,\quad T_i'^* J T'_k = 0,\quad T_i^* J T'_k = \delta_{ik},$$
$T_0$ orthogonal to all $T_i, T'_i$ and $T_0^* J T_0 = J_0$, such that $\Lambda_{x_f}$ is the set of $\sum_i T_i u_i + \sum_i T'_i u'_i + T_0 y$ with $u_i \in \Lambda_i$, $u'_i$ in the dual of $\Lambda_i$ and $y$ in the lattice of the model at $x_0$, and $S_k$ is the set of $\sum_{i \le k} T_i u_i$. Then at each infinite place $v$ there is a Levi chart for $W^{(v)}$ with $B_i = P_v^{-1} \varphi_v(T_i)$ and $B_0 = P_v^{-1} \varphi_v(T_0) P_{0,v}$.

Lean: `GlobalTheory.LeviIso.exists_charts`.

*Proof.* Put $A_i = P_v^{-1} \varphi_v(T_i)$, $C_i = (P_v^{-1} \varphi_v(T'_i))^* J_{\varepsilon_v}$ and $A_0 = P_v^{-1}\varphi_v(T_0) P_{0,v}$. The relations of the model give $C_i A_k = \delta_{ik}$, the orthogonality of $A_0$, and $A_0^* J_{\varepsilon_v} A_0 = J_{\varepsilon_{0}}$. The columns of the $A_i$ span the complex flag. Apply the theorem on complementary block forms. $\square$

### The Levi factor over all places

For $z \in M_j(\mathbb{C})^{f}$, one matrix per infinite place, put $\operatorname{N}(z) = \prod_v |\det z_v|^2$. Let $\mu_{GL_j}$ be the measure on $M_j(\mathbb{C})^f$ with density $\operatorname{N}(z)^{-j}$ for Lebesgue measure. For a lattice $\Lambda_i \subseteq E^{j}$ let $\operatorname{Aut}(\Lambda_i)$ be the image in $M_j(\mathbb{C})^f$ of the elements of $GL_j(E)$ that stabilise $\Lambda_i$.

Let $\Gamma_{x_f}$ be the set of $g \in G_\infty$ such that $g = \gamma_\infty$ for a $\gamma \in \Gamma$ with $x_f^{-1}\gamma_f x_f \in K_f$, and let $\Gamma_S$ be its subset of elements that fix each complex flag $W^{(v)}$. Let $\Gamma_M$ be the set of $m \in \prod_v M_v$ with $g = um$ for some $g \in \Gamma_S$ and $u \in \prod_v N_v$. For $g \in G_\infty$ put $\sigma_i(g) = \operatorname{sz}_{g,x_f}(S_i/S_{i-1})$.

**Theorem 3.2.7 (Levi product chart).** Let the flag $S$ come from an adapted model as above, with $j_i \ge 1$. Then there are a measurable map
$$\Theta \colon \prod_i M_{j_i}(\mathbb{C})^f \times G_{0,\infty} \to G_\infty$$
and constants $\kappa_i > 0$ with these properties:

1. $m \in \prod_v M_v$ exactly when $m = \Theta(z)$ with $\operatorname{N}(z_i) > 0$ for each $i$;
2. if $z_1 \in \prod_i \operatorname{Aut}(\Lambda_i)$ and $z_2 \in \Gamma_{0, x_0}$, then for each $z'$ there is $\gamma \in \Gamma_M$ with $\gamma\, \Theta(z') = \Theta(z_1 z'_1, z_2 z'_2)$;
3. $\sigma_i(\Theta(z)) = (\operatorname{N}(z_i)/\kappa_i)^{-1/(2 f j_i)}$;
4. $\Theta$ is injective;
5. for a product $\mu_M$ of gauge measures on the $M_v$, of dimension $(n - 2s)^2 + 2\sum_i j_i^2$, and gauge constants $c_{0,v}$ for the model, and every measurable $\phi \ge 0$,
$$
\begin{aligned}
\int \phi \, d\mu_M = {} & \prod_i 2^{f j_i^2} \prod_v c_{0,v} \\
& \cdot \int_{\operatorname{N}(z_1) > 0} \int \phi(\Theta(z_1, z_2))\, d\mu_{G_0}\, d\mu_{GL}.
\end{aligned}
$$

Lean: `GlobalTheory.LeviIso.levi_product` (also `GlobalTheory.T.flagLevi_realPlaces_product_measure`, a second name).

*Proof.* Take the Levi chart $\theta_v$ of the theorem on charts at each place and let $\Theta$ be their product. Properties 1, 4 and the multiplicativity come from the charts. For property 2, an element of $\operatorname{Aut}(\Lambda_i)$ or of the model group acts on the model and so on $\Lambda_{x_f}$; it fixes each $S_k$, so it lies in $\Gamma_S$, and its Levi part is in $\Gamma_M$. Property 3 is the product over $v$ of the identity $\tau_i(\theta_v(x)) = |\det x_i|^{-1/j_i}$. Property 5 is the product of the gauge measures of the charts. $\square$

### The integral over the Levi factor

**Theorem 3.2.8 (Levi integral).** Let the flag $S$ come from an adapted model, with $j_i \ge 1$. Let $\mu_M$ be a product of gauge measures on the $M_v$ of dimension $(n - 2s)^2 + 2 \sum_i j_i^2$, let $c_{0,v}$ be gauge constants for the model, and let $\Phi \colon (0,\infty)^a \to [0,\infty]$ be measurable. Then
$$
\begin{aligned}
& \operatorname{covol}_{\Gamma_M}\big(\Phi(\sigma)\, \mu_M, \textstyle\prod_v M_v\big) \\
& \le \prod_i 2^{f j_i^2} \operatorname{vol}_{\mathrm{sl}}(\Lambda_i) \cdot \prod_v c_{0,v} \operatorname{covol}_{\Gamma_{0,x_0}}(\mu_{G_0}, G_{0,\infty}) \\
& \quad \cdot \int_{(0,\infty)^a} \Phi(\tau) \prod_i \frac{2 f j_i}{\tau_i}\, d\tau.
\end{aligned}
$$
Here $\operatorname{vol}_{\mathrm{sl}}(\Lambda_i)$ is the covolume of $\operatorname{Aut}(\Lambda_i)$ in the slab $\{1 \le \operatorname{N}(z) < e\}$ for $\mu_{GL_{j_i}}$.

Lean: `GlobalTheory.FlagBase.LeviInt.covol_leviGroup_le` (also `GlobalTheory.T.levi_factor_integral_mod_integral_points_le`, a second name).

*Proof.* Take $\Theta$ and $\kappa_i$ from the Levi product chart.

1. For each $i$ take a fundamental set $D_i$ of $\operatorname{Aut}(\Lambda_i)$ in the slab, of measure close to $\operatorname{vol}_{\mathrm{sl}}(\Lambda_i)$. The scalar matrices $e^{t/(2fj_i)} \cdot 1$ move the slab through all of $\{\operatorname{N}(z) > 0\}$. So the union of the $e^{t/(2fj_i)} D_i$ over $t \in \mathbb{R}$ meets each orbit of $\operatorname{Aut}(\Lambda_i)$.
2. Take a fundamental set $D_0$ of $\Gamma_{0,x_0}$ in $G_{0,\infty}$ of measure close to its covolume. The covolume is not zero, so the ratio is controlled.
3. By property 2 of the chart, the image under $\Theta$ of the product of these sets meets each orbit of $\Gamma_M$ in $\prod_v M_v$. So the covolume is at most the integral of $\Phi(\sigma)$ over this image.
4. By property 5 this integral is a product. In the variable of $GL_{j_i}$, use polar coordinates for the scalar factor. By property 3 the change of variable $\tau_i = (\operatorname{N}(z_i)/\kappa_i)^{-1/(2fj_i)}$ turns $dt$ into $2 f j_i\, d\tau_i / \tau_i$ and turns $\Phi(\sigma)$ into $\Phi(\tau)$.
5. Let the measures of $D_i$ and $D_0$ go down to the covolumes. $\square$

**Remark 3.2.9 (Formalization).** The lattice $\Lambda_{x_f}$ is `GlobalTheory.PointLattice.lamX`, the size is `sizeQ`, and the slab volume is `slabVol`; their definitions are not unfolded here. The adapted model is the predicate `IsAdapted` (IsLatMeasurableConst.lean, line 12) and the Levi chart is `IsLeviChart`. The proof of the radical covolume uses `exists_selfDual_flag_of_saturated_isotropic_flag`, `selfDualHermitianFlag_piece_heights`, `covolume_le_prod_layers_unipotent`, `layer_covolume` (UnipotentRadicalIntegralPointsCovolume.lean, line 111) and `real_domain` (line 46). The lemma `real_domain` needs the hypothesis `IsCMUnram E`, which the proof takes from the instance. The complementary block forms are proved by `GlobalTheory.LeviIso.Chart.exists_leviChart`. The second names of the radical covolume, of the complementary block forms and of the Levi integral are proved by a `first | exact ...` combinator under `set_option maxHeartbeats 1000000`. The proof of the Levi integral uses the lemmas `exists_dom` (LeviFactorIntegralModIntegralPointsLe.lean, line 382) and `le_mul_covol` (line 189).
